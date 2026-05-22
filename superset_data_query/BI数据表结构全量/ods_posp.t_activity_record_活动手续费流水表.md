# ods_posp.t_activity_record (活动手续费流水表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 流水ID |
| activity_id | varchar |  | 活动ID |
| order_id | varchar |  | 订单号 |
| merch_no | varchar |  | 商户号 |
| fee_calc_type | varchar |  | 手续费计算类型：01 内卡借记卡 02 内卡贷记卡 03 银联二维码 04 云闪付优惠 11 外卡借记卡 12 外卡贷记卡 20 外币DCC 21 外币EDC 22 外币卡EDC-VM 30 微信 31 支付宝 D0 D0交易 T1 T1交易  |
| card_no | varchar |  | 卡号 |
| trans_time | varchar |  | 交易时间 |
| amount | varchar |  | 交易金额 |
| busi_type | varchar |  | 业务大类 |
| sub_busi_type | varchar |  | 业务小类 |
| fee | varchar |  | 原手续费 |
| derate_fee | varchar |  | 优惠手续费 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| merch_name | varchar |  | 商户名称 |
| trans_status | varchar |  | 消费状态 0未知 1成功 2失败 3已撤销 |
| account_status | varchar |  | 记账状态 0未知 1成功 2失败 |
| ori_order_id | varchar |  | 原订单id |
| periodical_settle | varchar |  | 0-实时结算 1-定期结算 |
| term_no | varchar |  | 终端号 |
| batch_no | varchar |  | 批次号 |
| vouch_no | varchar |  | 流水号 |
| refere_no | varchar |  | 系统参考号 |
| settle_time | varchar |  | 会计日期 |
| statistics_id | varchar |  | 关联统计表id |
| send_account_status | varchar |  | 会记账状态用以标记是否成功调用会记账接口，0未记账，1已记账 |
| card_type | varchar |  | 卡类型 |
| qr_pay_type | varchar |  | 码付类型 alipay wxpay unionpay |
| dt | integer | partition key |  |
