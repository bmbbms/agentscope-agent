# ods_agent.t_physn_bind (机具与用户的绑定关系表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| business_type | varchar |  | 业务类型 |
| system_customer_id | varchar |  | 客户号 |
| system_merchno | varchar |  | 商户号 |
| physn | varchar |  | 机身号 |
| bind_date | varchar |  | 绑定时间 |
| status | varchar |  | 绑定状态1=绑定，2=解绑 |
| unbind_date | varchar |  | 解绑时间，仅当status=2时有效 |
| unbind_user | varchar |  | 解绑人，仅当status=2时有效 |
| termno | varchar |  | 终端号 |
| physn_type | varchar |  | 机具类型 |
