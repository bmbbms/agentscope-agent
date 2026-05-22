# ods_posp.t_acc_freeze_list ()

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 订单ID |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| accounting_date | varchar |  | 会计日期 |
| trans_time | varchar |  | 交易时间 |
| vir_account_no | varchar |  | 虚拟账户号 |
| org_code | varchar |  | 所属机构代码 |
| merch_no | varchar |  | 商户号 |
| term_no | varchar |  | 终端号 |
| ccy_code | varchar |  | 币种 |
| amount | varchar |  | 交易金额 |
| fz_status | varchar |  | 冻结状态0-初始1-成功2-失败 |
| unfz_status | varchar |  | 解冻状态0-初始1-成功2-失败 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| fz_reason | varchar |  | 冻结原因 |
| remark | varchar |  | 备注 |
| ori_order_id | varchar |  | 关联原订单号 |
| fz_operator | varchar |  | 操作人 |
| dt | integer | partition key |  |
