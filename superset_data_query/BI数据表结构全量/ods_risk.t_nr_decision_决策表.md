# ods_risk.t_nr_decision (决策表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | id |
| body_type | varchar |  | 决策对象类型(01门店,02客户) |
| risk_desc | varchar |  | 决策结果（风险描述） |
| rule_ids | varchar |  | 规则集列表，逗号分割开 |
| body_feature_ids | varchar |  | 属性集列表，逗号分割开 |
| measure_codes | varchar |  | 决策措施列表,逗号分隔开 |
| decision_type | varchar |  | 决策类型，（0实时决策，1定时决策） |
| decision_desc | varchar |  | 决策项描述 |
| status | varchar |  | 状态(0 停用,1 启用) |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| modify_status | varchar |  | 可修改标志0否1是 |
| product | varchar |  | 产品类型（posp,mpos） |
| risk_level | varchar |  | 风险等级（提示notice，关注attention，预警alarm，警告warn） |
| push_risk_event | varchar |  | 是否推送风险事件（1是，0否） |
| risk_types | varchar |  | 决策风险类型（多个用逗号拼接） |
| monitor_dimension | varchar |  | 监测维度（入网时间、交易时间、金额、卡、地区） |
| formal_flag | varchar |  |  |
| rule_version | varchar |  |  |
| event_type | varchar |  | 事件类型 |
| rule_type | varchar |  | 规则类型（ 0基础规则 1标准规则） |
| free_measure_flag | varchar |  | 短期免处置标志 1 免处置 |
| rule_purpose | varchar |  | 规则用途，数据字典RulePurpose；riskMonitor 风险监测，riskTag 风险标记 |
| rule_monitor_object | varchar |  | 规则监测对象 |
| rule_trans_type | varchar |  | 规则交易类型 |
| rule_monitor_type | varchar |  | 规则监测类型，0基础监测 1 强化监测 |
