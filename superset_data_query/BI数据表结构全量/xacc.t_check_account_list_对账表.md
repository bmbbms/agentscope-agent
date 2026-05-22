# xacc.t_check_account_list (对账表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| settle_date | varchar |  | 清算日期 |
| chn_settle_date | varchar |  | 渠道清算日期 |
| accounting_date | varchar |  | 账务会计日期 |
| order_id | varchar |  | 订单号 |
| ori_order_id | varchar |  | 原交易订单号 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| trans_time | varchar |  | 交易时间 |
| area_code | varchar |  | 地区码 |
| lmerch_no | varchar |  | 左端商户号 |
| lmerch_name | varchar |  | 左端商户名称 |
| lterm_no | varchar |  | 左端终端号 |
| pmerch_no | varchar |  | 打印商户号 |
| pmerch_name | varchar |  | 打印商户名 |
| lvouch_no | varchar |  | 左端流水号 |
| lref_no | varchar |  | 左端系统参考号 |
| channel_no | varchar |  | 路由交易渠道号 |
| rmerch_no | varchar |  | 右端商户号 |
| rmerch_name | varchar |  | 右端商户名称 |
| rterm_no | varchar |  | 右端终端号(3002的终端号10位) |
| auth_code | varchar |  | 右端授权码 |
| rref_no | varchar |  | 右端参考号 |
| trace_no | varchar |  | 右端流水号11域 |
| transmsn_time | varchar |  | 右端交易传输时间7域 |
| acqins_code | varchar |  | 受理机构代码32域 |
| rorder_id | varchar |  | 右端订单号 |
| pos_entry_code | varchar |  | 输入方式 |
| ccy_code | varchar |  | 货币代码 |
| card_no | varchar |  | 交易卡号 |
| card_type | varchar |  | 卡类型 0--借记卡 1--贷记卡 |
| card_name | varchar |  | 卡名称 |
| card_flag | varchar |  | 卡标志：0-磁卡 1-接触IC卡 2-非接 3-非接云闪付 |
| pwd_sign_free_flag | varchar |  | 免密免签标志：0-免密免签 1-免密不免签 2-免签不免密 3-免密不免签 |
| is_internal_card | varchar |  | 内外卡标志：Y－非外卡，N－外卡 |
| standard_route | varchar |  | 路由标准商户或非标商户：0-标准 1-非标 |
| amount | varchar |  | 交易金额 |
| fee_amount | varchar |  | 交易手续费 |
| lret_code | varchar |  | 系统应答码 |
| chn_ret_code | varchar |  | 渠道系统码 |
| status | varchar |  | 系统状态，右端状态 |
| chn_status | varchar |  | 渠道勾对状态 0-未知,1-已勾对, 2-未勾对 |
| account_status | varchar |  | 记账标志-- 0-未知, 1-已记账,  2-未记账 |
| check_flag | varchar |  | 核对标志0-未核对 1-平账 2-或有长款 3-或有短款 4-长款 5-短款 |
| create_time | varchar |  | 创建时间 |
| remark | varchar |  | 备注 |
| debit_credit_flag | varchar |  | 借贷记方向 |
| agent_id | varchar |  | 渠道机构编号4849000默认为JL总部门 其他为代理商/渠道编号 |
| chn_amt | varchar |  | 渠道金额 |
| chn_fee | varchar |  | 渠道手续费 |
| divide_addfee | varchar |  | 分期付款手续费 |
| fee_calc_type | varchar |  | 手续费计算类型：01:内卡借记卡 02:内卡贷记卡03:银联二维码11:外卡借记卡12:外卡贷记卡20:外币DCC 21:外币EDC 22:外币卡EDC-VM 30:微信 31:支付宝 D0:D0交易 T1:T1交易 |
| fee_cap_flag | varchar |  | 是否封顶1-不封顶 2-封顶 |
| record_source | varchar |  | 分期付款期数，字段采用以前未用字段，所以名字改不了， |
| term_sn | varchar |  | 机身号 |
| add_fee | varchar |  | 附加手续费 |
| is_non_standard | varchar |  | 非标价格商户:1-非标 2-云闪付优惠 其他-标准 |
| user_order_id | varchar |  | 接入方的订单号 |
| fwd_inst_id_code | varchar |  | 发送机构代码（33域） |
| brand_serve_fee | varchar |  | 品牌服务费，通过品牌服务对账文件获取 |
| in_responsibility | varchar |  | 入账责任方,通过自己划拨对账文件获取 |
| chn_trans_type | varchar |  | 渠道交易类型 BizType 枚举，此字段为大数据这边自己加的类型 |
| coma_mer_fee | varchar |  | 商户手续费 o通过coma文件获取 |
| union_file_type | varchar |  | 银联类型  UnionType  枚举 |
| check_id | varchar |  | 对账id |
| reversal_flag | varchar |  | 冲正标志 A-原交易 R-冲正交易 |
| replenish_account_status | varchar |  | 补记账说明  ReplenishAccountStatus 枚举 |
| f_clearing_amt | varchar |  | 转接清算费 |
| f_rec_amt | varchar |  | 受理方应收交换费 |
| f_pay_amt | varchar |  | 受理方应付交换费 |
| ori_check_flag | varchar |  | 原对账状态,如果需要重新对账。每次记录原交易的对账状态 |
| file_path | varchar |  | 文件路径 |
| err_type | varchar |  | 差错类型-0-无-1-长款-2短款-3或有长款-4或有短款 |
| ori_chn_file_rowkey | varchar |  | 原渠道文件表ROWKEY-通过此字段更新渠道文件表左端信息-主要更新银联交易信息左端信息 |
| ori_trans_rowkey | varchar |  | 原交易流水中ROWKEY-根据此字段关联找出交易流水数据 |
| ori_check_date | varchar |  | 原始对账时间 |
| chn_reversal_flag | varchar |  | 渠道冲正标志A-原交易 R-冲正交易 |
| mer_sett_type | varchar |  | 1-月结 |
| entry_mode | varchar |  | 卡输入方式 22域 |
| agt_id | varchar |  | 直属代理商ID |
| top_agt_id | varchar |  | 一级代理商ID |
| belong_branch | varchar |  | 归属机构 |
| branch_company | varchar |  | 分公司ID |
| rate_id | varchar |  | 费率ID |
| err_flag | varchar |  | 差错标记-多次退货-只有一笔对账-其他的标记此标记-1:多笔反向交易并且记账成功 |
| qr_real_card_type | varchar |  | 码付卡类型 0 借记卡 1 贷记卡 |
| f90_2 | varchar |  | 原始交易的系统跟踪号 |
| f90_3 | varchar |  | 原始交易日期时间 |
| original_fee_amount | varchar |  | 原始交易手续费 |
| lstatus | varchar |  | 左端状态 |
| derate_amt | varchar |  | 权益优惠金额 |
| benefit_type | varchar |  | 权益类型0无权益(普通订单) 1预充值权益 2免充值权益 |
| check_amt | varchar |  | 系统对账金额 |
| chn_org_code | varchar |  | 渠道机构号 |
| dt | integer | partition key |  |
| chn_org_type | varchar | partition key |  |
