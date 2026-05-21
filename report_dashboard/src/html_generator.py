# -*- coding: utf-8 -*-
"""
HTML看板生成模块
生成商务风格的数据看板HTML文件
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, Any, List

# 添加路径以支持导入
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template_config_manager import get_template_config_manager


def format_number(value, decimal_places=0):
    """
    格式化数字为千分位格式

    Args:
        value: 数值
        decimal_places: 小数位数

    Returns:
        格式化后的字符串
    """
    try:
        if value is None:
            return '0'
        num = float(value)
        if decimal_places > 0:
            return f"{num:,.{decimal_places}f}"
        else:
            return f"{int(round(num)):,}"
    except:
        return '0'


def generate_large_pos_dashboard_html(data: Dict) -> str:
    """
    生成商户收款看板HTML（大POS）- 独立文件

    Args:
        data: 商户收款看板数据

    Returns:
        HTML字符串
    """
    # 预处理图表数据（SQL已返回正确范围的数据）
    two_year_trend = data.get('two_year_trend', []) if data.get('two_year_trend') else []  # 近25个月
    monthly_trend = data.get('monthly_trend', []) if data.get('monthly_trend') else []  # 近25个月
    business_amount_trend = data.get('business_amount_trend', []) if data.get('business_amount_trend') else []  # 近13个月
    business_count_trend = data.get('business_count_trend', []) if data.get('business_count_trend') else []  # 近13个月
    branch_decline_trade = data.get('branch_decline_trade', [])[:10]
    branch_decline_merchant = data.get('branch_decline_merchant', [])[:10]
    branch_increase_trade = data.get('branch_increase_trade', [])[:10]
    branch_increase_merchant = data.get('branch_increase_merchant', [])[:10]
    merchant_decline = data.get('merchant_decline', [])[:10]
    merchant_increase = data.get('merchant_increase', [])[:10]

    # 图表数据JSON
    two_year_chart_data = json.dumps(_generate_large_two_year_data(two_year_trend))
    business_amount_chart_data = json.dumps(_generate_business_amount_data(business_amount_trend))
    business_count_chart_data = json.dumps(_generate_business_count_data(business_count_trend))

    # KPI数据（从模板读取显示配置）
    summary = data.get('summary', {})
    kpi_items = []

    # 尝试从模板读取KPI配置
    try:
        template_mgr = get_template_config_manager()
        kpi_names = template_mgr.get_visible_kpi_names('large_pos')
    except:
        # 回退到默认列表
        kpi_names = ['交易总金额', '新增商户数', '活跃商户数']

    for key in kpi_names:
        if key in summary:
            item = summary[key]
            mom_val = item.get('mom', 0)
            # 千分位格式化（整数）
            display_val = format_number(item.get('display_value', 0), decimal_places=0)
            kpi_items.append({
                'label': key,
                'value': display_val,
                'unit': item.get('unit', ''),
                'mom': mom_val
            })

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>商户收款看板 - 大POS</title>
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
    <style>
        :root {{
            --bg-primary: #f5f7fa;
            --bg-card: #ffffff;
            --border-color: #e4e7ed;
            --text-primary: #303133;
            --text-secondary: #606266;
            --text-muted: #909399;
            --color-primary: #5a7be8;
            --color-success: #67c23a;
            --color-danger: #f56c6c;
            --color-warning: #e6a23c;
            --color-info: #909399;
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            line-height: 1.5;
        }}

        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 24px 40px;
            color: white;
        }}

        .header-content {{
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .header h1 {{
            font-size: 24px;
            font-weight: 600;
            letter-spacing: 0.5px;
        }}

        .header-meta {{
            display: flex;
            align-items: center;
            gap: 16px;
        }}

        .badge {{
            background: rgba(255,255,255,0.2);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 13px;
        }}

        .main {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 24px;
        }}

        /* KPI卡片 - 自适应布局 */
        .kpi-section {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 24px;
        }}

        .kpi-card {{
            background: var(--bg-card);
            border-radius: 8px;
            padding: 24px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            transition: all 0.3s ease;
            min-width: 250px;
        }}

        .kpi-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }}

        .kpi-label {{
            font-size: 14px;
            color: var(--text-muted);
            margin-bottom: 12px;
        }}

        .kpi-value {{
            font-size: 32px;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 4px;
        }}

        .kpi-unit {{
            font-size: 14px;
            color: var(--text-secondary);
            display: inline-block;
            margin-left: 4px;
        }}

        .kpi-trend {{
            font-size: 13px;
            margin-top: 12px;
            padding: 4px 10px;
            border-radius: 4px;
            display: inline-block;
        }}

        .kpi-trend.up {{
            background: rgba(245, 108, 108, 0.1);
            color: var(--color-danger);
        }}

        .kpi-trend.down {{
            background: rgba(103, 194, 58, 0.1);
            color: var(--color-success);
        }}

        /* 图表区域 */
        .chart-section {{
            background: var(--bg-card);
            border-radius: 8px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            page-break-inside: avoid;
            overflow: hidden;
        }}

        .chart-title {{
            font-size: 16px;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 20px;
            padding-left: 12px;
            border-left: 3px solid var(--color-primary);
            white-space: nowrap;
        }}

        .chart-container {{
            height: 350px;
            min-height: 350px;
            width: 100%;
            min-width: 600px;
        }}

        .chart-container-lg {{
            height: 400px;
            min-height: 400px;
            width: 100%;
            min-width: 600px;
        }}

        /* 图表网格布局 */
        .charts-row {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }}

        @media (max-width: 1100px) {{
            .charts-row {{
                grid-template-columns: 1fr;
            }}
        }}

        /* 表格样式 */
        .table-section {{
            background: var(--bg-card);
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 20px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        }}

        .table-header {{
            padding: 16px 24px;
            border-bottom: 1px solid var(--border-color);
            font-size: 16px;
            font-weight: 600;
            color: var(--text-primary);
            padding-left: 36px;
            border-left: 3px solid var(--color-primary);
            white-space: nowrap;
        }}

        .data-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
            table-layout: auto;
        }}

        .data-table th {{
            background: #fafafa;
            padding: 11px 12px;
            text-align: left;
            font-weight: 600;
            color: var(--text-secondary);
            border-bottom: 1px solid var(--border-color);
            white-space: nowrap;
        }}

        .data-table td {{
            padding: 11px 12px;
            border-bottom: 1px solid #f0f0f0;
            color: var(--text-primary);
            word-break: break-word;
        }}

        .data-table tr:last-child td {{
            border-bottom: none;
        }}

        .data-table tr:hover td {{
            background: #f5f7fa;
        }}

        .rank-badge {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 22px;
            height: 22px;
            border-radius: 50%;
            font-size: 12px;
            font-weight: 600;
            background: #e4e7ed;
            color: var(--text-secondary);
        }}

        .rank-badge.top3 {{
            background: linear-gradient(135deg, #f5af19, #f12711);
            color: white;
        }}

        .trend-up {{ color: var(--color-danger); font-weight: 600; }}
        .trend-down {{ color: var(--color-success); font-weight: 600; }}

        /* 表格网格布局 - 自适应 */
        .grid-2 {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(550px, 1fr));
            gap: 20px;
        }}

        @media (max-width: 1200px) {{
            .grid-2 {{ grid-template-columns: 1fr; }}
        }}

        @media (max-width: 768px) {{
            .kpi-section {{ grid-template-columns: 1fr; }}
            .header {{ padding: 16px 20px; }}
            .main {{ padding: 16px; }}
            .chart-container {{ min-width: 400px; }}
            .chart-container-lg {{ min-width: 400px; }}
        }}

        /* 打印专用样式 - 单页长PDF */
        @media print {{
            body {{
                background: white;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }}

            .header {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
                padding: 16px 24px;
            }}

            .main {{
                max-width: 1400px;
                padding: 16px 24px;
            }}

            .kpi-section {{
                margin-bottom: 20px;
                gap: 16px;
            }}

            .kpi-card {{
                padding: 20px;
            }}

            .chart-section {{
                margin-bottom: 16px;
                padding: 20px;
            }}

            .table-section {{
                margin-bottom: 16px;
            }}

            .grid-2 {{
                gap: 16px;
            }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <div class="header-content">
            <h1>商户收款看板</h1>
            <div class="header-meta">
                <span class="badge">大POS</span>
                <span class="badge">{data.get('latest_month', '')}</span>
                <span class="badge">更新: {data.get('update_time', '')}</span>
            </div>
        </div>
    </header>

    <main class="main">
        <!-- KPI Cards -->
        <section class="kpi-section">
            {_generate_kpi_cards_html(kpi_items)}
        </section>

        <!-- 近两年运营趋势 -->
        <section class="chart-section">
            <h3 class="chart-title">近两年运营趋势</h3>
            <div id="twoYearChart" class="chart-container"></div>
        </section>

        <!-- 业务类型趋势 -->
        <div class="grid-2">
            <section class="chart-section">
                <h3 class="chart-title">各业务类型近一年交易金额趋势</h3>
                <div id="businessAmountChart" class="chart-container-lg"></div>
            </section>
            <section class="chart-section">
                <h3 class="chart-title">各业务类型近一年交易笔数趋势</h3>
                <div id="businessCountChart" class="chart-container-lg"></div>
            </section>
        </div>

        <!-- 分公司排名 -->
        <div class="grid-2">
            <section class="table-section">
                <h3 class="table-header">分公司交易金额环比下降TOP10</h3>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>排名</th>
                            <th>归属分公司</th>
                            <th>上月交易额(万)</th>
                            <th>本月交易额(万)</th>
                            <th>环比</th>
                        </tr>
                    </thead>
                    <tbody>
                        {_generate_branch_table_rows(branch_decline_trade)}
                    </tbody>
                </table>
            </section>

            <section class="table-section">
                <h3 class="table-header">分公司新增商户环比下降TOP10</h3>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>排名</th>
                            <th>归属分公司</th>
                            <th>上月商户数</th>
                            <th>本月商户数</th>
                            <th>环比</th>
                        </tr>
                    </thead>
                    <tbody>
                        {_generate_branch_merchant_table_rows(branch_decline_merchant)}
                    </tbody>
                </table>
            </section>
        </div>

        <!-- 分公司上涨排名（已隐藏，数据保留） -->

        <!-- 商户排名 -->
        <div class="grid-2">
            <section class="table-section">
                <h3 class="table-header">商户交易金额环比上涨TOP10</h3>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>排名</th>
                            <th>商户名</th>
                            <th>上月交易额(万)</th>
                            <th>本月交易额(万)</th>
                            <th>环比</th>
                        </tr>
                    </thead>
                    <tbody>
                        {_generate_merchant_table_rows(merchant_increase, 'increase')}
                    </tbody>
                </table>
            </section>

            <section class="table-section">
                <h3 class="table-header">商户交易金额环比下降TOP10</h3>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>排名</th>
                            <th>商户名</th>
                            <th>上月交易额(万)</th>
                            <th>本月交易额(万)</th>
                            <th>环比</th>
                        </tr>
                    </thead>
                    <tbody>
                        {_generate_merchant_table_rows(merchant_decline, 'decline')}
                    </tbody>
                </table>
            </section>
        </div>
    </main>

    <script>
        // 图表数据
        const twoYearData = {two_year_chart_data};
        const businessAmountData = {business_amount_chart_data};
        const businessCountData = {business_count_chart_data};

        // tooltip按数值降序排序函数
        function sortTooltip(params) {{
            params.sort(function(a, b) {{
                return b.value - a.value;
            }});
            var result = params[0].axisValue + '<br/>';
            params.forEach(function(item) {{
                // 千分位格式化数值
                var val = item.value;
                if (typeof val === 'number') {{
                    // 整数用千分位，小数保留1位
                    if (Number.isInteger(val)) {{
                        val = val.toLocaleString('zh-CN');
                    }} else {{
                        val = val.toLocaleString('zh-CN', {{minimumFractionDigits: 1, maximumFractionDigits: 1}});
                    }}
                }}
                result += item.marker + ' ' + item.seriesName + ': <strong>' + val + '</strong><br/>';
            }});
            return result;
        }}

        // 近两年运营趋势图
        const twoYearChart = echarts.init(document.getElementById('twoYearChart'));
        twoYearChart.setOption({{
            tooltip: {{ trigger: 'axis', formatter: sortTooltip }},
            legend: {{ data: ['交易总金额', '新增商户数', '活跃商户数'], bottom: 0 }},
            grid: {{ left: '30px', right: '10px', bottom: '50px', top: '30px', containLabel: true }},
            xAxis: {{ type: 'category', data: twoYearData.months, axisLabel: {{ rotate: 45, color: '#606266' }} }},
            yAxis: [
                {{ type: 'value', name: '万元', position: 'left', axisLabel: {{ color: '#606266' }} }},
                {{ type: 'value', name: '户数', position: 'right', axisLabel: {{ color: '#e6a23c' }} }}
            ],
            series: [
                {{
                    name: '交易总金额',
                    type: 'bar',
                    data: twoYearData.amounts,
                    itemStyle: {{ color: '#5a7be8', borderRadius: [2, 2, 0, 0] }},
                    label: {{ show: true, position: 'top', fontSize: 10, color: '#5a7be8', formatter: function(p) {{ return p.value.value ? p.value.value.toLocaleString('zh-CN') : p.value.toLocaleString('zh-CN'); }} }}
                }},
                {{
                    name: '新增商户数',
                    type: 'line',
                    yAxisIndex: 1,
                    smooth: true,
                    data: twoYearData.newMerchants,
                    itemStyle: {{ color: '#67c23a' }},
                    label: {{ show: true, position: 'top', fontSize: 10, color: '#67c23a', formatter: function(p) {{ return p.value.value ? p.value.value.toLocaleString('zh-CN') : p.value.toLocaleString('zh-CN'); }} }}
                }},
                {{
                    name: '活跃商户数',
                    type: 'line',
                    yAxisIndex: 1,
                    smooth: true,
                    data: twoYearData.activeUsers,
                    itemStyle: {{ color: '#e6a23c' }},
                    label: {{ show: true, position: 'top', fontSize: 10, color: '#e6a23c', formatter: function(p) {{ return p.value.value ? p.value.value.toLocaleString('zh-CN') : p.value.toLocaleString('zh-CN'); }} }}
                }}
            ]
        }});

        // 业务类型交易金额趋势
        const businessAmountChart = echarts.init(document.getElementById('businessAmountChart'));
        businessAmountChart.setOption({{
            tooltip: {{ trigger: 'axis', formatter: sortTooltip }},
            legend: {{ data: ['外接码付', '理财POS', '传统POS'], bottom: 0 }},
            grid: {{ left: '30px', right: '10px', bottom: '50px', top: '30px', containLabel: true }},
            xAxis: {{ type: 'category', data: businessAmountData.months, axisLabel: {{ rotate: 45, color: '#606266' }} }},
            yAxis: {{ type: 'value', name: '万元', axisLabel: {{ color: '#606266' }} }},
            series: businessAmountData.series
        }});

        // 业务类型交易笔数趋势
        const businessCountChart = echarts.init(document.getElementById('businessCountChart'));
        businessCountChart.setOption({{
            tooltip: {{ trigger: 'axis', formatter: sortTooltip }},
            legend: {{ data: ['外接码付', '理财POS', '传统POS'], bottom: 0 }},
            grid: {{ left: '30px', right: '10px', bottom: '50px', top: '30px', containLabel: true }},
            xAxis: {{ type: 'category', data: businessCountData.months, axisLabel: {{ rotate: 45, color: '#606266' }} }},
            yAxis: {{ type: 'value', name: '万笔', axisLabel: {{ color: '#606266' }} }},
            series: businessCountData.series
        }});

        // 标记图表渲染完成
        window.chartsRendered = true;
        console.log('All charts rendered successfully');

        window.addEventListener('resize', () => {{
            twoYearChart.resize();
            businessAmountChart.resize();
            businessCountChart.resize();
        }});
    </script>
</body>
</html>'''

    return html


def generate_small_pos_dashboard_html(data: Dict) -> str:
    """
    生成立刷产品看板HTML（小POS）- 独立文件

    Args:
        data: 立刷产品看板数据

    Returns:
        HTML字符串
    """

    # 预处理图表数据（SQL已返回正确范围的数据）
    monthly_trend = data.get('monthly_trend', []) if data.get('monthly_trend') else []  # 近25个月
    product_amount = data.get('product_amount_trend', []) if data.get('product_amount_trend') else []  # 近13个月
    product_terminal = data.get('product_terminal_trend', []) if data.get('product_terminal_trend') else []  # 近13个月
    term_trend = data.get('term_trend', []) if data.get('term_trend') else []  # 近25个月终端绑定、激活、活跃趋势
    agent_decline_trade = data.get('agent_decline_trade', [])[:10]
    agent_decline_merchant = data.get('agent_decline_merchant', [])[:10]
    agent_increase_trade = data.get('agent_increase_trade', [])[:10]
    agent_increase_merchant = data.get('agent_increase_merchant', [])[:10]

    # 图表数据JSON
    two_year_chart_data = json.dumps(_generate_small_two_year_data(monthly_trend))
    avg_terminal_chart_data = json.dumps(_generate_avg_terminal_data(monthly_trend))  # 笔均台均取近25个月
    product_chart_data = json.dumps(_generate_product_trend_data(product_amount))
    terminal_chart_data = json.dumps(_generate_terminal_trend_data(product_terminal))
    term_trend_chart_data = json.dumps(_generate_term_trend_data(term_trend))  # 终端绑定、激活、活跃趋势

    # KPI数据（从模板读取显示配置）
    summary = data.get('summary', {})
    kpi_items = []

    # 尝试从模板读取KPI配置
    try:
        template_mgr = get_template_config_manager()
        kpi_names = template_mgr.get_visible_kpi_names('small_pos')
    except:
        # 回退到默认列表
        kpi_names = ['交易总金额', '新增商户数', '活跃商户数']

    for key in kpi_names:
        if key in summary:
            item = summary[key]
            mom_val = item.get('mom', 0)
            # 千分位格式化（整数）
            display_val = format_number(item.get('display_value', 0), decimal_places=0)
            kpi_items.append({
                'label': key,
                'value': display_val,
                'unit': item.get('unit', ''),
                'mom': mom_val
            })

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>立刷产品看板 - 小POS</title>
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
    <style>
        :root {{
            --bg-primary: #f5f7fa;
            --bg-card: #ffffff;
            --border-color: #e4e7ed;
            --text-primary: #303133;
            --text-secondary: #606266;
            --text-muted: #909399;
            --color-primary: #36a3eb;
            --color-success: #67c23a;
            --color-danger: #f56c6c;
            --color-warning: #e6a23c;
            --color-info: #909399;
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            line-height: 1.5;
        }}

        .header {{
            background: linear-gradient(135deg, #36a3eb 0%, #5b86e5 100%);
            padding: 24px 40px;
            color: white;
        }}

        .header-content {{
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .header h1 {{
            font-size: 24px;
            font-weight: 600;
            letter-spacing: 0.5px;
        }}

        .header-meta {{
            display: flex;
            align-items: center;
            gap: 16px;
        }}

        .badge {{
            background: rgba(255,255,255,0.2);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 13px;
        }}

        .main {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 24px;
        }}

        /* KPI卡片 - 自适应布局 */
        .kpi-section {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 24px;
        }}

        .kpi-card {{
            background: var(--bg-card);
            border-radius: 8px;
            padding: 24px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            transition: all 0.3s ease;
            min-width: 250px;
        }}

        .kpi-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }}

        .kpi-label {{
            font-size: 14px;
            color: var(--text-muted);
            margin-bottom: 12px;
        }}

        .kpi-value {{
            font-size: 32px;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 4px;
        }}

        .kpi-unit {{
            font-size: 14px;
            color: var(--text-secondary);
            display: inline-block;
            margin-left: 4px;
        }}

        .kpi-trend {{
            font-size: 13px;
            margin-top: 12px;
            padding: 4px 10px;
            border-radius: 4px;
            display: inline-block;
        }}

        .kpi-trend.up {{
            background: rgba(245, 108, 108, 0.1);
            color: var(--color-danger);
        }}

        .kpi-trend.down {{
            background: rgba(103, 194, 58, 0.1);
            color: var(--color-success);
        }}

        /* 图表区域 */
        .chart-section {{
            background: var(--bg-card);
            border-radius: 8px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            page-break-inside: avoid;
            overflow: hidden;
        }}

        .chart-title {{
            font-size: 16px;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 20px;
            padding-left: 12px;
            border-left: 3px solid var(--color-primary);
            white-space: nowrap;
        }}

        .chart-container {{
            height: 350px;
            min-height: 350px;
            width: 100%;
            min-width: 600px;
        }}

        .chart-container-lg {{
            height: 400px;
            min-height: 400px;
            width: 100%;
            min-width: 600px;
        }}

        /* 图表网格布局 */
        .charts-row {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }}

        @media (max-width: 1100px) {{
            .charts-row {{
                grid-template-columns: 1fr;
            }}
        }}

        /* 表格样式 */
        .table-section {{
            background: var(--bg-card);
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 20px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        }}

        .table-header {{
            padding: 16px 24px;
            border-bottom: 1px solid var(--border-color);
            font-size: 16px;
            font-weight: 600;
            color: var(--text-primary);
            padding-left: 36px;
            border-left: 3px solid var(--color-primary);
            white-space: nowrap;
        }}

        .data-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
            table-layout: auto;
        }}

        .data-table th {{
            background: #fafafa;
            padding: 11px 12px;
            text-align: left;
            font-weight: 600;
            color: var(--text-secondary);
            border-bottom: 1px solid var(--border-color);
            white-space: nowrap;
        }}

        .data-table td {{
            padding: 11px 12px;
            border-bottom: 1px solid #f0f0f0;
            color: var(--text-primary);
            word-break: break-word;
        }}

        .data-table tr:last-child td {{
            border-bottom: none;
        }}

        .data-table tr:hover td {{
            background: #f5f7fa;
        }}

        .rank-badge {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 22px;
            height: 22px;
            border-radius: 50%;
            font-size: 12px;
            font-weight: 600;
            background: #e4e7ed;
            color: var(--text-secondary);
        }}

        .rank-badge.top3 {{
            background: linear-gradient(135deg, #f5af19, #f12711);
            color: white;
        }}

        .trend-up {{ color: var(--color-danger); font-weight: 600; }}
        .trend-down {{ color: var(--color-success); font-weight: 600; }}

        /* 表格网格布局 - 自适应 */
        .grid-2 {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(550px, 1fr));
            gap: 20px;
        }}

        @media (max-width: 1200px) {{
            .grid-2 {{ grid-template-columns: 1fr; }}
        }}

        @media (max-width: 768px) {{
            .kpi-section {{ grid-template-columns: 1fr; }}
            .header {{ padding: 16px 20px; }}
            .main {{ padding: 16px; }}
            .chart-container {{ min-width: 400px; }}
            .chart-container-lg {{ min-width: 400px; }}
        }}

        /* 打印专用样式 - 单页长PDF */
        @media print {{
            body {{
                background: white;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }}

            .header {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
                padding: 16px 24px;
            }}

            .main {{
                max-width: 1400px;
                padding: 16px 24px;
            }}

            .kpi-section {{
                margin-bottom: 20px;
                gap: 16px;
            }}

            .kpi-card {{
                padding: 20px;
            }}

            .chart-section {{
                margin-bottom: 16px;
                padding: 20px;
            }}

            .table-section {{
                margin-bottom: 16px;
            }}

            .grid-2 {{
                gap: 16px;
            }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <div class="header-content">
            <h1>立刷产品看板</h1>
            <div class="header-meta">
                <span class="badge">小POS</span>
                <span class="badge">{data.get('latest_month', '')}</span>
                <span class="badge">更新: {data.get('update_time', '')}</span>
            </div>
        </div>
    </header>

    <main class="main">
        <!-- KPI Cards -->
        <section class="kpi-section">
            {_generate_kpi_cards_html(kpi_items)}
        </section>

        <!-- 近两年运营趋势 -->
        <section class="chart-section">
            <h3 class="chart-title">近两年运营趋势</h3>
            <div id="twoYearChart" class="chart-container"></div>
        </section>

        <!-- 笔均&台均趋势 -->
        <section class="chart-section">
            <h3 class="chart-title">近两年笔均&台均金额趋势</h3>
            <div id="avgTerminalChart" class="chart-container"></div>
        </section>

        <!-- 终端绑定、激活、活跃趋势图 -->
        <section class="chart-section">
            <h3 class="chart-title">近两年终端绑定、激活、活跃趋势</h3>
            <div id="termTrendChart" class="chart-container"></div>
        </section>

        <!-- 产品趋势图 -->
        <div class="grid-2">
            <section class="chart-section">
                <h3 class="chart-title">各产品交易金额趋势</h3>
                <div id="productChart" class="chart-container-lg"></div>
            </section>
            <section class="chart-section">
                <h3 class="chart-title">各产品新增终端趋势</h3>
                <div id="terminalChart" class="chart-container-lg"></div>
            </section>
        </div>

        <!-- 服务商排名 -->
        <div class="grid-2">
            <section class="table-section">
                <h3 class="table-header">服务商交易金额环比下降TOP10</h3>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>排名</th>
                            <th>服务商名称</th>
                            <th>上月交易额(万)</th>
                            <th>本月交易额(万)</th>
                            <th>环比</th>
                        </tr>
                    </thead>
                    <tbody>
                        {_generate_agent_table_rows(agent_decline_trade)}
                    </tbody>
                </table>
            </section>

            <section class="table-section">
                <h3 class="table-header">服务商新增商户环比下降TOP10</h3>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>排名</th>
                            <th>服务商名称</th>
                            <th>上月商户数</th>
                            <th>本月商户数</th>
                            <th>环比</th>
                        </tr>
                    </thead>
                    <tbody>
                        {_generate_agent_merchant_table_rows(agent_decline_merchant)}
                    </tbody>
                </table>
            </section>
        </div>

        <!-- 服务商上涨排名（已隐藏，数据保留） -->
    </main>

    <script>
        // 图表数据
        const twoYearData = {two_year_chart_data};
        const avgTerminalData = {avg_terminal_chart_data};
        const termTrendData = {term_trend_chart_data};
        const productData = {product_chart_data};
        const terminalData = {terminal_chart_data};

        // tooltip按数值降序排序函数
        function sortTooltip(params) {{
            params.sort(function(a, b) {{
                return b.value - a.value;
            }});
            var result = params[0].axisValue + '<br/>';
            params.forEach(function(item) {{
                // 千分位格式化数值
                var val = item.value;
                if (typeof val === 'number') {{
                    // 整数用千分位，小数保留1位
                    if (Number.isInteger(val)) {{
                        val = val.toLocaleString('zh-CN');
                    }} else {{
                        val = val.toLocaleString('zh-CN', {{minimumFractionDigits: 1, maximumFractionDigits: 1}});
                    }}
                }}
                result += item.marker + ' ' + item.seriesName + ': <strong>' + val + '</strong><br/>';
            }});
            return result;
        }}

        // 近两年运营趋势图
        const twoYearChart = echarts.init(document.getElementById('twoYearChart'));
        twoYearChart.setOption({{
            tooltip: {{ trigger: 'axis', formatter: sortTooltip }},
            legend: {{ data: ['交易总金额', '新增商户数'], bottom: 0 }},
            grid: {{ left: '30px', right: '10px', bottom: '50px', top: '30px', containLabel: true }},
            xAxis: {{ type: 'category', data: twoYearData.months, axisLabel: {{ rotate: 45, color: '#606266' }} }},
            yAxis: [
                {{ type: 'value', name: '万元', position: 'left', axisLabel: {{ color: '#606266' }} }},
                {{ type: 'value', name: '户数', position: 'right', axisLabel: {{ color: '#67c23a' }} }}
            ],
            series: [
                {{
                    name: '交易总金额',
                    type: 'bar',
                    data: twoYearData.amounts,
                    itemStyle: {{ color: '#36a3eb', borderRadius: [2, 2, 0, 0] }},
                    label: {{ show: true, position: 'top', fontSize: 10, color: '#36a3eb', formatter: function(p) {{ return p.value.value ? p.value.value.toLocaleString('zh-CN') : p.value.toLocaleString('zh-CN'); }} }}
                }},
                {{
                    name: '新增商户数',
                    type: 'line',
                    yAxisIndex: 1,
                    smooth: true,
                    data: twoYearData.newMerchants,
                    itemStyle: {{ color: '#67c23a' }},
                    label: {{ show: true, position: 'top', fontSize: 10, color: '#67c23a', formatter: function(p) {{ return p.value.value ? p.value.value.toLocaleString('zh-CN') : p.value.toLocaleString('zh-CN'); }} }}
                }}
            ]
        }});

        // 笔均&台均趋势图（单Y轴）
        const avgTerminalChart = echarts.init(document.getElementById('avgTerminalChart'));
        avgTerminalChart.setOption({{
            tooltip: {{ trigger: 'axis', formatter: sortTooltip }},
            legend: {{ data: ['笔均交易金额', '台均交易金额'], bottom: 0 }},
            grid: {{ left: '30px', right: '10px', bottom: '50px', top: '30px', containLabel: true }},
            xAxis: {{ type: 'category', data: avgTerminalData.months, axisLabel: {{ rotate: 45, color: '#606266' }} }},
            yAxis: {{ type: 'value', name: '元', axisLabel: {{ color: '#606266' }} }},
            series: [
                {{
                    name: '笔均交易金额',
                    type: 'line',
                    smooth: true,
                    data: avgTerminalData.avgAmount,
                    itemStyle: {{ color: '#36a3eb' }},
                    label: {{ show: true, position: 'top', fontSize: 10, color: '#36a3eb', formatter: function(p) {{ return p.value.value ? p.value.value.toLocaleString('zh-CN') : p.value.toLocaleString('zh-CN'); }} }}
                }},
                {{
                    name: '台均交易金额',
                    type: 'line',
                    smooth: true,
                    data: avgTerminalData.terminalAmount,
                    itemStyle: {{ color: '#e6a23c' }},
                    label: {{ show: true, position: 'top', fontSize: 10, color: '#e6a23c', formatter: function(p) {{ return p.value.value ? p.value.value.toLocaleString('zh-CN') : p.value.toLocaleString('zh-CN'); }} }}
                }}
            ]
        }});

        // 终端绑定、激活、活跃趋势图（柱状图+折线图混合）
        const termTrendChart = echarts.init(document.getElementById('termTrendChart'));
        termTrendChart.setOption({{
            tooltip: {{
                trigger: 'axis',
                formatter: function(params) {{
                    let result = params[0].axisValue + '<br/>';
                    // 按数值降序排序
                    params.sort((a, b) => b.value - a.value);
                    params.forEach(item => {{
                        const val = typeof item.value === 'object' ? item.value.value : item.value;
                        result += item.marker + item.seriesName + ': ' + val.toLocaleString('zh-CN') + ' 台<br/>';
                    }});
                    return result;
                }}
            }},
            legend: {{ data: ['新增终端绑定', '一阶段激活数', '活跃商户数'], bottom: 0 }},
            grid: {{ left: '30px', right: '10px', bottom: '50px', top: '30px', containLabel: true }},
            xAxis: {{ type: 'category', data: termTrendData.months, axisLabel: {{ rotate: 45, color: '#606266' }} }},
            yAxis: [
                {{
                    type: 'value',
                    name: '台',
                    position: 'left',
                    axisLabel: {{ color: '#606266', formatter: function(val) {{ return val.toLocaleString('zh-CN'); }} }}
                }},
                {{
                    type: 'value',
                    name: '台',
                    position: 'right',
                    axisLabel: {{ color: '#e6a23c', formatter: function(val) {{ return val.toLocaleString('zh-CN'); }} }},
                    splitLine: {{ show: false }}
                }}
            ],
            series: [
                {{
                    name: '新增终端绑定',
                    type: 'bar',
                    yAxisIndex: 0,
                    barGap: '10%',
                    data: termTrendData.bindTerminals,
                    itemStyle: {{ color: '#36a3eb' }},
                    label: {{ show: true, position: 'top', fontSize: 10, color: '#36a3eb' }}
                }},
                {{
                    name: '一阶段激活数',
                    type: 'bar',
                    yAxisIndex: 0,
                    data: termTrendData.activeTerminals,
                    itemStyle: {{ color: '#67c23a' }},
                    label: {{ show: true, position: 'top', fontSize: 10, color: '#67c23a' }}
                }},
                {{
                    name: '活跃商户数',
                    type: 'line',
                    yAxisIndex: 1,
                    smooth: true,
                    data: termTrendData.activeMerchants,
                    itemStyle: {{ color: '#e6a23c' }},
                    lineStyle: {{ width: 2 }},
                    symbol: 'circle',
                    symbolSize: 6,
                    label: {{ show: true, position: 'top', fontSize: 10, color: '#e6a23c' }}
                }}
            ]
        }});

        // 各产品交易金额趋势
        const productChart = echarts.init(document.getElementById('productChart'));
        productChart.setOption({{
            tooltip: {{ trigger: 'axis', formatter: sortTooltip }},
            legend: {{ data: productData.legend, bottom: 0, type: 'scroll' }},
            grid: {{ left: '30px', right: '10px', bottom: '60px', top: '30px', containLabel: true }},
            xAxis: {{ type: 'category', data: productData.months, axisLabel: {{ rotate: 45, color: '#606266' }} }},
            yAxis: {{ type: 'value', name: '亿元', axisLabel: {{ color: '#606266' }} }},
            series: productData.series
        }});

        // 各产品新增终端趋势
        const terminalChart = echarts.init(document.getElementById('terminalChart'));
        terminalChart.setOption({{
            tooltip: {{ trigger: 'axis', formatter: sortTooltip }},
            legend: {{ data: terminalData.legend, bottom: 0, type: 'scroll' }},
            grid: {{ left: '30px', right: '10px', bottom: '60px', top: '30px', containLabel: true }},
            xAxis: {{ type: 'category', data: terminalData.months, axisLabel: {{ rotate: 45, color: '#606266' }} }},
            yAxis: {{ type: 'value', name: '万台', axisLabel: {{ color: '#606266' }} }},
            series: terminalData.series
        }});

        // 标记图表渲染完成
        window.chartsRendered = true;
        console.log('All charts rendered successfully');

        window.addEventListener('resize', () => {{
            twoYearChart.resize();
            avgTerminalChart.resize();
            termTrendChart.resize();
            productChart.resize();
            terminalChart.resize();
        }});
    </script>
</body>
</html>'''

    return html


# ========== 辅助函数 ==========

def _generate_kpi_cards_html(kpi_items: List[Dict]) -> str:
    """生成KPI卡片HTML"""
    html = ''
    for item in kpi_items:
        mom_val = item.get('mom', 0)
        trend_class = 'up' if mom_val >= 0 else 'down'
        arrow = '↑' if mom_val >= 0 else '↓'

        html += f'''
            <div class="kpi-card">
                <div class="kpi-label">{item['label']}</div>
                <div class="kpi-value">{item['value']}<span class="kpi-unit">{item['unit']}</span></div>
                <div class="kpi-trend {trend_class}">环比 {arrow} {abs(mom_val):.2f}%</div>
            </div>'''
    return html


def _generate_large_two_year_data(trend_data: List) -> Dict:
    """生成大POS近两年趋势图数据"""
    if not trend_data:
        return {'months': [], 'amounts': [], 'newMerchants': [], 'activeUsers': []}

    n = len(trend_data)
    months = []
    amounts = []
    newMerchants = []
    activeUsers = []

    for idx, d in enumerate(trend_data):
        months.append(d.get('时间', ''))
        # 稀疏标签：近2年数据较多，每2个月显示一次，最新月和次新月必须显示
        show_label = False
        if n > 0:
            pos_from_end = n - 1 - idx
            if pos_from_end == 0 or pos_from_end == 1:  # 最新月和次新月
                show_label = True
            elif pos_from_end % 2 == 0:  # 每2个月显示一次
                show_label = True
        amounts.append({'value': float(d.get('交易总金额（万元）', 0) or 0), 'label': {'show': show_label}})
        newMerchants.append({'value': float(d.get('新增商户数', 0) or 0), 'label': {'show': show_label}})
        activeUsers.append({'value': float(d.get('活跃商户数', 0) or 0), 'label': {'show': show_label}})

    return {
        'months': months,
        'amounts': amounts,
        'newMerchants': newMerchants,
        'activeUsers': activeUsers
    }


def _generate_small_two_year_data(trend_data: List) -> Dict:
    """生成小POS近两年趋势图数据"""
    if not trend_data:
        return {'months': [], 'amounts': [], 'newMerchants': []}

    n = len(trend_data)
    months = []
    amounts = []
    newMerchants = []

    for idx, d in enumerate(trend_data):
        months.append(d.get('月份', ''))
        # 稀疏标签：每2个月显示一次，最新月和次新月必须显示
        show_label = False
        if n > 0:
            pos_from_end = n - 1 - idx
            if pos_from_end == 0 or pos_from_end == 1:
                show_label = True
            elif pos_from_end % 2 == 0:
                show_label = True
        amounts.append({'value': float(d.get('交易总金额（万元）', 0) or 0), 'label': {'show': show_label}})
        newMerchants.append({'value': float(d.get('新增商户数', 0) or 0), 'label': {'show': show_label}})

    return {
        'months': months,
        'amounts': amounts,
        'newMerchants': newMerchants
    }


def _generate_term_trend_data(trend_data: List) -> Dict:
    """生成终端绑定、激活、活跃趋势图数据
    新增终端绑定、一阶段激活数：左Y轴，柱状图非堆叠
    活跃商户数：右Y轴，折线图
    """
    if not trend_data:
        return {'months': [], 'bindTerminals': [], 'activeTerminals': [], 'activeMerchants': []}

    n = len(trend_data)
    months = [d.get('月份', '') for d in trend_data]

    # 柱状图数据（左Y轴）
    bind_terminals = []
    active_terminals = []
    # 折线图数据（右Y轴）
    active_merchants = []

    for idx, d in enumerate(trend_data):
        # 稀疏标签逻辑：每2个月显示一次，最新月和次新月必须显示
        show_label = False
        if n > 0:
            pos_from_end = n - 1 - idx
            if pos_from_end == 0 or pos_from_end == 1:
                show_label = True
            elif pos_from_end % 2 == 0:
                show_label = True

        bind_terminals.append({'value': float(d.get('新增终端绑定（台）', 0) or 0), 'label': {'show': show_label}})
        active_terminals.append({'value': float(d.get('一阶段激活数（台）', 0) or 0), 'label': {'show': show_label}})
        active_merchants.append({'value': float(d.get('活跃商户数（台）', 0) or 0), 'label': {'show': show_label}})

    return {
        'months': months,
        'bindTerminals': bind_terminals,
        'activeTerminals': active_terminals,
        'activeMerchants': active_merchants
    }


def _generate_avg_terminal_data(trend_data: List) -> Dict:
    """生成笔均&台均趋势图数据
    笔均交易金额（元）=交易金额(万元)/交易笔数(万笔)
    台均交易金额（元）=交易金额(万元)*10000/活跃商户数
    """
    if not trend_data:
        return {'months': [], 'avgAmount': [], 'terminalAmount': []}

    n = len(trend_data)
    months = []
    avg_amounts = []
    terminal_amounts = []

    for idx, d in enumerate(trend_data):
        months.append(d.get('月份', ''))
        total_amount = float(d.get('交易总金额（万元）', 0) or 0)
        total_count = float(d.get('交易总笔数（万笔）', 0) or 0)
        active_merchants = float(d.get('活跃商户数', 0) or 0)

        # 笔均交易金额（元）= 万元 / 万笔 = 元/笔
        if total_count > 0:
            avg_amount = round(total_amount / total_count)
        else:
            avg_amount = 0

        # 台均交易金额（元）= 万元 * 10000 / 活跃商户数
        if active_merchants > 0:
            terminal_amount = round(total_amount * 10000 / active_merchants)
        else:
            terminal_amount = 0

        # 稀疏标签逻辑
        show_label = False
        if n > 0:
            pos_from_end = n - 1 - idx
            if pos_from_end == 0 or pos_from_end == 1:
                show_label = True
            elif pos_from_end % 2 == 0:
                show_label = True
        avg_amounts.append({'value': avg_amount, 'label': {'show': show_label}})
        terminal_amounts.append({'value': terminal_amount, 'label': {'show': show_label}})

    return {
        'months': months,
        'avgAmount': avg_amounts,
        'terminalAmount': terminal_amounts
    }


def _generate_business_amount_data(monthly_data: List) -> Dict:
    """生成业务类型交易金额趋势数据"""
    if not monthly_data:
        return {'months': [], 'series': []}

    months = [d.get('月份', '') for d in monthly_data]
    n = len(monthly_data)

    colors = ['#5a7be8', '#67c23a', '#e6a23c']
    products = [
        ('外接码付', '外接码付(咕哚云)交易金额（万元）'),
        ('理财POS', '理财POS交易金额（万元）'),
        ('传统POS', '传统POS交易金额（万元）')
    ]

    series = []
    for i, (name, key) in enumerate(products):
        values = []
        for idx, d in enumerate(monthly_data):
            v = float(d.get(key, 0) or 0)
            # 稀疏标签逻辑
            show_label = False
            if n > 0:
                pos_from_end = n - 1 - idx
                if pos_from_end == 0 or pos_from_end == 1:
                    show_label = True
                elif pos_from_end % 2 == 0:
                    show_label = True
            values.append({'value': v, 'label': {'show': show_label}})
        series.append({
            'name': name,
            'type': 'line',
            'smooth': True,
            'data': values,
            'itemStyle': {'color': colors[i]},
            'label': {'show': True, 'position': 'top', 'fontSize': 12, 'color': colors[i]}
        })

    return {'months': months, 'series': series}


def _generate_business_count_data(monthly_data: List) -> Dict:
    """生成业务类型交易笔数趋势数据"""
    if not monthly_data:
        return {'months': [], 'series': []}

    months = [d.get('月份', '') for d in monthly_data]
    n = len(monthly_data)

    colors = ['#5a7be8', '#67c23a', '#e6a23c']
    products = [
        ('外接码付', '外接码付(咕哚云)交易笔数（万笔）'),
        ('理财POS', '理财POS交易笔数（万笔）'),
        ('传统POS', '传统POS交易笔数（万笔）')
    ]

    series = []
    for i, (name, key) in enumerate(products):
        values = []
        for idx, d in enumerate(monthly_data):
            v = float(d.get(key, 0) or 0)
            # 稀疏标签逻辑
            show_label = False
            if n > 0:
                pos_from_end = n - 1 - idx
                if pos_from_end == 0 or pos_from_end == 1:
                    show_label = True
                elif pos_from_end % 2 == 0:
                    show_label = True
            values.append({'value': v, 'label': {'show': show_label}})
        series.append({
            'name': name,
            'type': 'line',
            'smooth': True,
            'data': values,
            'itemStyle': {'color': colors[i]},
            'label': {'show': True, 'position': 'top', 'fontSize': 12, 'color': colors[i]}
        })

    return {'months': months, 'series': series}


def _generate_product_trend_data(product_data: List) -> Dict:
    """生成各产品交易金额趋势数据（7条线）"""
    if not product_data:
        return {'months': [], 'legend': [], 'series': []}

    data = product_data  # SQL已返回正确范围的数据
    months = [d.get('月份', '') for d in data]
    n = len(data)

    series = []
    colors = ['#36a3eb', '#67c23a', '#e6a23c', '#f56c6c', '#909399', '#b37feb', '#ff9f7f']
    products = [
        ('微电签', '微电签交易金额（亿元）'),
        ('微智能', '微智能交易金额（亿元）'),
        ('立刷畅享版', '立刷畅享版交易金额（亿元）'),
        ('骐骥版', '骐骥版交易金额（亿元）'),
        ('老电签', '老电签交易金额（亿元）'),
        ('上网宝', '上网宝交易金额（亿元）'),
        ('立刷小蓝牙', '立刷小蓝牙交易金额（亿元）')
    ]

    legend = []
    for i, (name, key) in enumerate(products):
        legend.append(name)
        values = []
        for idx, d in enumerate(data):
            val = d.get(key, 0)
            try:
                v = float(val) if val else 0
            except:
                v = 0
            # 稀疏标签：最新月(n-1)、次新月(n-2)必须显示，其他间隔显示
            # 从最新月往前数，索引0,2,4...显示，以及n-1和n-2必须显示
            show_label = False
            if n > 0:
                pos_from_end = n - 1 - idx  # 从末尾算的位置，0是最新的
                if pos_from_end == 0 or pos_from_end == 1:  # 最新月和次新月
                    show_label = True
                elif pos_from_end % 2 == 0:  # 其他间隔显示
                    show_label = True
            values.append({'value': v, 'label': {'show': show_label}})
        series.append({
            'name': name,
            'type': 'line',
            'smooth': True,
            'data': values,
            'itemStyle': {'color': colors[i]},
            'label': {'show': True, 'position': 'top', 'fontSize': 12, 'color': colors[i]}
        })

    return {'months': months, 'legend': legend, 'series': series}


def _generate_terminal_trend_data(terminal_data: List) -> Dict:
    """生成各产品新增终端趋势数据（7条线）"""
    if not terminal_data:
        return {'months': [], 'legend': [], 'series': []}

    data = terminal_data  # SQL已返回正确范围的数据
    months = [d.get('月份', '') for d in data]
    n = len(data)

    series = []
    colors = ['#36a3eb', '#67c23a', '#e6a23c', '#f56c6c', '#909399', '#b37feb', '#ff9f7f']
    products = [
        ('微电签', '微电签新增终端（万台）'),
        ('微智能', '微智能新增终端（万台）'),
        ('立刷畅享版', '立刷畅享版新增终端（万台）'),
        ('骐骥版', '骐骥版新增终端（万台）'),
        ('老电签', '老电签新增终端（万台）'),
        ('上网宝', '上网宝新增终端（万台）'),
        ('立刷小蓝牙', '立刷小蓝牙新增终端（万台）')
    ]

    legend = []
    for i, (name, key) in enumerate(products):
        legend.append(name)
        values = []
        for idx, d in enumerate(data):
            val = d.get(key, 0)
            try:
                v = float(val) if val else 0
            except:
                v = 0
            # 稀疏标签逻辑
            show_label = False
            if n > 0:
                pos_from_end = n - 1 - idx
                if pos_from_end == 0 or pos_from_end == 1:
                    show_label = True
                elif pos_from_end % 2 == 0:
                    show_label = True
            values.append({'value': v, 'label': {'show': show_label}})
        series.append({
            'name': name,
            'type': 'line',
            'smooth': True,
            'data': values,
            'itemStyle': {'color': colors[i]},
            'label': {'show': True, 'position': 'top', 'fontSize': 12, 'color': colors[i]}
        })

    return {'months': months, 'legend': legend, 'series': series}


def _generate_branch_table_rows(data: List, table_type: str = 'decline') -> str:
    """生成分公司交易表格行"""
    if not data:
        return '<tr><td colspan="5" style="text-align:center;color:#909399">暂无数据</td></tr>'

    html = ''
    for i, item in enumerate(data[:10], 1):
        rank_class = 'top3' if i <= 3 else ''
        mom = item.get('环比', 0)
        try:
            mom_val = float(mom) if mom else 0
        except:
            mom_val = 0
        mom_str = f'{mom_val:.2f}%' if mom_val else '-'
        # 根据表格类型和环比值决定颜色
        if table_type == 'increase':
            trend_class = 'trend-up'  # 上涨表格使用上涨颜色
        else:
            trend_class = 'trend-down'  # 下降表格使用下降颜色

        html += f'''
                        <tr>
                            <td><span class="rank-badge {rank_class}">{i}</span></td>
                            <td>{item.get('归属分公司', '-')}</td>
                            <td>{format_table_value(item.get('上月交易额（万元）', 0))}</td>
                            <td>{format_table_value(item.get('本月交易额（万元）', 0))}</td>
                            <td class="{trend_class}">{mom_str}</td>
                        </tr>'''
    return html


def _generate_branch_merchant_table_rows(data: List, table_type: str = 'decline') -> str:
    """生成分公司商户表格行"""
    if not data:
        return '<tr><td colspan="5" style="text-align:center;color:#909399">暂无数据</td></tr>'

    html = ''
    for i, item in enumerate(data[:10], 1):
        rank_class = 'top3' if i <= 3 else ''
        mom = item.get('环比', 0)
        try:
            mom_val = float(mom) if mom else 0
        except:
            mom_val = 0
        mom_str = f'{mom_val:.2f}%' if mom_val else '-'
        # 根据表格类型和环比值决定颜色
        if table_type == 'increase':
            trend_class = 'trend-up'  # 上涨表格使用上涨颜色
        else:
            trend_class = 'trend-down'  # 下降表格使用下降颜色

        html += f'''
                        <tr>
                            <td><span class="rank-badge {rank_class}">{i}</span></td>
                            <td>{item.get('归属分公司', '-')}</td>
                            <td>{format_table_value(item.get('上月商户数', 0))}</td>
                            <td>{format_table_value(item.get('本月商户数', 0))}</td>
                            <td class="{trend_class}">{mom_str}</td>
                        </tr>'''
    return html


def _generate_merchant_table_rows(data: List, trend_type: str) -> str:
    """生成商户表格行"""
    if not data:
        return '<tr><td colspan="5" style="text-align:center;color:#909399">暂无数据</td></tr>'

    html = ''
    for i, item in enumerate(data[:10], 1):
        rank_class = 'top3' if i <= 3 else ''
        mom = item.get('环比', 0)
        try:
            mom_val = float(mom) if mom else 0
        except:
            mom_val = 0
        mom_str = f'+{mom_val:.2f}%' if mom_val > 0 else f'{mom_val:.2f}%'
        trend_class = 'trend-down' if trend_type == 'decline' else 'trend-up'

        html += f'''
                        <tr>
                            <td><span class="rank-badge {rank_class}">{i}</span></td>
                            <td>{item.get('子商户名', '-')}</td>
                            <td>{format_table_value(item.get('上月交易额（万元）', 0))}</td>
                            <td>{format_table_value(item.get('本月交易额（万元）', 0))}</td>
                            <td class="{trend_class}">{mom_str}</td>
                        </tr>'''
    return html


def _generate_agent_table_rows(data: List, table_type: str = 'decline') -> str:
    """生成服务商交易表格行"""
    if not data:
        return '<tr><td colspan="5" style="text-align:center;color:#909399">暂无数据</td></tr>'

    html = ''
    for i, item in enumerate(data[:10], 1):
        rank_class = 'top3' if i <= 3 else ''
        mom = item.get('环比', 0)
        try:
            mom_val = float(mom) if mom else 0
        except:
            mom_val = 0
        mom_str = f'{mom_val:.2f}%' if mom_val else '-'
        # 根据表格类型决定颜色
        trend_class = 'trend-up' if table_type == 'increase' else 'trend-down'

        html += f'''
                        <tr>
                            <td><span class="rank-badge {rank_class}">{i}</span></td>
                            <td>{item.get('一级代理商名称', '-')}</td>
                            <td>{format_table_value(item.get('上月交易额（万元）', 0))}</td>
                            <td>{format_table_value(item.get('本月交易额（万元）', 0))}</td>
                            <td class="{trend_class}">{mom_str}</td>
                        </tr>'''
    return html


def _generate_agent_merchant_table_rows(data: List, table_type: str = 'decline') -> str:
    """生成服务商商户表格行"""
    if not data:
        return '<tr><td colspan="5" style="text-align:center;color:#909399">暂无数据</td></tr>'

    html = ''
    for i, item in enumerate(data[:10], 1):
        rank_class = 'top3' if i <= 3 else ''
        mom = item.get('环比', 0)
        try:
            mom_val = float(mom) if mom else 0
        except:
            mom_val = 0
        mom_str = f'{mom_val:.2f}%' if mom_val else '-'
        # 根据表格类型决定颜色
        trend_class = 'trend-up' if table_type == 'increase' else 'trend-down'

        html += f'''
                        <tr>
                            <td><span class="rank-badge {rank_class}">{i}</span></td>
                            <td>{item.get('一级代理商名称', '-')}</td>
                            <td>{format_table_value(item.get('上月商户数', 0))}</td>
                            <td>{format_table_value(item.get('本月商户数', 0))}</td>
                            <td class="{trend_class}">{mom_str}</td>
                        </tr>'''
    return html


def format_table_value(value) -> str:
    """格式化表格数值"""
    try:
        num = float(value) if value else 0
        if num == 0:
            return '-'
        return f'{num:,.0f}'
    except:
        return str(value) if value else '-'


# 保留旧函数兼容性
def generate_html_dashboard(small_pos_data: Dict, large_pos_data: Dict) -> str:
    """生成完整HTML看板（兼容旧接口）"""
    return generate_large_pos_dashboard_html(large_pos_data)