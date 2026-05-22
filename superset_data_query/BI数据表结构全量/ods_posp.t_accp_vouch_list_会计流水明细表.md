# ods_posp.t_acc_trans_list (记账流水)

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 订单ID |
| ori_order_id | varchar |  | 原始订单ID |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| accounting_date | varchar |  | 会计日期 |
| trans_time | varchar |  | 交易时间 |
| channel_no | varchar |  | 交易渠道  15 刷卡 25 迅联 |
| org_code | varchar |  | 所属机构代码 |
| merch_no | varchar |  | 商户号 |
| trem_no | varchar |  | 终端号 |
| batch_no | varchar |  | 批次号 |
| vouch_no | varchar |  | 流水号 |
| refer_no | varchar |  | 参考号 |
| ccy_code | varchar |  | 币种 |
| card_no | varchar |  | 交易卡号 |
| card_type | varchar |  | 卡类型0-借记卡 1-贷记卡 |
| is_internal_card | varchar |  | 内外卡标志Y内卡 N外卡 |
| amount | varchar |  | 交易金额 |
| fee | varchar |  | 手续费 |
| status | varchar |  | 记账状态0-初始1-成功2-失败 |
| update_status | varchar |  | 更新状态0-初始 3-已撤销 4-已冲正 5-已退货 |
| ret_code | varchar |  | 应答码 |
| ret_msg | varchar |  | 应答信息 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| accounting_type | varchar |  | 记账类型：0-正常记账 1-批结算补账 2-差错调整 |
| remarks | varchar |  |  |
| account_source | varchar |  | 记账来源 |
| vir_account_no | varchar |  | 商户虚户 |
| acc_describe | varchar |  | 账务描述 |
| add_fee | varchar |  | 附加手续费 |
| dt | integer | partition key |  |
