# ods_flowable.t_task_detail (任务详情表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| task_id | varchar |  | 任务编号 |
| proc_id | varchar |  | 流程编号 |
| task_type | varchar |  | 任务类型 0 审核类 1 业务类 |
| task_flag | varchar |  | 任务标志，0 初始化 1 业务完成 2 审核失败 3 审核成功 4 终止任务 5 终止流程 |
| reason | varchar |  | 任务审核原因，审核通过可为空 |
| source | varchar |  | 来源 |
| handle_man_id | varchar |  | 处理人编号 |
| handle_man | varchar |  | 处理人 |
| role_id | varchar |  | 处理人角色 |
| org_id | varchar |  | 所属公司ID |
| org_path | varchar |  | 所属公司ID链 |
| create_time | varchar |  | 任务创建时间 |
| remark | varchar |  | 备注 |
