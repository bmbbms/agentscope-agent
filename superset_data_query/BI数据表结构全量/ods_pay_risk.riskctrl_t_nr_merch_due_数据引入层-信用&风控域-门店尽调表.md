# ods_pay_risk.riskctrl_t_nr_due_op (数据引入层-信用&风控域-尽调操作记录)

| Column | Type | Extra | Comment |
|---|---|---|---|
| op_id | varchar |  | 尽调操作记录ID |
| due_id | varchar |  | 尽调ID |
| op_type | varchar |  | 操作类型1-新增2-反馈3-核实 |
| op_user | varchar |  | 操作人 |
| op_time | varchar |  | 操作时间 |
| remark | varchar |  | 操作备注 |
| measure_info | varchar |  | 处置措施 |
| op_user_id | varchar |  | 操作人id |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是,      false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
