# 代理商新增商户留存月统计

**表名**: `edw.agt_inc_mer_keep_1m`

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
| act_mer_num0 | bigint | 第0月活跃商户数 |
| act_mer_num1 | bigint | 第1月活跃商户数 |
| act_mer_num2 | bigint | 第2月活跃商户数 |
| act_mer_num3 | bigint | 第3月活跃商户数 |
| act_mer_num4 | bigint | 第4月活跃商户数 |
| act_mer_num5 | bigint | 第5月活跃商户数 |
| act_mer_num6 | bigint | 第6月活跃商户数 |
| act_mer_num7 | bigint | 第7月活跃商户数 |
| act_mer_num8 | bigint | 第8月活跃商户数 |
| act_mer_num9 | bigint | 第9月活跃商户数 |
| act_mer_num10 | bigint | 第10月活跃商户数 |
| act_mer_num11 | bigint | 第11月活跃商户数 |
| act_mer_num12 | bigint | 第12月活跃商户数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
