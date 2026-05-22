# ods_pay_risk.riskctrl_user_t_chargeback_ledger (数据引入层-信用&风控域-null)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  |  |
| import_date | varchar |  |  |
| channel_source | varchar |  |  |
| chargeback_reason | varchar |  |  |
| order_id | varchar |  |  |
| trans_time | varchar |  |  |
| card_no | varchar |  |  |
| card_media | varchar |  |  |
| term_sn | varchar |  |  |
| auth_code | varchar |  |  |
| r_refer_no | varchar |  |  |
| trade_amount | bigint |  |  |
| dispute_type | varchar |  |  |
| dispute_amount | bigint |  |  |
| channel_merch_no | varchar |  |  |
| channel_merch_name | varchar |  |  |
| channel_eng_name | varchar |  |  |
| sub_merch_no | varchar |  |  |
| sub_merch_name | varchar |  |  |
| merch_no | varchar |  |  |
| clearing_no | varchar |  |  |
| error_amount | bigint |  |  |
| error_currency | varchar |  |  |
| chargeback_plan | varchar |  |  |
| fund_plan | varchar |  |  |
| status | varchar |  |  |
| appeal_date | varchar |  |  |
| fund_result | varchar |  |  |
| bad_debt_amount | bigint |  |  |
| upgrade_arbitration_date | varchar |  |  |
| arbitration_plan | varchar |  |  |
| arbitration_reply_date | varchar |  |  |
| deal_measure_desc | varchar |  |  |
| deal_measure_result | varchar |  |  |
| remark | varchar |  |  |
| adj_arbitration_time | varchar |  |  |
| create_user | varchar |  |  |
| create_time | varchar |  |  |
| update_user | varchar |  |  |
| update_time | varchar |  |  |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
