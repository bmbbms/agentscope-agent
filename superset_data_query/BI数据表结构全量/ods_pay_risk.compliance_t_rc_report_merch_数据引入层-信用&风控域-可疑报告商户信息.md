# ods_pay_risk.compliance_t_rc_report_merch (数据引入层-信用&风控域-可疑报告商户信息)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键ID |
| report_id | varchar |  | 报告号 |
| merch_no | varchar |  | 商户号-SMID |
| merch_name | varchar |  | 商户名-CTNM |
| mcc_type | varchar |  | 行业类别-CTVC |
| cert_type | varchar |  | 证件类型-CITP |
| cert_no | varchar |  | 证件号码-CTID |
| address | varchar |  | 详细地址-CTAR |
| mobile_no | varchar |  | 联系电话-CCTL |
| email | varchar |  | 电子邮件-CEML |
| legal_name | varchar |  | 法人姓名-CRNM |
| legal_cert_type | varchar |  | 法人证件类型-CRIT |
| legal_cert_no | varchar |  | 法人证件号码-CRID |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| del_flag | varchar |  | 逻辑删除0-未删除1-删除 |
| nationality | varchar |  | 国籍 |
| net_time | varchar |  | 入网时间 |
| pbc_area_code | varchar |  | 商户归属地区 |
| account_type | varchar |  | 银行账户类型 |
| account_no | varchar |  | 结算卡号 |
| bank_name | varchar |  | 开户行 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
