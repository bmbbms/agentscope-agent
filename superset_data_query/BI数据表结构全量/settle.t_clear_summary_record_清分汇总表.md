# settle.t_clear_summary_record (清分汇总表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| clear_batch_no | varchar |  | 清算批次号 |
| clear_summary_id | varchar |  | 清分汇总id |
| settle_date | varchar |  | 结算时间 |
| business_date | varchar |  | 营业日期 |
| clear_date | varchar |  | 清算时间 |
| merch_no | varchar |  | 商户号 |
| settle_type | varchar |  | 清算方式：0-余额提现, 1-自动t1清算, 2-d0秒到, 3-仅t1清算, 4-指定账户代付, 5-直连, 6-自动d1, 7-仅d1清算 |
| settle_model | varchar |  | 结算类型:0-直连,1-间连 |
| clear_type | varchar |  | 清算类型0-交易1-转账2-差错3-提现6-冻结解冻 |
| clear_amt | varchar |  | 清算金额 |
| trans_amt | varchar |  | 交易金额 |
| trans_fee | varchar |  | 交易手续费 |
| trans_cnt | varchar |  | 交易笔数 |
| settle_no | varchar |  | 结算单编号 |
| settle_task_no | varchar |  | 结算任务号 |
| clear_status | varchar |  | 清算状态0-初始化1-处理中2-成功3-失败4-作废5-结算单已生成 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 修改时间 |
| hours | varchar |  | 小时 |
| check_val | varchar |  | 校验值 |
| collect_merch_no | varchar |  | 归集商户号 |
| actual_settle_date | varchar |  | 实际结算时间 |
| dt | integer | partition key |  |
