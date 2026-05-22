# ods_pay_cust.agent_user_t_pay_order_detail (数据引入层-客户域-支付订单详情表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 订单ID |
| user_id | decimal(22,0) |  | 代理商ID |
| parent_order_id | varchar |  | 父订单ID |
| request_busi | varchar |  | 请求业务00-授信还款01-营销充值02-机具升级 |
| pay_channel | varchar |  | 支付渠道1=代扣，2=立刷刷卡，3=营销户扣款 |
| amount | decimal(22,0) |  | 目标金额 |
| accounted_amt | decimal(22,0) |  | 到账金额 |
| charge | decimal(22,0) |  | 手续费 |
| merch_no | varchar |  | 入账商户号 |
| status | varchar |  | 状态00:成功;AG_ING:处理中其他失败 |
| out_order_id | varchar |  | 外部调用订单号 |
| card_no | varchar |  | 付款卡号 |
| remark | varchar |  | 订单描述 |
| resp_remark | varchar |  | 返回描述（失败原因描述） |
| ch_resp_time | varchar |  | 渠道响应时间 |
| rec_resp_time | varchar |  | 收到响应时间 |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| code_url | varchar |  | 支付链接 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
