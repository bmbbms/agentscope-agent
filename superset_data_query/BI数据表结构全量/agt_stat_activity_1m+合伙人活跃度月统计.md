# 合伙人活跃度日统计

**表名**: `edw.agt_stat_activity_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| belong_branch | string | 业务部门 |
| product_type | string | 产品类型 |
| net_type | string | 入网证件类型 |
| r_agt_id | string | 一级代理商ID |
| r_agt_company_name | string | 一级代理商(公司名称、名称） |
| act_mer_cnt | bigint | 活跃商户数 |
| act_term_cnt | bigint | 活跃终端数 |
| act_mer_cnt_7d | bigint | 近7日活跃商户数 |
| act_term_cnt_7d | bigint | 近7日活跃终端数 |
| act_mer_cnt_15d | bigint | 近15日活跃商户数 |
| act_term_cnt_15d | bigint | 近15日活跃终端数 |
| act_mer_cnt_30d | bigint | 近30日活跃商户数 |
| act_term_cnt_30d | bigint | 近30日活跃终端数 |
| act_mer_cnt_month | bigint | 当月活跃商户数 |
| act_term_cnt_month | bigint | 当月活跃终端数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
