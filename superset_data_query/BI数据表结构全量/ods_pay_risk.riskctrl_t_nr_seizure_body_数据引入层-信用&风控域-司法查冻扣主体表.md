# ods_pay_risk.riskctrl_t_nr_event_case_feedback (数据引入层-信用&风控域-风险案例反馈记录表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  |  |
| case_id | varchar |  | 案例ID |
| event_id | varchar |  | 事件ID |
| biz_remark | varchar |  | 反馈说明 |
| verify_status | varchar |  | 审核进度 |
| verify_suggestion | varchar |  |  |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| measure_desc | varchar |  | 措施描述 |
| merch_no | varchar |  | 子商户hao |
| audit_id | varchar |  | 审核记录ID |
| verify_time | varchar |  | 审核时间 |
| feed_back_source | varchar |  | 反馈来源 |
| create_user_id | varchar |  | 反馈人id |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
