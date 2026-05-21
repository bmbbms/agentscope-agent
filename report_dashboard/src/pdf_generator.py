# -*- coding: utf-8 -*-
"""
PDF生成模块
将HTML看板转换为PDF文件，支持ECharts图表渲染

支持自动检测和安装Playwright环境
"""

import os
import sys
import subprocess
from typing import Optional, Tuple


def check_playwright_installed() -> bool:
    """检查playwright Python库是否已安装"""
    try:
        import playwright
        return True
    except ImportError:
        return False


def check_chromium_installed() -> bool:
    """
    检查Chromium浏览器内核是否已安装

    Returns:
        True: Chromium已安装且可用
        False: Chromium未安装或不可用
    """
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            # 尝试启动浏览器，验证是否可用
            browser = p.chromium.launch(headless=True)
            browser.close()
        return True
    except Exception as e:
        # 常见错误类型
        error_msg = str(e)
        if "Executable doesn't exist" in error_msg:
            return False
        if "browser" in error_msg.lower() or "chromium" in error_msg.lower():
            return False
        # 其他错误可能是Copaw环境限制
        return False


def get_playwright_status() -> dict:
    """
    获取Playwright完整状态信息

    Returns:
        状态字典，包含安装情况和问题诊断
    """
    status = {
        'playwright_installed': False,
        'chromium_installed': False,
        'can_generate_pdf': False,
        'error_type': None,
        'solution': None
    }

    # 检查Playwright库
    if not check_playwright_installed():
        status['playwright_installed'] = False
        status['error_type'] = 'playwright_not_installed'
        status['solution'] = '需要安装playwright库: pip install playwright'
        return status

    status['playwright_installed'] = True

    # 检查Chromium浏览器
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            browser.close()
        status['chromium_installed'] = True
        status['can_generate_pdf'] = True
    except Exception as e:
        error_msg = str(e)
        status['chromium_installed'] = False
        status['can_generate_pdf'] = False

        # 诊断具体问题
        if "Executable doesn't exist" in error_msg:
            status['error_type'] = 'chromium_not_installed'
            status['solution'] = '需要安装Chromium内核: playwright install chromium'
        elif "browser" in error_msg.lower() or "chromium" in error_msg.lower():
            status['error_type'] = 'browser_unavailable'
            status['solution'] = '浏览器功能不可用，可能Copaw环境限制了浏览器运行'
        else:
            status['error_type'] = 'unknown_error'
            status['solution'] = f'未知错误: {error_msg}'

    return status


def auto_install_playwright() -> Tuple[bool, str]:
    """
    自动安装Playwright和Chromium浏览器

    Returns:
        (是否成功, 消息)
    """
    print("=" * 50)
    print("自动安装Playwright环境")
    print("=" * 50)

    # 第一步：安装playwright库
    if not check_playwright_installed():
        print("\n[1/2] 正在安装playwright库...")
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "playwright"],
                capture_output=True,
                text=True,
                timeout=120
            )
            if result.returncode != 0:
                return False, f"playwright库安装失败: {result.stderr}"
            print("playwright库安装成功")
        except subprocess.TimeoutExpired:
            return False, "playwright库安装超时（超过120秒）"
        except Exception as e:
            return False, f"playwright库安装异常: {str(e)}"
    else:
        print("\n[1/2] playwright库已安装，跳过")

    # 第二步：安装Chromium浏览器内核
    print("\n[2/2] 正在安装Chromium浏览器内核...")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "playwright", "install", "chromium"],
            capture_output=True,
            text=True,
            timeout=300  # Chromium下载可能需要较长时间
        )
        if result.returncode != 0:
            # 检查是否是权限或网络问题
            stderr = result.stderr
            if "permission" in stderr.lower():
                return False, f"Chromium安装权限不足，请联系管理员\n详情: {stderr}"
            elif "network" in stderr.lower() or "connect" in stderr.lower():
                return False, f"Chromium下载网络失败，请检查网络连接\n详情: {stderr}"
            else:
                return False, f"Chromium安装失败: {stderr}"

        print("Chromium浏览器内核安装成功")
    except subprocess.TimeoutExpired:
        return False, "Chromium下载超时（超过300秒），可能是网络较慢"
    except Exception as e:
        return False, f"Chromium安装异常: {str(e)}"

    # 第三步：验证安装
    print("\n[验证] 测试浏览器是否可用...")
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            browser.close()
        print("浏览器功能验证成功！")
        return True, "Playwright环境安装完成，PDF生成功能可用"
    except Exception as e:
        return False, f"安装完成但浏览器无法运行，可能Copaw环境限制: {str(e)}"


