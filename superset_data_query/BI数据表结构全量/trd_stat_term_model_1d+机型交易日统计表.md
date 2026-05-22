# 交易金额

**表名**: `edw.trd_mkt_org_trade_cp_1w`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| start_date | date | 统计开始日期 |
| end_date | date | 统计结束日期 |
| period | string | 统计周期-W |
| org_code | string | 机构号 |
| org_name | string | 项目(机构名称) |
| branch_company | string | 分公司ID |
| company_name | string | 分公司名称 |
| org_type | string | 项目类型(0-特约商户,1-代理商,2-通用产品,3-商户) |
| stk_mer_num | bigint | 存量商户数 |
| inc_mer_num | bigint | 新增商户数 |
| trd_mer_num | bigint | 有交易商户数 |
| trd_cnt | bigint | 交易笔数 |
| trd_amt | decimal |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计时间 |
