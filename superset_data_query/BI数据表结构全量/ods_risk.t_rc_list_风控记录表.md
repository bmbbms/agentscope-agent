# ods_risk.t_rc_list (风控记录表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| trans_time | varchar |  | 交易时间 yyyy-MM-dd HH:mm:ss |
| order_id | varchar |  | 订单号 |
| term_no | varchar |  | 终端号 |
| card_no | varchar |  | 卡号 |
| merch_name | varchar |  | 商户名称 |
| term_sn | varchar |  | 设备序列号/机身号 |
| card_type | varchar |  | 0-借记卡,1-贷记卡 |
| card_flag | varchar |  | 0-磁条卡,1-芯片卡 |
| card_mode | varchar |  | 0-接触，1-非接，2-云闪付 |
| bank_code | varchar |  | 发卡行编号 |
| bank_name | varchar |  | 发卡行名称 |
| amount | bigint |  | 金额 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| ret_code | varchar |  | 风控原因码 |
| sys_rule_code | varchar |  | 系统规则编码 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 记录创建时间 yyyy-MM-dd HH:mm:ss |
| id | varchar |  | 唯一标识 |
| acc_type | varchar |  | 出入账类型 |
| project | varchar |  | 归属项目 trade,commonWithdraw,fastWithdraw,morrowPayment,payment,partnerRegister,merchRegister,mposRegister |
| rule_params | varchar |  | 触发风控规则的参数 |
| area_code | varchar |  | 拦截地区地区码 |
| cust_no | varchar |  | 客户号 |
| position_detail | varchar |  | 详细位置 |
| dt | integer | partition key | 创建日期 |
