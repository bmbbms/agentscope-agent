# -*- coding: utf-8 -*-
"""
收单运营月报看板 - 主程序
运行此脚本生成看板PDF文件：
1. 商户收款看板（大POS）
2. 立刷产品看板（小POS）

用法：
  python run_dashboard.py              # 生成最新月份看板PDF
  python run_dashboard.py 202602       # 生成指定月份看板PDF
  python run_dashboard.py --html       # 同时生成HTML版本
  python run_dashboard.py 202602 --html # 指定月份+HTML
"""

import sys
import os
import argparse
from datetime import datetime

# 添加src目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from config import MODE, SUPERSET_CONFIG, OUTPUT_DIR
from api_client import create_data_fetcher
from html_generator import generate_large_pos_dashboard_html, generate_small_pos_dashboard_html


def get_timestamp() -> str:
    """获取当前时间戳字符串 yyyymmddhhmmss"""
    return datetime.now().strftime('%Y%m%d%H%M%S')


def main(stat_month: str = None, generate_html: bool = False):
    """主函数

    Args:
        stat_month: 统计月份，格式YYYYMM，默认为最新数据月份
        generate_html: 是否生成HTML版本（默认只生成PDF）
    """
    print('=' * 60)
    print('收单运营月报看板生成器')
    print('=' * 60)

    output_dir = os.path.join(os.path.dirname(__file__), OUTPUT_DIR)

    print(f'\n数据模式: {MODE}')
    print(f'输出目录: {output_dir}')
    if stat_month:
        print(f'指定月份: {stat_month}')
    print(f'默认输出: PDF')
    if generate_html:
        print(f'额外输出: HTML')

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 创建数据获取器
    print('\n[1/3] 正在获取数据...')
    print('  - 使用Superset BI API获取实时数据')
    fetcher = create_data_fetcher({
        'mode': 'api',
        'base_url': SUPERSET_CONFIG.get('base_url'),
        'username': SUPERSET_CONFIG.get('username'),
        'password': SUPERSET_CONFIG.get('password'),
    })

    # 获取两个看板的数据
    large_pos_data = fetcher.fetch_large_pos_dashboard(stat_month)
    small_pos_data = fetcher.fetch_small_pos_dashboard(stat_month)

    print(f'  - 商户收款看板（大POS）: 最新月份 {large_pos_data.get("latest_month", "N/A")}')
    print(f'  - 立刷产品看板（小POS）: 最新月份 {small_pos_data.get("latest_month", "N/A")}')

    # 输出核心指标
    print('\n=== 商户收款看板核心指标 ===')
    for k, v in large_pos_data.get('summary', {}).items():
        print(f'  {k}: {v.get("display_value", 0)} {v.get("unit", "")} (环比 {v.get("mom", 0)}%)')

    print('\n=== 立刷产品看板核心指标 ===')
    for k, v in small_pos_data.get('summary', {}).items():
        print(f'  {k}: {v.get("display_value", 0)} {v.get("unit", "")} (环比 {v.get("mom", 0)}%)')

    # 关闭数据源
    if hasattr(fetcher, 'close'):
        fetcher.close()

    # 获取实际数据月份和时间戳（用于文件命名）
    large_pos_month = large_pos_data.get("latest_month", "N/A")
    small_pos_month = small_pos_data.get("latest_month", "N/A")
    timestamp = get_timestamp()

    # 生成HTML看板（仅在用户要求时）
    large_pos_html_path = None
    small_pos_html_path = None

    if generate_html:
        print('\n[2/4] 正在生成HTML看板...')

        # 生成商户收款看板HTML
        large_pos_html = generate_large_pos_dashboard_html(large_pos_data)
        large_pos_html_path = os.path.join(output_dir, f'商户收款看板_{large_pos_month}_{timestamp}.html')
        with open(large_pos_html_path, 'w', encoding='utf-8') as f:
            f.write(large_pos_html)
        print(f'  - 商户收款看板HTML: {large_pos_html_path}')

        # 生成立刷产品看板HTML
        small_pos_html = generate_small_pos_dashboard_html(small_pos_data)
        small_pos_html_path = os.path.join(output_dir, f'立刷产品看板_{small_pos_month}_{timestamp}.html')
        with open(small_pos_html_path, 'w', encoding='utf-8') as f:
            f.write(small_pos_html)
        print(f'  - 立刷产品看板HTML: {small_pos_html_path}')

    # 生成PDF（默认生成）
    print('\n[3/4] 正在生成PDF看板...')
    pdf_files = []
    pdf_success = True

    try:
        from pdf_generator import html_to_pdf, get_playwright_status

        # 检查Playwright环境
        status = get_playwright_status()
        if not status['can_generate_pdf']:
            print(f'\n  [警告] PDF生成环境不可用')
            print(f'  原因: {status.get("solution", "未知")}')
            print(f'\n  替代方案:')
            print(f'    1. 输出HTML格式（在企微中也可查看）')
            print(f'    2. 联系Copaw平台管理员确认浏览器功能支持')

            # 如果用户没有明确要求HTML，提示但不自动生成
            if not generate_html:
                print(f'\n  如需HTML格式，请明确说明"生成HTML版本"')
                return
            pdf_success = False

        if pdf_success:
            # 如果没有生成HTML，先临时生成用于PDF转换
            temp_files = []
            if not large_pos_html_path:
                large_pos_html = generate_large_pos_dashboard_html(large_pos_data)
                large_pos_html_path = os.path.join(output_dir, f'_temp_商户收款看板_{large_pos_month}.html')
                with open(large_pos_html_path, 'w', encoding='utf-8') as f:
                    f.write(large_pos_html)
                temp_files.append(large_pos_html_path)

            if not small_pos_html_path:
                small_pos_html = generate_small_pos_dashboard_html(small_pos_data)
                small_pos_html_path = os.path.join(output_dir, f'_temp_立刷产品看板_{small_pos_month}.html')
                with open(small_pos_html_path, 'w', encoding='utf-8') as f:
                    f.write(small_pos_html)
                temp_files.append(small_pos_html_path)

            # 生成商户收款看板PDF（带时间戳）
            large_pdf_path = os.path.join(output_dir, f'商户收款看板_{large_pos_month}_{timestamp}.pdf')
            if html_to_pdf(large_pos_html_path, large_pdf_path, auto_setup=True):
                pdf_files.append(large_pdf_path)
            else:
                pdf_success = False

            # 生成立刷产品看板PDF（带时间戳）
            small_pdf_path = os.path.join(output_dir, f'立刷产品看板_{small_pos_month}_{timestamp}.pdf')
            if html_to_pdf(small_pos_html_path, small_pdf_path, auto_setup=True):
                pdf_files.append(small_pdf_path)
            else:
                pdf_success = False

            # 清理临时HTML文件（无论PDF是否成功都删除临时文件）
            for temp_file in temp_files:
                if os.path.exists(temp_file):
                    os.remove(temp_file)

    except ImportError:
        print('  错误: pdf_generator模块导入失败，无法生成PDF')
        pdf_success = False

    # 输出结果
    print(f'\n[4/4] 完成!')

    if pdf_files:
        print(f'\n生成的PDF文件:')
        for pdf in pdf_files:
            print(f'  - {pdf}')
        print('\n提示: PDF文件可直接在企微中查看')
    elif not pdf_success:
        print(f'\nPDF生成失败。')
        if not generate_html:
            print(f'如需HTML格式，请明确说明"生成HTML版本"')

    # 只有用户明确要求时才输出HTML文件信息
    if generate_html and large_pos_html_path and small_pos_html_path:
        print(f'\n生成的HTML文件:')
        print(f'  - {large_pos_html_path}')
        print(f'  - {small_pos_html_path}')


if __name__ == '__main__':
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='收单运营月报看板生成器')
    parser.add_argument('stat_month', nargs='?', help='统计月份（格式YYYYMM）')
    parser.add_argument('--html', action='store_true', help='同时生成HTML版本')

    args = parser.parse_args()
    main(args.stat_month, args.html)