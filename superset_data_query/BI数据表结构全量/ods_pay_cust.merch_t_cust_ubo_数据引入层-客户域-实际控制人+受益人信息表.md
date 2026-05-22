# ods_pay_cust.merch_t_cust_ubo (数据引入层-客户域-实际控制人/受益人信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| cust_id | varchar |  | 营业执照客户ID |
| subject_type | varchar |  | 主体类型1-受益所有人2-实际控制人 |
| cert_no | varchar |  | 个人证件号码 |
| cert_type | varchar |  | 个人证件类型01-身份证；02-护照；03-外地来往内地通行证；09-港澳居民来往内地通行证（回乡证）；10-台湾同胞来往内地通行证（台胞证）；15-外国人居留证；99-其他证件 |
| cert_name | varchar |  | 个人证件姓名 |
| cert_english_name | varchar |  | 个人证件英文名称 |
| begin_date | varchar |  | 证件有效期开始日期 |
| end_date | varchar |  | 证件有效期截止日期 |
| front_pic | varchar |  | 个人证件正面照片 |
| back_pic | varchar |  | 个人证件背面照片 |
| cert_address | varchar |  | 个人证件居住地址 |
| sex | varchar |  | 性别M-男F-女O-其他 |
| nation | varchar |  | 民族 |
| regist_proportion | varchar |  | 出资比例（%） |
| rank | varchar |  | 受益所有人/实际控制人层级 |
| path | varchar |  | 受益所有人/实际控制人控股情况 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| remark | varchar |  | 备注 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
| auth_flag | varchar |  | 是否认证通过 0-不通过 1-通过 |
| source | varchar |  | 来源 |
