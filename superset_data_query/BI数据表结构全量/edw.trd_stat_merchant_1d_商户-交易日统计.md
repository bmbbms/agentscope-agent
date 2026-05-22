# edw.trd_mkt_org_merch_trade_1d (机构-商户交易统计表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| org_code | varchar |  | 机构号 |
| org_name | varchar |  | 机构名 |
| branch_company | varchar |  | 所属分公司ID |
| org_type | varchar |  | 项目类型(0-特约商户,1-代理商,2-通用产品,3-商户) |
| merch_no | varchar |  | 商户号 |
| merch_name | varchar |  | 商户名 |
| trd_cnt | bigint |  | 交易笔数 |
| trd_amt | bigint |  | 交易金额 |
| org_trd_cnt | bigint |  | 外接交易笔数 |
| org_trd_amt | bigint |  | 外接交易金额 |
| normal_trd_cnt | bigint |  | 基础收单交易笔数 |
| normal_trd_amt | bigint |  | 基础收单交易金额 |
| org_trd_refund_cnt | bigint |  | 机构退款交易笔数 |
| org_trd_refund_amt | bigint |  | 机构退款交易金额 |
| dt | integer | partition key | 统计日期 |
