# ods_pay_risk.riskctrl_t_nr_event_merch (数据引入层-信用&风控域-事件子商户表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  |  |
| event_id | varchar |  | 事件ID |
| merch_no | varchar |  | 子商户号 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| merch_name | varchar |  | 子商户名称 |
| register_time | varchar |  | 入网时间 |
| org_path | varchar |  | 商户组织路径 |
| status | varchar |  | 反馈状态 |
| overtime_flag | varchar |  | 超时反馈 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| decision_measure | varchar |  | 预警已执行措施 |
| decision_measure_desc | varchar |  | 预警已执行措施描述 |
| risk_flag | varchar |  | 风险案例标识 |
| measure | varchar |  | 事件处置措施 |
| measure_desc | varchar |  | 事件处置措施描述 |
| product_type | varchar |  | 产品类型，示例：01-标准POS，02-扫码POS |
| meta_write_service | varchar |  | 写入服务 |
| meta_ori_table | varchar |  | 原表 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
