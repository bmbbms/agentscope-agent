# xacc.t_union_trans_list (银联对账单表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| file_name | varchar |  | 对账单文件名称 |
| ctime | varchar |  | 创建时间yyyyMMddhhmmdd |
| file_path | varchar |  | 文件路径 |
| file_type | varchar |  | 文件类型 ACOM ACOMN ERR等 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| ori_row_key | varchar |  | 有些流水需要关联原交易-记录原交易ROWKEY |
| chn_trans_type | varchar |  | 交易类型 转成 交易3.0的类型 BizType枚举等于业务小类 |
| jl_channel_no | varchar |  |  |
| f32 | varchar |  | 代理机构标识码 |
| f33 | varchar |  | 发送机构标识码 |
| f11 | varchar |  | 系统跟踪号 |
| f7 | varchar |  | 交易传输时间YYYYMMDDhhmmss |
| f2 | varchar |  | 主账号 即交易卡号 |
| f4 | varchar |  | 交易金额 |
| f95 | varchar |  | 部分代收时的承兑金额 |
| f28 | varchar |  | 交易手续费-持卡人交易手续费 |
| msg_type | varchar |  | 报文类型 |
| f3 | varchar |  | 交易类型码 |
| f18 | varchar |  | 商户类型 |
| f41 | varchar |  | 受卡机终端标识码-即终端号 |
| f42 | varchar |  | 受卡方标识码-即商户号 |
| f37 | varchar |  | 检索参考号 |
| f25 | varchar |  | 服务点条件码 |
| f38 | varchar |  | 授权应答码 |
| f100 | varchar |  | 接收机构标识码 |
| f90_2 | varchar |  | 原始交易的系统跟踪号 |
| f39 | varchar |  | 交易返回码 |
| f22 | varchar |  | 服务点输入方式 |
| rec_amt | varchar |  | 受理方应收交换费 |
| pay_amt | varchar |  | 受理方应付交换费 |
| clearing_amt | varchar |  | 转接清算费 |
| single_double_falg | varchar |  | 单双转换标志 |
| f23 | varchar |  | 卡片序列号 |
| f60_2_2 | varchar |  | 终端读取能力 |
| f60_2_3 | varchar |  | IC卡条件代码 |
| f90_3 | varchar |  | 原始交易日期时间YYYY-MDDhhmmss |
| issuer_iden_no | varchar |  | 发卡机构标识码 |
| region_flag | varchar |  | 交易地域标志   0是内卡-1-是外卡 |
| f60_2_5 | varchar |  | 终端类型 |
| f60_2_8 | varchar |  | ECI标志 |
| installment_pdg | varchar |  | 分期付款附加手续费 |
| other_msg | varchar |  | 其他信息 |
| auth_flag | varchar |  | 代授权标志 |
| spe_bill_type | varchar |  | 特殊计费类型 |
| spe_bill_level | varchar |  | 特殊计费档次 |
| trans_way | varchar |  | 交易发起方式 |
| acc_sett_type | varchar |  | 账户结算类型 |
| std_price_mer | varchar |  | 非标价格商户 -非标价格商户-1 非标商户 -0 或 空 标准商户 -2 优惠费率商户 |
| card_acc_grade | varchar |  | 卡账户等级 |
| card_product | varchar |  | 卡产品 |
| is_union_std_card | varchar |  | 是否银联标准卡 |
| other_remain_field | varchar |  | 保留使用 |
| installment_count | varchar |  | 分期付款期数 |
| rec_card_no | varchar |  | 保留使用-转入卡卡号 |
| order_no | varchar |  | 订单号 |
| pay_mode | varchar |  | 支付方式 |
| remain_field_1 | varchar |  | 保留使用 |
| remain_field_2 | varchar |  | 保留使用 |
| remain_field_3 | varchar |  | 保留使用 |
| remain_field_4 | varchar |  | 保留使用 |
| remain_field_5 | varchar |  | 保留使用 |
| remain_field_6 | varchar |  | 保留使用 |
| remain_field_7 | varchar |  | 保留使用 |
| remain_field_8 | varchar |  | 保留使用 |
| acc_grade | varchar |  | 账户等级 |
| is_counter_auth | varchar |  | 是否柜面核身 |
| card_type | varchar |  | 借贷记标识 需要转码 1-借记 2贷记 |
| debit_credit_flag | varchar |  | 借贷方向C-贷D借-根据交易方向和交易类型判断 |
| msg_date | varchar |  | 报文日期YYYYMMDD |
| region_code | varchar |  | 区域号 |
| region_name | varchar |  | 区域名 |
| in_responsibility | varchar |  | 入账责任方-从资金划拨文件中更新进来的 |
| brand_fee | varchar |  | 品牌服务费 |
| charge_type | varchar |  | 渠道类型1-间联-2-平台直连 |
| replenish_account_status | varchar |  | 补记账说明  ReplenishAccountStatus 枚举 |
| union_mer_type | varchar |  | 银联类型 商户类型  UnionType  枚举 |
| is_brand_fee_file | varchar |  | 是否品牌服务费文件数据-品牌服务费特定标示-Y-是 |
| parties_fee | varchar |  | 本方手续费-以下字段要通过脱机交易B文件--更新进来 |
| send_settle_org | varchar |  | 发送方清算机构 |
| receive_settle_org | varchar |  | 接收方清算机构 |
| revocation_flag | varchar |  | 撤销标志 |
| settle_date | varchar |  | 清算日期 |
| settle_frequency | varchar |  | 清算场次 |
| mer_address | varchar |  | 商户名称地址 |
| currency_type | varchar |  | 交易币种 |
| union_sett_org_dis_fee | varchar |  | 银联代理清算收单机构自动折扣手续费 |
| mer_fee | varchar |  | 商户手续费 |
| mer_sett_bank | varchar |  | 商户结算行 |
| mer_sett_bank_cost | varchar |  | 商户结算行费用 |
| in_card_no | varchar |  | 转入卡卡号 |
| instalment_period | varchar |  | 分期付款期数-COMA |
| order_id | varchar |  | 订单号-COMA |
| pay_type | varchar |  | 支付方式-COMA |
| recv_amount | varchar |  | 应到账 |
| recv_cost | varchar |  | 应到账费用 -应到账计算公式中-除去交易金额-就为应到账费用 |
| recv_amt | varchar |  | 应到账金额-->>> 应到账金额+应到账费用 = 应到账 |
| chn_pdg | varchar |  | 渠道手续费 |
| jl_settle_account | varchar |  | 结算账号 |
| jl_settle_cycle | varchar |  | 结算周期 0-D0 1-T1 |
| jl_account_name | varchar |  | 备付金账户名 |
| jl_account_type | varchar |  | 备付金账户类型 1-存管账户 2-收支账户 3-付款虚户 |
| lmer_no | varchar |  | 左端商户号 |
| lmer_name | varchar |  | 左端商户名称 |
| lmer_fee | varchar |  | 左端商户手续费 |
| rmerch_name | varchar |  | 右端商户名称 |
| lorder_id | varchar |  | 左端订单号 |
| lterm_no | varchar |  | 左端终端号 |
| is_coma | varchar |  | 是否COMA文件中的数据-用于判断直连交易 Y-是 |
| reversal_flag | varchar |  | 渠道冲正标志A-原交易 R-冲正交易 |
| pay_scene | varchar |  | 人脸识别标记 |
| receipt_role_one_cost | varchar |  | 收单方服务方角色 1 费用 |
| receipt_role_tow_cost | varchar |  | 收单方服务方角色 2 费用 |
| receipt_role_three_cost | varchar |  | 收单方服务方角色 3 费用 |
| receipt_role_four_cost | varchar |  | 收单方服务方角色 4 费用 |
| receipt_role_five_cost | varchar |  | 收单方服务方角色 5 费用 |
| receipt_role_six_cost | varchar |  | 收单方服务方角色 6 费用 |
| receipt_role_seven_cost | varchar |  | 收单方服务方角色 7 费用 |
| receipt_role_eight_cost | varchar |  | 收单方服务方角色 8 费用 |
| receipt_role_nine_cost | varchar |  | 收单方服务方角色 9 费用 |
| sett_org_custom_cost1 | varchar |  | 银联代理清算收单机构自定义费用 |
| sett_org_custom_cost2 | varchar |  | 银联代理清算收单机构自定义费用 2 |
| sett_org_custom_cost3 | varchar |  | 银联代理清算收单机构自定义费用 3 |
| chn_org_code | varchar |  | 渠道机构号 |
| acq_service_fee | varchar |  | 收单运营服务费 |
| pay_voucher_no | varchar |  | 付款凭证号 |
| asp_code | varchar |  | 应用服务提供方代码标识 |
| dt | integer | partition key |  |
| chn_org_type | varchar | partition key |  |
