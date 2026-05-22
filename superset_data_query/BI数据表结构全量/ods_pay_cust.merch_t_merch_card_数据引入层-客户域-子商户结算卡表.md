# ods_pay_cust.merch_t_merch_card (数据引入层-客户域-子商户结算卡表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | ID |
| merch_no | varchar |  | 子商户号 |
| merch_id | varchar |  | 商户ID |
| account_no | varchar |  | 银行账号 |
| account_type | varchar |  | 银行账户类型(1对公，0对私) |
| account_name | varchar |  | 银行账户户名 |
| mobile | varchar |  | 手机号 |
| auth_flag | varchar |  | 是否授权收款标志(0否，1是) |
| bank_code | varchar |  | 银行编码 |
| union_bank_no | varchar |  | 分支行联行号 |
| status | varchar |  | 状态(0初始1正常2停用3注销) |
| union_bank_name | varchar |  | 分支行名称 |
| master_flag | varchar |  | 主结算卡标志：1-主卡,0-副卡 |
| account_pic | varchar |  | 银行账号照片 |
| workbill_pic | varchar |  | 变更工单照片 |
| account_ocr_info | varchar |  | 银行卡OCR信息 |
| bank_name | varchar |  | 银行名称 |
| special_account_flag | varchar |  | 特殊账户标识，0，否；1，是 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| remark | varchar |  | 备注 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
