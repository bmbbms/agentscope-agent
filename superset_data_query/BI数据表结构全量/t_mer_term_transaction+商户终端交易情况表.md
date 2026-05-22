# 机身号交易统计(月)

**表名**: `edw.trd_stat_physn_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | string | 统计月份 |
| physn | string | 机身号 |
| model | string | 机型名称 |
| model_type | string | 机型类型 |
| cnt | bigint | 交易笔数 |
| amt | bigint | 交易金额 |
| metrics_amt_cnt | bigint | 大于指标的交易笔数 |
| metrics_amt | bigint | 指标金额 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
