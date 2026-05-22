# ods_posp.t_partner_id_info (服务商信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| agent_id | varchar |  | 合伙人ID |
| agent_name | varchar |  | 合伙人名称 |
| agent_type | varchar |  | 合伙人类型 |
| register_type | varchar |  | 入网类型(1营业执照，3个人) |
| register_src | varchar |  | 入网来源(1服务商、2合伙人、3分公司、4机构) |
| prov_code | varchar |  | 省份代码 |
| city_code | varchar |  | 城市代码 |
| area_code | varchar |  | 地区代码 |
| det_address | varchar |  | 详细联系地址 |
| addr_position | varchar |  | 地址位置信息(json串{ longitude   经度   latitude   纬度 }) |
| link_man | varchar |  | 联系人 |
| link_mobile | varchar |  | 联系手机号 |
| cert_type | varchar |  | 证件类型(01-身份证；02-护照；09-港澳居民来往内地通行证（回乡证）；10-台湾同胞来往内地通行证（台胞证）) |
| cert_no | varchar |  | 证件号码(加密存储) |
| cert_name | varchar |  | 证件人姓名 |
| cert_begin_date | varchar |  | 证件有效期开始日期 |
| cert_end_date | varchar |  | 证件有效期截止日期 |
| cert_face_pic | varchar |  | 证件正面照 |
| cert_back_pic | varchar |  | 证件背面照 |
| license_no | varchar |  | 营业执照注册号 |
| license_name | varchar |  | 营业执照商户名称 |
| license_type | varchar |  | 营业执照类型(个体工商户、企业) |
| license_begin_date | varchar |  | 营业执照有效期开始日期 |
| license_end_date | varchar |  | 营业执照有效期截止日期 |
| license_pic | varchar |  | 营业执照照片 |
| status | varchar |  | 状态(1正常2停用3注销) |
| audit_status | varchar |  | 审核状态(0待审核，1审核通过，2审核拒绝，3修改待审核，4修改审核拒绝) |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 记录创建时间 |
| update_time | varchar |  | 记录更新时间 |
| cert_orc_info | varchar |  | 证件ocr信息 |
| license_mobile | varchar |  |  |
| license_address | varchar |  |  |
| user_tax_type | varchar |  | 纳税人类型 |
| tax_point | varchar |  | 税点 |
