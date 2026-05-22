# ods_merch.t_un_merch_reported (商户银联报备流水表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| report_operate | varchar |  | 报备操作,I-新增,U-修改,D-删除 |
| channel_merch_no | varchar |  | 渠道商户号 |
| merch_cn_name | varchar |  | 商户中文名称 |
| merch_en_name | varchar |  | 商户英文名称 |
| merch_simple_name | varchar |  | 商户中文简称 |
| union_region_code | varchar |  |  |
| mcc | varchar |  | 商户类别码/mcc码 |
| license_no | varchar |  | 营业执照号码 |
| busi_address | varchar |  | 商户经营地址 |
| register_address | varchar |  | 商户注册地址 |
| cert_name | varchar |  | 法人代表姓名 |
| cert_no | varchar |  | 法人代表证件号码 |
| merch_no | varchar |  | 商户号 |
| region_code | varchar |  | 行政地区码 |
| cert_type | varchar |  | 法人证件类型 |
| reported_flag | varchar |  | 报备状态 0-报备中，1-报备成功，2-报备失败 |
| create_time | varchar |  | 创建时间 yyyy-MM-dd HH:mm:ss |
| update_time | varchar |  | 更新时间 yyyy-MM-dd HH:mm:ss |
| operator | varchar |  | 操作人 |
| failure_reason | varchar |  | 失败原因，响应码也存里面 |
| cust_no | varchar |  | 客户号 |
| business_identify_type | varchar |  | 营业证明文件类型 |
| contract_phone | varchar |  | 联系人电话 |
| contract_name | varchar |  | 联系人姓名 |
| account_type | varchar |  | 商户账号类型 |
| account_no | varchar |  | 商户账号 |
| account_name | varchar |  | 商户账户名称 |
| bank_no | varchar |  | 商户开户行行号 |
| bank_name | varchar |  | 商户开户行名称 |
| addr_position | varchar |  | 经纬度 |
| merch_status | varchar |  | 商户状态 |
| remark | varchar |  | 备注 |
| pwd_free | varchar |  | 免密免签: 0.不免签不免密 1.免签 2.免签免密 |
