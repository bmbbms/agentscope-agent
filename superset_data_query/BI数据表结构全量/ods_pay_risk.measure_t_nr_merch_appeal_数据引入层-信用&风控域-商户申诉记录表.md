# ods_pay_risk.measure_t_nr_merch_appeal (数据引入层-信用&风控域-商户申诉记录表)

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
| create_user | varchar |  | 申诉人 |
| update_user | varchar |  | 修改人 |
| create_time | varchar |  | 申诉时间 |
| update_time | varchar |  | 修改时间 |
| proc_id | varchar |  | 流程编号 |
| intensive_measure | varchar |  | 加强管控处置措施 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
