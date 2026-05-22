# ods_risk.t_nr_merch_appeal (商户申诉记录表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| merch_no | varchar |  | 商户号 |
| merch_name | varchar |  | 商户名称 |
| status | varchar |  | 状态:00-待初审01-待清算初审02-待清算复审03-已完成 |
| verify_result | varchar |  | 审核结果:00审核通过01审核不通过 |
| appeal_result | varchar |  | 申诉结果:00-申诉中01-申诉通过02-维持原判 |
| appeal_reason | varchar |  | 申诉意见 |
| appeal_measure | varchar |  | 申诉处置措施 |
| relieve_measure | varchar |  | 解除措施 |
| store_flag | varchar |  | 门店情况:1正常2异常 |
| trade_flag | varchar |  | 交易情况:1正常2异常 |
| busi_content | varchar |  | 业务内容 |
| due_id | varchar |  | 关联尽调ID:未关联或关联失败为空 |
| proc_id | varchar |  | 流程编号 |
| create_user | varchar |  | 申诉人 |
| update_user | varchar |  | 修改人 |
| create_time | varchar |  | 申诉时间 |
| update_time | varchar |  | 修改时间 |
| intensive_measure | varchar |  | 加强管控处置措施 |
