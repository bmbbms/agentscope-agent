# xacc.t_union_wetchat_all (银联微信对账文件)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| file_type | varchar |  | 文件类型   acom   acomn   err等 |
| trans_date | varchar |  | 交易时间 |
| official_account | varchar |  | 公众账号id |
| mer_no | varchar |  | 商户号 |
| special_mer_no | varchar |  | 特约商户号 |
| device_no | varchar |  | 设备号 |
| union_order_id | varchar |  | 银联订单号 |
| mer_order_id | varchar |  | 商户订单号 |
| user_id | varchar |  | 用户标识 |
| trans_type | varchar |  | 交易类型 |
| trans_status | varchar |  | 交易状态 |
| payment_bank | varchar |  | 付款银行 |
| currency_type | varchar |  | 货币种类 |
| should_settle_amount | varchar |  | 应结订单金额 |
| cash_coupon | varchar |  | 代金券金额 |
| union_refund_order_id | varchar |  | 银联退款单号 |
| mer_refund_ordre_id | varchar |  | 商户退款单号 |
| refund_amount | varchar |  | 退款金额 |
| recharge_ticket_refund_amount | varchar |  | 充值券退款金额 |
| refund_type | varchar |  | 退款类型 |
| refund_status | varchar |  | 退款状态 |
| product_name | varchar |  | 商品名称 |
| mer_data | varchar |  | 商户数据包 |
| fee | varchar |  | 手续费 |
| rate | varchar |  | 费率 |
| wetchat_amount | varchar |  | 微信对账单订单金额-解析对账单的金额 |
| amount | varchar |  | 订单金额-如果是退款-那么退款订单金额(refundamount)写入此字段-如果是消费-那么消费订单金额（wetchatamount）写入此字段-已增加在借贷记 |
| app_refund_amount | varchar |  | 申请退款金额 |
| rate_remark | varchar |  | 费率备注 |
| ctime | varchar |  | 对账时间-yyyy-mm-dd   hh:mm:ss |
| debit_credit_flag | varchar |  | 借贷记方向 |
| recv_amount | varchar |  | 应到账 |
| recv_cost | varchar |  | 应到账费用-应到账计算公式中，出去交易金额，就为应到账费用 |
| file_name | varchar |  | 对账单文件名称 |
| file_path | varchar |  | 文件路径 |
| busi_type | varchar |  | 文件类型   acoma-comn-err等 |
| busi_sub_type | varchar |  | 业务大类 |
| chn_trans_type | varchar |  | 交易类型，转成   交易3.0的类型   biztype枚举 |
| jl_channel_no | varchar |  | 嘉联渠道号 |
| jl_settle_account | varchar |  | 结算账号 |
| jl_settle_cycle | varchar |  | 结算周期   0-d0   1-t1 |
| jl_account_name | varchar |  | 备付金账户名 |
| jl_account_type | varchar |  | 备付金账户类型   1-存管账户   2-收支账户   3-付款虚户 |
| jl_bank_code | varchar |  | 开户行号 |
| jl_bank_name | varchar |  | 开户行名称 |
| lmer_no | varchar |  | 左端商户号 |
| lmer_name | varchar |  | 左端商户名称 |
| lmer_fee | varchar |  | 左端商户手续费 |
| rmerch_name | varchar |  | 右端商户名称 |
| lorder_id | varchar |  | 左端订单号 |
| lterm_no | varchar |  | 左端终端号 |
| reversal_flag | varchar |  | 渠道冲正标志a-原交易   r-冲正交易 |
| additional_data | varchar |  | 银联附加数据-json格式 |
| delay_date | varchar |  | 清算延迟时间YYYYMMDD |
| dt | integer | partition key |  |
| chn_org_code | varchar | partition key |  |
