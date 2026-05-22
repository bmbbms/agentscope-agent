# ods_merch.t_merch_card (商户结算卡信息)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_id | varchar |  | 商户ID |
| account_no | varchar |  | 银行账号 |
| account_type | varchar |  | 银行账户类型(对公，对私) |
| account_name | varchar |  | 银行账户户名 |
| mobile | varchar |  | 手机号 |
| auth_flag | varchar |  | 是否授权收款标志(0否，1是) |
| auth_cust_id | varchar |  | 授权客户ID（弃用） |
| auth_pic | varchar |  | 授权书照片 |
| bank_code | varchar |  | 银行编码 |
| union_bank_no | varchar |  | 分支行联行号 |
| status | varchar |  | 状态(0初始1正常2停用3注销) |
| remark | varchar |  | 备注 |
| union_bank_name | varchar |  | 分支行名称 |
| master_flag | varchar |  | 主结算卡标志 |
| account_pic | varchar |  | 银行账号照片 |
| signature_pic | varchar |  | 签名照片 |
| workbill_pic | varchar |  | 变更工单照片 |
| auth_cert_type | varchar |  | 账户法人证件类型（包含授权和非授权） |
| auth_cert_no | varchar |  | 账户法人证件号码（包含授权和非授权） |
| auth_cert_name | varchar |  | 账户法人姓名（包含授权和非授权） |
| auth_license_no | varchar |  | 账户营业执照注册号（包含授权和非授权） |
| auth_license_name | varchar |  | 账户营业执照商户名 （包含授权和非授权） |
| auth_cert_face_pic | varchar |  | 账户法人身份证正面照（仅包含授权信息） |
| auth_cert_back_pic | varchar |  | 账户法人身份证背面照（仅包含授权信息） |
| auth_license_pic | varchar |  | 账户营业执照照片 （仅包含授权信息） |
| account_ocr_info | varchar |  | 银行卡OCR信息 |
| create_time | varchar |  | 记录创建时间 |
| update_time | varchar |  | 记录更新时间 |
| bank_name | varchar |  | 银行名称 |
| cert_begin_date | varchar |  | 身份证有效期起始日期 |
| cert_end_date | varchar |  | 身份证有效期结束日期 |
| license_begin_date | varchar |  | 营业执照有效期起始日期 |
| license_end_date | varchar |  | 营业执照有效期结束日期 |
| id | varchar |  |  |
| auth_cert_attorney_pic | varchar |  | 法人账户授权委托书 |
| fund_relation_pic | varchar |  | 资金关系证明 |
| auth_face_pic | varchar |  | 授权收款人人脸照片 |
| special_account_flag | varchar |  | 特殊账户标识，0，否；1，是 |
