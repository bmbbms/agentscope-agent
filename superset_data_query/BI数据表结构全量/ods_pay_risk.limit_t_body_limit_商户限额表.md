# ods_pay_risk.limit_t_body_limit (商户限额表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| limit_id | varchar |  | 商户限额ID |
| merch_no | varchar |  | 商户号 |
| busi_type | varchar |  | 业务类型:交易-1001、快速提现-1002 |
| pay_type | varchar |  | 支付类型:借记卡、贷记卡、扫码、银联二维码、外币卡 |
| limit_type | varchar |  | 额度类型 |
| limit_value | bigint |  | 额度值 |
| temp_limit_value | bigint |  | 临时额度值 |
| begin_time | varchar |  | 临时额度有效开始时间 |
| end_time | varchar |  | 临时额度有效结束时间 |
| remark | varchar |  | 备注 |
| company_path | varchar |  | 分公司ID链 |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| modify_status | varchar |  | 可修改状态:0-不可修改  1-可修改 |
| is_handle | varchar |  | 是否人工干预  1-是 0-否 2-客服额度超时处理 |
| is_scene | varchar |  | 是否设置场景限额 |
| last_temp_limit_value | bigint |  | 上一次临时限额 |
| last_end_time | varchar |  | 上一次临时限额结束时间 |
| last_begin_time | varchar |  | 上一次临时限额开始时间 |
| meta_is_delete | boolean |  | 是否删除(false:否 是:true) |
| meta_write_service | varchar |  | 写入服务 |
| meta_output_time | varchar |  | 写入时间 |
