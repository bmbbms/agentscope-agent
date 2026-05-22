# xacc.t_union_alipay_list (银联支付宝对账文件)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| ctime | varchar |  | 对账时间yyyyMMddHHmmss |
| union_order_id | varchar |  | 银联交易号 |
| mer_order_id | varchar |  | 商户订单号 |
| business_type | varchar |  | 业务类型 0-交易-1-退款 |
| product_name | varchar |  | 商品名称 |
| create_time | varchar |  | 创建时间 |
| finish_time | varchar |  | 完成时间 |
| shop_no | varchar |  | 门店编号 |
| shop_name | varchar |  | 门店名称 |
| operation_person | varchar |  | 操作员 |
| term_no | varchar |  | 终端号 |
| rec_account | varchar |  | 对方账户 |
| order_amount | varchar |  | 订单金额 |
| rel_recv_amt | varchar |  | 商家实收 |
| alipay_red | varchar |  | 支付宝红包 |
| collect_integral | varchar |  | 集分宝 |
| alipay_discount | varchar |  | 支付宝优惠 |
| business_discount | varchar |  | 商家优惠 |
| ticket_destroy_amt | varchar |  | 券核销金额 |
| ticket_name | varchar |  | 券名称 |
| business_red_amt | varchar |  | 商家红包消费金额 |
| card_cons_amt | varchar |  | 卡消费金额 |
| refund_batch_no | varchar |  | 退款批次号 |
| service_charge | varchar |  | 服务费 |
| rel_recv_net_amt | varchar |  | 实收净额 |
| mer_no | varchar |  | 商户识别号 |
| trans_type | varchar |  | 交易方式0-条码支付 1-扫码支付 |
| remark | varchar |  | 备注 |
| installment_fee | varchar |  | 花呗分期手续费 |
| installment_number | varchar |  | 花呗分期数 |
| amount | varchar |  | 订单金额-退款取退款金额-消费取交易金额 |
| debit_credit_flag | varchar |  | 借贷记方向 |
| recv_amount | varchar |  | 应到账 |
| recv_cost | varchar |  | 应到账费用 ,应到账计算公式中，出去交易金额，就为应到账费用 |
| file_name | varchar |  | 对账单文件名称 |
| file_path | varchar |  | 文件路径 |
| busi_type | varchar |  | 文件类型 ACOMA，COMN,ERR等 |
| busi_sub_type | varchar |  | 业务大类 |
| chn_trans_type | varchar |  | 交易类型，转成 交易3.0的类型 BizType枚举 |
| jl_channel_no | varchar |  | 嘉联渠道号 |
| jl_settle_account | varchar |  | 结算账号 |
| jl_settle_cycle | varchar |  | 结算周期 0-D0 1-T1 |
| jl_account_name | varchar |  | 备付金账户名 |
| jl_account_type | varchar |  | 备付金账户类型 1-存管账户 2-收支账户 3-付款虚户 |
| jl_bank_code | varchar |  | 开户行号 |
| jl_bank_name | varchar |  | 开户行名称 |
| lmer_no | varchar |  | 左端商户号 |
| lmer_name | varchar |  | 左端商户名称 |
| lmer_fee | varchar |  | 左端商户手续费 |
| rmerch_name | varchar |  | 右端商户名称 |
| lorder_id | varchar |  | 左端订单号 |
| lterm_no | varchar |  | 左端终端号 |
| chn_pdg | varchar |  | 渠道手续费 |
| file_type | varchar |  | 文件类型 ACOMA，COMN,ERR等 |
| reversal_flag | varchar |  | 渠道冲正标志A-原交易 R-冲正交易 |
| apply_id | varchar |  | 应用 ID |
| pid | varchar |  | PID |
| activity_flag | varchar |  | 活动标识 |
| product_code | varchar |  | 销售产品码 |
| additional_data | varchar |  | 银联附加数据-json格式 |
| delay_date | varchar |  | 清算延迟时间YYYYMMDD |
| dt | integer | partition key |  |
| chn_org_code | varchar | partition key |  |
