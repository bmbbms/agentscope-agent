# -*- coding: utf-8 -*-
"""
模板验证器
负责模板结构验证、指标保护检查、安全防护
"""

import json
import os
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """验证结果"""
    valid: bool
    errors: List[str]
    warnings: List[str]

    def add_error(self, error: str):
        self.errors.append(error)
        self.valid = False

    def add_warning(self, warning: str):
        self.warnings.append(warning)

    def __str__(self):
        if self.valid:
            return f"[PASS] 验证通过，警告: {len(self.warnings)}"
        return f"[FAIL] 验证失败，错误: {len(self.errors)}，警告: {len(self.warnings)}"


class TemplateValidator:
    """模板验证器"""

    # 关键指标保护列表
    PROTECTED_INDICATORS = ['交易总金额', '新增商户数', '活跃商户数']

    # 必须的模板结构
    REQUIRED_FIELDS = ['version', 'dashboard_types']

    # 必须的看板配置结构
    REQUIRED_DASHBOARD_FIELDS = ['title', 'kpi']

    # 必须的KPI结构
    REQUIRED_KPI_FIELDS = ['items']

    # 支持的看板类型
    SUPPORTED_DASHBOARD_TYPES = ['large_pos', 'small_pos']

    # 支持的图表类型
    SUPPORTED_CHART_TYPES = ['mixed_bar_line', 'stacked_bar', 'multi_line', 'bar', 'line']

    def __init__(self, custom_protected_indicators: List[str] = None):
        """
        初始化验证器

        Args:
            custom_protected_indicators: 自定义保护指标列表，覆盖默认值
        """
        if custom_protected_indicators:
            self.PROTECTED_INDICATORS = custom_protected_indicators

    def validate_template(self, template: Dict) -> ValidationResult:
        """
        全面验证模板

        Args:
            template: 模板配置字典

        Returns:
            ValidationResult 验证结果对象
        """
        result = ValidationResult(valid=True, errors=[], warnings=[])

        # 结构验证
        self._validate_structure(template, result)

        # 指标验证
        self._validate_indicators(template, result)

        # 图表验证
        self._validate_charts(template, result)

        # 表格验证
        self._validate_tables(template, result)

        # 关键指标保护验证
        self._validate_protected_indicators(template, result)

        return result

    def _validate_structure(self, template: Dict, result: ValidationResult):
        """验证模板基本结构"""
        # 检查必须字段
        for field in self.REQUIRED_FIELDS:
            if field not in template:
                result.add_error(f"缺少必须字段: {field}")

        # 检查看板类型
        dashboard_types = template.get('dashboard_types', {})
        if not dashboard_types:
            result.add_error("dashboard_types 不能为空")
            return

        for dtype in dashboard_types.keys():
            if dtype not in self.SUPPORTED_DASHBOARD_TYPES:
                result.add_warning(f"未知的看板类型: {dtype}")

        # 检查每个看板的必须字段
        for dtype, config in dashboard_types.items():
            for field in self.REQUIRED_DASHBOARD_FIELDS:
                if field not in config:
                    result.add_error(f"看板 {dtype} 缺少必须字段: {field}")

            # 检查KPI结构
            kpi = config.get('kpi', {})
            for field in self.REQUIRED_KPI_FIELDS:
                if field not in kpi:
                    result.add_error(f"看板 {dtype} 的KPI缺少必须字段: {field}")

    def _validate_indicators(self, template: Dict, result: ValidationResult):
        """验证指标配置"""
        dashboard_types = template.get('dashboard_types', {})

        for dtype, config in dashboard_types.items():
            kpi_items = config.get('kpi', {}).get('items', [])

            if not kpi_items:
                result.add_error(f"看板 {dtype} 的KPI指标列表为空")
                continue

            # 检查每个指标项的结构
            for item in kpi_items:
                required_item_fields = ['id', 'name', 'field']
                for field in required_item_fields:
                    if field not in item:
                        result.add_error(f"看板 {dtype} 的KPI指标 {item.get('name', 'unknown')} 缺少字段: {field}")

            # 检查KPI数量
            protected_config = template.get('protected_config', {})
            min_kpi_count = protected_config.get('min_kpi_count', 3)
            visible_items = [i for i in kpi_items if i.get('visible', True)]
            if len(visible_items) < min_kpi_count:
                result.add_warning(f"看板 {dtype} 的可见KPI指标数量({len(visible_items)})低于最小要求({min_kpi_count})")

    def _validate_charts(self, template: Dict, result: ValidationResult):
        """验证图表配置"""
        dashboard_types = template.get('dashboard_types', {})

        for dtype, config in dashboard_types.items():
            charts = config.get('charts', [])

            for chart in charts:
                # 检查必须字段
                required_chart_fields = ['id', 'title', 'type']
                for field in required_chart_fields:
                    if field not in chart:
                        result.add_error(f"看板 {dtype} 的图表 {chart.get('title', 'unknown')} 缺少字段: {field}")

                # 检查图表类型是否支持
                chart_type = chart.get('type')
                if chart_type not in self.SUPPORTED_CHART_TYPES:
                    result.add_warning(f"看板 {dtype} 的图表 {chart.get('title', 'unknown')} 使用了未知的图表类型: {chart_type}")

                # 检查series配置
                series = chart.get('series', [])
                if not series:
                    result.add_warning(f"看板 {dtype} 的图表 {chart.get('title', 'unknown')} 没有series配置")

                for s in series:
                    required_series_fields = ['name', 'field']
                    for field in required_series_fields:
                        if field not in s:
                            result.add_error(f"看板 {dtype} 图表 {chart.get('title', 'unknown')} 的series缺少字段: {field}")

    def _validate_tables(self, template: Dict, result: ValidationResult):
        """验证表格配置"""
        dashboard_types = template.get('dashboard_types', {})

        for dtype, config in dashboard_types.items():
            tables = config.get('tables', [])

            for table in tables:
                required_table_fields = ['id', 'title', 'data_source']
                for field in required_table_fields:
                    if field not in table:
                        result.add_warning(f"看板 {dtype} 的表格 {table.get('title', 'unknown')} 缺少字段: {field}")

    def _validate_protected_indicators(self, template: Dict, result: ValidationResult):
        """验证关键指标保护"""
        protected_config = template.get('protected_config', {})
        protected_list = protected_config.get('protected_indicators', self.PROTECTED_INDICATORS)

        dashboard_types = template.get('dashboard_types', {})

        for dtype, config in dashboard_types.items():
            kpi_items = config.get('kpi', {}).get('items', [])
            kpi_names = [item.get('name') for item in kpi_items if item.get('visible', True)]

            # 检查关键指标是否存在
            for protected_name in protected_list:
                if protected_name not in kpi_names:
                    # 检查是否只是隐藏而非删除
                    hidden_items = [item for item in kpi_items if item.get('name') == protected_name and not item.get('visible', True)]
                    if hidden_items:
                        result.add_warning(f"看板 {dtype} 的关键指标 {protected_name} 被隐藏，建议保持可见")
                    else:
                        result.add_error(f"看板 {dtype} 缺少关键指标: {protected_name}")

    def check_deletion_protection(self, template: Dict, indicator_name: str) -> Tuple[bool, str]:
        """
        检查指标删除操作是否被保护

        Args:
            template: 模板配置
            indicator_name: 要删除的指标名称

        Returns:
            (是否允许删除, 原因说明)
        """
        protected_config = template.get('protected_config', {})
        protected_list = protected_config.get('protected_indicators', self.PROTECTED_INDICATORS)

        if indicator_name in protected_list:
            return False, f"'{indicator_name}' 是关键保护指标，不允许删除。如需隐藏，可设置 visible=false。"

        return True, f"'{indicator_name}' 可以删除。"

    def check_indicator_changes(self, template: Dict, changes: Dict) -> ValidationResult:
        """
        检查指标变更操作的安全性

        Args:
            template: 当前模板
            changes: 变更操作字典，包含:
                - add: 要添加的指标列表
                - remove: 要删除的指标列表
                - modify: 要修改的指标字典

        Returns:
            ValidationResult
        """
        result = ValidationResult(valid=True, errors=[], warnings=[])

        # 检查删除操作
        remove_list = changes.get('remove', [])
        for indicator_name in remove_list:
            allowed, msg = self.check_deletion_protection(template, indicator_name)
            if not allowed:
                result.add_error(msg)

        # 检查修改操作
        modify_dict = changes.get('modify', {})
        for indicator_name, modify_info in modify_dict.items():
            # 如果修改导致visible=false，给出警告
            if modify_info.get('visible') == False:
                if indicator_name in self.PROTECTED_INDICATORS:
                    result.add_warning(f"关键指标 '{indicator_name}' 被隐藏，可能影响看板完整性")

        return result

    def sanitize_template(self, template: Dict) -> Dict:
        """
        清理模板中的危险配置

        Args:
            template: 原始模板

        Returns:
            清理后的模板
        """
        # 确保关键指标存在
        sanitized = template.copy()

        dashboard_types = sanitized.get('dashboard_types', {})
        protected_config = sanitized.get('protected_config', {})
        protected_list = protected_config.get('protected_indicators', self.PROTECTED_INDICATORS)

        for dtype, config in dashboard_types.items():
            kpi_items = config.get('kpi', {}).get('items', [])
            kpi_names = [item.get('name') for item in kpi_items]

            # 添加缺失的关键指标（如果被意外删除）
            for protected_name in protected_list:
                if protected_name not in kpi_names:
                    # 创建默认的关键指标项
                    default_item = {
                        'id': protected_name.lower().replace(' ', '_'),
                        'name': protected_name,
                        'field': protected_name.lower().replace(' ', '_'),
                        'unit': '单位',
                        'protected': True,
                        'order': len(kpi_items) + 1,
                        'visible': True
                    }
                    kpi_items.append(default_item)
                    print(f"[自动修复] 添加缺失的关键指标: {protected_name}")

            # 重新排序
            kpi_items.sort(key=lambda x: x.get('order', 999))

        return sanitized

    def get_change_summary(self, old_template: Dict, new_template: Dict) -> Dict:
        """
        比较新旧模板，生成变更摘要

        Args:
            old_template: 原模板
            new_template: 新模板

        Returns:
            变更摘要字典
        """
        summary = {
            'kpi_changes': [],
            'chart_changes': [],
            'table_changes': [],
            'setting_changes': []
        }

        # 比较KPI变更
        for dtype in ['large_pos', 'small_pos']:
            old_kpi = old_template.get('dashboard_types', {}).get(dtype, {}).get('kpi', {}).get('items', [])
            new_kpi = new_template.get('dashboard_types', {}).get(dtype, {}).get('kpi', {}).get('items', [])

            old_ids = {i.get('id') for i in old_kpi}
            new_ids = {i.get('id') for i in new_kpi}

            added = new_ids - old_ids
            removed = old_ids - new_ids

            for id in added:
                item = next((i for i in new_kpi if i.get('id') == id), None)
                if item:
                    summary['kpi_changes'].append({
                        'dashboard': dtype,
                        'action': 'add',
                        'indicator': item.get('name')
                    })

            for id in removed:
                item = next((i for i in old_kpi if i.get('id') == id), None)
                if item:
                    summary['kpi_changes'].append({
                        'dashboard': dtype,
                        'action': 'remove',
                        'indicator': item.get('name')
                    })

        # 比较图表变更
        for dtype in ['large_pos', 'small_pos']:
            old_charts = old_template.get('dashboard_types', {}).get(dtype, {}).get('charts', [])
            new_charts = new_template.get('dashboard_types', {}).get(dtype, {}).get('charts', [])

            old_chart_ids = {c.get('id') for c in old_charts}
            new_chart_ids = {c.get('id') for c in new_charts}

            added = new_chart_ids - old_chart_ids
            removed = old_chart_ids - new_chart_ids

            for id in added:
                chart = next((c for c in new_charts if c.get('id') == id), None)
                if chart:
                    summary['chart_changes'].append({
                        'dashboard': dtype,
                        'action': 'add',
                        'chart': chart.get('title')
                    })

            for id in removed:
                chart = next((c for c in old_charts if c.get('id') == id), None)
                if chart:
                    summary['chart_changes'].append({
                        'dashboard': dtype,
                        'action': 'remove',
                        'chart': chart.get('title')
                    })

        return summary


# 单例
_validator_instance = None

def get_template_validator(protected_indicators: List[str] = None) -> TemplateValidator:
    """获取验证器实例"""
    global _validator_instance

    if _validator_instance is None:
        _validator_instance = TemplateValidator(protected_indicators)

    return _validator_instance