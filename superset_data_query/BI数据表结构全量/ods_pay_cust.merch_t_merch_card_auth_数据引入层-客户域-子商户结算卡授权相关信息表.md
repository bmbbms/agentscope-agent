# ods_pay_cust.merch_t_merch_card_auth (数据引入层-客户域-子商户结算卡授权相关信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | ID |
| merch_no | varchar |  | 子商户号 |
| merch_id | varchar |  | 商户ID |
| account_no | varchar |  | 银行账号 |
| auth_cust_id | varchar |  | 授权客户ID |
| auth_pic | varchar |  | 授权书照片 |
| auth_cert_type | varchar |  | 授权账户法人证件类型，取值范围同cert_type |
| auth_cert_no | varchar |  | 授权账户法人证件号码 |
| auth_cert_name | varchar |  | 授权账户法人姓名 |
| auth_license_no | varchar |  | 授权账户营业执照注册号 |
| auth_license_name | varchar |  | 授权账户营业执照商户名 |
| auth_cert_face_pic | varchar |  | 授权账户法人身份证正面照 |
| auth_cert_back_pic | varchar |  | 授权账户法人身份证背面照 |
| auth_license_pic | varchar |  | 授权账户营业执照照片 |
| cert_begin_date | varchar |  | 身份证有效期起始日期 |
| cert_end_date | varchar |  | 身份证有效期结束日期 |
| license_begin_date | varchar |  | 营业执照有效期起始日期 |
| license_end_date | varchar |  | 营业执照有效期结束日期 |
| auth_cert_attorney_pic | varchar |  | 法人账户授权委托书 |
| fund_relation_pic | varchar |  | 资金关系证明 |
| auth_face_pic | varchar |  | 授权收款人人脸照片 |
| signature_pic | varchar |  | 签名照片 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| remark | varchar |  | 备注 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
