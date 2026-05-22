# ods_pay_cust.report_t_visa_term (数据引入层-客户域-VISA右端终端)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号-右端商户号 |
| term_no | varchar |  | 终端号 |
| status | varchar |  | 状态，0-停用，1-启用，2-注销 |
| term_sn | varchar |  | 机身号 |
| term_sequence_no | varchar |  | 终端序列号 |
| term_type | varchar |  | 终端设备类型01ATM,02传统POS,03MPOS,04智能POS,05II型固定电话POS |
| term_model | varchar |  | 终端机具型号(crm_new.T_Tms_Device表里的机具型号model字段) |
| change_status_time | varchar |  | 状态变更的时间 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 新增时间 |
| create_name | varchar |  | 新增人 |
| update_name | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
| change_status_type | varchar |  | 状态变更类型 1-风险停用/注销，2-无交易停用/注销，3-正常停用/注销 4-资料整改停用/注销 |
