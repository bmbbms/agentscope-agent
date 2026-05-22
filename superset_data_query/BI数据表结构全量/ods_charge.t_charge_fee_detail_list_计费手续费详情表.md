# ods_charge.t_charge_fee_detail_list (计费手续费详情表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 订单号 |
| ori_order_id | varchar |  | 原交易订单号 |
| pay_order_id | varchar |  | 支付订单号 |
| charge_fee_type | varchar |  | 计费费率类型 01:内卡借记,02:内卡贷记,03:银联二维码,04-云闪付贷记,05-云闪付借记,08-会员消费,11:外卡借记卡,12:外卡贷记卡,20:外币DCC,21:外币EDC,22:外币卡EDC-VM,29-QQ支付,30:微信,31:支付宝,40-人脸借记,41-人脸贷记,T0:快速提现,T1:普通提现,M0-首笔免费,M1-非接双免,M2-手机pay双免,M3-银联二维码,M4-外卡,M5-内卡, |
| merch_no | varchar |  | 商户号 |
| amount | varchar |  | 记账金额 |
| fee_rate | varchar |  | 手续费费率 |
| calc_type | varchar |  | 手续费费率类型： 0-基础费率 1-渠道活动费率 4-会员费率 5-业务活动费率 |
| trans_fee | varchar |  | 基础手续费 |
| finnal_fee | varchar |  | 最终手续费 |
| fee_cap_flag | varchar |  | 手续费封顶标记 0-不封顶费率 1-封顶费率 2-触发封顶 |
| amount_detail | varchar |  | 交易金额详情 |
| fee_detail | varchar |  | 交易手续费详情 |
| extra_fee_detail | varchar |  | 额外手续费详情 |
| activity_derate_flag | varchar |  | 是否优惠减免 |
| month_settle_flag | varchar |  | 是否月结 |
| benefit_flag | varchar |  | 是否存在权益 |
| create_time | varchar |  | 创建时间 |
| insurance_fee | varchar |  | 保险费金额 |
| add_fee | varchar |  | 附加手续费 |
| dt | integer | partition key |  |
