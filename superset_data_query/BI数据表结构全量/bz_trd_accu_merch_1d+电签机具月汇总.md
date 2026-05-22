# 电签机具月汇总

**表名**: `edw.bz_trd_accu_merch_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| merch_no | string | 商户号 |
| trans_month | string | 交易月份 |
| rent_time | string | 服务费完成时间 |
| total_amount | double | 交易额 |
| total_count | double | 交易笔数 |
| trans_date | string |  |
| update_time | string | 更新时间 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
