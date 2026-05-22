# ods_pay_risk.limit_t_limit_op (数据引入层-信用&风控域-商户限额操作记录表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| op_id | varchar |  | 操作记录ID |
| out_id | varchar |  | 外部ID |
| op_type | varchar |  | 操作类型,add-新增modify-修改 |
| merch_no | varchar |  | 商户号 |
| pay_type | varchar |  | 支付类型 |
| limit_type | varchar |  | 额度类型 |
| limit_value | decimal(22,0) |  | 额度值 |
| begin_time | varchar |  | 额度有效开始时间 |
| end_time | varchar |  | 额度有效结束时间 |
| create_time | varchar |  | 操作时间 |
| create_user | varchar |  | 操作人 |
| remark | varchar |  | 操作备注 |
| limit_flag | varchar |  | 调额标志1-超限调额2-超限调额通过3-超限调额不通过 |
| status | varchar |  | 状态 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
