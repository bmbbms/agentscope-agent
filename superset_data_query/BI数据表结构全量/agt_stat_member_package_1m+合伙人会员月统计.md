# 合伙人会员月统计

**表名**: `edw.agt_stat_member_package_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | string | 统计月份-yyyymm |
| belong_branch | string | 业务部门 |
| r_agt_id | string | 一级代理商ID |
| r_agt_company_name | string | 一级代理商名(公司名,名字) |
| product_type | string | 产品类型(POS+/MPOS/立刷商户版) |
| package_id | string | 套餐ID |
| package_name | string | 套餐名称 |
| op_mon | string | 开通时长(月) |
| inc_order | string | 会员订单数 |
| stk_order | string | 累计会员订单数 |
| inc_cont_order | string | 新增续费订单数 |
| stk_cont_order | string | 累计续费订单数 |
| inc_vip | string | 新增会员数 |
| stk_vip | string | 累计会员数 |
| stk_valid_vip | string | 累计有效会员数 |
| inc_cont_vip | string | 续费会员数 |
| inc_first_cont_vip | string | 首次续费会员数 |
| stk_cont_vip | string | 累计续费会员数 |
| stk_cont_valid_vip | string | 累计续费有效会员数 |
| inc_card_mask | string | 刷卡达标数 |
| stk_card_mask | string | 累计刷卡达标数 |
| inc_deposit_expire | string | 押金过期数 |
| stk_deposit_expire | string | 累计押金过期数 |
| inc_deposit_refund | string | 已退押金数 |
| stk_deposit_refund | string | 累计已退押金数 |
| expire_vip | string | 到期会员数 |
| expire_cont_vip | string | 到期续费会员数 |
| act_vip | string | 活动商户数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
