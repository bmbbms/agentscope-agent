# ods_pay_cust.report_t_visa_merch (数据引入层-客户域-VISA右端商户)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| merch_name | varchar |  | 商户名 |
| english_name | varchar |  | 商户英文名称 |
| channel_operate_name | varchar |  | 渠道经营名称 |
| status | varchar |  | 商户状态:0-停用1-正常3-注销4-待启用 |
| cust_no | varchar |  | 客户号 |
| left_merch_no | varchar |  | 左端商户名 |
| area_code | varchar |  | 地区码 |
| city_english_name | varchar |  | 城市英文名 |
| mcc | varchar |  | 商户MCC码 |
| product_type | varchar |  | 产品类型：1是大POS，2是小POS，3是嘉联业务 |
| change_status_type | varchar |  | 状态变更类型,1-风险停用/注销,2-无交易停用/注销,3-正常停用/注销4-资料整改停用/注销 |
| change_status_time | varchar |  | 状态变更时间 |
| reported_time | varchar |  | 报备时间 |
| remark | varchar |  | 备注 |
| create_name | varchar |  | 新增人 |
| create_time | varchar |  | 新增时间 |
| update_name | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
| signed_date | varchar |  | 商户签约时间，即商户首次交易时间 |
