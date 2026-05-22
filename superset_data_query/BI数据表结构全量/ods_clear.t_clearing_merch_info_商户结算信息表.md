# ods_clear.t_clearing_merch_info (商户结算信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| settle_type | varchar |  | 清算方式（商户虚户使用）0-余额提现1  -自动t+1清算 2-d0秒到 3-仅t+1清算 4-指定账户代付5:直连 6 -自动d+1  7 - 仅d+1清算 |
| business_date | varchar |  | 营业时间 hhmmss如：4点-4点 |
| business_start_date | varchar |  | 开始时间-生效日期 |
| business_end_date | varchar |  | 结束时间-截至日期 |
| status | varchar |  | 账户状态:：0-未激活；1-正常；2-冻结；9-已销户 |
| pay_date | varchar |  | 付款时间点4点，例如为040000 |
| holday_flag | varchar |  | 节假日清算标记:0-节假日分开打款 |
| operator | varchar |  | 操作人 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
