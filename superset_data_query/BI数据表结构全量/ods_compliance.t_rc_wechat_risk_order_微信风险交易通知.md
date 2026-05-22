# ods_compliance.t_rc_wechat_risk_order (微信风险交易通知)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  |  |
| mch_id | varchar |  | 微信服务商号 |
| sub_mch_id | varchar |  |  |
| agent_id | varchar |  | 一级代理商号 |
| agent_name | varchar |  | 一级代理商名称 |
| merch_no | varchar |  | 左端商户号 |
| merch_name | varchar |  | 左端商户名 |
| transaction_id | varchar |  | 风险交易的微信订单 |
| event_code | varchar |  | 事件单号 |
| risk_level | varchar |  | 风险级别 |
| risk_level_desc | varchar |  | 风险描述 |
| status | varchar |  | 状态，0-删除，1-正常 |
| deal_measure | varchar |  | 处理措施:01-排除,03-交易黑名单,04-提现黑名单99-其他 |
| verify_status | varchar |  | 审核状态，0未审核 1审核通过 2审核不通过 |
| verify_desc | varchar |  | 审核记录 |
| verify_time | varchar |  | 审核时间 |
| verify_user | varchar |  | 审核人 |
| create_time | varchar |  |  |
| update_time | varchar |  |  |
| create_user | varchar |  | 创建人 |
| update_user | varchar |  | 更新人 |
| remark | varchar |  | 备注 |
| sync_status | varchar |  | 反馈状态  1反馈成功 2反馈失败 |
