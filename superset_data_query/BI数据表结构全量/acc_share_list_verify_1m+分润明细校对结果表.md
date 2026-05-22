# 分润明细校对结果表

**表名**: `edw.acc_share_list_verify_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| exec_month | string | 核对月份 |
| agent_id | string | 代理商ID |
| agent_name | string | 代理商名称 |
| agent_account | string | 代理商帐号 |
| accrual_tax_amount | double | 分明明细-含税金额 |
| this_provision | double | 财务统计-当月分润 |
| diff_amount | double | 差异金额 |
| update_time | string | 更新时间 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
