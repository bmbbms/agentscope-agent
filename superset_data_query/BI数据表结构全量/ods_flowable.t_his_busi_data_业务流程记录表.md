# ods_flowable.t_his_busi_data (业务流程记录表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| proc_id | varchar |  | 流程编号 |
| task_id | varchar |  | 任务编号 |
| model_id | varchar |  | 模型编号 01:表格型,02:对比型,03:图文型,04:详情型 |
| model_name | varchar |  | 模型名称 |
| group_id | varchar |  | 分组 |
| priority | varchar |  | 优先级，数值越小，优先级越高 |
| data_type | varchar |  | 数据类型 1.数据 2 列表 3 图片 4.附件  |
| data_key | varchar |  | 数据名称 |
| data_key_ref | varchar |  | 数据名称翻译值 |
| data_val | varchar |  | 数据值 |
| data_val_ref | varchar |  | 数据值翻译值 |
| old_data_val | varchar |  | 数据原值 |
| old_data_val_ref | varchar |  | 数据原值翻译值 |
| model_type | varchar |  | 模型类型 1.审核模版 2.业务模版 |
| model_key | varchar |  | 模版KEY |
| data_belong | varchar |  | 数据所属节点 |
| task_key | varchar |  | 任务名称 |
| dt | integer | partition key |  |
