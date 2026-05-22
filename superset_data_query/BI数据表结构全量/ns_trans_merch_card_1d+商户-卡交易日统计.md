# 商户-卡交易日统计

**表名**: `edw.ns_trans_merch_card_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| merch_no | string | 商户号,交易商户号 |
| mod_name | string | 机型名称 |
| pay_token | string | 交易卡号,open_id/app_id |
| pay_type | string | 支付类型,微信|支付宝 |
| trade_cnt | bigint | 交易笔数(正向) |
| trade_amt | bigint | 交易金额(正向) |
| trade_ne_cnt | bigint | 交易笔数(反向) |
| trade_ne_amt | bigint | 交易金额(反向) |
| effective_trade_cnt | bigint | 有效交易笔数(正向)
  `effective_trade_amt` bigint COMMENT  |
| effective_trade_ne_cnt | bigint | 有效交易笔数(反向)
  `effective_trade_ne_amt` bigint COMMENT  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计日期 |
