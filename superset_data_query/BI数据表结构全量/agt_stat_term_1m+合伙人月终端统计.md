# 合伙人月终端统计

**表名**: `edw.agt_stat_term_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | string | 统计月份 |
| belong_branch | string | 业务部门 |
| agt_id | string | 代理商ID |
| agt_name | string | 代理商名称 |
| agt_company_name | string | 代理商公司名 |
| r_agt_id | string | 一级代理商ID |
| r_agt_name | string | 一级代理商名称 |
| r_agt_company_name | string | 一级代理商公司名 |
| s_agt_id | string | 二级代理商ID |
| s_agt_name | string | 二级代理商名 |
| s_agt_company_name | string | 二级代理商公司名 |
| agt_path | string | 代理商层级路径 |
| product_type | string | 产品类型(POS+/MPOS/立刷商户版) |
| model | string | 终端类型(机型) |
| ext_term | string | 出机台数 |
| inc_term | string | 新增终端数 |
| stk_term | string | 存量终端数 |
| stk_using_term | string | 累计启用终端数 |
| inc_rent_term | string | 新增租机终端数 |
| stk_rent_term | string | 存量租机终端数 |
| stop_term | string | 停用终端数 |
| cancel_term | string | 撤机终端数 |
| stk_cancel_term | string | 累计撤机终端数 |
| inc_act_term | string | 激活终端数 |
| stk_act_term | string | 累计激活终端数 |
| inc_stock_num | bigint | 新增库存数 |
| total_stock_num | bigint | 总库存数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
