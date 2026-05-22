# ods_posp.t_withhold_trans_list (代扣交易流水表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 订单号 |
| agreement_id | varchar |  | 关联扣费协议ID |
| voucher_id | varchar |  | 凭证ID |
| ori_order_id | varchar |  | 退款/冲正原订单号 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| merch_no | varchar |  | 商户号 |
| term_no | varchar |  | 终端号 |
| term_sn | varchar |  | 终端序列号 对应押金/租金关联终端 |
| source | varchar |  | 请求来源 |
| agent_id | varchar |  | 代理商ID |
| trans_time | varchar |  | 请求时间 |
| amount | varchar |  | 应扣费金额 |
| status | varchar |  | 状态 0扣款中 1成功 2失败 3已冲正 4已退款 |
| ret_code | varchar |  | 返回码 |
| ret_msg | varchar |  | 返回信息 |
| create_time | varchar |  | 记录创建时间 |
| update_time | varchar |  | 记录更新时间 |
| remarks | varchar |  | 备注 |
| begin_date | varchar |  | 扣费起始日期 |
| end_date | varchar |  | 扣费结束日期 |
| batch_no | varchar |  | 批次号 |
| order_type | varchar |  | 订单类型（1 对公打款，2 扣交易款，3 扫码付款） |
| pay_mode | varchar |  | 付款方式（1，支付宝   2，微信，3 线下，4免收） |
| real_amount | varchar |  | 实际付款金额 |
| free_amount | varchar |  | 减免金额 |
| merch_name | varchar |  | 商户名 |
| agent_name | varchar |  | 代理商名字 |
| pay_order_id | varchar |  | 付款订单号/商户订单号 |
| accounting_tag | varchar |  |  |
| own_refund | varchar |  |  |
| finish_time | varchar |  |  |
| fee_type | varchar |  | 费率类型 |
| dt | integer | partition key |  |
