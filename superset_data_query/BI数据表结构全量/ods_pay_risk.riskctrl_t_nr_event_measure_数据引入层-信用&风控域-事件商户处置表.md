# ods_pay_risk.riskctrl_t_agent_busi_auth (数据引入层-信用&风控域-代理商权限配置表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | ID |
| body_type | varchar |  | 主体类型(00分公司，01代理商) |
| body_value | varchar |  | 主体值 |
| op_source | varchar |  |  |
| business_type | varchar |  | 业务类型 |
| on_status | varchar |  | 权限状态 |
| on_relate | varchar |  | 是否级联：1-是，0-否 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| modify_status | varchar |  | 可修改状态 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
