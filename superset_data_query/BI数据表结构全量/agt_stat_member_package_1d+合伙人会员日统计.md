# 合伙人会员日统计

**表名**: `edw.agt_stat_member_package_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | string | 统计日期-yyyymmdd |
| belong_branch | string | 业务部门 |
| r_agt_id | string | 一级代理商ID |
| r_agt_company_name | string | 一级代理商名(公司名,名字) |
| product_type | string | 产品类型(POS+/MPOS/立刷商户版) |
| package_id | string | 套餐ID |
| package_name | string | 套餐名称 |
| op_mon | string | 开通时长(月) |
| inc_order | string | 会员订单数 |
| inc_cont_order | string | 续费订单数 |
| inc_vip | string | 新增会员数 |
| inc_cont_vip | string | 续费会员数 |
| inc_first_cont_vip | string | 首次续费会员数 |
| inc_card_mask | string | 刷卡达标数 |
| inc_deposit_expire | string | 押金过期数 |
| inc_deposit_refund | string | 已退押金数 |
| expire_vip | string | 到期会员数 |
| expire_cont_vip | string | 到期续费会员数 |
| act_vip | string | 活动商户数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
