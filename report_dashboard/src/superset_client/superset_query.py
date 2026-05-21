#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Superset BI 数据查询脚本
支持执行 SQL 查询并导出为 Excel
"""

import requests
import pandas as pd
import time
import json
import os
from typing import Optional, Dict, Any
from urllib.parse import urljoin


def get_config():
    """从环境变量获取配置"""
    return {
        'url': os.environ.get('SUPERSET_URL', ''),
        'username': os.environ.get('SUPERSET_USERNAME', ''),
        'password': os.environ.get('SUPERSET_PASSWORD', '')
    }


class SupersetClient:
    """Superset BI 客户端"""

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
                # 直接返回列表
                return [(db.get('id'), db.get('database_name')) for db in data]
            elif isinstance(data, dict):
                # 嵌套格式
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
    ) -> Optional[pd.DataFrame]:
        """
        执行 SQL 查询

        Args:
            sql: SQL 查询语句
            database_name: 数据库名称（与 database_id 二选一）
            database_id: 数据库 ID（与 database_name 二选一）
            timeout: 超时时间（秒）

        Returns:
            pd.DataFrame: 查询结果
        """
        if not self.access_token:
            print("[ERROR] 请先登录")
            return None

        # 获取数据库 ID
        if database_id is None:
            if database_name:
                database_id = self.get_database_id(database_name)
            else:
                # 获取第一个数据库
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
            "queryLimit": 100000,  # 结果限制
            "runAsync": False,  # 同步执行
            "ctas_method": "TABLE"  # 创建表方式
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

            # 解析结果
            if 'result' in result:
                data = result['result']
                if isinstance(data, dict):
                    # 获取列和数据
                    columns = data.get('columns', [])
                    rows = data.get('data', [])

                    if columns and rows:
                        # 提取列名
                        col_names = [col.get('name') or col.get('column_name', f'col_{i}')
                                    for i, col in enumerate(columns)]

                        df = pd.DataFrame(rows, columns=col_names)
                        print(f"[OK] 查询成功，返回 {len(df)} 行数据")
                        return df
                    else:
                        print("[ERROR] 查询结果为空")
                        return pd.DataFrame()

            # 尝试其他格式
            if 'data' in result:
                df = pd.DataFrame(result['data'])
                print(f"[OK] 查询成功，返回 {len(df)} 行数据")
                return df

            print(f"[ERROR] 无法解析查询结果: {result}")
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
        df: pd.DataFrame,
        output_path: str,
        sheet_name: str = "Sheet1"
    ) -> bool:
        """
        将 DataFrame 导出为 Excel 文件

        Args:
            df: 要导出的 DataFrame
            output_path: 输出文件路径
            sheet_name: 工作表名称

        Returns:
            bool: 导出是否成功
        """
        try:
            df.to_excel(output_path, index=False, sheet_name=sheet_name, engine='openpyxl')
            print(f"[OK] 数据已导出到: {output_path}")
            return True
        except Exception as e:
            print(f"[ERROR] 导出 Excel 失败: {e}")
            return False


def query_superset(
    base_url: str,
    username: str,
    password: str,
    sql: str,
    database_name: Optional[str] = None,
    output_excel: Optional[str] = None
) -> Optional[pd.DataFrame]:
    """
    便捷函数：执行 Superset 查询

    Args:
        base_url: Superset 服务地址
        username: 用户名
        password: 密码
        sql: SQL 查询语句
        database_name: 数据库名称（可选）
        output_excel: Excel 输出路径（可选）

    Returns:
        pd.DataFrame: 查询结果
    """
    client = SupersetClient(base_url, username, password)

    if not client.login():
        return None

    df = client.execute_sql(sql, database_name=database_name)

    if df is not None and not df.empty and output_excel:
        client.export_to_excel(df, output_excel)

    return df


def main():
    """主函数示例"""
    import argparse

    parser = argparse.ArgumentParser(description='Superset BI 数据查询工具')
    parser.add_argument('--url', required=True, help='Superset 服务地址，如 http://localhost:8088')
    parser.add_argument('--username', '-u', required=True, help='用户名')
    parser.add_argument('--password', '-p', required=True, help='密码')
    parser.add_argument('--sql', '-s', help='SQL 查询语句')
    parser.add_argument('--sql-file', '-f', help='SQL 文件路径')
    parser.add_argument('--database', '-d', help='数据库名称')
    parser.add_argument('--output', '-o', help='输出 Excel 文件路径')
    parser.add_argument('--list-db', action='store_true', help='列出所有可用数据库')

    args = parser.parse_args()

    # 创建客户端
    client = SupersetClient(args.url, args.username, args.password)

    # 登录
    if not client.login():
        return

    # 列出数据库
    if args.list_db:
        databases = client.list_databases()
        print("\n可用的数据库:")
        for db_id, db_name in databases:
            print(f"  - ID: {db_id}, 名称: {db_name}")
        return

    # 获取 SQL
    sql = args.sql
    if args.sql_file:
        with open(args.sql_file, 'r', encoding='utf-8') as f:
            sql = f.read()

    if not sql:
        print("[ERROR] 请提供 SQL 查询语句 (--sql 或 --sql-file)")
        return

    # 执行查询
    df = client.execute_sql(sql, database_name=args.database)

    if df is not None:
        if args.output:
            client.export_to_excel(df, args.output)
        else:
            print("\n查询结果:")
            print(df.to_string())


if __name__ == '__main__':
    main()