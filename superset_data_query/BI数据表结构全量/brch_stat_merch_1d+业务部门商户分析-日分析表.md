# 业务部门商户分析-日分析表

**表名**: `edw.brch_stat_merch_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | bigint | 统计日期yyyyMMdd |
| belong_branch | string | 业务部门 |
| stock_flag | string | 存量标识：1-存量2-新增 |
| mer_num | bigint | 总商户数 |
| posp_mer_num | bigint | posp商户数 |
| posp_lic_num | bigint | posp营业商户数 |
| posp_oth_num | bigint | 其他商户，目前主要是posp租赁商户数 |
| posp_micro_num | bigint | posp小微商户数 |
| posp_cancel_num | bigint | posp注销商户数 |
| posp_pub_num | bigint | posp对公收款商户数 |
| posp_auth_num | bigint | posp授权收款商户数 |
| ls_reg_num | bigint | ls注册用户数 |
| ls_real_num | bigint | ls实名用户数 |
| ls_bind_num | bigint | ls绑机用户数 |
| ls_act_num | bigint | ls激活用户数 |
| lsp_reg_num | bigint | lsp注册用户数 |
| lsp_real_num | bigint | lsp实名用户数 |
| lsp_bind_num | bigint | lsp绑机用户数 |
| lsp_give_rent_num | bigint | lsp已交押金数 |
| lsp_standard_num | bigint | lsp刷卡达标数 |
| lsp_over_rent_user | bigint | lsp押金过期数 |
| lsp_refund_rent_num | bigint | lsp已退押金数 |
| branch_company | string | 分公司编号 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
