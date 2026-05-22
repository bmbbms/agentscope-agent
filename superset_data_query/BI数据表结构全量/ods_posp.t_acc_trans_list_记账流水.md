# ods_posp.t_accp_vouch_list (会计流水明细表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| acc_vouch_no | varchar |  | 会计传票号 |
| order_id | varchar |  | 订单编号 |
| ori_order_id | varchar |  | 原交易订单号 |
| accounting_date | varchar |  | 会计日期 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| subject_entry_no | varchar |  | 科目分录编号 |
| debit_credit_flag | varchar |  | 借贷方向,D-借，C-贷 |
| subject_code | varchar |  | 记账科目代码 |
| org_code | varchar |  | 机构代码 |
| vir_account_no | varchar |  | 记账账户 |
| source_ccy | varchar |  | 源币种 |
| source_amt | varchar |  | 源交易金额 |
| exp_rate | varchar |  | 汇率 |
| account_ccy | varchar |  | 记账币种 |
| account_amt | varchar |  | 记账金额 |
| exter_acc_flag | varchar |  | 外部户标记 N-内部户 Y-外部户 |
| accounting_flag | varchar |  | 会计科目已记账标记 |
| acc_status | varchar |  | 传票标志: 0-正常 Y-抹账或冲账 |
| check_status | varchar |  | 复核标志：0-不需要复核，1-需要复核，2-已复核 |
| settle_status | varchar |  | 传票状态：0-未结算，1-已结算 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| trans_time | varchar |  | 交易时间 |
| account_source | varchar |  | 记账来源 |
| dt | integer | partition key |  |
