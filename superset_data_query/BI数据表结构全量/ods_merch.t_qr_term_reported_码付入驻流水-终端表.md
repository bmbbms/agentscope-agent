# ods_merch.t_qr_term_reported (码付入驻流水-终端表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| institution_id | varchar |  | 收单机构好 |
| channel_id | varchar |  | 渠道id |
| merch_no | varchar |  | 商户号 |
| channel_merch_no | varchar |  | 渠道商户号 |
| merch_name | varchar |  | 商户名称 |
| appid | varchar |  | 微信分配的公众账号ID |
| sub_appid | varchar |  | 微信分配的子商户公众账号ID |
| device_sn | varchar |  | 机身号 |
| device_type | varchar |  | "自动柜员机（含AT|M和CDM）和多媒|体自助终端|02传统POS|03|mPOS|04智能POS|05II型固定电话|06云闪付终端|07保留使用|08手机POS|09刷脸付终端|10条码支付受理终端|11辅助受理终端" |
| device_seq_id | varchar |  | "出现要求：|终端类型（device_type）填写|为02、03、04、05、06、08、09或10时，必须填写商户端设备序列号。" |
| device_address | varchar |  | 商户端设备布放地 |
| status | varchar |  | 状态，0-停用，1-启用，2-注销 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 新增时间 |
| create_name | varchar |  | 新增人 |
| update_name | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| fail_reason | varchar |  | 失败原因 |
| term_no | varchar |  | 终端号 |
| reported_flag | varchar |  | 报备状态 |
