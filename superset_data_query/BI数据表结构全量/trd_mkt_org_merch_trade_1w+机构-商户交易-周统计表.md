# 商户终端最后交易情况表

**表名**: `edw.t_term_last_transaction`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| merch_no | string | 商户号 |
| term_no | string | 终端号（无终端号则显示为空） |
| dev_sn | string | 机身号 |
| product_type | string | 产品类型(2-MPOS, 5-POSP) |
| last_trade_time | string | 最后一笔交易时间 |
| last_sus_trade_time | string | 最后一笔成功交易时间 |
| last_trade_amt | string | 最后一笔交易金额 |
| last_sus_trade_amt | string | 最后一笔成功交易金额 |
| first_trade_time | string | 首次交易时间 |
| first_trade_amt | bigint | 首次交易金额 |
| first_succ_trade_time | string | 首次成功交易时间 |
| first_succ_trade_amt | bigint | 首次成功交易金额 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计日期 |
