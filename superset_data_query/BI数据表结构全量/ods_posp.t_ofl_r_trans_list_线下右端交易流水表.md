# ods_posp.t_ofl_r_trans_list (线下右端交易流水表 )

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 订单号 |
| ori_order_id | varchar |  | 原订单号 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| channel_no | varchar |  | 渠道编号 |
| rmerch_no | varchar |  | 商户号 |
| rmerch_name | varchar |  | 商户名称 |
| rterm_no | varchar |  | 终端号 |
| card_no | varchar |  | 卡号 |
| ccy_code | varchar |  | 货币代码 |
| amount | varchar |  | 交易金额 |
| mchnt_type | varchar |  | 商户类型（18域) |
| pos_entry_mode | varchar |  | 服务点输入方式码 F22 |
| transmsn_time | varchar |  | 交易传输时间（7域） |
| trace_no | varchar |  | 跟踪号（11域） |
| acq_inst_id_code | varchar |  | 受理机构代码（32） |
| fwd_inst_id_code | varchar |  | 发送机构代码（33域） |
| installment | varchar |  | 分期付款期数 |
| auth_code | varchar |  | 授权码 |
| refer_no | varchar |  | 系统参考号 |
| trans_time | varchar |  | 交易时间，右端上送渠道时间 |
| settle_date | varchar |  | 清算日期 |
| status | varchar |  | 交易状态：0－已发送，1－待确认，2－成功，3－失败，4－已撤消，5－已冲正，6－已退货 |
| ret_code | varchar |  | 交易应答码 |
| ret_msg | varchar |  | 应答信息 |
| term_device_type | varchar |  | 右端终端设备类型02-POS 03-MPOS |
| stock_flag | varchar |  | 存量标志，0-存量1-新增 |
| create_time | varchar |  | 记录创建时间 |
| update_time | varchar |  | 最后跟新时间 |
| remark | varchar |  | 备注 |
| batch_no | varchar |  | 批次号 |
| card_organization | varchar |  | 信用卡卡组织(63.1)域 |
| billing_amount | varchar |  | DCC交易持卡人扣账金额 |
| conversion_rate | varchar |  | DCC交易持卡人扣账汇率 |
| billing_ccycode | varchar |  | DCC交易持卡人扣账货币代码 |
| trans_region_flag | varchar |  | 交易地域信息：0－银联卡境内交易，1－银联卡跨境交易，2－外卡收单交易，3－银联卡境外交易 |
| dcc_query_order_id | varchar |  | DCC汇率查询的订单号 |
| channel_code | varchar |  | 渠道机构编号 |
| r_reference_no | varchar |  | 渠道检索参考号 |
| discount_amount | varchar |  | 优惠金额 |
| exter_discount_amount | varchar |  | 额外立减金额 |
| finnal_amount | varchar |  | 实付金额 |
| discount_settle_type | varchar |  | 优惠金额是否参与清结算，0-不参与，1-参与 |
| spec_fee_type | varchar |  | 特殊计费类型 |
| spec_fee_level | varchar |  | 特殊计费档次 |
| dt | integer | partition key |  |
