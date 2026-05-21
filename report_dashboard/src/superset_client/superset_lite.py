#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Superset BI 数据查询脚本（轻量版）
不依赖pandas，直接返回字典列表
"""

import requests
import time
import json
import os
from typing import Optional, Dict, Any, List
from urllib.parse import urljoin


def get_config():
    """从环境变量获取配置"""
    return {
        'url': os.environ.get('SUPERSET_URL', ''),
        'username': os.environ.get('SUPERSET_USERNAME', ''),
        'password': os.environ.get('SUPERSET_PASSWORD', '')
    }


class SupersetClientLite:
    """Superset BI 客户端（轻量版，不依赖pandas）"""

    def __init__(self, base_url: str, username: str, password: str):
        """
        初始化 Superset 客户端

        Args:
            base_url: Superset 服务地址，如 http://localhost:8088
            username: 用户名
            password: 密码
        """
        self.base_url = base_url.rstrip('/')
        self.username = username
        self.password = password
        self.access_token = None
        self.refresh_token = None
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
            "provider": "ldap"  # 使用 LDAP 认证
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = self.session.post(login_url, json=payload, headers=headers)
            response.raise_for_status()

            data = response.json()
            self.access_token = data.get('access_token')
            self.refresh_token = data.get('refresh_token')

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

            # 如果没找到精确匹配，返回第一个数据库
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
            list: 数据库列表
        """
        url = urljoin(self.base_url, '/api/v1/database/')

        try:
            response = self.session.get(url)
            response.raise_for_status()

            data = response.json()
            # 处理不同的响应格式
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
        timeout: int = 300
    ) -> Optional[List[Dict]]:
        """
        执行 SQL 查询

        Args:
            sql: SQL 查询语句
            database_name: 数据库名称（与 database_id 二选一）
            database_id: 数据库 ID（与 database_id 二选一）
            timeout: 超时时间（秒）

        Returns:
            List[Dict]: 查询结果（字典列表）
        """
        if not self.access_token:
            print("[ERROR] 请先登录")
            return None

        # 获取数据库 ID
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

        # 执行 SQL
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

        print(f"正在执行 SQL 查询...")

        try:
            response = self.session.post(
                execute_url,
                json=payload,
                headers=headers,
                timeout=timeout
            )
            response.raise_for_status()

            result = response.json()

            # 解析结果 - 优先处理顶层data格式（Superset新API格式）
            if 'data' in result and isinstance(result['data'], list):
                # 直接返回顶层data数组（字典格式）
                data_rows = result['data']
                print(f"[OK] 查询成功，返回 {len(data_rows)} 行数据")
                return data_rows

            # 兼容旧格式（result.data格式）
            if 'result' in result:
                data = result['result']
                if isinstance(data, dict):
                    columns = data.get('columns', [])
                    rows = data.get('data', [])

                    if columns and rows:
                        # 提取列名
                        col_names = [col.get('name') or col.get('column_name', f'col_{i}')
                                    for i, col in enumerate(columns)]

                        # 构建字典列表
                        result_list = []
                        for row in rows:
                            row_dict = {}
                            for i, col_name in enumerate(col_names):
                                if i < len(row):
                                    row_dict[col_name] = row[i]
                            result_list.append(row_dict)

                        print(f"[OK] 查询成功，返回 {len(result_list)} 行数据")
                        return result_list
                    else:
                        print("[ERROR] 查询结果为空")
                        return []

            print(f"[ERROR] 无法解析查询结果")
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

    def export_to_excel(
        self,
        data: List[Dict],
        output_path: str,
        sheet_name: str = "Sheet1"
    ) -> bool:
        """
        将数据导出为 Excel 文件（使用openpyxl）

        Args:
            data: 要导出的字典列表
            output_path: 输出文件路径
            sheet_name: 工作表名称

        Returns:
            bool: 导出是否成功
        """
        try:
            from openpyxl import Workbook
            wb = Workbook()
            ws = wb.active
            ws.title = sheet_name

            if data:
                # 写入表头
                headers = list(data[0].keys())
                ws.append(headers)

                # 写入数据
                for row_dict in data:
                    row = [row_dict.get(h) for h in headers]
                    ws.append(row)

            wb.save(output_path)
            print(f"[OK] 数据已导出到: {output_path}")
            return True
        except Exception as e:
            print(f"[ERROR] 导出 Excel 失败: {e}")
            return False


# 别名，保持兼容
SupersetClient = SupersetClientLite