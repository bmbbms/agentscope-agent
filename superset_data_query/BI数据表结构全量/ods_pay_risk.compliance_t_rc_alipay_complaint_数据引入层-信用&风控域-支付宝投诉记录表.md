# ods_pay_risk.compliance_t_rc_alipay_complaint (数据引入层-信用&风控域-支付宝投诉记录表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 支付宝投诉记录ID |
| merch_no | varchar |  | 子商户号 |
| merch_name | varchar |  | 商户名称 |
| channel_merch_no | varchar |  | 渠道商户号 |
| agent_id | varchar |  | 代理商ID |
| agent_name | varchar |  | 代理商名称 |
| risk_type | varchar |  | 风险类型 |
| channel_risk_type | varchar |  | 渠道风险类型 |
| risk_description | varchar |  | 风险描述 |
| risk_identification_time | varchar |  | 风险识别时间 |
| complaint_time | varchar |  | 投诉时间 |
| complaint_detail | varchar |  | 投诉内容 |
| risk_tag | varchar |  | 风险标签 |
| remark | varchar |  | 备注 |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| company_id | varchar |  | 归属分公司ID |
| company_name | varchar |  | 归属分公司名称 |
| srv_id | varchar |  | 服务商ID |
| push_flag | varchar |  | 推送标识0未推送1已推送 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
