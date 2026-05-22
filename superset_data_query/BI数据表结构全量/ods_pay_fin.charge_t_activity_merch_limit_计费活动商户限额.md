# ods_pay_fin.charge_t_activity_merch_limit (计费活动商户限额)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键ID |
| activity_id | varchar |  | 活动ID |
| merch_no | varchar |  | 商户号 |
| fee_calc_type | varchar |  | 计费类型，多个逗号分隔 |
| status | varchar |  | 状态1正常2过期 |
| limit_quota | bigint |  | 限额 |
| warn_quota | bigint |  | 预警额度 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 是否删除(false:否 是:true) |
| meta_output_time | varchar |  | 写入时间 |
| meta_ori_table | varchar |  | 原始表名 |
