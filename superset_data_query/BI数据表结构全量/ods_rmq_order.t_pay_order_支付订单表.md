# ods_rmq_order.t_pay_order (支付订单表)

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
| status | varchar |  | 订单状态 0-初始 1-待确认 2-成功 3-失败 |
| expire_time | varchar |  | 支付过期时间 |
| trans_type | varchar |  | 交易类型：SALE(消费) VSALE(消费撤销) REFUND(退货) AUTH(预授权) VAUTH(预授权撤销) CAUTH(预授权完成) VCAUTH(预授权完成撤销) RCAUTH(预授权完成退款) |
| pay_type | varchar |  | 支付方式：微信支付-wxpay 支付宝-alipay 银联二维码-unionpay 银行卡-bankpay |
| area_code | varchar |  | 交易地区码 |
| location | varchar |  | 交易位置 |
| fee | bigint |  | 手续费，正常扣除手续费使用填写使用+号， 退回手续费请使用-号 |
| fee_type | varchar |  | 手续费类型(同计费系统) |
| pay_token | varchar |  | 提交支付所使用的tocken，如果是是用微信支付宝，银联二维码，则是使用的auth_code,如果是使用的是刷卡支付，则填写脱敏后的银行卡号 |
| ret_code | varchar |  | 响应码 |
| ret_msg | varchar |  | 响应信息 |
| auth_code | varchar |  | 授权码 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| pay_method | varchar |  | 0-银行卡磁条，1-银行卡插卡，2-银行卡非接，3-非接双免，4-手机pay，5-码付被扫，6码付主扫 |
| pwd_free | varchar |  | 0-免密免签 1-免密不免签 2-免签不免密 3-不免密不免签 |
| busi_sub_type | varchar |  | 交易小类 |
| is_internal_card | varchar |  | Y-内卡 N-外卡 |
| fund_type | varchar |  | 0-借记卡 1-贷记卡 2-余额支付 |
| add_fee | bigint |  | 附加手续费 |
| ccy_code | varchar |  | 货币代码 |
| channel_no | varchar |  | 渠道编号 10001、10011-银联微信,10005-银联二维码,10009、10020-银联支付宝,10017-网联微信,10018-网联支付宝,10019-深银联-微信渠道,10021-银联QQ,10023-银联分期码,25-讯联,26-连通,27-万事网联,9-广银联（平台直连）,14-深圳银联（平台直连）,15-总银联（间连）,1001-天津银联（平台直连）,1018-四川银联（平台直连）,1025-北京银联(平台直连),2006-上海银联(平台直连),18-工卡消费 |
| fee_detail | varchar |  | 交易手续费详情 |
| settle_amount | bigint |  | 渠道结算金额 |
| trans_merch_no | varchar |  | 交易商户号 |
| meta_write_service | varchar |  | 数据写入服务 |
| meta_output_time | varchar |  | 数据写入时间 |
| meta_ori_table | varchar |  | 源数据表 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| discount_amount | bigint |  | 优惠金额 |
| finnal_amount | bigint |  | 实付金额 |
| position_detail | varchar |  | 位置信息 |
| chn_pomotion_detail | varchar |  | 优惠信息 |
| open_id | varchar |  | open_id |
| sub_open_id | varchar |  | sub_open_id |
| pwd_fee | varchar |  | 免签免密标志 |
| hbfq_info | varchar |  | 花呗分期信息 |
| sign_info | varchar |  | 记账签名信息 |
| card_flag | varchar |  | 卡标记 |
| benefit_amount | varchar |  | 权益优惠金额 |
| attach_info | varchar |  | 附加信息 |
| channel_info | varchar |  | 渠道信息 |
| org_code | varchar |  | 机构号 |
| card_interval | varchar |  | 终端读卡时间 |
| device_model | varchar |  | 终端机型 |
| dt | integer | partition key | 创建日期 |
