# 代理商新增终端留存日统计

**表名**: `edw.agt_inc_mer_keep_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | bigint | 统计日期 |
| product_type | string | 业务部门 |
| belong_branch | string | 一级代理商ID |
| r_agt_id | string | 一级代理商名 |
| r_agt_name | string | 一级代理商名 |
| r_agt_company | string | 产品类型 |
| inc_mer_num | bigint | 新增商户数 |
| act_mer_num0 | bigint | 第0天活跃商户数 |
| act_mer_num1 | bigint | 第1天活跃商户数 |
| act_mer_num2 | bigint | 第2天活跃商户数 |
| act_mer_num3 | bigint | 第3天活跃商户数 |
| act_mer_num4 | bigint | 第4天活跃商户数 |
| act_mer_num5 | bigint | 第5天活跃商户数 |
| act_mer_num6 | bigint | 第6天活跃商户数 |
| act_mer_num7 | bigint | 第7天活跃商户数 |
| act_mer_num8 | bigint | 第8天活跃商户数 |
| act_mer_num9 | bigint | 第9天活跃商户数 |
| act_mer_num10 | bigint | 第10天活跃商户数 |
| act_mer_num11 | bigint | 第11天活跃商户数 |
| act_mer_num12 | bigint | 第12天活跃商户数 |
| act_mer_num13 | bigint | 第13天活跃商户数 |
| act_mer_num14 | bigint | 第14天活跃商户数 |
| act_mer_num15 | bigint | 第15天活跃商户数 |
| act_mer_num16 | bigint | 第16天活跃商户数 |
| act_mer_num17 | bigint | 第17天活跃商户数 |
| act_mer_num18 | bigint | 第18天活跃商户数 |
| act_mer_num19 | bigint | 第19天活跃商户数 |
| act_mer_num20 | bigint | 第20天活跃商户数 |
| act_mer_num21 | bigint | 第21天活跃商户数 |
| act_mer_num22 | bigint | 第22天活跃商户数 |
| act_mer_num23 | bigint | 第23天活跃商户数 |
| act_mer_num24 | bigint | 第24天活跃商户数 |
| act_mer_num25 | bigint | 第25天活跃商户数 |
| act_mer_num26 | bigint | 第26天活跃商户数 |
| act_mer_num27 | bigint | 第27天活跃商户数 |
| act_mer_num28 | bigint | 第28天活跃商户数 |
| act_mer_num29 | bigint | 第29天活跃商户数 |
| act_mer_num30 | bigint | 第30天活跃商户数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
