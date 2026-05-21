# -*- coding: utf-8 -*-
"""
看板生成配置文件模板

部署时请复制此文件为 config.py 并通过环境变量设置：
  SUPERSET_URL - Superset服务地址
  SUPERSET_USERNAME - 用户名
  SUPERSET_PASSWORD - 密码
"""

import os

# 数据获取模式
MODE = 'api'

# Superset BI配置
# 账户密码通过环境变量设置：
#   SUPERSET_URL - Superset服务地址
#   SUPERSET_USERNAME - 用户名
#   SUPERSET_PASSWORD - 密码
SUPERSET_CONFIG = {
    'base_url': os.environ.get('SUPERSET_URL', ''),
    'username': os.environ.get('SUPERSET_USERNAME', ''),
    'password': os.environ.get('SUPERSET_PASSWORD', ''),
    'database': os.environ.get('SUPERSET_DATABASE', ''),
}

# 输出配置
OUTPUT_DIR = os.environ.get('DASHBOARD_OUTPUT_DIR', 'output')

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

# 关键指标保护列表（不允许删除）
PROTECTED_INDICATORS = ['交易总金额', '新增商户数', '活跃商户数']