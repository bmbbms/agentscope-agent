# ods_merch.t_control_man (受益所有人/实际控制人表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| cert_type | varchar |  | 证件类型 |
| cert_no | varchar |  | 证件号码 |
| cert_name | varchar |  | 证件姓名 |
| begin_date | varchar |  | 证件有效期开始时间-yyyyMMdd |
| end_date | varchar |  | 证件有效期结束时间-yyyyMMdd |
| face_pic | varchar |  | 证件正面照 |
| back_pic | varchar |  | 证件背面照 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间-yyyy-MM-dd HH:mm:ss |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间-yyyy-MM-dd HH:mm:ss |
| update_user | varchar |  | 更新人 |
| subject_type | varchar |  | 主体类型 1受益所有人 2控制人 |
| source | varchar |  | 1入网传入 2 渠道识别 3 管理平台录入 |
| cust_id | varchar |  | 客户号 |
| cert_address | varchar |  | 证件地址 |
| nation | varchar |  | 国籍 |
| regist_proportion | varchar |  | 出资比例（%） |
| rank | varchar |  | 受益所有人/实际控制人 层级 |
| path | varchar |  | 受益所有人/实际控制人 控股情况 |
| auth_flag | varchar |  | 是否认证通过 |
| attachment_path | varchar |  | 图片地址 |
| sex | varchar |  | 性别 |
| cert_english_name | varchar |  | 证件英文名称 |
