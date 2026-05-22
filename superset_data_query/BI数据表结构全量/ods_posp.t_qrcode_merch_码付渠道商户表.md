# ods_posp.t_qr_pay_order (右端码付流水表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 交易订单ID |
| ori_order_id | varchar |  | 原交易订单号 |
| app_id | varchar |  | 接入应用ID |
| merch_no | varchar |  | 接入商户号 |
| term_no | varchar |  | 终端号 |
| channel_id | varchar |  | 渠道ID |
| notify_trans_no | varchar |  | 渠道交易订单 入驻机构交易订单号，仅收到入驻机构回调时，产生数据 |
| trans_type | varchar |  | 交易类型,0-主扫订单(APP扫二维码)，1-被扫订单(扫码枪扫二维码)，2-退款订单，3撤销订单，4-H5支付订单，5-手工退款 |
| trans_time | varchar |  | 交易时间 |
| amount | varchar |  | 交易金额 |
| status | varchar |  | 订单状态 0-新建订单，1-等待确认，2-成功，3-失败,4-已撤销/已冲正，5-已退款,6-部分退款 |
| qr_code | varchar |  | 当前预下单请求生成的二维码码串,请求入驻机构后返回 |
| notify_amount | varchar |  | 异步通知之后返回的实际支付总金额 |
| subject | varchar |  | 订单标题 |
| subject_detail | varchar |  | 订单描述 |
| notify_url | varchar |  | 订单回调地址 |
| auth_code | varchar |  | 授权码 |
| channel_merch_id | varchar |  | 渠道入驻商户ID |
| channel_order_id | varchar |  | 渠道订单号 |
| ret_code | varchar |  | 渠道应答码 |
| ret_msg | varchar |  | 渠道应答信息 |
| create_time | varchar |  | 创建时间 |
| notify_time | varchar |  | 交易通知结果时间,仅收到入驻机构回调时，产生数据,可以看做是成功时间 |
| remark | varchar |  | 备注 |
| update_time | varchar |  | 修改时间 |
| sub_openid | varchar |  | 用户openid |
| sub_appid | varchar |  | 商户appid |
| channel_agent | varchar |  | 收款方机构代码 |
| token_id_url | varchar |  | 微信返回的tokenid |
| settle_date | varchar |  | 清算日期，银联才有 |
| channel_status | varchar |  | 是否回调 |
| chn_trans_time | varchar |  | 渠道交易时间 |
| pay_info | varchar |  | 支付信息(银联) |
| settle_key | varchar |  | 清算主键 |
| pos_condition_code | varchar |  | 服务点条件码 |
| refer_no | varchar |  | 检索参考号 |
| revocation_status | varchar |  | 撤销状态0:待撤销,1:失败,2:成功 |
| area_info | varchar |  | 区域信息 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| channel_fee | varchar |  | 渠道手续费 |
| bank_name | varchar |  | 交易银行名称 |
| card_type | varchar |  | 交易卡类型 |
| discount_amount | varchar |  | 优惠金额 |
| rent_jump_status | varchar |  | 是否租赁合同跳码商户 0-否, 1-是 |
| lmer_no | varchar |  | 左端商户号 |
| pmer_no | varchar |  | 打印商户号 |
| lmer_name | varchar |  | 左端商户名称 |
| fee_calc_type | varchar |  | 手续费计算类型_01内卡借记卡|02内卡贷记卡|03银联二维码|11外卡借记卡|12外卡贷记卡|20外币DCC|21外币EDC|22外币卡EDC-VM|30微信|31支付宝|D0D0交易|T1T1交易 |
| settlement_amount | varchar |  | 应结订单金额.即实际清算的金额.=订单金额-非全额入账的优惠金额 |
| discount_name | varchar |  | 优惠活动名称 |
| coupon_info | varchar |  | 优惠信息 |
| dt | integer | partition key |  |
