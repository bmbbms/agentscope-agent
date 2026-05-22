# ods_merch.t_cust_realname (客户(自然人/法人)实名认证信息)

| Column | Type | Extra | Comment |
|---|---|---|---|
| cust_id | varchar |  | 客户号 |
| cert_type | varchar |  | 个人证件类型01-身份证；02-护照；03-港澳通行证；08-军官证；09-港澳居民来往内地通行证（回乡证）；10-台湾同胞来往内地通行证（台胞证）；11-警官证；12-士兵证；13-户口簿；14-临时身份证；15-外国人居留证；99-其他证件 |
| cert_no | varchar |  | 个人证件号码 |
| cert_name | varchar |  | 个人证件姓名 |
| sex | varchar |  | 性别M男，F女 |
| nation | varchar |  | 民族 |
| birthday | varchar |  | 生日 |
| prov_code | varchar |  | 所在省份 |
| city_code | varchar |  | 所在城市 |
| area_code | varchar |  | 所在地区 |
| det_address | varchar |  | 详细地址 |
| cert_address | varchar |  | 身份证居住地址 |
| addr_position | varchar |  | 地址位置信息(json串{ longitude   经度   latitude   纬度 }) |
| office | varchar |  | 发证机关 |
| begin_date | varchar |  | 有效期开始日期 |
| end_date | varchar |  | 有效期截止日期 |
| face_pic | varchar |  | 个人证件正面照地址 |
| back_pic | varchar |  | 个人证件背面照地址 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| face_ocr_info | varchar |  | 个人证件正面OCR |
| back_ocr_info | varchar |  | 个人证件背面OCR |
| mobile | varchar |  | 手机号 |
| country | varchar |  | 国家 |
| cert_english_name | varchar |  | 证件英文名 |
