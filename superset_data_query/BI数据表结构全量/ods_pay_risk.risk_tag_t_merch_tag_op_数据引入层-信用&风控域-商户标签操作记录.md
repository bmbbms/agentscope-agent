# ods_pay_risk.riskctrl_t_union_pay_laundering (银联-洗钱)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| case_no | varchar |  | 案例编号 |
| merch_no | varchar |  | 商户号 |
| merch_name | varchar |  | 商户名称 |
| trade_account_no | varchar |  | 交易主体卡号 |
| case_create_time | varchar |  | 案例生成日期 |
| account_org_name | varchar |  | 交易主体银行卡开卡机构名称 |
| account_org_code | varchar |  | 交易主体银行卡开卡机构代码 |
| trade_num | varchar |  | 涉案交易笔数 |
| trade_amount | varchar |  | 涉案交易金额 |
| channel_merch_no | varchar |  | 渠道商户号 |
| channel_merch_name | varchar |  | 渠道商户名称 |
| case_check_status | varchar |  | 案例审核状态 |
| account_type | varchar |  | 卡类型 |
| acquiring_agency_code | varchar |  | 交易对手收单机构代码CACD域 |
| acquiring_agency_name | varchar |  | 收单机构名称 |
| mcc_code | varchar |  | MCC |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| sub_merch_no | varchar |  | 子商户号 |
| sub_merch_name | varchar |  | 子商户名称 |
