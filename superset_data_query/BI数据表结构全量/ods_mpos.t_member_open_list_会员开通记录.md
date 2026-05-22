# ods_mpos.t_member_open_list (会员开通记录)

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 购买订单ID |
| merch_no | varchar |  | 商户号 |
| produce | varchar |  | 产品类型 |
| package_id | varchar |  | 套餐ID |
| start_time | varchar |  | 开通时间 |
| end_time | varchar |  | 到期时间 |
| op_mon | varchar |  | 开通时长(月) |
| amount | varchar |  | 开通费用 |
| source | varchar |  | 开通费用来源 |
| acc_flag | varchar |  | 是否记账,0:未记账, 1:已记账 |
| is_exprie | varchar |  | 是否到期 |
| status | varchar |  | 状态(0初始化,1.待付款,2付款中,3.付款成功,4.付款失败,5未知) |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| pos_merch_no | varchar |  | POS+商户号 |
| pay_order_id | varchar |  | 支付订单号 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| merch_name | varchar |  | 商户名 |
| possn | varchar |  | 机身号 |
| first_pay | varchar |  | 1.首冲 0.续费 |
| card_no | varchar |  | 卡号 |
| sign_pic | varchar |  | 签名地址 |
| term_type | varchar |  | 终端类型 |
| agent_id | varchar |  | 代理商号 |
| need_acc | varchar |  | 是否需要记账(转账)：0-否,1-是 |
| package_name | varchar |  | 套餐名称 |
| vip_period_deducted | varchar |  | 会员有效期是否扣除: 0/空-未扣除,1-已扣除 |
| acc_date | varchar |  | 记账时间 yyyy-mm-dd hh24:mi:ss |
