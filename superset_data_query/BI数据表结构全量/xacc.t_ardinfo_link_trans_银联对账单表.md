# xacc.t_ardinfo_link_trans (银联对账单表)

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
| f32 | varchar |  | 代理机构标识码 |
| f33 | varchar |  | 发送机构标识码 |
| f11 | varchar |  | 系统跟踪号 |
| f7 | varchar |  | 交易传输时间 |
| f2 | varchar |  | 主账号 |
| f4 | varchar |  | 交易金额 |
| message_type | varchar |  | 报文类型 |
| f3 | varchar |  | 交易类型码 |
| f18 | varchar |  | 商户类型 |
| f41 | varchar |  | 受卡机终端标识码 |
| f42 | varchar |  | 受卡方标识码 |
| f43 | varchar |  | 受卡方名称地址 |
| f37 | varchar |  | 检索参考号 |
| f25 | varchar |  | 服务点条件码 |
| f38 | varchar |  | 授权应答码 |
| f100 | varchar |  | 接收机构标识码 |
| f90_2 | varchar |  | 原始交易的系统跟踪号 |
| f39 | varchar |  | 交易返回码 |
| f49 | varchar |  | 交易货币 |
| f22 | varchar |  | 服务点输入方式 |
| f50 | varchar |  | 清算货币 |
| f5 | varchar |  | 清算金额 |
| f9 | varchar |  | 清算汇率 |
| f15 | varchar |  | 清算日期 |
| f16 | varchar |  | 兑换日期 |
| f51 | varchar |  | 持卡人账户货币 |
| f6 | varchar |  | 持卡人扣账金额 |
| f10 | varchar |  | 持卡人扣账金额 |
| ought_receive_fee | varchar |  | 应收手续费（交易币种 |
| ought_payment_fee | varchar |  | 应付手续费（交易币种） |
| ought_receive_fee_sett | varchar |  | 应收手续费（清算币种） |
| ought_payment_fee_sett | varchar |  | 应付手续费（清算币种） |
| transfer_service_fee | varchar |  | 转接服务费 |
| trans_fee | varchar |  | 持卡人交易手续费 |
| f23 | varchar |  | 卡片序列号 |
| f60_2_2 | varchar |  | 终端读取能力 |
| f60_2_3 | varchar |  | IC 卡条件代码 |
| f90_3 | varchar |  | 原始系统日期时间 |
| issuer_iden_no | varchar |  | 发卡机构标识码 |
| f60_2_5 | varchar |  | 终端类型 |
| credit_card_company | varchar |  | 国际信用卡公司/外资机构标识 |
| f60_2_8 | varchar |  | ECI 标志 |
| reserved_use | varchar |  | 保留使用 |
| debit_credit_flag | varchar |  | 借贷记方向 |
| reversal_flag | varchar |  | 冲正标志R |
| discount_flag | varchar |  | 优惠标记　１:优惠　空：不优惠 |
| dt | integer | partition key |  |
| chn_org_code | varchar | partition key |  |
