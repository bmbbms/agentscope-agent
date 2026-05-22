# xdata.t_full_trade_bill (交易流水全量表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | 主键 |
| order_id | varchar |  | 订单编号 |
| ori_order_id | varchar |  | 原订单编号 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| trade_type | varchar |  | 原交易类型 |
| card_no | varchar |  | 交易卡号 |
| amt | bigint |  | 交易金额 |
| term_sn | varchar |  | 机身号 |
| lmer_no | varchar |  | 左端商户号 |
| lmer_name | varchar |  | 左端商户名称 |
| pmer_no | varchar |  | 打印商户号 |
| pmer_name | varchar |  | 打印商户名称 |
| lterm_no | varchar |  | 左端终端号 |
| dev_no | varchar |  | 终端设备序列号 |
| lbatch_no | varchar |  | 左端批次号 |
| lvouch_no | varchar |  | 左端流水号 |
| lrefer_no | varchar |  | 左端系统参考号 |
| auth_no | varchar |  | 授权码 |
| entry_mode | varchar |  | 服务点输入方式码 |
| ori_lbatch_no | varchar |  | 原左端批次号 |
| ori_lvouch_no | varchar |  | 原左端流水号 |
| ori_lrefer_no | varchar |  | 原左端系统参考号 |
| chn_order_id | varchar |  | 渠道订单号 |
| card_type | varchar |  | 卡类型0-借记卡，1-贷记卡 |
| card_name | varchar |  | 卡名称 |
| ccy_code | varchar |  | 货币代码 |
| card_flag | varchar |  | 卡标志：0-磁卡 1-接触IC卡 2-非接 3-非接云闪付 4-手机pay |
| pwdfree | varchar |  | 免密免签标志：0-免密免签 1-免密不免签 2-免签不免密 3-不免密不免签 |
| internal_flag | varchar |  | 内外卡标志：Y－非外卡，N－外卡 |
| area_code | varchar |  | 地区代码 |
| std_route | varchar |  | 路由标准商户或非标商户：0-标准 1-非标 |
| chn_no | varchar |  | 渠道编号 |
| trans_time | varchar |  | 交易时间 |
| sett_date | varchar |  | 清算日期 |
| status | varchar |  | 交易状态：0－已发送，1－待确认，2－成功，3－失败，4－已撤消，5－已冲正，6－已退货 7－预授权 |
| ret_code | varchar |  | 应答码 |
| ret_msg | varchar |  | 应答信息 |
| fee_amt | bigint |  | 交易手续费 |
| bank_code | varchar |  | 发卡行编号 |
| acq_code | varchar |  | 受理机构代码（32） |
| fwd_code | varchar |  | 发送机构代码（33域） |
| qr_chn_id | varchar |  | 码付渠道编号 |
| agent_id | varchar |  | 渠道机构编号 |
| ex_card_flag | varchar |  | 外卡通道选择标识(63域) |
| flush_flag | varchar |  | 冲正标记 |
| confirm_flag | varchar |  | 交易确认状态：0-待确认 1-已收到终端确认报文 |
| card_org | varchar |  | 信用卡组织(60.1域返回) |
| dcc_amt | bigint |  | DCC交易执卡人扣账金额 |
| dcc_ccycode | varchar |  | DCC交易执卡人扣账货币代码 |
| dcc_rate | varchar |  | DCC交易执卡人扣账汇率 |
| en_rmer_name | varchar |  | 右端商户英文名 |
| ldev_type | varchar |  | 终端设备类型 02-传统POS 03-MPOS 04-智能POS |
| term_version | varchar |  | 终端应用版本 |
| ori_amt | bigint |  | 原始交易金额 |
| user_order_id | varchar |  | 订单支付时，服务商的订单号 |
| rmer_no | varchar |  | 右端商户号 |
| rmer_name | varchar |  | 右端商户名 |
| rterm_no | varchar |  | 右端终端号 |
| transmsn_time | varchar |  | 交易传输时间(7域) |
| rvouch_no | varchar |  | 右端跟踪号(11域) |
| rrefer_no | varchar |  | 右端系统参考号 |
| rstatus | varchar |  | 右端交易状态 |
| rret_code | varchar |  | 右端应答码 |
| rret_msg | varchar |  | 右端应答信息 |
| rdev_type | varchar |  | 右端终端设备类型 |
| rbatch_no | varchar |  | 右端批次号 |
| region_flag | varchar |  | 交易地域信息 |
| dcc_order_id | varchar |  | DCC汇率查询的订单号 |
| chn_refer_no | varchar |  | 右端渠道检索参考号 |
| discount_amt | bigint |  | 优惠金额 |
| ex_discount_amt | bigint |  | 额外立减金额 |
| real_amt | bigint |  | 实付金额 |
| discount_sett_type | varchar |  | 优惠金额是否参与清结算 |
| spec_fee_type | varchar |  | 特殊计费类型 |
| spec_fee_level | varchar |  | 特殊计费档次 |
| accounting_date | varchar |  | 会计日期 |
| cap_flag | varchar |  | 0-不封顶商户 1-封顶商户 2-触发封顶 |
| source | varchar |  | 2-mpos 3-trade2.0 4-trade3.0 5-pos+ 6-码付 |
| qr_pay_code | varchar |  | 支付码 |
| c_time | varchar |  | 记录创建时间 |
| u_time | varchar |  | 记录更新时间 |
| position_info | varchar |  | 位置信息 |
| account_flag | varchar |  | 记账标记：0-未记账 1-已记账 |
| batchup_flag | varchar |  | 批上送标记 0-未批上送 1-对账平勾兑 2-批上送勾兑 |
| stock_flag | varchar |  | 存量标识 0-存量 1-新增 |
| indirect_flag | varchar |  | 间联标识 1-间联 2-直联 |
| agt_id | varchar |  | 直属代理商ID |
| agt_name | varchar |  | 直属代理商名称 |
| top_agt_id | varchar |  | 一级代理商ID |
| top_agt_name | varchar |  | 一级代理商名称 |
| agt_path | varchar |  | 代理商路径 |
| belong_branch | varchar |  | 归属机构 |
| clerk | varchar |  | 渠道经理(业务员) |
| mer_type | varchar |  | 商户类型 |
| fee_calc_type | varchar |  | 手续费计算类型 01-内卡借记卡 02-内卡贷记卡 03-银联二维码 11-外卡借记卡 12-外卡贷 |
| additional_fee | bigint |  | 附加手续费 |
| rtrans_time | varchar |  | 右端交易时间 |
| chn_amt | bigint |  | 渠道交易额 |
| chn_fee | bigint |  | 渠道手续费 |
| acc_status | varchar |  | 记账标识 |
| acc_type | varchar |  | 记账类型 |
| pay_info | varchar |  | 支付信息 |
| settle_key | varchar |  | 清算key |
| area_info | varchar |  | 银联区域 |
| trade_ip | varchar |  | 交易IP |
| lon | varchar |  | 经度 |
| lat | varchar |  | 纬度 |
| chn_code | varchar |  | 渠道机构编码_对账渠道chn_code |
| update_status | varchar |  | 更新状态0-初始3-已撤销4-已冲正5-已退货 |
| batchup_update_time | varchar |  | 批上送时间 |
| check_date | varchar |  | 对账日期-yyyymmdd |
| chn_check_date | varchar |  | 渠道账单日期-yyyymmdd |
| final_check_date | varchar |  | 账单对平日期-yyyymmdd |
| check_flag | varchar |  | 核对标志 |
| cd_direct | varchar |  | 借贷方向 |
| profit_fee | bigint |  | 分润手续费 |
| profit_date | varchar |  | 分润日期-yyyymmdd |
| fee_rate | varchar |  | 扣率(针对MPOS) |
| ramt | bigint |  | 右端交易金额 |
| mpos_order_id | varchar |  | MPOS订单ID |
| branch_company | varchar |  | 分公司ID |
| brand_fee | bigint |  | 品牌服务费 |
| mer_sett_type | varchar |  | 1-月结 |
| rate_id | varchar |  | 费率ID |
| qr_card_type | varchar |  | 码付款卡类型 01 借记卡 02 贷记卡（含准贷记卡） |
| qr_bank_name | varchar |  | 交易银行名称 |
| qr_real_card_type | varchar |  | 码付卡类型 0 借记卡 1 贷记卡 |
| mer_fee | bigint |  | 商户手续费,只取左端交易流水的费用 |
| ori_busi_sub_type | varchar |  | 原交易小类 |
| fyp_amt | bigint |  | 保费手续费 |
| lr_type | varchar |  | 机构标识: 1-左端，2-右端 |
| term_group_id | varchar |  | 终端组ID |
| appid | varchar |  | appid |
| openid | varchar |  | openid |
| bank_name | varchar |  | 开户行名称 |
| bank_no | varchar |  | 开户行行号 |
| remark | varchar |  | POSP左端端流水备注信息 |
| busi_bank_code | varchar |  | 商户拓展银行号 |
| busi_bank_path | varchar |  | 商户拓展银行号层级路径 |
| busi_bank_name | varchar |  | 商户拓展银行名称 |
| bank_work_no | varchar |  | 银行客户经理银行工号 |
| bank_manager_id | varchar |  | 银行客户经理ID |
| bank_manager_name | varchar |  | 银行客户经理名称 |
| busi_id | varchar |  | 业务编号,CONSUME：消费 REFUND：退货 VIP：会员 RENT：押金 WITHDRAW：提现 GUARANTEE：担保 SERVICE_FEE：服务费 |
| expire_time | varchar |  | 订单过期时间 |
| dis_amount | bigint |  | 权益优惠金额 |
| acc_amount | bigint |  | 记账金额 |
| dis_fee | bigint |  | 优惠手续费 |
| acc_merch_no | varchar |  | 记账商户号 |
| benefit_type | varchar |  | 类型: 0-无权益(普通订单) 1-预充值权益 2-免充值权益 |
| chn_dis_amount | bigint |  | 渠道平台优惠金额(参与清算) |
| chn_trade_amount | bigint |  | 渠道交易金额 |
| chn_mer_dis_amount | bigint |  | 渠道商户优惠金额(不参与清算) |
| store_id | varchar |  | 门店号 |
| store_name | varchar |  | 门店名称 |
| trans_type | varchar |  | 交易类型 |
| subject | varchar |  | 商品信息 |
| flow_status | varchar |  | 流程状态 0－初始，1－受理成功，2－成功，3－失败，4－已撤消，5－已完成 |
| ori_trans_fee | bigint |  | 原始手续费 |
| mer_area_code | varchar |  | 商户入网地区码 |
| settlement_amount | varchar |  | 应结订单金额.即实际清算的金额.=订单金额-非全额入账的优惠金额 |
| pay_type | varchar |  | 交易类型：wxpay、alipay、unionpay [for 担保交易] |
| org_code | varchar |  | 机构号，来源外接码付表 t_out_qr_pay_order |
| chn_out_order_id | varchar |  | 渠道外部订单号 |
| pos_condition_code | varchar |  | 服务点条件码 |
| discount_name | varchar |  | 优惠活动名称 |
| coupon_info | varchar |  | 优惠信息 |
| dt | integer | partition key |  |
