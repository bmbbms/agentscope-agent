# ods_merch.t_merch_attachment_warn (子商户附件预警表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| cust_no | varchar |  | 客户号 |
| merch_no | varchar |  | 子商户号 |
| merch_name | varchar |  | 商户名称 |
| agent_id | varchar |  | 服务商id |
| agent_name | varchar |  | 服务商名称 |
| department_name | varchar |  | 业务部门名称 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| warn_type | varchar |  | 预警类型0-持续预警1-入网预警 |
| dup_file | varchar |  | 重复的文件信息，{fileType:fileId} |