def try_setup_playwright() -> Tuple[bool, str]:
    """
    尝试设置Playwright环境（检测+自动安装）

    Returns:
        (是否可用, 状态消息)
    """
    # 先检查状态
    status = get_playwright_status()

    if status['can_generate_pdf']:
        return True, "Playwright环境已就绪"

    # 如果Playwright库未安装，尝试自动安装
    if not status['playwright_installed']:
        print(f"\n检测到Playwright未安装，正在自动安装...")
        success, msg = auto_install_playwright()
        if success:
            return True, msg
        else:
            return False, f"自动安装失败: {msg}"

    # 如果Chromium未安装，尝试自动安装
    if not status['chromium_installed']:
        if status['error_type'] == 'chromium_not_installed':
            print(f"\n检测到Chromium未安装，正在自动安装...")
            success, msg = auto_install_playwright()
            if success:
                return True, msg
            else:
                return False, f"自动安装失败: {msg}"

    # 如果是环境限制问题，无法自动解决
    if status['error_type'] == 'browser_unavailable':
        return False, "Copaw环境可能限制了浏览器运行功能，无法生成PDF\n建议：输出HTML格式，或联系Copaw管理员"

    return False, f"Playwright环境不可用: {status.get('solution', '未知问题')}"


def html_to_pdf(html_path: str, pdf_path: str, wait_time: int = 8000,
                auto_setup: bool = True) -> bool:
    """
    将HTML文件转换为PDF（单页长页面，不分页）

    Args:
        html_path: HTML文件路径
        pdf_path: 输出PDF路径
        wait_time: 等待图表渲染的时间（毫秒），默认8秒
        auto_setup: 是否自动检测和安装Playwright环境

    Returns:
        是否成功
    """
    # 自动检测和设置环境
    if auto_setup:
        available, msg = try_setup_playwright()
        if not available:
            print(f"\nPDF生成环境不可用: {msg}")
            print("\n替代方案:")
            print("  1. 使用HTML格式输出（在企微中也可查看）")
            print("  2. 联系Copaw平台管理员确认浏览器功能支持")
            return False

    try:
        from playwright.sync_api import sync_playwright

        # 确保路径是绝对路径
        html_path = os.path.abspath(html_path)
        pdf_path = os.path.abspath(pdf_path)

        # 确保输出目录存在
        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

        print("  正在渲染PDF...")
        with sync_playwright() as p:
            # 启动浏览器，设置更稳定的参数
            browser = p.chromium.launch(
                headless=True,
                args=[
                    '--no-sandbox',
                    '--disable-setuid-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-web-security',
                    '--font-render-hinting=none'
                ]
            )
            # 使用更大的页面宽度和高度，确保图表完整显示
            page = browser.new_page(
                viewport={'width': 1500, 'height': 2000},
                device_scale_factor=1.5  # 提高渲染质量
            )

            # 加载HTML文件
            page.goto(f"file:///{html_path.replace(os.sep, '/')}", wait_until='networkidle')

            # 等待ECharts脚本加载
            try:
                page.wait_for_function('typeof echarts !== "undefined"', timeout=10000)
            except:
                print("  警告: ECharts加载超时，继续渲染...")

            # 等待图表渲染完成（检测标记或超时）
            try:
                page.wait_for_function('window.chartsRendered === true', timeout=15000)
                print("  图表渲染完成")
            except:
                print("  警告: 图表渲染检测超时，继续生成PDF...")

            # 额外等待确保渲染稳定
            page.wait_for_timeout(2000)

            # 额外等待所有图表容器有内容
            try:
                page.wait_for_function('''
                    const charts = document.querySelectorAll('[id$="Chart"]');
                    let ready = true;
                    charts.forEach(c => {
                        if (c.offsetWidth < 100 || c.offsetHeight < 100) ready = false;
                    });
                    return ready;
                ''', timeout=5000)
            except:
                pass

            # 获取页面实际高度
            page_height = page.evaluate('document.documentElement.scrollHeight')
            page_width = page.evaluate('document.documentElement.scrollWidth')

            # 生成单页PDF，宽度固定1500，高度根据内容自动调整
            page.pdf(
                path=pdf_path,
                width=f'{max(page_width, 1500)}px',
                height=f'{page_height + 100}px',  # 加一点余量
                print_background=True,
                margin={
                    'top': '0mm',
                    'bottom': '0mm',
                    'left': '0mm',
                    'right': '0mm'
                }
            )

            browser.close()

        print(f"PDF生成成功（单页长页面）: {pdf_path}")
        return True

    except Exception as e:
        error_msg = str(e)
        print(f"\nPDF生成失败: {error_msg}")

        # 提供针对性解决方案
        if "Executable doesn't exist" in error_msg:
            print("\n原因: Chromium浏览器内核未安装")
            print("解决: 运行 playwright install chromium")
        elif "browser" in error_msg.lower():
            print("\n原因: Copaw环境可能限制了浏览器运行")
            print("解决: 联系Copaw管理员，或使用HTML格式输出")
        else:
            print("\n原因: 未知错误")
            print(f"详情: {error_msg}")

        return False


