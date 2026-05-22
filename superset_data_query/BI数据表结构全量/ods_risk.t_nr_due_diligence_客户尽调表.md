# ods_risk.t_nr_due_diligence (客户尽调表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键ID |
| cust_no | varchar |  | 客户号 |
| cust_name | varchar |  | 客户名称 |
| source | varchar |  | 尽职调查来源(1:内部风险监测,2:客户风险评级,3:黑名单核查,4:渠道预警可疑,5:商户大额交易) |
| source_detail | varchar |  | 来源source为4渠道风险事件时，输入渠道来源详情 |
| risk_trans_amount | bigint |  | 可疑交易金额 |
| risk_trans_times | bigint |  | 可疑交易次数 |
| initiate_user | varchar |  | 发起人 |
| survey_matters | varchar |  | 调查事项（发起人填写） |
| investigator | varchar |  | 调查人 |
| investigate_time | varchar |  | 调查时间 |
| survey_way | varchar |  | 调查方式(1:实地调查,2:电话调查,3:信函调查,4:其他方式) |
| deal_result | varchar |  | 处理结果 1正常 2异常 |
| description | varchar |  | 具体处理措施描述 |
| survey_conclusion | varchar |  | 调查反馈 |
| verify_reason | varchar |  | 审核意见 |
| remarks | varchar |  | 备注 |
| survey_status | varchar |  | 调查状态 0待调查 1已调查 |
| is_scene_verify | varchar |  | 是否现场核实 0-否 1-是 |
| verify_time | varchar |  | 审核时间 |
| update_time | varchar |  | 更新时间 |
| create_time | varchar |  | 发起时间 |
| risk_features | varchar |  |  |
| out_id | varchar |  |  |
| over_time | varchar |  | 超时时间 |
| event_source | varchar |  | 调查来源 |
| risk_type | varchar |  | 风险类型 |
| survey_type | varchar |  | 调查类型 |
| over_days | bigint |  | 尽调时限 |
| survey_statement | varchar |  | 尽调说明 |
| reason | varchar |  | 调查原因 |
