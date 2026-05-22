# ods_posp.t_acc_payment_list (POSP提现付款交易流水)

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 提现订单号 |
| pay_date | varchar |  | 付款日期 |
| withdraw_date | varchar |  | 提现时间 |
| withdraw_type | varchar |  | 结算周期0-T0 1-T1 |
| source | varchar |  | 提现来源 |
| org_code | varchar |  | 机构代码 |
| merch_no | varchar |  | 客户编号 |
| account_no | varchar |  | 账户号 |
| account_name | varchar |  | 账户名称 |
| account_type | varchar |  | 账户类型 |
| cnaps_code | varchar |  | 联行行号 |
| cnaps_name | varchar |  | 联行名称（支行名称） |
| amount | varchar |  | 付款金额 |
| fee | varchar |  | 付款手续费 |
| payment_vouch | varchar |  | 付款凭证 |
| state | varchar |  | 使用状态0:未使用(提现请求)，1，已生成批量代付文件，2：成功，3：处理中，4：失败,5-初始化, 6-预处理（管理系统请求重新付款），7暂不付，8-预处理(秒到) |
| operation | varchar |  | 操作状态1-为操作 2-导出 3-代付 6-重新付款 7-失败退款直接退款 8-再次付款失败退款 |
| quick_pay_flag | varchar |  | 是否秒到：0秒到1-延迟到账 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| update_version | varchar |  | 更新版本号 |
| remark | varchar |  | 备注说明 |
| postscript | varchar |  | 付款附言 |
| org_merch_no | varchar |  | 机构商户 |
| merch_type | varchar |  | 商户类型，0-机构商户号，1-商户号 |
| cert_no | varchar |  | 证件号 |
| dt | integer | partition key |  |
