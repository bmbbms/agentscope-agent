# ods_pay_risk.riskctrl_t_nr_event_measure (数据引入层-信用&风控域-事件商户处置表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| feedback_id | varchar |  | 反馈ID |
| audit_id | varchar |  | 初复审ID |
| event_id | varchar |  | 事件ID |
| merch_no | varchar |  | 商户号 |
| measure_category_desc | varchar |  | 处置措施类别 |
| measure_key | varchar |  | 处置措施KEY |
| measure_desc | varchar |  | 措施描述 |
| measure_param | varchar |  | 处置参数JSON |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
