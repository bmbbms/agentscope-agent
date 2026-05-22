# ods_pay_risk.riskctrl_t_nr_seizure_body (数据引入层-信用&风控域-司法查冻扣主体表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| merch_name | varchar |  | 商户名称 |
| case_status | varchar |  | 案件状态：0-待处理；1-处理中；3-已处理；5-已结案 |
| close_case_user | varchar |  | 结案人 |
| close_case_time | varchar |  | 结案时间 |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
| case_result | varchar |  | 结案结果:00-排除可疑，01-存在可疑，02-不确定 |
