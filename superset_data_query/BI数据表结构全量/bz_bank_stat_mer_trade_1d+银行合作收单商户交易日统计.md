# 银行合作收单商户交易日统计

**表名**: `edw.bz_bank_stat_mer_trade_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| trans_date | string | 交易时间 |
| belong_branch | string | 业务部门 |
| branch_company | string | 分公司ID |
| top_agt_id | string | 一级代理商ID |
| agt_id | string | 代理商ID |
| lmerch_no | string | 商户号 |
| lmerch_name | string | 商户名 |
| group_id | string | 终端组(门店)id |
| lterm_no | string | 终端号 |
| pmerch_name | string | 打印商户名 |
| term_sn | string | 机身号 |
| fee_calc_type | string | 手续费计算类型 |
| update_time | string | 更新时间 |
| stroke_count | string | 笔数 |
| amount_sum | string | 金额 |
| fee_amount_sum | string | 手续费 |
| payable_amount | string | 应付金额 |
| busi_bank_id | string | 商户拓展银行号 |
| busi_bank_path | string | 商户拓展银行号层级路径 |
| busi_bank_name | string | 商户拓展银行名称 |
| bank_manager_id | string | 银行客户经理id |
| bank_manager_name | string | 银行客户经理名称 |
| bank_work_no | string | 银行客户经理工号 |
| group_name | string | 集团名称(门店名称) |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
