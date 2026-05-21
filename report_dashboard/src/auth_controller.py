# -*- coding: utf-8 -*-
"""
权限控制器
负责用户身份验证、权限检查、操作日志记录
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional


class AuthController:
    """权限控制器"""

    # 权限级别定义
    PERMISSION_LEVELS = {
        'admin': 3,      # 最高权限，可执行所有操作包括重置默认
        'authorized': 2, # 授权用户，可保存模板
        'user': 1,       # 普通用户，可临时调整和预览
        'guest': 0       #访客，仅可查看
    }

    def __init__(self, allowed_users: List[str] = None, admin_users: List[str] = None):
        """
        初始化权限控制器

        Args:
            allowed_users: 授权用户列表（可保存模板）
            admin_users: 管理员用户列表（可重置默认）
        """
        # 从环境变量获取授权用户
        self.allowed_users = allowed_users or self._get_allowed_users_from_env()
        self.admin_users = admin_users or self._get_admin_users_from_env()

        # 操作日志文件路径
        self.log_file = 'config/template_operations.log'

    def get_current_user_id(self) -> str:
        """
        从Copaw平台获取当前用户工号

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

    def _get_allowed_users_from_env(self) -> List[str]:
        """从环境变量获取授权用户列表"""
        users_str = os.environ.get('DASHBOARD_ALLOWED_USERS', '')
        if users_str:
            return [u.strip() for u in users_str.split(',') if u.strip()]
        return []

    def _get_admin_users_from_env(self) -> List[str]:
        """从环境变量获取管理员用户列表"""
        users_str = os.environ.get('DASHBOARD_ADMIN_USERS', 'admin')
        if users_str:
            return [u.strip() for u in users_str.split(',') if u.strip()]
        return ['admin']

    def is_authorized_user(self, user: str) -> bool:
        """
        检查用户是否有保存模板权限

        Args:
            user: 用户名

        Returns:
            是否有权限
        """
        if not user:
            return False

        # 管理员也有保存权限
        if user in self.admin_users:
            return True

        return user in self.allowed_users

    def is_admin_user(self, user: str) -> bool:
        """
        检查用户是否是管理员

        Args:
            user: 用户名

        Returns:
            是否是管理员
        """
        if not user:
            return False
        return user in self.admin_users

    def get_user_permission_level(self, user: str) -> str:
        """
        获取用户权限级别

        Args:
            user: 用户名

        Returns:
            权限级别字符串: 'admin', 'authorized', 'user', 'guest'
        """
        if not user:
            return 'guest'

        if user in self.admin_users:
            return 'admin'

        if user in self.allowed_users:
            return 'authorized'

        return 'user'

    def get_permission_level_value(self, user: str) -> int:
        """
        获取用户权限级别数值

        Args:
            user: 用户名

        Returns:
            权限级别数值
        """
        level = self.get_user_permission_level(user)
        return self.PERMISSION_LEVELS.get(level, 0)

    def can_save_template(self, user: str) -> bool:
        """
        检查用户是否可以保存模板

        Args:
            user: 用户名

        Returns:
            是否可以保存
        """
        return self.get_permission_level_value(user) >= self.PERMISSION_LEVELS['authorized']

    def can_reset_default(self, user: str) -> bool:
        """
        检查用户是否可以重置默认模板

        Args:
            user: 用户名

        Returns:
            是否可以重置
        """
        return self.get_permission_level_value(user) >= self.PERMISSION_LEVELS['admin']

    def can_modify_template(self, user: str) -> bool:
        """
        检查用户是否可以临时调整模板（所有用户都可以）

        Args:
            user: 用户名

        Returns:
            是否可以调整
        """
        # 所有用户都可以临时调整
        return True

    def log_operation(self, user: str, operation: str, details: Dict = None):
        """
        记录操作日志

        Args:
            user: 操作用户
            operation: 操作类型
            details: 操作详情
        """
        log_entry = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'user': user,
            'operation': operation,
            'details': details or {},
            'permission_level': self.get_user_permission_level(user)
        }

        # 确保日志目录存在
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        # 写入日志文件
        log_path = self._resolve_path(self.log_file)
        try:
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')
        except Exception as e:
            print(f"记录日志失败: {e}")

    def _resolve_path(self, path: str) -> str:
        """解析路径"""
        if os.path.isabs(path):
            return path

        # 从当前文件位置推断项目根目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(current_dir)  # src的父目录
        return os.path.join(base_dir, path)

    def get_recent_operations(self, limit: int = 20) -> List[Dict]:
        """
        获取最近的操作日志

        Args:
            limit: 返回条数限制

        Returns:
            操作日志列表
        """
        log_path = self._resolve_path(self.log_file)

        if not os.path.exists(log_path):
            return []

        operations = []
        try:
            with open(log_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                # 取最近的记录
                for line in lines[-limit:]:
                    try:
                        entry = json.loads(line.strip())
                        operations.append(entry)
                    except:
                        pass
        except Exception as e:
            print(f"读取日志失败: {e}")

        return operations

    def format_permission_message(self, user: str) -> str:
        """
        格式化用户权限信息消息

        Args:
            user: 用户名

        Returns:
            权限信息字符串
        """
        level = self.get_user_permission_level(user)

        messages = {
            'admin': f"当前用户: {user} [管理员] - 可执行所有操作",
            'authorized': f"当前用户: {user} [授权用户] - 可保存模板、调整配置",
            'user': f"当前用户: {user} [普通用户] - 可临时调整、预览效果（无法保存）",
            'guest': f"当前用户: {user} [访客] - 仅可查看"
        }

        return messages.get(level, f"当前用户: {user}")

    def format_no_permission_message(self, user: str, operation: str) -> str:
        """
        格式化无权限提示消息

        Args:
            user: 用户名
            operation: 请求的操作

        Returns:
            提示消息字符串
        """
        level = self.get_user_permission_level(user)

        if operation == 'save_template':
            return f"用户 '{user}' 无保存模板权限。\n当前权限级别: {level}\n请联系管理员获取授权，或设置环境变量 DASHBOARD_ALLOWED_USERS"

        elif operation == 'reset_default':
            return f"用户 '{user}' 无重置默认模板权限。\n当前权限级别: {level}\n仅管理员可执行此操作"

        return f"用户 '{user}' 无执行 '{operation}' 的权限。"

    def check_current_user_permission(self) -> Dict:
        """
        检查当前用户（Copaw平台自动注入）的权限状态

        Returns:
            包含用户信息和权限状态的字典
        """
        user_id = self.get_current_user_id()

        if not user_id:
            return {
                'user_id': '',
                'level': 'guest',
                'can_save': False,
                'can_reset': False,
                'message': '未获取到用户身份，请确保在Copaw平台环境中运行'
            }

        level = self.get_user_permission_level(user_id)

        return {
            'user_id': user_id,
            'level': level,
            'can_save': self.can_save_template(user_id),
            'can_reset': self.can_reset_default(user_id),
            'message': self.format_permission_message(user_id)
        }

    def is_current_user_authorized(self) -> bool:
        """
        快速检查当前用户是否有保存模板权限

        Returns:
            是否有权限
        """
        user_id = self.get_current_user_id()
        return self.is_authorized_user(user_id)


# 单例
_auth_instance = None

def get_auth_controller(allowed_users: List[str] = None, admin_users: List[str] = None) -> AuthController:
    """获取权限控制器实例"""
    global _auth_instance

    if _auth_instance is None:
        _auth_instance = AuthController(allowed_users, admin_users)

    return _auth_instance