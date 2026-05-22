# 机构-商户交易-周统计表

**表名**: `edw.trd_mkt_org_merch_trade_1w`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| start_date | string | 统计开始日期:周一 |
| end_date | string | 统计结束:周日 |
| org_code | string | 机构号 |
| org_name | string | 机构名 |
| branch_company | string | 所属分公司ID |
| org_type | string | 项目类型(0-特约商户,1-代理商,2-通用产品,3-商户) |
| merch_no | string | 商户号 |
| merch_name | string | 商户名 |
| trd_cnt | bigint | 交易笔数 |
| trd_amt | bigint | 交易金额 |
| org_trd_cnt | bigint | 外接交易笔数 |
| org_trd_amt | bigint | 外接交易金额 |
| normal_trd_cnt | bigint | 基础收单交易笔数 |
| normal_trd_amt | bigint | 基础收单交易金额 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计周-一年的第几周 |
