# ods_pay_risk.measure_t_delay_measure (数据引入层-信用&风控域-延迟处置表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| merch_no | varchar |  | 商户号 |
| order_id | varchar |  | 交易订单号 |
| freeze_order_id | varchar |  | 冻结订单号 |
| amount | bigint |  | 金额 |
| measure_key | varchar |  | 处置措施key |
| measure_days | bigint |  | 处置/冻结时效（单位：天） |
| measure_start_time | varchar |  | 处置开始时间 |
| measure_end_time | varchar |  | 处置到期时间 |
| measure_source | varchar |  | 处置来源，逗号分隔，以,分隔 |
| measure_released | varchar |  | 是否解除处置0-否，1-是 |
| measure_user | varchar |  | 处置人 |
| measure_reason | varchar |  | 处置原因 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
| dt | integer | partition key | 分区日期 |
