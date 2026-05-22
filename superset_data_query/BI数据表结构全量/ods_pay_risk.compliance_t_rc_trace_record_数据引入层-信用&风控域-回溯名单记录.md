# ods_pay_risk.compliance_t_rc_trace_record (数据引入层-信用&风控域-回溯名单记录)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  |  |
| status | varchar |  | 状态，0-已回溯，1-回溯成功，2-回溯失败，3-没有命中，4-回溯处理失败 |
| origin_id | varchar |  | 源名单id |
| origin_value | varchar |  | 源名单信息 |
| origin_type | varchar |  | 源名单类型 |
| origin_flag | varchar |  | 源名单标志 |
| origin_source | varchar |  | 源名单来源 |
| target_id | varchar |  | 目标名单id，风险事件id |
| target_value | varchar |  | 目标名单信息 |
| target_type | varchar |  | 目标名单类型 |
| target_flag | varchar |  | 目标名单标志 |
| result | varchar |  | 操作结果0-新增名单，1-启用名单，2-名单存在，3推送到风险事件，4风险停用 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| fail_reasons | varchar |  | 失败原因 |
| target_cust_no | varchar |  | 名单回溯客户号 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
| dt | integer | partition key | 分区日期 |
