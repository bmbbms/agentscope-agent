# 分析图表-经营排行榜

**表名**: `edw.manage_trade_rank_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | string | 统计日期(yyyyMMdd) |
| belong_branch | string | 业务部门 |
| branch_company | string | 分公司ID |
| agt_id | string | 代理商ID |
| agt_name | string | 代理商公司名称（代理商名称） |
| s_agt_id | string | 二级代理商id |
| s_agt_name | string | 二级代理商id |
| glevel | string | 代理商层级 |
| amt | bigint | 交易额 |
| cnt | bigint | 交易笔数 |
| inc_mer | bigint | 新增商户数 |
| inc_term | bigint | 新增终端数 |
| income | bigint | 总收益 |
| branch_company_name | string | 分公司名称 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
