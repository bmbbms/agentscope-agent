# ods_pay_rev.agent_t_customer_activate_detail (激活达标记录)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 自增id,使用序列S_T_ACTIVATE_DETAIL_ID |
| merchno | varchar |  | 商户号 |
| business_type | bigint |  | 业务类型 |
| activate_time | varchar |  | 激活时间 |
| card_no | varchar |  | 激活卡号 |
| activate_top | bigint |  | 本次激活金额上限(废弃) |
| policy_id | bigint |  | 营销政策id |
| list_id | varchar |  | 激活交易流水id |
| status | varchar |  | 激活状态,1--激活成功,2--未激活（废弃） |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间 |
| user_id | bigint |  | 一级代理商 |
| physn | varchar |  | 机身号 |
| activate_amount | bigint |  | 激活金额 |
| activate_status | varchar |  | 激活状态,0--未激活,1--已激活 |
| bonus_status | varchar |  | 奖励状态,0--未发放，1--已发放 |
| activate_stair | bigint |  | 激活阶段 |
| path | varchar |  | 激活path |
| physn_type | bigint |  |  |
