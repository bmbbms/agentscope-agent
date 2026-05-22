# ods_merch.t_merch_auth_card (商户认证卡信息)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_id | varchar |  | 商户id |
| account_no | varchar |  | 卡号 |
| account_name | varchar |  | 户名 |
| mobile | varchar |  | 手机号，加密保存 |
| bank_code | varchar |  | 银行编码 |
| bank_name | varchar |  | 银行名称 |
| mine_flag | varchar |  | 是否是自己的卡 |
| status | varchar |  | 状态(0初始1正常2停用3注销) |
| remark | varchar |  | 备注 |
| account_pic | varchar |  | 银行账号照片 |
| account_ocr_info | varchar |  | 银行卡ocr信息 |
| create_time | varchar |  | 记录创建时间 |
| update_time | varchar |  | 记录更新时间 |
| cert_no | varchar |  | 身份证号，加密保存 |
| card_type | varchar |  | 卡类型，0-借记卡，1贷记卡，2预付费卡 |
