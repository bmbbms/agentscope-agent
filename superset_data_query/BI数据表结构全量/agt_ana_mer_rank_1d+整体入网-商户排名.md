# 整体入网-商户排名

**表名**: `edw.agt_ana_mer_rank_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | string | 统计日期(yyyyMMdd) |
| belong_branch | string | 业务部门 |
| product_type | string | 产品类型 |
| agt_id | string | 代理商ID |
| agt_name | string | 代理商公司名称（代理商名称） |
| glevel | string | 代理商层级 |
| inc_mer | bigint | 新增商户数 |
| stk_mer | bigint | 存量商户数 |
| inc_mer_premon | bigint | 上月同期新增商户数 |
| stk_mer_permon | bigint | 上月同期存量商户数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
