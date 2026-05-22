# ods_pay_cust.report_t_mastercard_term (万事达网联终端表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| term_no | varchar |  | 终端号 |
| channel_merch_no | varchar |  | 渠道商户号，即右端商户号 |
| term_seq_no | varchar |  | 终端序列号（tusn）全支付行业唯一，厂商报备到银联的 |
| sn | varchar |  | sn号，嘉联自定义的设备序列号 |
| status | varchar |  | 终端状态:0-注销1-启用2-冻结 |
| term_type | varchar |  | 终端类型01：ATM；02：传统POS；03：MPOS；04：智能POS；05：II型固话POS；06：扫码设备（主要是指支持扫码+非接功能的终端设备，支持扫码的各类POS终端仍按照02，03,04三类上送）；07：显码设备08：手机POS09：人脸识别终端 |
| term_model | varchar |  | 终端型号 |
| last_report_time | varchar |  | 最近一次更新时间，即流水表最近一次的创建时间，用来判断报备回调是否要覆盖该记录 |
| merch_no | varchar |  | 左端商户号 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| remark | varchar |  | 备注 |
| create_user | varchar |  | 创建人 |
| update_user | varchar |  | 更新人 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 是否删除(false:否 是:true) |
| meta_output_time | varchar |  | 写入时间 |
| meta_ori_table | varchar |  | 原始表名 |
