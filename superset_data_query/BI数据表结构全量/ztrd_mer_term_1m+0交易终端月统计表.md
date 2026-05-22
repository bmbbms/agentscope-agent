# 商户无交易月统计

**表名**: `edw.ztrd_merch_stat_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| merch_no | string | 商户号 |
| status | string | 商户状态(1:启用 2:停用 3:已注销) |
| net_date | string | 入网日期 |
| last_trans_time | string | 最后一次交易时间 |
| last_succ_trans_time | string | 最后一次成功交易时间 |
| no_trans_months | string | 无交易月份数 |
| no_succ_trans_months | string | 无成功交易月份数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计月份 |
