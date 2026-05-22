# 代理商合伙人提现年统计

**表名**: `edw.agt_stat_withdraw_1y`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| belong_branch | string | 业务部门 |
| r_agt_id | string | 一级代理商 |
| r_agt_name | string | 一级代理商名(公司名称/名称) |
| product_type | string | 产品类型 |
| cnt | bigint | 提现笔数 |
| amt | bigint | 提现金额 |
| fee_amt | bigint | 提现手续费 |
| d0_cnt | bigint | 快速提现笔数 |
| d0_amt | bigint | 快速提现金额 |
| t1_cnt | bigint | 一般提现笔数 |
| t1_amt | bigint | 一般提现金额 |
| priv_cnt | bigint | 对私提现笔数 |
| priv_amt | bigint | 对私提现金额 |
| pub_cnt | bigint | 对公提现笔数 |
| pub_amt | bigint | 对公提现金额 |
| branch_company | string | 分公司ID |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
