# ods_pay_cust.merch_t_merch_contact (数据引入层-客户域-商户联系人信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| contact_type | varchar |  | 联系人类型65-经营者/法人66-经办人。 |
| contact_name | varchar |  | 联系人姓名 |
| contact_english_name | varchar |  | 联系人英文姓名 |
| contact_cert_type | varchar |  | 联系人证件类型(01-身份证；02-护照；03-港澳通行证；08-军官证；09-港澳居民来往内地通行证（回乡证）；10-台湾同胞来往内地通行证（台胞证）；11-警官证；12-士兵证；13-户口簿；14-临时身份证；15-外国人居留证；99-其他证件) |
| contact_cert_no | varchar |  | 联系人证件号码 |
| contact_cert_front_pic | varchar |  | 联系人证件正面照片 |
| contact_cert_back_pic | varchar |  | 联系人证件反面照片 |
| contact_cert_begin_date | varchar |  | 联系人证件有效期开始时间 |
| contact_cert_end_date | varchar |  | 联系人证件有效期结束时间 |
| contact_phone | varchar |  | 联系人手机号 |
| contact_email | varchar |  | 联系人邮箱 |
| contact_address | varchar |  | 联系人详细地址 |
| contact_wx | varchar |  | 联系人微信号 |
| sex | varchar |  | 性别M-男F-女O-其他 |
| country | varchar |  | 国籍 |
| status | varchar |  | 联系人状态1正常，2停用，9删除 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| create_user | varchar |  | 创建人 |
| update_user | varchar |  | 更新人 |
| remark | varchar |  | 备注 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
| contact_area | varchar |  | 联系人地区 |
