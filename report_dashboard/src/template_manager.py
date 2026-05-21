# -*- coding: utf-8 -*-
"""
模板管理核心类
负责模板的加载、保存、备份、历史版本管理

重要：任何模板修改都需要授权用户确认才可保存，否则只是临时修改
"""

import json
import os
import shutil
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import copy


class TemplateManager:
    """模板管理器"""

    def __init__(self, config: Dict, allowed_users: List[str] = None, admin_users: List[str] = None):
        """
        初始化模板管理器

        Args:
            config: 配置字典，包含:
                - default_template_path: 默认模板路径
                - backup_dir: 备份目录
                - history_dir: 历史版本目录
                - max_history_count: 最大历史保留数
            allowed_users: 授权用户列表（可保存模板）
            admin_users: 管理员用户列表（可重置默认）
        """
        self.default_template_path = config.get('default_template_path', 'config/default_template.json')
        self.backup_dir = config.get('backup_dir', 'config/')
        self.history_dir = config.get('history_dir', 'config/template_history/')
        self.max_history_count = config.get('max_history_count', 20)
        self.allowed_users = allowed_users or []
        self.admin_users = admin_users or []
        self.current_template = None
        self.temp_template = None  # 临时模板（未保存的修改）
        self.has_unsaved_changes = False  # 是否有未保存的修改

        # 确保目录存在
        self._ensure_dirs()

    def _get_current_user_id(self) -> str:
        """
        从Copaw平台获取当前用户工号

        Copaw平台在企业微信机器人场景下会自动注入UserId环境变量

        Returns:
            用户工号字符串，未获取到时返回空字符串
        """
        # Copaw平台注入的用户标识（优先级最高）
        user_id = os.environ.get('UserId', '')

        # 兼容其他可能的变量名
        if not user_id:
            user_id = os.environ.get('USER_ID', '')

        if not user_id:
            user_id = os.environ.get('COPAW_USER_ID', '')

        return user_id.strip()

    def _ensure_dirs(self):
        """确保必要的目录存在"""
        os.makedirs(self.backup_dir, exist_ok=True)
        os.makedirs(self.history_dir, exist_ok=True)

    def _get_base_dir(self) -> str:
        """获取项目根目录"""
        # 从当前文件位置推断项目根目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # src 目录的父目录即为项目根目录
        return os.path.dirname(current_dir)

    def _resolve_path(self, path: str) -> str:
        """解析路径，转换为绝对路径"""
        if os.path.isabs(path):
            return path
        return os.path.join(self._get_base_dir(), path)

    def load_template(self) -> Dict:
        """
        加载当前模板（如果有临时修改则使用临时模板）

        Returns:
            模板配置字典
        """
        # 如果有临时修改，返回临时模板
        if self.has_unsaved_changes and self.temp_template is not None:
            return self.temp_template

        template_path = self._resolve_path(self.default_template_path)

        if os.path.exists(template_path):
            with open(template_path, 'r', encoding='utf-8') as f:
                self.current_template = json.load(f)
                return self.current_template
        else:
            # 返回内置默认模板
            self.current_template = self._get_builtin_template()
            return self.current_template

    def apply_temp_change(self, changes: Dict, dashboard_type: str = None) -> Tuple[bool, str]:
        """
        应用临时修改（不保存到文件，需要授权用户确认后才可保存）

        Args:
            changes: 修改内容
            dashboard_type: 看板类型（'large_pos' 或 'small_pos'），如果为None则修改全局配置

        Returns:
            (成功标志, 消息)
        """
        # 加载当前模板作为基础
        if self.temp_template is None:
            self.temp_template = copy.deepcopy(self.load_template())

        try:
            if dashboard_type:
                # 修改特定看板的配置
                if dashboard_type in self.temp_template.get('dashboard_types', {}):
                    for key, value in changes.items():
                        self.temp_template['dashboard_types'][dashboard_type][key] = value
                else:
                    return False, f"未知的看板类型: {dashboard_type}"
            else:
                # 修改全局配置
                for key, value in changes.items():
                    self.temp_template[key] = value

            self.has_unsaved_changes = True
            return True, "修改已应用（临时），需要授权用户确认后才可保存为模板"
        except Exception as e:
            return False, f"应用修改失败: {str(e)}"

    def request_save(self, requesting_user: str = None) -> Tuple[bool, str]:
        """
        请求保存模板（需要授权用户确认）

        Args:
            requesting_user: 请求保存的用户，如果为None则自动从Copaw获取当前用户

        Returns:
            (是否可以保存, 消息)
        """
        if not self.has_unsaved_changes:
            return False, "没有未保存的修改"

        # 自动获取当前用户身份
        user = requesting_user or self._get_current_user_id()

        if not user:
            return False, "无法获取当前用户身份，请确保在Copaw平台环境中运行"

        # 检查用户权限（授权用户或管理员都可以保存）
        if user not in self.allowed_users and user not in self.admin_users:
            return False, f"用户 '{user}' 不是授权用户，无法保存模板。\n请联系管理员添加您的工号到 DASHBOARD_ALLOWED_USERS 环境变量"

        return True, f"授权用户 '{user}' 确认保存"

    def confirm_and_save(self, user: str = None) -> Tuple[bool, str]:
        """
        授权用户确认后保存模板

        Args:
            user: 确认保存的授权用户，如果为None则自动从Copaw获取当前用户

        Returns:
            (成功标志, 消息)
        """
        if not self.has_unsaved_changes or self.temp_template is None:
            return False, "没有未保存的修改"

        # 自动获取当前用户身份
        user_id = user or self._get_current_user_id()

        if not user_id:
            return False, "无法获取当前用户身份，请确保在Copaw平台环境中运行"

        # 检查用户权限
        if user_id not in self.allowed_users and user_id not in self.admin_users:
            return False, f"用户 '{user_id}' 不是授权用户，无法保存模板。\n请联系管理员添加您的工号到 DASHBOARD_ALLOWED_USERS 环境变量"

        # 调用保存方法
        success, message = self.save_template(self.temp_template, user_id)

        if success:
            # 清除临时状态
            self.has_unsaved_changes = False
            self.temp_template = None

        return success, message

    def check_user_permission(self, user: str = None) -> Dict:
        """
        检查用户权限状态

        Args:
            user: 用户ID，如果为None则自动从Copaw获取当前用户

        Returns:
            权限状态字典
        """
        user_id = user or self._get_current_user_id()

        if not user_id:
            return {
                'user_id': '',
                'is_authorized': False,
                'is_admin': False,
                'can_save': False,
                'message': '无法获取当前用户身份'
            }

        is_admin = user_id in self.admin_users
        is_authorized = user_id in self.allowed_users or is_admin

        return {
            'user_id': user_id,
            'is_authorized': is_authorized,
            'is_admin': is_admin,
            'can_save': is_authorized,
            'message': f"当前用户: {user_id}，权限: {'管理员' if is_admin else ('授权用户' if is_authorized else '普通用户')}"
        }

    def discard_changes(self) -> Tuple[bool, str]:
        """
        放弃未保存的修改

        Returns:
            (成功标志, 消息)
        """
        if not self.has_unsaved_changes:
            return False, "没有未保存的修改"

        self.temp_template = None
        self.has_unsaved_changes = False
        return True, "已放弃未保存的修改"

    def get_pending_changes_summary(self) -> Dict:
        """
        获取未保存修改的摘要

        Returns:
            修改摘要字典
        """
        if not self.has_unsaved_changes or self.temp_template is None:
            return {'has_changes': False}

        # 对比当前模板和临时模板
        changes = {
            'has_changes': True,
            'dashboard_types': {}
        }

        current = self.current_template or {}
        temp = self.temp_template

        for dtype in ['large_pos', 'small_pos']:
            current_kpi = current.get('dashboard_types', {}).get(dtype, {}).get('kpi', {}).get('items', [])
            temp_kpi = temp.get('dashboard_types', {}).get(dtype, {}).get('kpi', {}).get('items', [])

            if current_kpi != temp_kpi:
                changes['dashboard_types'][dtype] = {
                    'kpi_changed': True,
                    'current_kpi_count': len(current_kpi),
                    'temp_kpi_count': len(temp_kpi)
                }

        return changes

    def _get_builtin_template(self) -> Dict:
        """获取内置默认模板（当配置文件不存在时使用）"""
        return {
            "version": "1.0",
            "created_at": datetime.now().strftime('%Y-%m-%d'),
            "updated_at": datetime.now().strftime('%Y-%m-%d'),
            "updated_by": "system",
            "description": "内置默认模板",
            "dashboard_types": {
                "large_pos": {
                    "title": "商户收款看板（大POS）",
                    "kpi": {
                        "items": [
                            {"id": "total_amount", "name": "交易总金额", "field": "total_amount", "unit": "亿元", "protected": True, "order": 1, "visible": True},
                            {"id": "new_merchants", "name": "新增商户数", "field": "new_merchants", "unit": "户", "protected": True, "order": 2, "visible": True},
                            {"id": "active_merchants", "name": "活跃商户数", "field": "active_merchants", "unit": "户", "protected": True, "order": 3, "visible": True}
                        ]
                    },
                    "charts": [],
                    "tables": []
                },
                "small_pos": {
                    "title": "立刷产品看板（小POS）",
                    "kpi": {
                        "items": [
                            {"id": "total_amount", "name": "交易总金额", "field": "total_amount", "unit": "亿元", "protected": True, "order": 1, "visible": True},
                            {"id": "new_merchants", "name": "新增商户数", "field": "new_merchants", "unit": "户", "protected": True, "order": 2, "visible": True},
                            {"id": "active_merchants", "name": "活跃商户数", "field": "active_merchants", "unit": "户", "protected": True, "order": 3, "visible": True}
                        ]
                    },
                    "charts": [],
                    "tables": []
                }
            },
            "protected_config": {
                "protected_indicators": ["交易总金额", "新增商户数", "活跃商户数"],
                "min_kpi_count": 3,
                "required_charts": []
            }
        }

    def save_template(self, template: Dict, user: str) -> Tuple[bool, str]:
        """
        保存模板（自动备份）

        Args:
            template: 新模板配置
            user: 操作用户

        Returns:
            (成功标志, 消息)
        """
        # 先创建备份
        backup_path = self.create_backup()
        if backup_path:
            print(f"已创建备份: {backup_path}")

        # 更新模板元数据
        template['updated_at'] = datetime.now().strftime('%Y-%m-%d')
        template['updated_by'] = user

        # 版本号递增
        current_version = template.get('version', '1.0')
        try:
            major, minor = current_version.split('.')
            template['version'] = f"{major}.{int(minor) + 1}"
        except:
            template['version'] = '1.1'

        # 保存模板
        template_path = self._resolve_path(self.default_template_path)
        try:
            with open(template_path, 'w', encoding='utf-8') as f:
                json.dump(template, f, ensure_ascii=False, indent=2)

            self.current_template = template

            # 同时保存一份到历史目录
            self._save_to_history(template, user)

            return True, f"模板已保存，版本: {template['version']}"
        except Exception as e:
            return False, f"保存失败: {str(e)}"

    def create_backup(self) -> Optional[str]:
        """
        创建当前模板的备份

        Returns:
            备份文件路径，失败返回None
        """
        template_path = self._resolve_path(self.default_template_path)

        if not os.path.exists(template_path):
            return None

        # 备份文件名格式: default_template_backup_YYYYMMDD.json
        backup_name = f"default_template_backup_{datetime.now().strftime('%Y%m%d')}.json"
        backup_path = self._resolve_path(os.path.join(self.backup_dir, backup_name))

        try:
            shutil.copy2(template_path, backup_path)
            return backup_path
        except Exception as e:
            print(f"备份失败: {e}")
            return None

    def _save_to_history(self, template: Dict, user: str):
        """保存到历史版本目录"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        history_name = f"template_{timestamp}.json"
        history_path = self._resolve_path(os.path.join(self.history_dir, history_name))

        # 添加历史记录元数据
        history_template = template.copy()
        history_template['history_saved_at'] = timestamp
        history_template['history_saved_by'] = user

        try:
            with open(history_path, 'w', encoding='utf-8') as f:
                json.dump(history_template, f, ensure_ascii=False, indent=2)

            # 清理过多的历史文件
            self._cleanup_history()
        except Exception as e:
            print(f"保存历史版本失败: {e}")

    def _cleanup_history(self):
        """清理过多的历史文件，保留最近 max_history_count 个"""
        history_path = self._resolve_path(self.history_dir)

        if not os.path.exists(history_path):
            return

        # 获取所有历史文件
        files = [f for f in os.listdir(history_path) if f.startswith('template_') and f.endswith('.json')]
        files.sort(reverse=True)  # 按时间倒序

        # 删除超出数量的文件
        if len(files) > self.max_history_count:
            for old_file in files[self.max_history_count:]:
                old_path = os.path.join(history_path, old_file)
                try:
                    os.remove(old_path)
                    print(f"已清理历史文件: {old_file}")
                except Exception as e:
                    print(f"清理失败: {old_file}, {e}")

    def get_history_list(self) -> List[Dict]:
        """
        获取历史版本列表

        Returns:
            历史版本信息列表
        """
        history_path = self._resolve_path(self.history_dir)

        if not os.path.exists(history_path):
            return []

        files = [f for f in os.listdir(history_path) if f.startswith('template_') and f.endswith('.json')]
        files.sort(reverse=True)

        history_list = []
        for i, filename in enumerate(files, 1):
            file_path = os.path.join(history_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    template = json.load(f)
                    history_list.append({
                        'index': i,
                        'filename': filename,
                        'version': template.get('version', 'N/A'),
                        'updated_at': template.get('updated_at', 'N/A'),
                        'updated_by': template.get('updated_by', 'N/A'),
                        'description': template.get('description', '')
                    })
            except Exception as e:
                print(f"读取历史文件失败: {filename}, {e}")

        return history_list

    def rollback_to_version(self, version_filename: str) -> Tuple[bool, str]:
        """
        回退到指定历史版本

        Args:
            version_filename: 历史版本文件名

        Returns:
            (成功标志, 消息)
        """
        history_path = self._resolve_path(self.history_dir)
        source_path = os.path.join(history_path, version_filename)

        if not os.path.exists(source_path):
            return False, f"历史版本不存在: {version_filename}"

        # 先备份当前模板
        self.create_backup()

        # 复制历史版本到默认模板位置
        template_path = self._resolve_path(self.default_template_path)
        try:
            shutil.copy2(source_path, template_path)

            # 更新模板
            self.current_template = self.load_template()

            return True, f"已回退到版本: {self.current_template.get('version', 'N/A')}"
        except Exception as e:
            return False, f"回退失败: {str(e)}"

    def get_dashboard_config(self, dashboard_type: str) -> Dict:
        """
        获取指定看板类型的配置

        Args:
            dashboard_type: 'large_pos' 或 'small_pos'

        Returns:
            看板配置字典
        """
        template = self.load_template()
        return template.get('dashboard_types', {}).get(dashboard_type, {})

    def get_kpi_items(self, dashboard_type: str) -> List[Dict]:
        """获取指定看板的KPI指标列表"""
        config = self.get_dashboard_config(dashboard_type)
        return config.get('kpi', {}).get('items', [])

    def get_chart_items(self, dashboard_type: str) -> List[Dict]:
        """获取指定看板的图表列表"""
        config = self.get_dashboard_config(dashboard_type)
        return config.get('charts', [])

    def get_table_items(self, dashboard_type: str) -> List[Dict]:
        """获取指定看板的表格列表"""
        config = self.get_dashboard_config(dashboard_type)
        return config.get('tables', [])

    def get_available_indicators(self, dashboard_type: str) -> List[Dict]:
        """获取可用的指标列表（用于用户选择添加）"""
        template = self.load_template()
        return template.get('available_indicators', {}).get(dashboard_type, [])

    def get_protected_indicators(self) -> List[str]:
        """获取受保护的指标名称列表"""
        template = self.load_template()
        return template.get('protected_config', {}).get('protected_indicators', [])


# 单例模式
_template_manager_instance = None

def get_template_manager(config: Dict = None, allowed_users: List[str] = None, admin_users: List[str] = None) -> TemplateManager:
    """
    获取模板管理器实例

    Args:
        config: 配置字典
        allowed_users: 授权用户列表（可保存模板）
        admin_users: 管理员用户列表（可重置默认）

    Returns:
        TemplateManager实例
    """
    global _template_manager_instance

    if _template_manager_instance is None:
        if config is None:
            config = {
                'default_template_path': 'config/default_template.json',
                'backup_dir': 'config/',
                'history_dir': 'config/template_history/',
                'max_history_count': 20
            }

        # 如果没有传入授权用户列表，尝试从config模块获取
        if allowed_users is None or admin_users is None:
            try:
                import sys
                sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
                from config import ALLOWED_USERS, ADMIN_USERS
                if allowed_users is None:
                    allowed_users = ALLOWED_USERS
                if admin_users is None:
                    admin_users = ADMIN_USERS
            except:
                if allowed_users is None:
                    allowed_users = []
                if admin_users is None:
                    admin_users = []

        _template_manager_instance = TemplateManager(config, allowed_users, admin_users)

    return _template_manager_instance