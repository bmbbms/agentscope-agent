# 机构-机构交易统计表

**表名**: `edw.trd_mkt_org_trade_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| org_code | string | 机构号 |
| org_name | string | 项目(机构名称) |
| branch_company | string | 所属分公司 |
| company_name | string | 所属分公司名称 |
| org_type | string | 项目类型(0-特约商户,1-代理商,2-通用产品,3-商户) |
| stk_mer_num | bigint | 累计商户数 |
| inc_mer_num | bigint | 新增商户数 |
| trd_mer_num | bigint | 当日有交易商户数 |
| trd_cnt | bigint | 交易笔数 |
| trd_amt | bigint | 交易金额 |
| org_trd_cnt | bigint | 外接交易笔数 |
| org_trd_amt | bigint | 外接交易金额 |
| normal_trd_cnt | bigint | 基础收单交易笔数 |
| normal_trd_amt | bigint | 基础收单交易金额 |
| org_trd_refund_cnt | bigint | 机构退款交易笔数 |
| org_trd_refund_amt | bigint | 机构退款交易金额 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计日期 |
