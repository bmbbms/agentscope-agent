# dwd.just_assist_trade_list (司法协查流水)

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 订单号 |
| ori_order_id | varchar |  | 原订单号 |
| chn_order_id | varchar |  | 渠道订单号 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| busi_sub_type_desc | varchar |  | 业务小类描述 |
| lterm_no | varchar |  | 终端号 |
| lmer_no | varchar |  | 商户号 |
| lmer_name | varchar |  | 商户名 |
| pmer_no | varchar |  | 打印商户号 |
| pmer_name | varchar |  | 打印商户名称 |
| card_no | varchar |  | 交易卡号 |
| card_type | varchar |  | 卡类型 |
| card_type_desc | varchar |  | 卡类型描述 |
| openid | varchar |  | openid |
| appid | varchar |  | appid |
| qr_pay_code | varchar |  | 支付码 |
| bank_name | varchar |  | 开户行信息 |
| amt | bigint |  | 交易金额 |
| fee_amt | bigint |  | 交易手续费 |
| fee_calc_type_desc | varchar |  | 费用计算类型描述 |
| fee_calc_type | varchar |  | 费用计算类型 |
| ret_code | varchar |  | 应答码 |
| trans_time | varchar |  | 交易时间 |
| term_sn | varchar |  | 机身号 |
| rterm_no | varchar |  | 右端终端号 |
| rmer_no | varchar |  | 右端商户号 |
| rmer_name | varchar |  | 右端商户名 |
| status | varchar |  | 交易状态 |
| status_desc | varchar |  | 交易状态描述 |
| trade_ip | varchar |  | 交易IP |
| lon | varchar |  | 经度 |
| lat | varchar |  | 纬度 |
| area_code | varchar |  | 交易地区码 |
| allname | varchar |  | 交易省市 |
| position_info | varchar |  | 位置信息 |
| dt | integer | partition key |  |
