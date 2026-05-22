# ods_pay_risk.riskctrl_t_nr_decision_measure (数据引入层-信用&风控域-决策措施)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | id |
| decision_id | varchar |  | 决策id |
| measure_code | varchar |  | 处理措施 |
| deal_type | varchar |  | 处理对象（门店，客户） |
| measure_desc | varchar |  | 处理措施描述 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
