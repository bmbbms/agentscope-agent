# ods_clear.t_clearing_quick_list (D0清算流水表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 订单号 |
| withdraw_order_id | varchar |  | 提现订单号 |
| merch_no | varchar |  | 商户号 |
| trans_amt | bigint |  | 交易金额 |
| trans_fee | bigint |  | 交易手续费 |
| settle_amt | bigint |  | 结算金额 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| status | varchar |  | 状态0-待提现，1提现成功 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| card_type | varchar |  | 卡类型 |
| ret_code | varchar |  | 返回码 |
| ret_msg | varchar |  | 返回信息 |
| trans_time | varchar |  | 交易时间 |
| fee_calc_type | varchar |  | 计费类型 |
| dt | integer | partition key |  |
