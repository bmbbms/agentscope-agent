# ods_posp.t_qrcode_merch (码付渠道商户表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| unique_id | varchar |  | 渠道端唯一编号 |
| merch_no | varchar |  | 渠道商户号 |
| state | varchar |  | 状态 |
| channel_id | varchar |  | 渠道编号 |
| channel_type | varchar |  | 渠道类型 |
| merch_type | varchar |  | 商户类型 |
| charge_type | varchar |  | 计费类型 |
| rate_id | varchar |  | 费率ID,嘉联在支付宝,微信端的费率ID,即mch_id,appid |
| channel_org_id | varchar |  | 渠道商编号 |
| institution_id | varchar |  | 机构号 |
| merch_level | varchar |  | 商户等级 |
| join_flow_id | varchar |  | 支付宝活动入驻流水号 |
| join_state | varchar |  | 支付宝活动入驻状态 0 已申请报名 1审核成功 2审核拒绝 3报名成功 |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 yyyy-MM-dd HH:mm:ss |
| update_user | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 yyyy-MM-dd HH:mm:ss |
| remark | varchar |  | 备注 |
| join_rate | varchar |  | 支付宝活动扣率 |
| join_remark | varchar |  | 支付宝活动备注 |
| channel_merch_name | varchar |  | 渠道商户名称 |
| channel_operate_name | varchar |  | 渠道经营名称 |
| business | varchar |  | 结算规则id |
| industry_id | varchar |  | 行业id |
| gold_plan_status | varchar |  | 点金计划开启状态，0未开启，1开启 |
| mcc | varchar |  | mcc |
| region_code | varchar |  | 地区码 |
| cust_no | varchar |  | 客户号 |
| left_merch_no | varchar |  | 左端商户号 |
| merch_ticket_status | varchar |  | 商家小票开启状态，0未开启（默认），1开启 |
| apply_auth_flag | varchar |  | 实名认证标志 0 未认证 1 已认证 2-已销户 |
| channel_name | varchar |  | 通道名称 10009-银联支付宝 10011-银联微信 10017-网联微信  10018-网联支付宝 |
| netsunion_merch_no | varchar |  | 网联渠道商户编码 |
