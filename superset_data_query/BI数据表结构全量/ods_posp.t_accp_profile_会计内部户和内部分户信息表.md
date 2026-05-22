# ods_posp.t_acc_balance (账户余额表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| vir_account_no | varchar |  | 虚拟账户号 |
| balance | varchar |  | 帐户余额 |
| fz_balance | varchar |  | 冻结资金 |
| debit_credit_flag | varchar |  | 借贷方向：D-借方；C-贷方；B-轧差 |
| status | varchar |  | 账户状态0-初始1-正常2-账户冻结3-非法余额 |
| check_value | varchar |  | 校验值 |
| operator | varchar |  | 操作员 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| remark | varchar |  | 备注 |
| update_version | varchar |  | 更新版本号 |
