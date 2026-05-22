# 开通时长(月)

**表名**: `edw.agt_act_vip_keep_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| expire_month | bigint | 到期月份/统计月份 |
| belong_branch | string | 业务部门 |
| branch_company | string | 分公司编号 |
| r_agt_id | string | 一级代理商ID |
| r_agt_name | string |  |
| r_agt_company_name | string | 一级代理商公司名 |
| product_type | string | 产品类型 |
| package_id | string | 套餐ID |
| package_name | string | 套餐名称 |
| op_mon | decimal |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
