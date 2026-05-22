# 商户达标交易(计算交易卡数) - 日统计

**表名**: `edw.ns_trans_merch_reach_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| agt_id | string | 直属代理商 |
| agt_path | string | 代理商层级 |
| first_merch_no | string | 首次入网商户号 |
| cust_no | string | 客户号 |
| register_type | string | 商户类型-营业执照|小微-同商户号-取第一条 |
| net_date | string | 入网日期 |
| trade_cnt | bigint | 交易笔数(正向) |
| trade_amt | bigint | 交易金额(正向) |
| trade_ne_cnt | bigint | 交易笔数(反向) |
| trade_ne_amt | bigint | 交易金额(反向) |
| effective_trade_cnt | bigint | 有效交易笔数(正向)|单笔交易金额 >= 2 |
| effective_trade_amt | bigint | 有效交易金额(正向)|单笔交易金额 >= 2 |
| effective_trade_ne_cnt | bigint | 有效交易笔数(反向)|单笔交易金额 >= 2 |
| effective_trade_ne_amt | bigint | 有效交易金额(反向)|单笔交易金额 >= 2 |
| inc_effective_token_num | bigint | 新增有效卡号数 |
| total_effective_token_num | bigint | 累计有效卡号数 |
| merch_no | string | 商户号 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计日期 |
