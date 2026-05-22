# 合伙人统计-财务月统计

**表名**: `edw.agt_stat_finance_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | string | 统计月份 |
| agt_id | string | 代理商ID |
| agt_name | string | 代理商名称 |
| glevel | string | 代理商级别 |
| account_type | string | 账户类型(1001-普通账户 2001-营销账户 3001-合作账户) |
| all_profit | string | 历史总分润 |
| all_withdraw | string | 历史总提现 |
| all_reduce | string | 历史调减 |
| all_add | string | 历史调增 |
| all_actprofit | string | 历史激活奖励 |
| all_reduce_amount | string | 历史扣款 |
| all_pay_amount | string | 历史付款 |
| all_no_pay | string | 历史提现未付 |
| this_profit | string | 本月分润 |
| this_withdraw | string | 本月提现 |
| this_reduce | string | 本月调减 |
| this_add | string | 本月调增 |
| this_actprofit | string | 本月激活奖励 |
| this_reduce_amount | string | 本月扣款 |
| this_pay_amount | string | 本月付款 |
| this_no_pay | string | 本月提现未付 |
| bal | string | 余额 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
