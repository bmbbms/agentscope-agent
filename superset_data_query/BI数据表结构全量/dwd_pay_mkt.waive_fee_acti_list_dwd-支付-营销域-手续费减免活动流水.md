# dwd_pay_mkt.waive_fee_acti_list (dwd-支付-营销域-手续费减免活动流水)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 流水id |
| data_source | varchar |  | 数据来源：1.正向，2.反向 |
| order_id | varchar |  | 订单号 |
| act_id | varchar |  | 活动id |
| merch_no | varchar |  | 商户号 |
| merch_name | varchar |  | 商户名称 |
| trans_amount | decimal(22,0) |  | 交易金额 |
| ori_trans_fee | decimal(22,0) |  | 原手续费 |
| waive_trans_fee | decimal(22,0) |  | 优惠手续费 |
| trans_status | varchar |  | 消费状态 0未知 1成功 2失败 3已撤销 |
| trans_time | varchar |  | 交易时间(yyyy-MM-dd HH:mm:ss) |
| fee_calc_type | varchar |  | 计费类型 |
| qr_pay_type | varchar |  | 码付类型 |
| term_no | varchar |  | 终端号 |
| loan_type | varchar |  | 借贷类型 |
| busi_type | varchar |  | 业务大类 |
| sub_busi_type | varchar |  | 业务小类 |
| card_no | varchar |  | 卡号 |
| account_status | varchar |  | 记账状态 0未知 1成功 2失败 |
| ori_order_id | varchar |  | 原订单id |
| periodical_settle | varchar |  | 结算周期，0-实时周期，1-定时结算 |
| batch_no | varchar |  | 批次号 |
| vouch_no | varchar |  | 流水号 |
| refer_no | varchar |  | 系统参考号 |
| settle_time | varchar |  | 会记日期(yyyy-MM-dd HH:mm:ss) |
| card_type | varchar |  | 卡类型 0-借记卡、1-贷记卡、3-余额 |
| user_token | varchar |  | 用户token |
| pay_token | varchar |  | 支付token |
| create_time | varchar |  | 创建时间(yyyy-MM-dd HH:mm:ss) |
| update_time | varchar |  | 更新时间(yyyy-MM-dd HH:mm:ss) |
| dt | integer | partition key | 创建日期(取自create_time) |
