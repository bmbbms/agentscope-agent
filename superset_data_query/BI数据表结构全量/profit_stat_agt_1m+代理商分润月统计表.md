# 代理商分润月统计表

**表名**: `edw.profit_stat_agt_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| rowkey | string | rowkey |
| belong_branch | string | 业务部门 |
| agt_id | string | 代理商id |
| agt_name | string | 代理商名称 |
| r_agt_id | string | 一级代理商id |
| r_agt_name | string | 一级代理商名称 |
| glevel | string | 代理商级别 |
| product_type | string | 产品类型 |
| branch_company | string | 分公司id |
| trd_profit | string | 交易分润 |
| em_profit_cnt | string | 提现分润笔数 |
| em_profit | string | 提现分润 |
| serv_profit | string | 服务费分润 |
| act_profit | string | 激活奖励 |
| lsp_vip_profit | string | 会员费分润 |
| lsp_dpst_profit | string | 押金分润 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
