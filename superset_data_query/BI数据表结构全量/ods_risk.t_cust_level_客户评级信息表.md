# ods_risk.t_cust_level (客户评级信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| cust_no | varchar |  | 客户号 |
| cust_name | varchar |  | 客户名称 |
| cust_level | varchar |  | 评级级别 |
| cust_score | varchar |  | 评级分数 |
| level_version | varchar |  | 评级指标版本 |
| last_level_time | varchar |  | 最后评级时间 |
| last_level_op_id | varchar |  | 最后评级记录ID |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| status | varchar |  | 状态:状态，0:初始，1:正常，3:已注销 |
| audit_status | varchar |  | 审核状态:审核状态，1-待初审2待复审3已复审 |
| remark | varchar |  | 备注 |
| cust_type | varchar |  | 客户类型(P个人客户，C企业客户) |
| register_type | varchar |  | 入网类型(1:营业执照入网,2:租赁合同入网,3:小微商户入网,4:立刷电签商户,5:立刷商户) |
