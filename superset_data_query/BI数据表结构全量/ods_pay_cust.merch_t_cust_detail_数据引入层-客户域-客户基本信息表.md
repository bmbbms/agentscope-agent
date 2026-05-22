# ods_pay_cust.merch_t_cust_detail (数据引入层-客户域-客户基本信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| cust_no | varchar |  | 客户号802开头 |
| cust_id | varchar |  | 客户ID |
| type | varchar |  | 客户类型P-个人,C-企业 |
| cust_name | varchar |  | 客户的商户名称 |
| cust_english_name | varchar |  | 客户英文名称 |
| status | varchar |  | 客户状态1-启用2-停用3-注销 |
| change_status_time | varchar |  | 客户状态变更时间 |
| register_time | varchar |  | 客户入网时间 |
| mobile | varchar |  | 客户手机号 |
| mcc | varchar |  | MCC码 |
| pwd_free | varchar |  | 免密免签:0.不免签不免密1.免签2.免签免密 |
| business_code | varchar |  | 经营地区码6位 |
| business_name | varchar |  | 经营名称 |
| business_address | varchar |  | 经营地址 |
| business_position | varchar |  | 经营地址位置信息(json串{"longitude":"经度","latitude":"纬度"}) |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| create_user | varchar |  | 创建人 |
| update_user | varchar |  | 更新人 |
| remark | varchar |  | 备注信息 |
| status_change_type | varchar |  | 状态变更类型1-风险停用/注销；2-无交易停用/注销；3-正常停用/注销4-资料整改停用/注销 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
| merch_no | varchar |  | 第一个入网的子商户 |
