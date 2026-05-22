# ods_dcep_trans.t_dcep_trans_list (数字货币交易流水)

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 订单号 |
| ori_order_id | varchar |  | 原交易订单号 |
| access_app_id | varchar |  | 外部接入应用ID |
| out_order_id | varchar |  | 外部订单号 |
| merch_no | varchar |  | 商户号 |
| term_no | varchar |  | 终端号 |
| term_sn | varchar |  | 机身号 |
| ums_mch_id | varchar |  | 渠道商户号 |
| amount | bigint |  | 交易金额 |
| trans_time | varchar |  | 交易时间yyyy-MM-dd HH:mm:ss |
| trans_type | varchar |  | 交易类型:1-正向交易；2-退款交易,3-撤销交易 |
| trans_sub_type | varchar |  | 受理方式,1-终端扫APP，2-扫动态二维码 |
| state | varchar |  | 交易状态，0-订单初始化状态，交易未发送到渠道；1-支付中，订单已经发送到渠道，等待渠道扣款；2-支付成功；3-交易失败, 4-已退款；5-已关单 |
| chn_order_id | varchar |  | 渠道订单号 |
| auth_code | varchar |  | 二维码信息/授权码 |
| mch_id | varchar |  | 银行提供给嘉联的商户号 |
| bank_code | varchar |  | 银行编号 |
| bank_name | varchar |  | 受理银行名称 |
| bank_org_id | varchar |  | 受理银行ID |
| remark | varchar |  | 备注 |
| ret_code | varchar |  | 渠道响应码 |
| ret_msg | varchar |  | 渠道响应信息 |
| create_time | varchar |  | 创建时间yyyy-MM-dd HH:mm:ss |
| update_time | varchar |  | 更新时间yyyy-MM-dd HH:mm:ss |
| promotion_info | varchar |  | 营销信息 |
