# 0交易终端月统计表

**表名**: `edw.ztrd_mer_term_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | string | 统计月份 |
| period | string | 频率/周期 1/3/6/12月  1：近一个月0交易，即为dt月份 |
| span_month | string | 月份跨度period 不为1时显示 yyyymm~yyyymm |
| product_type | string | 产品类型 - 5-大POS/2-MPOS |
| branch_company | string | 分公司ID |
| belong_branch | string | 业务部门ID |
| agt_id | string | 代理商ID |
| agt_account | string | 代理商帐号 |
| agt_name | string | 代理商名称 |
| agt_company | string | 代理商公司 |
| r_agt_id | string | 一级代理商ID |
| r_agt_account | string | 一级代理商帐号 |
| r_agt_name | string | 一级代理商名称 |
| r_agt_company | string | 一级代理商公司 |
| s_agt_id | string | 二级代理商ID |
| s_agt_account | string | 二级代理商帐号 |
| s_agt_name | string | 二级代理商名称 |
| s_agt_company | string | 二级代理商公司 |
| agt_path | string | 代理商层级 |
| merch_no | string | 商户号 |
| merch_name | string | 商户名 |
| contact_man | string | 商户联系人 |
| contact_mobile | string | 联系电话 |
| install_addr | string | 商户地址/装机地址 |
| mer_status | string | 商户状态1:正常，2:停用，3:注销 |
| term_no | string | 终端号 |
| net_time | string | 终端入网时间 |
| dev_sn | string | 机身号 |
| term_status | string | 终端状态0待启用1启用2停用3注销 |
| create_time | string | 生成时间 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
