# ods_mpos.t_insurance_order (延迟到账险)

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 订单号 |
| trans_amount | varchar |  | 交易金额 |
| config_id | varchar |  | 保单费率ID |
| fee | varchar |  | 保单费 |
| repay_amount | varchar |  | 赔偿金额 |
| status | varchar |  | "保单状态 0-初始订单,1-订单已发送,2-保险成功,3-保险失败" |
| ctime | varchar |  | 创建时间 |
| utime | varchar |  | 投保时间 |
| customer_id | varchar |  | 客户ID |
| phone | varchar |  | 手机号码 |
| trans_id | varchar |  | 交易订单号 |
| ply_no | varchar |  | 保单号 |
| node_id | varchar |  | 手机系统类型 |
| version | varchar |  | 系统版本号 |
| order_uuid | varchar |  | 保险存储的UUID |
| channel_id | varchar |  | 渠道编号 |
| auditer_id | varchar |  | 审核人 |
| audit_time | varchar |  | 审核时间 |
| cert_no | varchar |  | 证件号 |
| name | varchar |  | 姓名 |
| sex | varchar |  |  |
| address | varchar |  |  |
| busi_type | varchar |  | 业务类型。0：对公 1：对私 |
| busi_sub_type | varchar |  | 业务小类(4001充值，4002退款) |
| adjust_fee | varchar |  |  |
| dt | integer | partition key |  |
