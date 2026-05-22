# 代理商新增终端留存月统计

**表名**: `edw.agt_inc_term_keep_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | bigint | 统计日期 |
| product_type | string | 产品类型 |
| belong_branch | string | 业务部门 |
| r_agt_id | string | 一级代理商ID |
| r_agt_name | string | 一级代理商名 |
| r_agt_company | string | 一级代理商公司名 |
| term_type | string | 终端类型 |
| inc_term_num | bigint | 新增商户数 |
| act_term_num0 | bigint | 第0月活跃商户数 |
| act_term_num1 | bigint | 第1月活跃商户数 |
| act_term_num2 | bigint | 第2月活跃商户数 |
| act_term_num3 | bigint | 第3月活跃商户数 |
| act_term_num4 | bigint | 第4月活跃商户数 |
| act_term_num5 | bigint | 第5月活跃商户数 |
| act_term_num6 | bigint | 第6月活跃商户数 |
| act_term_num7 | bigint | 第7月活跃商户数 |
| act_term_num8 | bigint | 第8月活跃商户数 |
| act_term_num9 | bigint | 第9月活跃商户数 |
| act_term_num10 | bigint | 第10月活跃商户数 |
| act_term_num11 | bigint | 第11月活跃商户数 |
| act_term_num12 | bigint | 第12月活跃商户数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
