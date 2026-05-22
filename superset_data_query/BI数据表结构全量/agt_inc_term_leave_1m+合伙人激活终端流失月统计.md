# 合伙人激活终端流失月统计

**表名**: `edw.agt_inc_term_leave_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | bigint | 统计月份 |
| belong_branch | string | 业务部门 |
| branch_company | string | 分公司ID |
| r_agt_id | string | 一级代理商ID |
| r_agt_name | string | 一级代理商名 |
| product_type | string | 产品类型 |
| term_type | string | 终端类型 |
| term_num | bigint | 激活终端数 |
| lv_term_num1 | bigint | 第1月流失数 |
| lv_term_num2 | bigint | 第2月流失数 |
| lv_term_num3 | bigint | 第3月流失数 |
| lv_term_num4 | bigint | 第4月流失数 |
| lv_term_num5 | bigint | 第5月流失数 |
| lv_term_num6 | bigint | 第6月流失数 |
| lv_term_num7 | bigint | 第7月流失数 |
| lv_term_num8 | bigint | 第8月流失数 |
| lv_term_num9 | bigint | 第9月流失数 |
| lv_term_num10 | bigint | 第10月流失数 |
| lv_term_num11 | bigint | 第11月流失数 |
| lv_term_num12 | bigint | 第12月流失数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
