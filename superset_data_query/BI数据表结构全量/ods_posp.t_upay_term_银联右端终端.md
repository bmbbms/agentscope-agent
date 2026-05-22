# ods_posp.t_upay_term (银联右端终端)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| term_no | varchar |  | 终端号 |
| term_sn | varchar |  | 机身号 |
| stock_flag | varchar |  | 存量标识，Y-存量，N-新增 |
| term_device_type | varchar |  | 终端设备类型 01 ATM,02 传统POS,03 MPOS,04 智能POS,05 II型固定电话POS |
| status | varchar |  | 状态，0-停用，1-启用，2-注销 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 新增时间 |
| create_name | varchar |  | 新增人 |
| update_name | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| shop_id | varchar |  | 门店id |
| status_modify_time | varchar |  | 状态变更的时间 |
| device_model | varchar |  | 终端机具型号(crm_new.T_Tms_Device表里的机具型号model字段) |
| term_sequence_no | varchar |  | 终端序列号 |
| union_device_type | varchar |  | 银联终端类型 |
