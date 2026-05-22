#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
快速查询脚本 - 直接运行，传入 SQL 即可
支持敏感数据自动脱敏（默认开启）
"""

from superset_query import SupersetClient, get_config
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='Superset BI 快速查询工具（默认脱敏导出）')
    parser.add_argument('--sql', '-s', help='SQL 查询语句')
    parser.add_argument('--sql-file', '-f', help='SQL 文件路径')
    parser.add_argument('--output', '-o', default='output.xlsx', help='输出 Excel 文件路径 (默认: output.xlsx)')
    parser.add_argument('--database', '-d', help='数据库名称 (可选)')
    parser.add_argument('--list-db', action='store_true', help='列出所有可用数据库')
    parser.add_argument('--preview', '-p', type=int, default=20, help='预览前 N 行数据 (默认: 20)')
    parser.add_argument('--no-mask', action='store_true', help='关闭脱敏功能，导出明文数据（仅限授权场景使用）')

    args = parser.parse_args()

    # 安全提示
    if args.no_mask:
        print("\n" + "="*50)
        print("⚠️  警告：已关闭数据脱敏功能！")
        print("请确保您有权导出明文敏感数据！")
        print("="*50 + "\n")

    # 从配置读取 URL 和用户名
    config = get_config()
    superset_url = config.get('url')
    username = config.get('username')

    if not superset_url or not username:
        print("错误：未能在配置中找到 Superset URL 或用户名")
        sys.exit(1)

    print(f"Superset 地址: {superset_url}")
    print(f"用户名: {username}")
    
    # 创建客户端并登录 (密码从 config 中读取)
    try:
        client = SupersetClient(superset_url, username)
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)

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

            # 导出 Excel（默认脱敏）
            enable_mask = not args.no_mask
            client.export_to_excel(df, args.output, enable_mask=enable_mask)
        else:
            print("查询结果为空")
    else:
        print("查询失败")


if __name__ == '__main__':
    main()
