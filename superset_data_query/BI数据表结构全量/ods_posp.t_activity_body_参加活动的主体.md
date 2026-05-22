# ods_posp.t_activity_body (参加活动的主体)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 关联ID |
| activity_id | varchar |  | 活动ID |
| body_type | varchar |  | 主体类型1商户 2公司 3代理商 |
| body_value | varchar |  | 主体值 |
| status | varchar |  | 状态 1未开始 2已开始 3已结束 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| body_name | varchar |  | 主体名称 |
| begin_time | varchar |  | 开始时间(默认活动开始时间) |
| end_time | varchar |  | 结束时间(默认活动结束时间) |
| account_period | varchar |  | 账单周期 1日 2周 3月 |
| custom_id | varchar |  | 客户号 |
| custom_name | varchar |  | 客户名称 |
| use_status | varchar |  | 商户参与状态1参与，2移除 |
| bind_activity_time | varchar |  | 是否绑定活动时间1是，0否 |
| limit_term | varchar |  | 是否限制终端，1是 0否 |
| priority | varchar |  | 优先级 值越大优先级高 |
