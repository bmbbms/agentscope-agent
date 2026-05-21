# -*- coding: utf-8 -*-
"""
看板生成配置文件

请根据实际情况修改以下配置
"""

import os
import base64

def _decrypt_password(encrypted_base64: str, key: str = 'superset_key') -> str:
    """可逆加密（解密），用于解密内置的密码"""
    if not encrypted_base64:
        return ''
    try:
        encrypted_bytes = base64.b64decode(encrypted_base64)
        key_bytes = key.encode('utf-8')
        decrypted_bytes = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(encrypted_bytes)])
        return decrypted_bytes.decode('utf-8')
    except Exception:
        return ''

# 数据获取模式
MODE = 'api'

# Superset BI配置
SUPERSET_CONFIG = {
    'base_url': os.environ.get('SUPERSET_BASE_URL', '').strip(),
    'username': os.environ.get('SUPERSET_USERNAME', '').strip(),
    'password_encrypted': os.environ.get('SUPERSET_PASSWORD_ENCRYPTED', '').strip(),
    'database': os.environ.get('SUPERSET_DATABASE', '').strip(),
}

# 动态反解密密码
SUPERSET_CONFIG['password'] = os.environ.get('SUPERSET_PASSWORD', '').strip() or _decrypt_password(
    SUPERSET_CONFIG['password_encrypted']
)

# 输出配置
OUTPUT_DIR = 'output'

# ============================================================
# 模板管理配置
# ============================================================

# 模板配置
TEMPLATE_CONFIG = {
    'default_template_path': 'config/default_template.json',
    'backup_dir': 'config/',
    'history_dir': 'config/template_history/',
    'max_history_count': 20,  # 保留最近20个历史版本
}

# 授权用户列表（可保存模板）
# 通过环境变量配置: DASHBOARD_ALLOWED_USERS=user1,user2,user3
ALLOWED_USERS = os.environ.get('DASHBOARD_ALLOWED_USERS', '').split(',') if os.environ.get('DASHBOARD_ALLOWED_USERS') else []

# 管理员用户列表（可重置默认模板）
# 通过环境变量配置: DASHBOARD_ADMIN_USERS=admin1,admin2
ADMIN_USERS = os.environ.get('DASHBOARD_ADMIN_USERS', 'admin').split(',') if os.environ.get('DASHBOARD_ADMIN_USERS') else ['admin']


# ============================================================
# 用户身份获取（Copaw平台注入UserId）
# ============================================================

def get_current_user_id() -> str:
    """
    从Copaw平台获取当前用户工号

    Copaw平台在企业微信机器人场景下会自动注入UserId环境变量
    该UserId即为用户的企业微信工号

    Returns:
        用户工号字符串，未获取到时返回空字符串
    """
    # Copaw平台注入的用户标识
    user_id = os.environ.get('UserId', '')

    # 兼容其他可能的变量名
    if not user_id:
        user_id = os.environ.get('USER_ID', '')

    if not user_id:
        user_id = os.environ.get('COPAW_USER_ID', '')

    return user_id.strip()

# ============================================================
# 环比计算说明：
# 环比上涨TOP10 = (最新月数据 - 次新月数据) / 次新月数据 > 0，按环比降序取前10
# 环比下降TOP10 = (最新月数据 - 次新月数据) / 次新月数据 < 0，按环比升序取前10
