# settle.t_clear_record (清分明细表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| voucher_id | varchar |  | 凭证号 |
| clear_summary_id | varchar |  | 清分汇总id |
| clear_date | varchar |  | 清算时间 |
| settle_date | varchar |  | 结算时间 |
| clear_batch_no | varchar |  | 清分批次号 |
| order_id | varchar |  | 订单号 |
| clear_type | varchar |  | 清分类型：0-交易款,1-转账转入,2-转账转出,3-差错,4-提现,5-冻结,6-解冻,7-费用,8-其他 |
| settle_type | varchar |  | 清算方式：0-余额提现, 1-自动t1清算, 2-d0秒到, 3-仅t1清算, 4-指定账户代付, 5-直连, 6-自动d1, 7-仅d1清算 |
| settle_mode | varchar |  | 结算类型:0-直连,1-间连 |
| business_date | varchar |  | 营业日期 |
| merch_no | varchar |  | 商户号 |
| settle_merch_no | varchar |  | 结算商户号 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| trans_amt | varchar |  | 交易金额,单位为分 |
| trans_fee | varchar |  | 交易手续费,单位为分 |
| add_fee | varchar |  | 附加手续费,单位为分 |
| clear_amt | varchar |  | 清算金额,单位为分 |
| clear_time | varchar |  | 清分时间 |
| trans_time | varchar |  | 交易时间 |
| fee_calc_type | varchar |  | 计费类型: 02-内卡贷记卡-03-银联二维码-04-云闪付贷记卡 |
| term_no | varchar |  | 终端号 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| hours | varchar |  | 小时 |
| dt | integer | partition key |  |
