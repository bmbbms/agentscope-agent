# -*- coding: utf-8 -*-
"""
Superset BI 数据查询客户端
"""

# 使用轻量版（不依赖pandas，避免numpy兼容性问题）
from .superset_lite import SupersetClient, SupersetClientLite, get_config

__all__ = ['SupersetClient', 'SupersetClientLite', 'get_config']