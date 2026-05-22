# ods_dcep_trans.t_bank_org_merch (商户入驻受理银行信息)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 入驻ID |
| merch_no | varchar |  | 商户号 |
| ums_mch_id | varchar |  | 渠道商户号 |
| bank_org_id | varchar |  | 受理银行ID |
| wallet_id | varchar |  | 钱包ID |
| state | varchar |  | 启用状态，0-未启用，1已启用 |
| buss_type | varchar |  | 业务种类编码,参照人行标准字典送值 |
| buss_code | varchar |  | 业务类型编码,参照人行标准字典送值 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| merch_name | varchar |  | 商户名称 |
| short_name | varchar |  | 商户简称 |
| source | varchar |  | 来源，0-管理平台,1-嘉联支付APP,默认0 |
