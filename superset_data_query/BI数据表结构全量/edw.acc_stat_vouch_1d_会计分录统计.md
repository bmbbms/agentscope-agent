# edw.acc_stat_vouch_1d (会计分录统计)

| Column | Type | Extra | Comment |
|---|---|---|---|
| accounting_date | bigint |  | 会计日期 |
| busi_type | varchar |  | 交易大类编码 |
| busi_type_name | varchar |  | 交易大类名称 |
| busi_sub_type | varchar |  | 交易小类编码 |
| busi_sub_type_name | varchar |  | 交易小类名称 |
| subject_entry_no | varchar |  | 分录编码 |
| subject_entry_name | varchar |  | 分录编码名称 |
| acc_status | varchar |  | 传票标志 |
| debit_subject_code | varchar |  | 借方科目代码 |
| debit_subject_name | varchar |  | 借方科目名称 |
| credit_subject_code | varchar |  | 贷方科目代码 |
| credit_subject_name | varchar |  | 贷方科目名称 |
| cnt | decimal(22,0) |  | 笔数 |
| account_amt | bigint |  | 记账金额 |
| source_amt | bigint |  | 源交易金额 |
| dt | integer | partition key | 分区日期 |
