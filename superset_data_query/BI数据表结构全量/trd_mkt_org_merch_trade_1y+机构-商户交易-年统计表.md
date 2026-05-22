# 终端交易汇总表

**表名**: `edw.t_term_trans_info`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | string | 交易日期 |
| branch_company | string | 分公司ID |
| belong_branch | string | 业务部门 |
| agt_id | string | 代理商ID |
| r_agt_id | string | 一级代理商ID |
| lterm_no | string | 终端号 |
| lmer_no | string | 商户号 |
| lmer_name | string | 商户名 |
| pmer_name | string | 打印商户名 |
| amt | bigint | 交易金额 |
| cnt | bigint | 交易笔数 |
| fee_calc_type | string | 计费类型 |
| fee_amt | bigint | 交易手续费 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
