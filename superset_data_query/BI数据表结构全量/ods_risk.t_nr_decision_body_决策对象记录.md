# ods_risk.t_nr_decision_body (决策对象记录)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | id |
| decision_id | varchar |  | 决策id |
| body_value | varchar |  | 决策主体 |
| body_type | varchar |  | 决策主体类型(01门店，02客户) |
| body_name | varchar |  | 决策对象名称 |
| risk_desc | varchar |  | 决策结果（决策风险描述） |
| measure_codes | varchar |  | 决策处理措施(多个id) |
| decision_time | varchar |  | 决策处理时间 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| alarm_id | varchar |  | 决策预警主体id |
| dt | integer | partition key | CREATE_TIME |
