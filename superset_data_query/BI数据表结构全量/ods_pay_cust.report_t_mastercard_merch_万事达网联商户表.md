# ods_pay_cust.report_t_mastercard_merch (万事达网联商户表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| channel_merch_no | varchar |  | 渠道商户号，即右端商户号 |
| merch_no | varchar |  | 左端商户号 |
| merch_name | varchar |  | 商户名称 |
| status | varchar |  | 商户状态:0-注销1-启用2-冻结 |
| merch_shortname | varchar |  | 商户简称 |
| english_name | varchar |  | 商户英文名称 |
| mcc | varchar |  | mcc码 |
| area_code | varchar |  | 地区代码 |
| last_report_time | varchar |  | 最近一次报备时间，即流水表最近一次的创建时间，用来判断报备回调是否要覆盖该记录 |
| merch_area_code | varchar |  | 商户平台地区码 |
| area_english_name | varchar |  | 地区英文名称 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| remark | varchar |  |  |
| create_user | varchar |  | 创建人 |
| update_user | varchar |  | 更新人 |
| status_change_reason | varchar |  | 状态变更原因 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 是否删除(false:否 是:true) |
| meta_output_time | varchar |  | 写入时间 |
| meta_ori_table | varchar |  | 原始表名 |
| english_business_address | varchar |  | 英文经营地址 |
