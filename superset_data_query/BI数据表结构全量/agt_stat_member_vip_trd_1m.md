# agt_stat_member_vip_trd_1m

**表名**: `edw.agt_stat_member_vip_trd_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | string | 统计日期-yyyymm(会计月份) |
| belong_branch | string | 业务部门 |
| agt_id | string | 代理商ID |
| agt_name | string | 代理商名称 |
| agt_company_name | string | 代理商公司名称 |
| r_agt_id | string | 一级代理商ID |
| r_agt_name | string | 一级代理商名称 |
| r_agt_company_name | string | 一级代理商公司名称 |
| s_agt_id | string | 二级代理商ID |
| s_agt_name | string | 二级代理商名称 |
| s_agt_company_name | string | 二级代理商公司名称 |
| agt_path | string | 代理商层级路径 |
| busi_type | string | 业务大类 |
| trd_cnt | string | 交易笔数 |
| trd_amt | string | 交易金额 |
| ic_dfee_cnt | string | IC卡双免笔数 |
| ic_dfee_amt | string | IC卡双免金额 |
| quick_dfree_cnt | string | 云闪付双免笔数 |
| quick_dfree_amt | string | 云闪付双免金额 |
| unqrcode_cnt | string | 银联二维码笔数 |
| unqrcode_amt | string | 银联二维码金额 |
| stk_cnt | string | 存量会员交易笔数 |
| stk_amt | string | 存量会员交易金额 |
| stk_ic_dfee_cnt | string | 存量会员IC卡双免笔数 |
| stk_ic_dfee_amt | string | 存量会员IC卡双免金额 |
| stk_quick_dfree_cnt | string | 存量会员云闪付双免笔数 |
| stk_quick_dfree_amt | string | 存量会员云闪付双免金额 |
| stk_unqrcode_cnt | string | 存量会员银联二维码笔数 |
| stk_unqrcode_amt | string | 存量会员银联二维码金额 |
| inc_cnt | string | 增量会员交易笔数 |
| inc_amt | string | 增量会员交易金额 |
| inc_ic_dfee_cnt | string | 增量会员IC卡双免笔数 |
| inc_ic_dfee_amt | string | 增量会员IC卡双免金额 |
| inc_quick_dfree_cnt | string | 增量会员云闪付双免笔数 |
| inc_quick_dfree_amt | string | 增量会员云闪付双免金额 |
| inc_unqrcode_cnt | string | 增量会员银联二维码笔数 |
| inc_unqrcode_amt | string | 增量会员银联二维码金额 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
