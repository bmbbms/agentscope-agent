# 合伙人统计-激活奖励月统计

**表名**: `edw.agt_stat_act_rwd_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | string | 统计月份(yyyyMM) |
| r_agt_id | string | 一级代理商ID |
| r_agt_name | string | 一级代理商名称 |
| physn_type | string | 机型 |
| act_type | string | 激活分类 |
| act_num | string | 激活台数 |
| amount | string | 金额 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
