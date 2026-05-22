# agt_org_profit_1d

**表名**: `edw.agt_org_profit_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | string | 日期 |
| belong_branch | string | 业务部门 |
| org_id | string | 机构ID |
| org_name | string | 机构名称 |
| org_comp_name | string | 机构公司名称 |
| r_agt_id | string | 一级代理商ID |
| r_agt_comp_name | string | 一级代理商公司名称 |
| r_agt_name | string | 一级代理商名称 |
| cnt | string | 交易笔数 |
| amt | string | 交易金额 |
| r_settle_price | string | 一级交易结算底价 |
| r_withdraw_settle_price | string | 一级提现费结算底价 |
| r_withdraw_profit | string | 一级提现分润 |
| org_trade_settle_price | string | 机构交易结算底价 |
| org_withdraw_settle_price | string | 机构提现费结算底价 |
| trade_profit | string | 交易分润 |
| withdraw_profit | string | 提现分润 |
| total_profit | string | 总分润 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
