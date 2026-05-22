# ods_mpos.t_member_rentconfig (商户押金)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号(立刷) |
| produce | varchar |  | LS-立刷，LSP-立刷商户版，FS-飞刷等等 |
| rent_amount | varchar |  | 押金 |
| status | varchar |  | 0-未收 1-已收 2-已退 3-冲销购机款 |
| total_amount | varchar |  | 累计交易金额 |
| refund_deal_amount | varchar |  | 退还押金的交易金额 |
| refund_date | varchar |  | 预计退还时间 |
| real_refund_date | varchar |  | 实际退还时间 |
| create_time | varchar |  | 添加时间 |
| update_time | varchar |  | 更新时间 |
| pos_merch_no | varchar |  | POS+商户号 |
| order_id | varchar |  | 订单号 |
| pay_status | varchar |  | 付款状态 （0   初始订单  1： 待付款  2 ：付款中 3 ：付款成功 4 ：付款失败  5 ：未知状态 6.已失效） |
| trans_time | varchar |  | 交易时间(收到押金的时间) |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| term_no | varchar |  | 终端号 |
| term_sn | varchar |  | 机身号 |
| merch_name | varchar |  | 商户名 |
| card_no | varchar |  | 银行卡号 |
| acc_flag | varchar |  | 是否记账 1.记账 2.未记账 |
| agree_flag | varchar |  | 创建协议状态  1 成功  2 失败 |
| pay_order_id | varchar |  | 订单号，用于记账 |
| sign_pic | varchar |  | 签购单图片URL |
| agent_id | varchar |  | 代理商号 |
| type | varchar |  | 0-立刷商户版押金订单 1-OEM订单 |
| settle_merch_no | varchar |  | 清算商户号 |
| refund_type | varchar |  | 押金退还类型 0-到期退 1-随时退 |
| pay_channel | varchar |  | 系统类型：openSys-开放平台  orderSys-订单pos平台 |
| account_type | varchar |  | 主要判断出是否记账，1记账，0不记账 -区别于acc_flag |
| ret_msg | varchar |  |  |
| ret_code | varchar |  | 交易错误码 |
| acc_date | varchar |  | 记账日期 |
