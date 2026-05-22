# ods_compliance.t_rc_alipay_risk_push (支付宝风险推送记录)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  |  |
| status | varchar |  | 状态，0-未处理，1-已处理 |
| pid | varchar |  | 申请业务合作伙伴ID |
| smid | varchar |  | 涉嫌风险子商户在支付宝被分配的商户ID |
| external_id | varchar |  |  |
| source_id | varchar |  |  |
| agent_id | varchar |  | 一级代理商号 |
| agent_name | varchar |  | 一级代理商名称 |
| merch_no | varchar |  | 左端商户号 |
| merch_name | varchar |  | 左端商户名 |
| trade_nos | varchar |  | 风险交易号样例 |
| alipay_trade_nos | varchar |  | 支付宝流水号 |
| bank_card_no | varchar |  | 银行卡号 |
| risk_type | varchar |  | 风险类型，如欺诈、赌博、套现、套费率 |
| risk_level | varchar |  | 风险情况描述，如欺诈风险（欺诈风险极高，且有投诉） |
| risk_desc | varchar |  | 风险定位原因说明，如套费率：例如：买卖家关系异常 |
| deal_measure | varchar |  |  |
| verify_status | varchar |  |  |
| verify_desc | varchar |  |  |
| verify_time | varchar |  |  |
| verify_user | varchar |  |  |
| create_user | varchar |  |  |
| update_user | varchar |  |  |
| create_time | varchar |  |  |
| update_time | varchar |  |  |
| remark | varchar |  |  |
