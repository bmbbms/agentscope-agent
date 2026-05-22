# 整体入网-存量商户

**表名**: `edw.brch_stk_stat_netin_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | string | 统计月份(yyyyMM) |
| belong_branch | string | 业务部门 |
| product_type | string | 产品类型 |
| inc_mer_num | bigint | 商户的增量 |
| stk_mer_num | bigint | 商户的存量 |
| stk_mt_num | bigint | 上月商户的存量 |
| stk_yt_num | bigint | 去年同期商户的存量 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
