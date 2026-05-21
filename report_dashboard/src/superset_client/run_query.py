#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
快速查询脚本 - 直接运行，传入 SQL 即可
"""

from superset_query import SupersetClient, get_config
import argparse
import sys
import os


# 从环境变量读取配置
config = get_config()
SUPERSET_URL = config['url']
USERNAME = config['username']
PASSWORD = config['password']


def main():
    # 检查环境变量
    if not SUPERSET_URL or not USERNAME or not PASSWORD:
        print("错误：请先设置环境变量")
        print("  SUPERSET_URL      - Superset 服务地址")
        print("  SUPERSET_USERNAME - 用户名")
        print("  SUPERSET_PASSWORD - 密码")
        print("\nWindows 设置方法:")
        print('  setx SUPERSET_URL "https://superset-bi.jlpay.com"')
        print('  setx SUPERSET_USERNAME "your_username"')
        print('  setx SUPERSET_PASSWORD "your_password"')
        sys.exit(1)
    parser = argparse.ArgumentParser(description='Superset BI 快速查询工具')
    parser.add_argument('--sql', '-s', help='SQL 查询语句')
    parser.add_argument('--sql-file', '-f', help='SQL 文件路径')
    parser.add_argument('--output', '-o', default='output.xlsx', help='输出 Excel 文件路径 (默认: output.xlsx)')
    parser.add_argument('--database', '-d', help='数据库名称 (可选)')
    parser.add_argument('--list-db', action='store_true', help='列出所有可用数据库')
    parser.add_argument('--preview', '-p', type=int, default=20, help='预览前 N 行数据 (默认: 20)')

    args = parser.parse_args()

    # 创建客户端并登录
    client = SupersetClient(SUPERSET_URL, USERNAME, PASSWORD)

    print("正在连接 Superset...")
    if not client.login():
        print("登录失败，请检查网络和账号信息")
        sys.exit(1)

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
        print("请提供 SQL 查询语句 (--sql 或 --sql-file)")
        parser.print_help()
        sys.exit(1)

    # 执行查询
    print(f"\n执行 SQL:\n{sql}\n")
    df = client.execute_sql(sql, database_name=args.database)

    if df is not None:
        if not df.empty:
            # 预览数据
            print(f"\n数据预览 (前 {args.preview} 行):")
            print(df.head(args.preview).to_string())
            print(f"\n共 {len(df)} 行, {len(df.columns)} 列")

            # 导出 Excel
            client.export_to_excel(df, args.output)
        else:
            print("查询结果为空")
    else:
        print("查询失败")


if __name__ == '__main__':
    main()