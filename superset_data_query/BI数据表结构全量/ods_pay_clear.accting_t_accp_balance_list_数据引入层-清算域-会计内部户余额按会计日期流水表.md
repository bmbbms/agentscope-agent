# ods_pay_clear.accting_t_accp_balance_list (数据引入层-清算域-会计内部户余额按会计日期流水表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| accounting_date | varchar |  | 会计日期 |
| vir_account_no | varchar |  | 虚拟账户号 |
| subject_code | varchar |  | 科目代码 |
| balance_dir_flag | varchar |  | 余额方向D-借方；C-贷方；B-轧差(按借方，允许未负数) |
| begin_balance | bigint |  | 期初余额 |
| debit_amount | bigint |  | 借方发生额 |
| credit_amount | bigint |  | 贷方发生额 |
| end_balance | bigint |  | 期末余额 |
| check_value | varchar |  | 校验值 |
| status | varchar |  | 账户状态0-初始1-正常2-账户冻结3-非法余额 |
| begin_bal_flag | varchar |  | 期初余额标记,0-未截转1-已截转 |
| end_day_flag | varchar |  | 日结标记,0-未日结1-已日结 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| remarks | varchar |  | 备注 |
| update_version | bigint |  | 更新版本号 |
| meta_write_service | varchar |  | 写入服务 |
| meta_ori_table | varchar |  | 原表 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
