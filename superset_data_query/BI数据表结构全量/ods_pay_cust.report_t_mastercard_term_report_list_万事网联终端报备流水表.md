# ods_pay_cust.report_t_mastercard_term_report_list (万事网联终端报备流水表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| report_id | bigint |  | 报备Id |
| terminal_id | varchar |  | 终端号 |
| channel_merch_no | varchar |  | 商户号 |
| merch_no | varchar |  | 左端商户号 |
| action | varchar |  | 导入标志,I:增加U:修改D:删除 |
| status | bigint |  | 报备状态,0:报备中1:报备成功2:报备失败 |
| channel_date | varchar |  | yyMMdd格式日期 |
| channel_ret_code | varchar |  | 渠道返回状态码 |
| channel_ret_msg | varchar |  | 渠道返回状态信息 |
| req_body | varchar |  | 渠道请求参数json格式 |
| terminal_serial_number | varchar |  | 终端序列号 |
| terminal_type | varchar |  | 终端类型,01:ATM02:传统POS03:MPOS04:智能POS05:II型固话POS06:扫码设备（主要是指支持扫码+非接功能的终端设备，支持扫码的各类POS终端仍按照02，03,04三类上送）07:显码设备08:手机POS09:人脸识别终端 |
| terminal_product_type | varchar |  | 终端产品型号 |
| terminal_status | varchar |  | 终端状态:0-注销1-启用2-冻结 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| remark | varchar |  | 备注 |
| sn | varchar |  | sn号 |
| create_user | varchar |  | 创建人 |
| update_user | varchar |  | 更新人 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 是否删除(false:否 是:true) |
| meta_output_time | varchar |  | 写入时间 |
| meta_ori_table | varchar |  | 原始表名 |
