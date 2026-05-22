# ods_risk.t_nr_alarm_body (预警主体)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | ID |
| product | varchar |  | 产品类型,产品类型 posp,mpos |
| busi_type | varchar |  | 业务大类,posp, LS,TICKET |
| body_value | varchar |  | 预警主体 |
| body_name | varchar |  | 预警主体名称 |
| alarm_date | varchar |  | 预警日期,预警日期:yyyy-mm-dd |
| status | varchar |  | 状态（01待处理、02处理中、03已处理） |
| risk_status | varchar |  | 风险状态（00排除可疑审核中，11 排除可疑，22有风险） |
| event_status | varchar |  | 生成事件（0推送事件，1事件已完成） |
| deal_reason | varchar |  | 处理意见 |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| event_type | varchar |  | 事件类型（04 代付，其他为非代付） |
| op_source | varchar |  | 处理方式 |
| dt | integer | partition key | CREATE_TIME |
