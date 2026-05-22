# 合伙人激活终端流失日统计

**表名**: `edw.agt_inc_term_leave_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | bigint | 统计日期 |
| belong_branch | string | 业务部门 |
| branch_company | string | 分公司ID |
| r_agt_id | string | 一级代理商ID |
| r_agt_name | string | 一级代理商名 |
| product_type | string | 产品类型 |
| term_type | string | 终端类型 |
| term_num | bigint | 激活终端数 |
| lv_term_num1 | bigint | 第1天流失数 |
| lv_term_num2 | bigint | 第2天流失数 |
| lv_term_num3 | bigint | 第3天流失数 |
| lv_term_num4 | bigint | 第4天流失数 |
| lv_term_num5 | bigint | 第5天流失数 |
| lv_term_num6 | bigint | 第6天流失数 |
| lv_term_num7 | bigint | 第7天流失数 |
| lv_term_num8 | bigint | 第8天流失数 |
| lv_term_num9 | bigint | 第9天流失数 |
| lv_term_num10 | bigint | 第10天流失数 |
| lv_term_num11 | bigint | 第11天流失数 |
| lv_term_num12 | bigint | 第12天流失数 |
| lv_term_num13 | bigint | 第13天流失数 |
| lv_term_num14 | bigint | 第14天流失数 |
| lv_term_num15 | bigint | 第15天流失数 |
| lv_term_num16 | bigint | 第16天流失数 |
| lv_term_num17 | bigint | 第17天流失数 |
| lv_term_num18 | bigint | 第18天流失数 |
| lv_term_num19 | bigint | 第19天流失数 |
| lv_term_num20 | bigint | 第20天流失数 |
| lv_term_num21 | bigint | 第21天流失数 |
| lv_term_num22 | bigint | 第22天流失数 |
| lv_term_num23 | bigint | 第23天流失数 |
| lv_term_num24 | bigint | 第24天流失数 |
| lv_term_num25 | bigint | 第25天流失数 |
| lv_term_num26 | bigint | 第26天流失数 |
| lv_term_num27 | bigint | 第27天流失数 |
| lv_term_num28 | bigint | 第28天流失数 |
| lv_term_num29 | bigint | 第29天流失数 |
| lv_term_num30 | bigint | 第30天流失数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
