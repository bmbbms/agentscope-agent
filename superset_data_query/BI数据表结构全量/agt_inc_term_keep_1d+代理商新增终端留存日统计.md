# 代理商新增终端留存日统计

**表名**: `edw.agt_inc_term_keep_1d`

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
| act_term_num0 | bigint | 第0天活跃商户数 |
| act_term_num1 | bigint | 第1天活跃商户数 |
| act_term_num2 | bigint | 第2天活跃商户数 |
| act_term_num3 | bigint | 第3天活跃商户数 |
| act_term_num4 | bigint | 第4天活跃商户数 |
| act_term_num5 | bigint | 第5天活跃商户数 |
| act_term_num6 | bigint | 第6天活跃商户数 |
| act_term_num7 | bigint | 第7天活跃商户数 |
| act_term_num8 | bigint | 第8天活跃商户数 |
| act_term_num9 | bigint | 第9天活跃商户数 |
| act_term_num10 | bigint | 第10天活跃商户数 |
| act_term_num11 | bigint | 第11天活跃商户数 |
| act_term_num12 | bigint | 第12天活跃商户数 |
| act_term_num13 | bigint | 第13天活跃商户数 |
| act_term_num14 | bigint | 第14天活跃商户数 |
| act_term_num15 | bigint | 第15天活跃商户数 |
| act_term_num16 | bigint | 第16天活跃商户数 |
| act_term_num17 | bigint | 第17天活跃商户数 |
| act_term_num18 | bigint | 第18天活跃商户数 |
| act_term_num19 | bigint | 第19天活跃商户数 |
| act_term_num20 | bigint | 第20天活跃商户数 |
| act_term_num21 | bigint | 第21天活跃商户数 |
| act_term_num22 | bigint | 第22天活跃商户数 |
| act_term_num23 | bigint | 第23天活跃商户数 |
| act_term_num24 | bigint | 第24天活跃商户数 |
| act_term_num25 | bigint | 第25天活跃商户数 |
| act_term_num26 | bigint | 第26天活跃商户数 |
| act_term_num27 | bigint | 第27天活跃商户数 |
| act_term_num28 | bigint | 第28天活跃商户数 |
| act_term_num29 | bigint | 第29天活跃商户数 |
| act_term_num30 | bigint | 第30天活跃商户数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
