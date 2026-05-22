# 商户分润收益月排名

**表名**: `edw.mer_stat_profit_rank_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| merch_no | string | 商户号 |
| merch_name | string | 商户名称 |
| mcc | string | mcc |
| product_type | string | 产品类型 |
| busi_type | string | 业务大类(1001/2001) |
| agt_id | string | 代理商ID |
| agt_name | string | 代理商名称 |
| r_agt_id | string | 一级代理商ID |
| r_agt_name | string | 一级代理商名称 |
| s_agt_id | string | 二级代理商ID |
| s_agt_name | string | 二级代理商名称 |
| belong_branch | string | 业务部门ID  |
| branch_company | string | 分公司ID |
| agt_path | string | 代理商层级路径 |
| profit | bigint | 分润 |
| income | bigint | 收益 |
| pri_profit | bigint | 上期分润 |
| pri_income | bigint | 上期收益 |
| end_date | string | 统计截止日期 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
