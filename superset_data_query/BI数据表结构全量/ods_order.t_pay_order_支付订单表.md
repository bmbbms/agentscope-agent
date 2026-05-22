# ods_order.t_pay_order (支付订单表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 订单号 |
| ori_order_id | varchar |  | 原订单号 |
| busi_type | varchar |  | 业务大类 |
| out_order_id | varchar |  | 外部订单号 |
| merch_no | varchar |  | 商户号 |
| term_no | varchar |  | 终端号 |
| term_sn | varchar |  | 机身号 |
| print_merch_name | varchar |  | 打印商户名 |
| agent_id | varchar |  | 机构号/代理商号 |
| sources | varchar |  | 服务请求来源 |
| trans_time | varchar |  | 交易时间 |
| amount | bigint |  | 订单金额 |
| status | varchar |  | 订单状态;0-初始 1-待确认 2-成功 3-失败 |
| expire_time | varchar |  | 支付过期时间 |
| trans_type | varchar |  | 交易类型：SALE(消费),VSALE(消费撤销),REFUND(退货),AUTH(预授权),VAUTH(预授权撤销),CAUTH(预授权完成),VCAUTH(预授权完成撤销),RCAUTH(预授权完成退款) |
| pay_type | varchar |  | 支付方式,微信支付-wxpay;支付宝-alipay;银联二维码-unionpay;银行卡-bankpay |
| area_code | varchar |  | 交易地区码 |
| location | varchar |  | 交易位置 |
| fee | bigint |  | 手续费，正常扣除手续费使用填写使用+号， 退回手续费请使用-号 |
| fee_type | varchar |  | 手续费类型(同计费系统) |
| pay_token | varchar |  | 提交支付所使用的tocken,如果是是用微信支付宝，银联二维码，则是使用的auth_code,如果是使用的是刷卡支付，则填写脱敏后的银行卡号 |
| ret_code | varchar |  | 响应码 |
| ret_msg | varchar |  | 响应信息 |
| auth_code | varchar |  | 授权码 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| dt | integer | partition key |  |
