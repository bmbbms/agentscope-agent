# ods_pay_risk.risk_merch_t_cust_level_log (数据引入层-信用&风控域-客户评级日志表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| log_id | varchar |  | 日志ID |
| cust_no | varchar |  | 客户号 |
| log_name | varchar |  | 操作名称 |
| busi_type | varchar |  | 业务类型 |
| busi_key_id | varchar |  | 业务ID |
| remark | varchar |  | 描述 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
