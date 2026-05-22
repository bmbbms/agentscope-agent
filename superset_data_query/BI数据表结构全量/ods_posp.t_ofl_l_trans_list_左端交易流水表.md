# ods_posp.t_ofl_l_trans_list (左端交易流水表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 订单编号 |
| ori_order_id | varchar |  | 原订单编号 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| card_no | varchar |  | 卡号 |
| amount | varchar |  | 交易金额 |
| term_sn | varchar |  | 机身号 |
| settle_id | varchar |  | 清算用户ID |
| lmerch_no | varchar |  | 商户号 |
| lmerch_name | varchar |  | 商户名称 |
| print_merch_no | varchar |  | 打印商户号 |
| print_merch_name | varchar |  | 打印商户名称 |
| lterm_no | varchar |  | 终端号 |
| term_device_serial_no | varchar |  | 终端设备序列号 |
| lbatch_no | varchar |  | 批次号 |
| lvouch_no | varchar |  | 流水号 |
| lrefer_no | varchar |  | 系统参考号，供下游使用，平台生成 |
| auth_code | varchar |  | 授权码 |
| pos_entry_mode | varchar |  | 服务点输入方式码 |
| ori_lbatch_no | varchar |  | 原批次号 |
| ori_lvouch_no | varchar |  | 原流水号 |
| ori_lrefer_no | varchar |  | 原系统参考号 |
| qr_pay_code | varchar |  | 二维码付款码 |
| chn_order_id | varchar |  | 渠道订单号 |
| card_type | varchar |  | 卡类型：0.借记卡，1.贷记卡 |
| card_name | varchar |  | 卡名称 |
| ccy_code | varchar |  | 货币代码 |
| card_flag | varchar |  | 卡标志：0-磁卡 1-接触IC卡 2-非接 3-非接云闪付 4-手机pay |
| pwd_sign_free_flag | varchar |  | 免密免签标志：0-免密免签 1-免密不免签 2-免签不免密 3-不免密不免签 |
| is_internal_card | varchar |  | 内外卡标志：Y－非外卡，N－外卡 |
| area_code | varchar |  | 地区代码 |
| standard_route | varchar |  | 路由标准商户或非标商户：0-标准 1-非标 |
| channel_no | varchar |  | 渠道编号 |
| trans_time | varchar |  | 交易时间 |
| settle_date | varchar |  | 清算日期 |
| status | varchar |  | 交易状态：0－已发送，1－待确认，2－成功，3－失败，4－已撤消，5－已冲正，6－已退货 7－预授权已完成 |
| ret_code | varchar |  | 应答码 |
| ret_msg | varchar |  | 应答信息 |
| create_time | varchar |  | 记录创建时间 |
| update_time | varchar |  | 记录更新时间 |
| remark | varchar |  | 备注 |
| position_info | varchar |  | 位置：ADDRESS |
| account_flag | varchar |  | 记账标记  0-未记账 1-已记账 |
| fee_amount | varchar |  | 交易手续费，记账成功时更新 |
| fee_calc_type | varchar |  | 手续费计算类型：01 内卡借记卡 02 内卡贷记卡 03 银联二维码 04 云闪付优惠(贷记卡) 05 云闪付优惠(借记卡) 08 会员消费 11 外卡借记卡 12 外卡贷记卡 20 外币DCC 21 外币EDC 22 外币卡EDC-VM 30 微信 31 支付宝 D0 D0交易 T1 T1交易  |
| bank_code | varchar |  | 发卡行编号 |
| acq_code | varchar |  | 受理机构代码 |
| qr_channel_id | varchar |  | 码付渠道编号，10001：微众银行-微信渠道；10000：深结算-支付宝渠道；10005：银联二维码 |
| batchup_flag | varchar |  | 批上送标记 0-未批上送 1-对账平勾兑 2-批上送勾兑 |
| agent_id | varchar |  | 渠道机构编号，4849000默认为JL总部门，其他为代理商/渠道编号 |
| exter_card_flag | varchar |  | 外卡通道选择标识(63域），JLD-DCC通道，JLW-EDC通道 |
| flush_flag | varchar |  | 冲正标记 |
| confirm_flag | varchar |  | 交易确认状态：0-待确认 1-已收到终端确认报文 2-日切补记账 |
| card_organization | varchar |  | 信用卡组织（60.1域返回） |
| billing_amount | varchar |  | DCC交易执卡人扣账金额 |
| billing_ccycode | varchar |  | DCC交易执卡人扣账货币代码 |
| conversion_rate | varchar |  | DCC交易执卡人扣账汇率 |
| en_rmerch_name | varchar |  | 右端商户英文名 |
| term_device_type | varchar |  | 终端设备类型 02-传统POS 03-MPOS 04-智能POS |
| term_encrypt_random | varchar |  | 加密随机因子 |
| term_serial_encrypt_data | varchar |  | 硬件序列号密文数据 |
| term_app_version | varchar |  | 终端应用版本号 |
| stock_flag | varchar |  | 存量标识 0-存量 1-新增 |
| ori_amount | varchar |  | 原始交易金额 |
| user_order_id | varchar |  | 订单支付时，服务商的订单号 |
| discount_settle_type | varchar |  |  |
| finnal_amount | varchar |  |  |
| exter_discount_amount | varchar |  |  |
| discount_amount | varchar |  |  |
| dt | integer | partition key |  |
