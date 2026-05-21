# -*- coding: utf-8 -*-
"""
模板配置管理器
负责加载模板配置，支持临时模板与默认模板切换
"""

import json
import os
import shutil
from datetime import datetime
from typing import Dict, List, Optional


class TemplateConfigManager:
    """模板配置管理器"""

    def __init__(self, config: Dict):
        """
        初始化模板配置管理器

        Args:
            config: 配置字典，包含:
                - default_template_path: 默认模板路径
                - temp_template_path: 临时模板路径
        """
        self.default_template_path = config.get('default_template_path', 'config/default_template.json')
        self.temp_template_path = config.get('temp_template_path', 'config/temp_template.json')
        self._template_cache = None

    def _get_base_dir(self) -> str:
        """获取项目根目录"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.dirname(current_dir)

    def _resolve_path(self, path: str) -> str:
        """解析路径"""
        if os.path.isabs(path):
            return path
        return os.path.join(self._get_base_dir(), path)

    def load_template(self) -> Dict:
        """
        加载模板配置
        优先级：临时模板 > 默认模板

        Returns:
            模板配置字典
        """
        # 优先加载临时模板
        temp_path = self._resolve_path(self.temp_template_path)
        if os.path.exists(temp_path):
            print(f"  [模板] 使用临时模板: {self.temp_template_path}")
            with open(temp_path, 'r', encoding='utf-8') as f:
                self._template_cache = json.load(f)
                return self._template_cache

        # 加载默认模板
        default_path = self._resolve_path(self.default_template_path)
        if os.path.exists(default_path):
            print(f"  [模板] 使用默认模板: {self.default_template_path}")
            with open(default_path, 'r', encoding='utf-8') as f:
                self._template_cache = json.load(f)
                return self._template_cache

        raise FileNotFoundError("未找到模板配置文件")

    def get_kpi_config(self, dashboard_type: str) -> List[Dict]:
        """
        获取指定看板的KPI配置

        Args:
            dashboard_type: 'large_pos' 或 'small_pos'

        Returns:
            KPI配置列表
        """
        template = self.load_template()
        return template.get('dashboard_types', {}).get(dashboard_type, {}).get('kpi', {}).get('items', [])

    def get_visible_kpi_names(self, dashboard_type: str) -> List[str]:
        """
        获取可见的KPI指标名称列表

        Args:
            dashboard_type: 'large_pos' 或 'small_pos'

        Returns:
            KPI名称列表
        """
        items = self.get_kpi_config(dashboard_type)
        visible_items = [item for item in items if item.get('visible', True)]
        visible_items.sort(key=lambda x: x.get('order', 999))
        return [item.get('name') for item in visible_items]

    def get_data_field_mapping(self) -> Dict:
        """
        获取数据字段映射配置

        Returns:
            字段映射字典
        """
        template = self.load_template()
        return template.get('data_field_mapping', {})

    def has_temp_template(self) -> bool:
        """检查是否存在临时模板"""
        temp_path = self._resolve_path(self.temp_template_path)
        return os.path.exists(temp_path)

    def create_temp_template(self, template: Dict) -> bool:
        """
        创建临时模板

        Args:
            template: 模板配置

        Returns:
            是否成功
        """
        temp_path = self._resolve_path(self.temp_template_path)
        try:
            # 确保目录存在
            os.makedirs(os.path.dirname(temp_path), exist_ok=True)

            template['is_temp'] = True
            template['temp_created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            with open(temp_path, 'w', encoding='utf-8') as f:
                json.dump(template, f, ensure_ascii=False, indent=2)

            self._template_cache = template
            print(f"  [模板] 已创建临时模板: {self.temp_template_path}")
            return True
        except Exception as e:
            print(f"  [模板] 创建临时模板失败: {e}")
            return False

    def delete_temp_template(self) -> bool:
        """
        删除临时模板（回退到默认模板）

        Returns:
            是否成功
        """
        temp_path = self._resolve_path(self.temp_template_path)
        if os.path.exists(temp_path):
            try:
                os.remove(temp_path)
                self._template_cache = None
                print(f"  [模板] 已删除临时模板，回退到默认模板")
                return True
            except Exception as e:
                print(f"  [模板] 删除临时模板失败: {e}")
                return False
        return True  # 临时模板不存在也算成功

    def update_kpi_config(self, dashboard_type: str, kpi_items: List[Dict]) -> Dict:
        """
        更新KPI配置并创建临时模板

        Args:
            dashboard_type: 看板类型
            kpi_items: 新的KPI配置列表

        Returns:
            更新后的模板
        """
        template = self.load_template()
        if dashboard_type in template.get('dashboard_types', {}):
            template['dashboard_types'][dashboard_type]['kpi']['items'] = kpi_items
        self.create_temp_template(template)
        return template

    def get_template_status(self) -> Dict:
        """
        获取模板状态信息

        Returns:
            状态信息字典
        """
        has_temp = self.has_temp_template()
        template = self.load_template()

        return {
            'using_temp': has_temp,
            'template_path': self.temp_template_path if has_temp else self.default_template_path,
            'version': template.get('version', 'N/A'),
            'updated_at': template.get('updated_at', 'N/A'),
            'temp_created_at': template.get('temp_created_at') if has_temp else None
        }


# 单例
_template_config_manager = None

def get_template_config_manager(config: Dict = None) -> TemplateConfigManager:
    """获取模板配置管理器实例"""
    global _template_config_manager

    if _template_config_manager is None:
        if config is None:
            config = {
                'default_template_path': 'config/default_template.json',
                'temp_template_path': 'config/temp_template.json'
            }
        _template_config_manager = TemplateConfigManager(config)

    return _template_config_manager