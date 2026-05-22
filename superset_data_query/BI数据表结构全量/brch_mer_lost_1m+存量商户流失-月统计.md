# 存量商户流失-月统计

**表名**: `edw.brch_mer_lost_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | bigint | 统计月份 |
| belong_branch | string | 业务部门 |
| product_type | string | 产品类型 |
| normal_mer_cnt | double | 启用商户数 |
| last_1m_lost_mer_cnt | double | 近一个月无交易商户数 |
| last_3m_lost_mer_cnt | double | 近三个月无交易商户数 |
| last_6m_lost_mer_cnt | double | 近半年无交易商户数 |
| last_12m_lost_mer_cnt | double | 近一年无交易商户数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
