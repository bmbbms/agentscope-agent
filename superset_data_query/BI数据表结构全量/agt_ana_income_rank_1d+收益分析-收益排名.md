# 收益分析-收益排名

**表名**: `edw.agt_ana_income_rank_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | string | 统计日期(yyyyMMdd) |
| agt_id | string | 代理商ID |
| agt_name | string | 代理商名称 |
| belong_branch | string | 业务部门 |
| product_type | string | 产品类型 |
| income | bigint | 交易收益 |
| income_1 | bigint | 上月同期交易收益 |
| profit | bigint | 交易分润 |
| profit_1 | bigint | 上月同期交易分润 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
