# 笔数

**表名**: `edw.acc_stat_vouch_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| accounting_date | bigint | 会计日期 |
| busi_type | string | 交易大类编码 |
| busi_type_name | string | 交易大类名称 |
| busi_sub_type | string | 交易小类编码 |
| busi_sub_type_name | string | 交易小类名称 |
| subject_entry_no | string | 分录编码 |
| subject_entry_name | string | 分录编码名称 |
| acc_status | string | 传票标志 |
| debit_subject_code | string | 借方科目代码 |
| debit_subject_name | string | 借方科目名称 |
| credit_subject_code | string | 贷方科目代码 |
| credit_subject_name | string | 贷方科目名称 |
| cnt | decimal |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
