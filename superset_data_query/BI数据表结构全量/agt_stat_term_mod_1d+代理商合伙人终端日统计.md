# 代理商合伙人终端日统计

**表名**: `edw.agt_stat_term_mod_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| belong_branch | string | 业务部门 |
| r_agt_id | string | 一级代理商 |
| r_agt_name | string | 一级代理商名 |
| r_agt_comp_name | string | 一级代理商公司名称 |
| r_agt_acc | string | 一级代理商账号 |
| s_agt_id | string | 二级代理商 |
| s_agt_name | string | 二级代理商名 |
| s_agt_comp_name | string | 二级代理商公司名称 |
| s_agt_acc | string | 二级代理商账号 |
| agt_id | string | 直属代理商 |
| agt_name | string | 直属代理商名 |
| agt_comp_name | string | 直属代理商公司名称 |
| agt_acc | string | 直属代理商账号 |
| agt_path | string | 代理商路径 |
| data_from | string | 产品类型 |
| model | string | 终端类型 |
| inc_term_num | bigint | 新增终端数 |
| stop_term_num | bigint | 停用终端数 |
| cancel_term_num | bigint | 撤机终端数 |
| act_term_num | bigint | 激活终端数 |
| ext_term_num | bigint | 出机台数 |
| branch_company | string | 分公司编号 |
| inc_stock_num | bigint | 新增库存数 |
| total_stock_num | bigint | 总库存数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
