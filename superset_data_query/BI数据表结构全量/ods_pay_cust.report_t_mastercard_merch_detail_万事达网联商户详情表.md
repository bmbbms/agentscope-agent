# ods_pay_cust.report_t_mastercard_merch_detail (万事达网联商户详情表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| channel_merch_no | varchar |  | 渠道商户号 |
| acquirer_ica | varchar |  | 收单机构代码 |
| country_code | varchar |  | 国家代码 |
| license_type | varchar |  | 商户营业证明文件类型01：营业执照编码02：统一社会信用代码03：组织机构代码证04：经营许可证05：税务登记证06：个人身份证99：其他 |
| license_no | varchar |  | 营业证明文件号码，对于企业单位，应与商户工商营业执照上的号码一致；对于事业单位，应与事业单位法人证书上登记号码一致。 |
| business_address | varchar |  | 商户经营地址 |
| register_address | varchar |  | 商户注册地址 |
| funding_method | varchar |  | 资金入账方式1-收单行入账,2-结算行入账 |
| legal_person_name | varchar |  | 法人代表姓名 |
| certificate_type | varchar |  | 法人代表证件类型，01：身份证02：护照03：军官证04：户口簿05：士兵证06：港澳居民来往内地通行证07：台湾同胞来往内地通行证08：临时身份证09：外国人居留证10：警官证11：港澳居民居住证12：台湾居民居住证99：其他 |
| certificate_no | varchar |  | 法人代表证件号码 |
| contact | varchar |  | 商户联系人 |
| contact_address | varchar |  | 商户联系人通讯地址 |
| contact_phone | varchar |  | 商户联系人电话 |
| contact_mobile | varchar |  | 商户联系人移动电话 |
| development_method | varchar |  | 商户拓展方式，1-自主拓展2-委托外包 |
| out_service_agency | varchar |  | 收单外包服务机构，“商户拓展方式”=2时填 |
| merch_url | varchar |  | 网站访问的域名地址，“商户属性”=02或03时填写 |
| web_app_name | varchar |  | 网站或APP名称，“商户属性”=02或03时填写 |
| icp_license_number | varchar |  | ICP许可证编号，“商户属性”=02或03时 |
| merch_attribute | varchar |  | 商户属性01：实体特约商户02：网络特约商户03：实体兼网络特约商户 |
| settlement_card_no | varchar |  | 商户收单清算账户 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 是否删除(false:否 是:true) |
| meta_output_time | varchar |  | 写入时间 |
| meta_ori_table | varchar |  | 原始表名 |
