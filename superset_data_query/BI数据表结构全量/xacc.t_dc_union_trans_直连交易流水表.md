# xacc.t_dc_union_trans (直连交易流水表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| check_date | varchar |  | 对账时间 |
| pay_bank | varchar |  | 付款银行 |
| check_id | varchar |  | 对账标识 |
| store_no | varchar |  | 门店编号 |
| device_no | varchar |  | 设备编号 |
| mer_refund_no | varchar |  | 商户退款单号 |
| extend_four | varchar |  | 扩展字段4 |
| extend_three | varchar |  | 扩展字段3 |
| extend_two | varchar |  | 扩展字段2 |
| trip_order_id | varchar |  | 第三方订单号 |
| user_id | varchar |  | 用户标识 |
| trans_type | varchar |  | 交易类型 |
| currency | varchar |  | 货币种类 |
| plat_order_id | varchar |  | 平台订单号 |
| cashier | varchar |  | 收银员 |
| sub_merch_no | varchar |  | 子商户号 |
| settle_amt | varchar |  | 结算金额 |
| total_amt | varchar |  | 总金额 |
| refund_status | varchar |  | 退款状态 |
| mer_data | varchar |  | 商户数据包 |
| trans_time | varchar |  | 交易时间 |
| official_account_id | varchar |  | 公众账号ID |
| terminal_type | varchar |  | 终端类型 |
| merch_no | varchar |  | 商户号 |
| product_short_name | varchar |  | 商户名称1 |
| sub_mer_id | varchar |  | 子商户ID |
| rech_ticket_amt | varchar |  | 免充值券金额 |
| refund_amt | varchar |  | 退款金额 |
| trip_merch_no | varchar |  | 第三方商户号 |
| product_name | varchar |  | 商品名称 |
| plat_refund_no | varchar |  | 平台退款单号 |
| trans_status | varchar |  | 交易状态 |
| mer_order_id | varchar |  | 商户订单号 |
| business_red_packet | varchar |  | 企业红包金额 |
| fee | varchar |  | 手续费 |
| actual_amt | varchar |  | 实收金额 |
| refund_type | varchar |  | 退款类型 |
| business_refund_amt | varchar |  | 企业红包退款金额 |
| rate | varchar |  | 费率 |
| dt | integer | partition key |  |
| chn_org_code | varchar | partition key |  |