def html_to_image(html_path: str, image_path: str, wait_time: int = 3000,
                  full_page: bool = True, width: int = 1200,
                  auto_setup: bool = True) -> bool:
    """
    将HTML文件转换为图片

    Args:
        html_path: HTML文件路径
        image_path: 输出图片路径
        wait_time: 等待图表渲染的时间（毫秒）
        full_page: 是否截取完整页面
        width: 页面宽度
        auto_setup: 是否自动检测和安装Playwright环境

    Returns:
        是否成功
    """
    if auto_setup:
        available, msg = try_setup_playwright()
        if not available:
            print(f"\n图片生成环境不可用: {msg}")
            return False

    try:
        from playwright.sync_api import sync_playwright

        html_path = os.path.abspath(html_path)
        image_path = os.path.abspath(image_path)
        os.makedirs(os.path.dirname(image_path), exist_ok=True)

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={'width': width, 'height': 900})

            page.goto(f"file:///{html_path.replace(os.sep, '/')}")
            page.wait_for_timeout(wait_time)

            if full_page:
                page.screenshot(path=image_path, full_page=True)
            else:
                page.screenshot(path=image_path)

            browser.close()

        print(f"图片已生成: {image_path}")
        return True

    except Exception as e:
        print(f"图片生成失败: {e}")
        return False


def generate_dashboard_pdf(html_dir: str, output_dir: str, stat_month: str,
                           auto_setup: bool = True) -> dict:
    """
    生成看板PDF文件

    Args:
        html_dir: HTML文件目录
        output_dir: 输出目录
        stat_month: 统计月份
        auto_setup: 是否自动检测和安装Playwright环境

    Returns:
        生成的文件路径字典
    """
    result = {'pdf': [], 'images': [], 'html': [], 'errors': []}

    # 先检测环境状态
    if auto_setup:
        status = get_playwright_status()
        if not status['can_generate_pdf']:
            print(f"\n[警告] PDF生成环境不可用: {status.get('solution', '')}")
            print("将输出HTML格式作为替代方案")

    # 看板文件列表
    dashboards = [
        (f'商户收款看板_{stat_month}.html', f'商户收款看板_{stat_month}.pdf'),
        (f'立刷产品看板_{stat_month}.html', f'立刷产品看板_{stat_month}.pdf'),
    ]

    for html_name, pdf_name in dashboards:
        html_path = os.path.join(html_dir, html_name)
        pdf_path = os.path.join(output_dir, pdf_name)

        if os.path.exists(html_path):
            # 尝试生成PDF
            success = html_to_pdf(html_path, pdf_path, auto_setup=auto_setup)
            if success:
                result['pdf'].append(pdf_path)
            else:
                result['errors'].append(f'{pdf_name}: PDF生成失败')
                # 保留HTML作为替代
                result['html'].append(html_path)

                # 同时生成图片（可选）
                image_name = pdf_name.replace('.pdf', '.png')
                image_path = os.path.join(output_dir, image_name)
                if html_to_image(html_path, image_path, auto_setup=False):
                    result['images'].append(image_path)

    return result


if __name__ == '__main__':
    # 测试或诊断
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == '--check':
        # 诊断模式
        print("=" * 50)
        print("Playwright环境诊断")
        print("=" * 50)
        status = get_playwright_status()
        print(f"\nPlaywright库: {'已安装' if status['playwright_installed'] else '未安装'}")
        print(f"Chromium内核: {'已安装' if status['chromium_installed'] else '未安装'}")
        print(f"PDF生成可用: {'是' if status['can_generate_pdf'] else '否'}")
        if status['error_type']:
            print(f"问题类型: {status['error_type']}")
        if status['solution']:
            print(f"解决方案: {status['solution']}")

        if not status['can_generate_pdf']:
            print("\n" + "=" * 50)
            print("尝试自动修复...")
            print("=" * 50)
            success, msg = auto_install_playwright()
            print(f"\n结果: {msg}")

    elif len(sys.argv) > 2:
        html_file = sys.argv[1]
        pdf_file = sys.argv[2]
        html_to_pdf(html_file, pdf_file)
    elif len(sys.argv) > 1:
        html_file = sys.argv[1]
        pdf_file = html_file.replace('.html', '.pdf')
        html_to_pdf(html_file, pdf_file)
    else:
        print("用法:")
        print("  python pdf_generator.py --check       # 诊断Playwright环境")
        print("  python pdf_generator.py <html_file>   # 转换HTML为PDF")
        print("  python pdf_generator.py <html> <pdf>  # 指定输出路径")
        print("\n首次使用会自动安装Playwright环境")