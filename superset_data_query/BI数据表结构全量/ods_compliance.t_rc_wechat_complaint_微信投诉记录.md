# ods_compliance.t_rc_wechat_complaint (微信投诉记录)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  |  |
| out_trade_no | varchar |  | 商户订单号 |
| complaint_time | varchar |  | 投诉时间 |
| amount | bigint |  | 订单金额 |
| payer_phone | varchar |  | 投诉人联系方式 |
| complaint_detail | varchar |  | 投诉具体描述 |
| complaint_state | varchar |  | 投诉单状态 |
| transaction_id | varchar |  | 投诉对应的微信订单号 |
| frozen_end_time | varchar |  | 冻结结束时间 |
| sub_mchid | varchar |  | 子商户号 |
| complaint_handle_state | varchar |  | 投诉单处理状态 |
| agent_id | varchar |  | 一级代理商编号 |
| agent_name | varchar |  | 一级代理商名称 |
| merch_no | varchar |  | 左端商户号 |
| merch_name | varchar |  | 左端商户名 |
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
