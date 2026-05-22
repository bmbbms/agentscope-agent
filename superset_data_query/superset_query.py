#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Superset BI 数据查询脚本
支持执行 SQL 查询并导出为 Excel（含敏感数据自动脱敏）
"""

import os
import re
import json
import requests
import pandas as pd
import base64
from typing import Optional, List
from urllib.parse import urljoin


# ==================== 敏感字段识别与脱敏规则 ====================

# 敏感字段关键词映射
SENSITIVE_KEYWORDS = {
    'id_card': ['id_card', 'idcard', 'cert_no', 'certid', 'identity', '身份证', '证件号', 'id_no', 'passport', '护照', '军官证'],
    'mobile': ['mobile', 'phone', 'tel', '手机', '电话', 'mobile_no', 'phone_no', 'tel_no'],
    'bank_card': ['card_no', 'cardnum', 'bankcard', '银行卡', '卡号', 'card_number', 'bank_card', 'account_no', 'bank_account'],
    'fixed_phone': ['fixed_phone', 'tel_no', '座机', '固定电话', 'telephone']
}

# ==================== 中文列名动态加载 ====================

# 表结构目录路径（存放各表的字段中英文映射）
TABLE_SCHEMA_DIR = os.path.join(os.path.dirname(__file__), 'BI数据表结构全量')

# 缓存文件路径
CACHE_FILE = os.path.join(os.path.dirname(__file__), 'column_mapping_cache.json')

# 全局缓存
_column_mapping_cache = None
_cache_timestamp = 0


def parse_table_schema_files() -> dict:
    """
    从表结构目录解析所有.md文件（支持递归），提取字段中英文映射
    返回: {英文字段名: 中文列名} 字典
    """
    mapping = {}
    
    if not os.path.exists(TABLE_SCHEMA_DIR):
        print(f"[警告] 表结构目录不存在: {TABLE_SCHEMA_DIR}")
        return mapping
    
    for root_dir, dirs, files in os.walk(TABLE_SCHEMA_DIR):
        for filename in files:
            if not filename.endswith('.md'):
                continue
            
            filepath = os.path.join(root_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                # 寻找表头并定位 英文字段列(0) 和 中文说明列
                in_table = False
                name_idx = -1
                comment_idx = -1
                
                for line in lines:
                    line = line.strip()
                    if not line.startswith('|') or not line.endswith('|'):
                        in_table = False
                        continue
                        
                    parts = [p.strip() for p in line.split('|')[1:-1]]
                    if not parts:
                        continue
                        
                    # 识别表头
                    if any(header in parts[0].lower() for header in ['column', 'field', '字段名', '列名']):
                        in_table = True
                        name_idx = 0
                        # 尝试寻找中文注释列的下标
                        for i, p in enumerate(parts):
                            p_lower = p.lower()
                            if any(k in p_lower for k in ['comment', '说明', '中文名', '描述', '含义']):
                                comment_idx = i
                                break
                        if comment_idx == -1:
                            # 默认如果没找到特征词，取最后一列
                            comment_idx = len(parts) - 1
                        continue
                        
                    # 跳过分隔符行 `|---|---|`
                    if in_table and all(set(p.strip()) <= {'-', ':'} for p in parts if p.strip()):
                        continue
                        
                    # 解析数据行
                    if in_table and name_idx != -1 and comment_idx != -1 and len(parts) > max(name_idx, comment_idx):
                        field_name = parts[name_idx].strip('`').strip().lower()
                        chinese_name = parts[comment_idx].strip()
                        
                        if field_name and chinese_name and not chinese_name.startswith('-'):
                            mapping[field_name] = chinese_name
                            
            except Exception as e:
                print(f"[警告] 解析表结构文件失败 {filename}: {e}")
                continue
    
    return mapping


def get_schema_dir_mtime() -> float:
    """获取表结构目录的最新修改时间（包含子目录）"""
    if not os.path.exists(TABLE_SCHEMA_DIR):
        return 0
    
    max_mtime = 0
    for root_dir, dirs, files in os.walk(TABLE_SCHEMA_DIR):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(root_dir, filename)
                try:
                    mtime = os.path.getmtime(filepath)
                    max_mtime = max(max_mtime, mtime)
                except OSError:
                    pass
    return max_mtime


def load_cached_mapping() -> dict:
    """
    加载中文列名映射（带缓存和自动更新）
    - 首次加载时从表结构文件解析
    - 检测表结构文件变化时自动重新加载
    - 缓存到JSON文件，下次启动更快
    """
    global _column_mapping_cache, _cache_timestamp
    
    # 获取表结构目录最新修改时间
    current_mtime = get_schema_dir_mtime()
    
    # 如果缓存存在且表结构未变化，直接返回缓存
    if _column_mapping_cache is not None and current_mtime <= _cache_timestamp:
        return _column_mapping_cache
    
    # 尝试从缓存文件加载
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                cached_data = json.load(f)
            cached_mtime = cached_data.get('timestamp', 0)
            
            # 如果缓存文件的timestamp比表结构目录新，直接使用缓存
            if cached_mtime >= current_mtime:
                _column_mapping_cache = cached_data.get('mapping', {})
                _cache_timestamp = cached_mtime
                print(f"[缓存] 从缓存文件加载中文列名映射，共 {len(_column_mapping_cache)} 个字段")
                return _column_mapping_cache
        except Exception as e:
            print(f"[警告] 读取缓存文件失败: {e}")
    
    # 从表结构文件重新解析
    print(f"[解析] 表结构文件已更新，重新解析中文列名映射...")
    mapping = parse_table_schema_files()
    
    # 保存到缓存文件
    try:
        cache_data = {
            'timestamp': current_mtime,
            'mapping': mapping
        }
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(cache_data, f, ensure_ascii=False, indent=2)
        print(f"[缓存] 已保存中文列名映射到缓存，共 {len(mapping)} 个字段")
    except Exception as e:
        print(f"[警告] 保存缓存文件失败: {e}")
    
    _column_mapping_cache = mapping
    _cache_timestamp = current_mtime
    
    return mapping


def get_column_chinese_name(column_name: str, mapping: dict = None) -> str:
    """
    获取字段的中文列名
    参数:
        column_name: 英文字段名
        mapping: 中文映射字典（默认从缓存加载）
    返回:
        中文列名（未找到则返回原字段名）
    """
    if mapping is None:
        mapping = load_cached_mapping()
    
    # 统一小写匹配
    return mapping.get(column_name.lower(), column_name)

# 脱敏处理函数
def mask_bank_card(value: str) -> str:
    """
    银行卡号脱敏：
    - 长度大于10位：显示前6位 + **** + 后4位
    - 长度小于等于10位：显示前2位 + **** + 后2位
    """
    if not value or pd.isna(value):
        return value
    value = str(value).strip()
    if len(value) > 10:
        return value[:6] + '****' + value[-4:]
    elif len(value) > 4:
        return value[:2] + '****' + value[-2:]
    return value[:1] + '****'

def mask_id_card(value: str) -> str:
    """
    身份证号/军官证/护照脱敏：
    - 长度大于8位：显示前6位 + **** + 后4位
    - 长度小于等于8位：显示前2位 + **** + 后2位
    """
    if not value or pd.isna(value):
        return value
    value = str(value).strip()
    if len(value) > 8:
        return value[:6] + '****' + value[-4:]
    elif len(value) > 4:
        return value[:2] + '****' + value[-2:]
    return value[:1] + '****'

def mask_mobile(value: str) -> str:
    """
    手机号脱敏：
    - 长度大于11位：显示前4位 + **** + 后3位
    - 长度等于11位：显示前3位 + **** + 后4位
    - 长度大于4小于11位：显示前2位 + **** + 后2位
    """
    if not value or pd.isna(value):
        return value
    value = str(value).strip()
    if len(value) > 11:
        return value[:4] + '****' + value[-3:]
    elif len(value) == 11:
        return value[:3] + '****' + value[-4:]
    elif len(value) > 4:
        return value[:2] + '****' + value[-2:]
    return value[:1] + '****'

def mask_fixed_phone(value: str) -> str:
    """
    固定电话脱敏：区号不隐藏，7-8位电话号码保留最后3位，其余用 * 代替
    示例：0531-12345678 → 0531-*****678
    """
    if not value or pd.isna(value):
        return value
    value = str(value).strip()
    # 检查是否有区号
    if '-' in value:
        parts = value.split('-', 1)
        area_code = parts[0]
        phone_number = parts[1] if len(parts) > 1 else ''
        if len(phone_number) >= 3:
            masked_phone = '*' * (len(phone_number) - 3) + phone_number[-3:]
            return area_code + '-' + masked_phone
        return area_code + '-' + phone_number
    # 没有区号的情况
    if len(value) >= 3:
        return '*' * (len(value) - 3) + value[-3:]
    return value

# 脱敏函数映射
MASK_FUNCTIONS = {
    'id_card': mask_id_card,
    'mobile': mask_mobile,
    'bank_card': mask_bank_card,
    'fixed_phone': mask_fixed_phone
}


def detect_sensitive_columns(columns: List[str]) -> dict:
    """
    检测敏感字段列

    Args:
        columns: 列名列表

    Returns:
        dict: {列名: 敏感类型}
    """
    sensitive_cols = {}
    for col in columns:
        col_lower = str(col).lower()
        for sensitive_type, keywords in SENSITIVE_KEYWORDS.items():
            for keyword in keywords:
                if keyword.lower() in col_lower:
                    sensitive_cols[col] = sensitive_type
                    break
            if col in sensitive_cols:
                break
    return sensitive_cols


def mask_dataframe(df: pd.DataFrame, columns_to_mask: dict = None) -> tuple:
    """
    对DataFrame中的敏感列进行脱敏

    Args:
        df: 原始DataFrame
        columns_to_mask: 指定要脱敏的列 {列名: 敏感类型}，如果为None则自动检测

    Returns:
        tuple: (脱敏后的DataFrame, 脱敏列信息列表)
    """
    if df is None or df.empty:
        return df, []

    # 如果未指定列，自动检测
    if columns_to_mask is None:
        columns_to_mask = detect_sensitive_columns(df.columns.tolist())

    if not columns_to_mask:
        return df, []

    masked_columns = []
    df_masked = df.copy()

    for col, sensitive_type in columns_to_mask.items():
        if col in df_masked.columns:
            mask_func = MASK_FUNCTIONS.get(sensitive_type)
            if mask_func:
                df_masked[col] = df_masked[col].apply(mask_func)
                masked_columns.append(f"{col}({sensitive_type})")

    return df_masked, masked_columns


# ==================== 金额单位转换 ====================

# 金额字段关键词
AMOUNT_KEYWORDS = ['amt', 'amount', '金额', '交易金额', 'trans_amt', 'fee_amt', 'money', 'price', '费用', '手续费', '清算金额', '结算金额']

def detect_amount_columns(columns: List[str]) -> List[str]:
    """
    检测金额字段列（单位为分，需要转换为元）

    Args:
        columns: 列名列表

    Returns:
        list: 金额字段列名列表
    """
    amount_cols = []
    for col in columns:
        col_lower = str(col).lower()
        for keyword in AMOUNT_KEYWORDS:
            if keyword.lower() in col_lower:
                # 排除已经标注为元的字段
                if '元' not in col and '_yuan' not in col_lower:
                    amount_cols.append(col)
                break
    return amount_cols


# ==================== Superset 客户端 ====================

# ==================== 配置信息 ====================

# 简单的可逆加密，用于防止代码中明文显示密码
# 可以使用 encrypt_password("真实密码") 得到加密字符串并填入这里
def encrypt_password(password: str, key: str = 'superset_key') -> str:
    """可逆加密（加密）"""
    pass_bytes = password.encode('utf-8')
    key_bytes = key.encode('utf-8')
    encrypted_bytes = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(pass_bytes)])
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def decrypt_password(encrypted_base64: str, key: str = 'superset_key') -> str:
    """可逆加密（解密）"""
    encrypted_bytes = base64.b64decode(encrypted_base64)
    key_bytes = key.encode('utf-8')
    decrypted_bytes = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(encrypted_bytes)])
    return decrypted_bytes.decode('utf-8')

# Superset 配置
SUPERSET_CONFIG = {
    'url': os.environ.get('SUPERSET_BASE_URL', '').strip(),
    'username': os.environ.get('SUPERSET_USERNAME', '').strip(),
    'password_encrypted': os.environ.get('SUPERSET_PASSWORD_ENCRYPTED', '').strip(),
    'password': os.environ.get('SUPERSET_PASSWORD', '').strip(),
}

def get_config():
    """获取配置信息"""
    return {
        'url': SUPERSET_CONFIG['url'],
        'username': SUPERSET_CONFIG['username'],
        'password': SUPERSET_CONFIG['password'] or decrypt_password(SUPERSET_CONFIG['password_encrypted'])
    }


class SupersetClient:
    """Superset BI 客户端"""

    def __init__(self, base_url: str = None, username: str = None, password: str = None):
        """
        初始化 Superset 客户端

        Args:
            base_url: Superset 服务地址，如 http://localhost:8088（默认使用配置值）
            username: 用户名（默认使用配置值）
            password: 密码（默认使用配置值）
        """
        config = get_config()
        self.base_url = (base_url or config['url']).rstrip('/')
        self.username = username or config['username']
        self.password = password or config.get('password')
        
        if not self.password:
            raise ValueError("未能获取密码配置，无法登录。")

        self.access_token = None
        self.session = requests.Session()

    def login(self) -> bool:
        """
        登录 Superset 获取 access token

        Returns:
            bool: 登录是否成功
        """
        login_url = urljoin(self.base_url, '/api/v1/security/login')

        payload = {
            "username": self.username,
            "password": self.password,
            "provider": "ldap"
        }

        headers = {"Content-Type": "application/json"}

        try:
            response = self.session.post(login_url, json=payload, headers=headers)
            response.raise_for_status()

            data = response.json()
            self.access_token = data.get('access_token')

            if self.access_token:
                self.session.headers.update({
                    'Authorization': f'Bearer {self.access_token}'
                })
                print(f"[OK] 登录成功: {self.username}")
                return True
            else:
                print("[ERROR] 登录失败: 未获取到 access token")
                return False

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] 登录失败: {e}")
            return False

    def get_database_id(self, database_name: str) -> Optional[int]:
        """
        根据数据库名称获取数据库 ID

        Args:
            database_name: 数据库名称

        Returns:
            int: 数据库 ID，未找到返回 None
        """
        url = urljoin(self.base_url, '/api/v1/database/')

        try:
            response = self.session.get(url)
            response.raise_for_status()

            data = response.json()
            databases = data.get('result', {}).get('data', [])

            for db in databases:
                if db.get('database_name') == database_name:
                    return db.get('id')

            if databases:
                print(f"警告: 未找到数据库 '{database_name}'，使用第一个可用数据库")
                return databases[0].get('id')

            return None

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] 获取数据库列表失败: {e}")
            return None

    def list_databases(self) -> list:
        """
        列出所有可用的数据库

        Returns:
            list: 数据库列表 [(id, name), ...]
        """
        url = urljoin(self.base_url, '/api/v1/database/')

        try:
            response = self.session.get(url)
            response.raise_for_status()

            data = response.json()
            if isinstance(data, list):
                return [(db.get('id'), db.get('database_name')) for db in data]
            elif isinstance(data, dict):
                databases = data.get('result', {})
                if isinstance(databases, list):
                    return [(db.get('id'), db.get('database_name')) for db in databases]
                databases = data.get('result', {}).get('data', [])
                return [(db.get('id'), db.get('database_name')) for db in databases]
            return []

        except requests.exceptions.RequestException as e:
            print(f"[ERROR] 获取数据库列表失败: {e}")
            return []

    def execute_sql(
        self,
        sql: str,
        database_name: Optional[str] = None,
        database_id: Optional[int] = None,
        timeout: int = 300,
        enable_mask: bool = True,
        enable_chinese_columns: bool = True
    ) -> Optional[pd.DataFrame]:
        """
        执行 SQL 查询（默认自动脱敏）

        Args:
            sql: SQL 查询语句
            database_name: 数据库名称（与 database_id 二选一）
            database_id: 数据库 ID（与 database_name 二选一）
            timeout: 超时时间（秒）
            enable_mask: 是否启用敏感数据脱敏，默认True（安全优先）
            enable_chinese_columns: 是否启用中文列名转换，默认True

        Returns:
            pd.DataFrame: 查询结果（已脱敏）
        """
        if not self.access_token:
            print("[ERROR] 请先登录")
            return None

        if database_id is None:
            if database_name:
                database_id = self.get_database_id(database_name)
            else:
                databases = self.list_databases()
                if databases:
                    database_id = databases[0][0]
                else:
                    print("[ERROR] 没有可用的数据库")
                    return None

        if database_id is None:
            print("[ERROR] 未找到有效的数据库")
            return None

        execute_url = urljoin(self.base_url, '/api/v1/sqllab/execute/')

        payload = {
            "database_id": database_id,
            "sql": sql,
            "queryLimit": 100000,
            "runAsync": False,
            "ctas_method": "TABLE"
        }

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        print("正在执行 SQL 查询...")

        try:
            response = self.session.post(
                execute_url,
                json=payload,
                headers=headers,
                timeout=timeout
            )
            response.raise_for_status()

            result = response.json()

            if 'result' in result:
                data = result['result']
                if isinstance(data, dict):
                    columns = data.get('columns', [])
                    rows = data.get('data', [])

                    if columns and rows:
                        col_names = [col.get('name') or col.get('column_name', f'col_{i}')
                                    for i, col in enumerate(columns)]
                        df = pd.DataFrame(rows, columns=col_names)
                        
                        # 自动脱敏（默认开启）
                        if enable_mask:
                            df, masked_cols = mask_dataframe(df)
                            if masked_cols:
                                print(f"[安全] 已对敏感字段脱敏: {', '.join(masked_cols)}")
                        
                        # 中文列名转换（可选）
                        if enable_chinese_columns:
                            column_mapping = load_cached_mapping()
                            chinese_cols = {k: v for k, v in column_mapping.items() if k in df.columns}
                            if chinese_cols:
                                df.rename(columns=chinese_cols, inplace=True)
                                print(f"[列名] 已转换为中文: {len(chinese_cols)} 个字段")
                        
                        print(f"[OK] 查询成功，返回 {len(df)} 行数据")
                        return df
                    else:
                        print("[ERROR] 查询结果为空")
                        return pd.DataFrame()

            if 'data' in result:
                df = pd.DataFrame(result['data'])
                
                # 自动脱敏（默认开启）
                if enable_mask:
                    df, masked_cols = mask_dataframe(df)
                    if masked_cols:
                        print(f"[安全] 已对敏感字段脱敏: {', '.join(masked_cols)}")
                
                # 中文列名转换（可选）
                if enable_chinese_columns:
                    column_mapping = load_cached_mapping()
                    chinese_cols = {k: v for k, v in column_mapping.items() if k in df.columns}
                    if chinese_cols:
                        df.rename(columns=chinese_cols, inplace=True)
                        print(f"[列名] 已转换为中文: {len(chinese_cols)} 个字段")
                
                print(f"[OK] 查询成功，返回 {len(df)} 行数据")
                return df

            print("[ERROR] 无法解析查询结果")
            return None

        except requests.exceptions.Timeout:
            print(f"[ERROR] 查询超时（{timeout}秒）")
            return None
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] 查询失败: {e}")
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_detail = e.response.json()
                    print(f"  错误详情: {error_detail}")
                except:
                    print(f"  响应内容: {e.response.text}")
            return None

    def query_and_export(
        self,
        sql: str,
        output_path: str,
        database_name: Optional[str] = None,
        database_id: Optional[int] = None,
        timeout: int = 300,
        enable_mask: bool = True,
        column_names: Optional[dict] = None,
        sheet_name: str = "Sheet1"
    ) -> Optional[pd.DataFrame]:
        """
        一站式查询+脱敏+中文列名+导出Excel（推荐使用）
        
        Args:
            sql: SQL 查询语句
            output_path: 输出Excel文件路径
            database_name: 数据库名称
            database_id: 数据库 ID
            timeout: 超时时间（秒）
            enable_mask: 是否启用脱敏，默认True
            column_names: 自定义列名映射 {英文: 中文}，若为None则使用默认映射
            sheet_name: Excel工作表名称
            
        Returns:
            pd.DataFrame: 查询结果DataFrame
        """
        # 执行查询（不在此处脱敏，由export_to_excel处理）
        df = self.execute_sql(
            sql, 
            database_name=database_name, 
            database_id=database_id, 
            timeout=timeout,
            enable_mask=False  # 暂不脱敏，由export_to_excel统一处理
        )
        
        if df is None or df.empty:
            print("[ERROR] 查询无数据，无法导出")
            return None
        
        # 中文列名转换
        if column_names:
            df.rename(columns=column_names, inplace=True)
            print(f"[列名] 已转换为中文: {len(column_names)} 个字段（自定义映射）")
        else:
            # 使用动态加载的映射
            column_mapping = load_cached_mapping()
            chinese_cols = {k: v for k, v in column_mapping.items() if k in df.columns}
            if chinese_cols:
                df.rename(columns=chinese_cols, inplace=True)
                print(f"[列名] 已转换为中文: {len(chinese_cols)} 个字段（动态映射）")
        
        # 导出（自动脱敏）
        success = self.export_to_excel(df, output_path, sheet_name=sheet_name, enable_mask=enable_mask)
        
        if success:
            return df
        return None

    def export_to_excel(
        self,
        df: pd.DataFrame,
        output_path: str,
        sheet_name: str = "Sheet1",
        enable_mask: bool = True
    ) -> bool:
        """
        将 DataFrame 导出为 Excel 文件（支持自动脱敏）

        Args:
            df: 要导出的 DataFrame
            output_path: 输出文件路径
            sheet_name: 工作表名称
            enable_mask: 是否启用敏感数据脱敏（默认True）

        Returns:
            bool: 导出是否成功
        """
        try:
            if enable_mask:
                df_export, masked_cols = mask_dataframe(df)
                if masked_cols:
                    print(f"[安全] 已对敏感字段脱敏: {', '.join(masked_cols)}")
            else:
                df_export = df
                print("[警告] 已关闭脱敏功能，请确保数据安全！")

            df_export.to_excel(output_path, index=False, sheet_name=sheet_name, engine='openpyxl')
            print(f"[OK] 数据已导出到: {output_path}")
            return True
        except Exception as e:
            print(f"[ERROR] 导出 Excel 失败: {e}")
            return False


def query_superset(
    password: str,
    sql: str,
    base_url: str = None,
    username: str = None,
    database_name: Optional[str] = None,
    output_excel: Optional[str] = None,
    enable_mask: bool = True
) -> Optional[pd.DataFrame]:
    """
    便捷函数：执行 Superset 查询

    Args:
        password: 密码（明文，会与配置中的哈希进行验证）
        sql: SQL 查询语句
        base_url: Superset 服务地址（可选，默认使用配置值）
        username: 用户名（可选，默认使用配置值）
        database_name: 数据库名称（可选）
        output_excel: Excel 输出路径（可选）
        enable_mask: 是否启用脱敏（默认True）

    Returns:
        pd.DataFrame: 查询结果
    """
    client = SupersetClient(base_url, username, password)

    if not client.login():
        return None

    df = client.execute_sql(sql, database_name=database_name)

    if df is not None and not df.empty and output_excel:
        client.export_to_excel(df, output_excel, enable_mask=enable_mask)

    return df
