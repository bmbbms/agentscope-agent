# 代理商合伙人商户日统计

**表名**: `edw.agt_stat_mer_1d`

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
| inc_mer | bigint | 新增商户数 |
| inc_license | bigint | 新增营业商户数 |
| inc_rent_mer | bigint | 新增租赁商户数 |
| inc_micro_mer | bigint | 新增小微商户数 |
| pub_mer | bigint | 新增对公收款商户数 |
| auth_mer | bigint | 新增授权收款商户数 |
| cancel_mer | bigint | 注销商户数 |
| app_real_usr | bigint | 实名用户数 |
| app_bind_usr | bigint | 绑机用户数 |
| give_rent_user | bigint | 已交押金数 |
| standard_user | bigint | 刷卡达标数 |
| over_rent_user | bigint | 押金过期数 |
| apply_refund_rent_user | bigint | 已退押金数 |
| branch_company | string | 分公司编号 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
