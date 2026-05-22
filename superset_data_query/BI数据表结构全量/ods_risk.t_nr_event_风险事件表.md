# ods_risk.t_nr_event (风险事件表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 事件ID |
| merch_no | varchar |  | 商户号 |
| merch_name | varchar |  | 商户名 |
| type | varchar |  | 事件类型 |
| source | varchar |  | 事件来源 |
| status | varchar |  | 处理状态 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| attribute | varchar |  | 事件属性 |
| remark | varchar |  |  |
| source_id | varchar |  | 来源ID |
| audit_op_id | varchar |  | 初审详情操作记录ID |
| anti_status | varchar |  | 反洗钱处理状态 |
| risk_level | varchar |  | 风险等级 |
| case_type | varchar |  | 案件类型 |
| description | varchar |  | 事件描述 |
| rule_risk_level | varchar |  | 规则最高风险等级 |
| deal_result | varchar |  | 风险事件处理结果 |
| deal_day_limit | bigint |  | 处理时效（工作日） |
| deal_deadline | varchar |  | 处理截止日期 |
| deal_body | varchar |  | 处理主体 |
| severity | varchar |  | 超时处理标识 |
| overtime_flag | varchar |  |  |
| due_id | varchar |  | 尽调ID |
| due_over_time | varchar |  | 尽调超时时间 |
| source_id_from | varchar |  | 来源ID的机构、推送本事件数据的机构 |
| op_source | varchar |  | 处理方式 SYS-系统自动处理，MAN-人工处理 |
| auto_deal_reason | varchar |  | 自动处理原因 |
| auto_second_audit_flag | varchar |  |  |
