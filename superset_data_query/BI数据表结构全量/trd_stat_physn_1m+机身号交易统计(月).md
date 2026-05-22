# 交易金额

**表名**: `edw.trd_mkt_org_merch_trade_cp_1w`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| start_date | date | 统计开始日期 |
| end_date | date | 统计结束日期 |
| period | string | 统计周期-W |
| org_code | string | 机构号 |
| org_name | string | 项目(机构名称) |
| branch_company | string | 所属分公司 |
| org_type | string | 项目类型(0-特约商户,1-代理商,2-通用产品,3-商户) |
| merch_no | string | 商户号 |
| merch_name | string | 商户名 |
| trd_cnt | bigint | 交易笔数 |
| trd_amt | decimal |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计时间 |
