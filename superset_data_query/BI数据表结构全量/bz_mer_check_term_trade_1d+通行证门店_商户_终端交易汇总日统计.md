# 通行证门店/商户/终端交易汇总月统计

**表名**: `edw.bz_mer_check_term_trade_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| trans_month | string | 会计日期-yyyymm |
| belong_branch | string | 业务部门 |
| branch_company | string | 分公司ID |
| top_agt_id | string | 一级代理商ID |
| agt_id | string | 代理商ID |
| lmerch_no | string | 商户号 |
| lmerch_name | string | 商户名 |
| group_id | string | 终端组(门店)id |
| group_name | string | 终端组(门店)名称 |
| lterm_no | string | 终端号 |
| pmerch_name | string | 打印商户名 |
| term_sn | string | 机身号 |
| fee_calc_type | string | 手续费计算类型 |
| update_time | string | 更新时间 |
| stroke_count | string | 笔数 |
| amount_sum | string | 金额 |
| fee_amount_sum | string | 手续费 |
| payable_amount | string | 应付金额 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
