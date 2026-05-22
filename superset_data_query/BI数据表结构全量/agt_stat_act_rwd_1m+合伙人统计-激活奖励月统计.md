# 合伙人活跃度月统计

**表名**: `edw.agt_stat_activity_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | string | 月份 |
| belong_branch | string | 业务部门 |
| product_type | string | 产品类型 |
| net_type | string | 入网证件类型 |
| r_agt_id | string | 一级代理商ID |
| r_agt_company_name | string | 一级代理商(公司名称、名称） |
| act_mer_cnt | string | 活跃商户数 |
| high_act_mer_cnt | string | 高活跃商户数 |
| act_term_cnt | string | 活跃终端数 |
| high_act_term_cnt | string | 高活跃终端数 |
| stk_act_mer_cnt | string | 存量活跃商户数 |
| inc_act_mer_cnt | string | 新增活跃商户数 |
| stk_high_act_mer_cnt | string | 存量高活跃商户数 |
| inc_high_act_mer_cnt | string | 新增高活跃商户数 |
| act_3m_mer_cnt | string | 近三月活跃商户数 |
| act_3m_term_cnt | string | 近三月活跃终端数 |
| no_trd_3m_mer_cnt | string | 近三月无交易商户数 |
| no_trd_6m_mer_cnt | string | 近六月无交易商户数 |
| good_mer_cnt | string | 优质商户数 |
| sleep_mer_cnt | string | 休眠商户数 |
| act_6m_mer_cnt | string | 近六月活跃商户数 |
| act_6m_term_cnt | string | 近六月活跃终端数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
