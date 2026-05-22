# ods_pay_risk.riskctrl_t_judicature_risk (司法风险)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| merch_no | varchar |  | 商户号 |
| merch_name | varchar |  | 商户名 |
| sub_merch_no | varchar |  | 子商户号 |
| sub_merch_name | varchar |  | 子商户名 |
| judicature_type | varchar |  | 司法类型 |
| register_time | varchar |  | 入网时间 |
| contact_mobile | varchar |  | 联系人电话 |
| contact_name | varchar |  | 联系人 |
| legal_person_name | varchar |  | 法人名字 |
| legal_person_cert_no | varchar |  | 法人证件号 |
| union_bank_name | varchar |  | 开户行 |
| account_name | varchar |  | 户名 |
| account_no | varchar |  | 开户账号 |
| auth_flag | varchar |  | 收款类型 |
| register_address | varchar |  | 入网详细地址 |
| trade_time | varchar |  | 最后成功交易时间 |
| salesman | varchar |  | 业务员名称 |
| department_name | varchar |  | 业务部门 |
| company_name | varchar |  | 分公司名称 |
| top_agent_id | varchar |  | 一级代理商id |
| top_agent_name | varchar |  | 一级代理商名称 |
| second_agent_id | varchar |  | 二级代理商id |
| second_agent_name | varchar |  | 二级代理商名称 |
| direct_agent_id | varchar |  | 直属代理商id |
| direct_agent_name | varchar |  | 直属代理商名称 |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| push_event | varchar |  | 0: 否； 1：是 |
| event_id | varchar |  | 事件id |
| deal_status | varchar |  | 处理状态 0 待处理 1处理中 2已处理 |
| handle_result | varchar |  | 处理结果 0未排除可疑 1排除可疑 |
| case_type | varchar |  | 案件类型 |
| search_time | varchar |  | 查询时间 |
| search_unit | varchar |  | 查询单位 |
| trade_order | varchar |  |  |
| trade_amount | decimal(22,0) |  |  |
| deal_result_desc | varchar |  | 处理结果描述 |
| product_type | varchar |  | 产品类型：01-标准POS；02-扫码POS；03-SAAS； |
| search_reason | varchar |  |  |
| feature_analysis | varchar |  |  |
