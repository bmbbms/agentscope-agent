# ods_merch.t_qr_merch_reported (码付入驻流水-商户表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | bigint |  | 主键 |
| channel_org_id | varchar |  | 渠道商编号 |
| rate_type | varchar |  | 渠道商户费率类型 |
| channel_merch_type | varchar |  | 渠道商户类型 |
| shop_id | varchar |  | 门店编号 |
| merch_no | varchar |  | 商户号 |
| channel_merch_no | varchar |  | 渠道商户号 |
| merch_name | varchar |  | 商户名称 |
| shop_name | varchar |  | 商户简称 |
| service_phone | varchar |  | 商户客服电话 |
| mcc | varchar |  | 标准商户类别码 |
| busi_category | varchar |  | 经营类目 |
| license_no | varchar |  | 商户证件编号（企业或者个体工商户提供营业执照，事业单位提供事证号） |
| corp_type | varchar |  | 商户证件类型，取值范围：NATIONAL_LEGAL：营业执照；NATIONAL_LEGAL_MERGE:营业执照(多证合一)；INST_RGST_CTF：事业单位法人证书 |
| contact_info | varchar |  | 商户联系人信息 |
| address_info | varchar |  | 商户地址信息 |
| bank_card_info | varchar |  | 商户对应银行所开立的结算卡信 |
| pay_code_info | varchar |  | 商户的支付二维码中信息，用于营销活动 |
| alipay_account_no | varchar |  | 商户的支付宝账号 |
| remark | varchar |  | 商户备注信息，可填写额外信息 |
| contact_name | varchar |  | 联系人,方便银联在必要时能联系上商家 |
| contact_phone | varchar |  | 联系电话,方便银联在必要时能联系上商家 |
| contact_email | varchar |  | 联系邮箱 |
| contact_wechatid_type | varchar |  | 联系人微信账号类型 |
| contact_wechatid | varchar |  | 联系人微信帐号 |
| reported_flag | varchar |  | 报备状态 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| failure_reason | varchar |  | 报备失败原因 |
| reported_type | varchar |  | 报备类型(银联-微信-10011,银联-支付宝-10009) |
| operation_type | varchar |  | 操作类型0标识第一次入驻，1标识商户更新报备信息 |
| cust_no | varchar |  | 客户号 |
| operator | varchar |  | 操作人 |
| flow_id | varchar |  | 流水id |
| cert_name | varchar |  | 法人姓名 |
| merch_status | varchar |  | 商户状态 |
