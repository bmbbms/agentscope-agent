# 整体入网-每日新增商户

**表名**: `edw.brch_inc_netin_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| period | string | 统计周期(M:按月统计,D:按日统计) |
| stat_time | string | 统计时间(yyyyMMdd/yyyyMM) |
| stat_date | string | 统计日期(yyyyMMdd) |
| belong_branch | string | 业务部门 |
| product_type | string | 产品类型 |
| inc_mer_num | bigint | 增量商户数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
