# 数据引入层-客户域-会计分录-提现统计

**表名**: `edw.t_accp_withdraw_total`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | bigint | 会计日期yyyyMMdd |
| acc_sub_type | string | 业务小类 |
| vir_account_no | string | 分户（编码） |
| vir_account_name | string | 分户（名称） |
| account_amt | bigint | 出金金额 |
| vouch_type | string | 来源类型：sys/ori_000000；sys/agent_200310；sys/agent_10008 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
