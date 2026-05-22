# ods_pay_risk.riskctrl_t_nr_measure_record (商户处理记录表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| merch_name | varchar |  | 商户名称 |
| merch_no | varchar |  | 商户号 |
| measure | varchar |  | 处理措施 |
| source | varchar |  | 处理来源 |
| source_id | varchar |  | 来源ID |
| result_id | varchar |  | 结果ID |
| notice | varchar |  | 是否通知：1是0否 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| cust_no | varchar |  | 客户号 |
| reason | varchar |  | 处置原因 |
| measure_detail | varchar |  | 处置详情 |
| risk_info_id | varchar |  | 风险信息ID |
| risk_types | varchar |  | 风险类型 |
| product | varchar |  | 产品类型 |
| status | varchar |  | 处理状态00初始01执行成功02执行失败 |
| measure_param_detail | varchar |  | 处置参数详情 |
| body_type | varchar |  | 处置主体类型（cust,merch） |
| dt | integer | partition key | create_time |
