# ods_pay_cust.merch_t_cust_license (数据引入层-客户域-营业执照信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| cust_id | varchar |  | 客户ID |
| cert_cust_id | varchar |  | 法人客户ID，关联法人表主键 |
| license_no | varchar |  | 营业执照号 |
| credit_no | varchar |  | 统一社会信用代码 |
| org_license | varchar |  | 组织机构代码证/三证合一前的营业执照号 |
| license_name | varchar |  | 营业执照名称 |
| license_region_code | varchar |  | 营业执照上的地区码，可能为省市区任意一级 |
| license_address | varchar |  | 营业执照注册地址 |
| business_scope | varchar |  | 经营范围 |
| office | varchar |  | 发证机关 |
| regist_date | varchar |  | 核准日期 |
| regist_cny | varchar |  | 币种默认人民币 |
| regist_amt | decimal(22,6) |  | 注册资金（万元） |
| actual_amt | decimal(22,6) |  | 实收资金（万元） |
| regist_status | varchar |  | 营业执照登记状态0-在营（开业），1-撤销，2-吊销，3-迁出，4-撤销登记，5-注销，6-其他 |
| corp_type | varchar |  | 企业类型，1、个体工商户；2、企业3、其他组织；4、政府及事业单位；6-社会组织；7-民办非企业 |
| open_date | varchar |  | 开业日期 |
| cancel_date | varchar |  | 注销日期 |
| revoke_date | varchar |  | 吊销日期 |
| begin_date | varchar |  | 营业执照有效期开始日期 |
| end_date | varchar |  | 营业执照有效期截止日期 |
| license_pic | varchar |  | 营业执照照片 |
| small_company_flag | varchar |  | 是否为小微企业，1-是小微企业，0-不是小微企业 |
| certification_type | varchar |  | 登记证书类型01-事业单位法人证书|02-组织机构代码证|03-税务登记证|04-医疗机构执业许可证|05-办学许可证|06-统一社会信用代码证书|07-社会团体法人登记证书|08-民办非企业单位登记证书|09-基金会法人登记证书|10-律师事务所执业许可证|11-基层群众性自治组织特别法人统一社会信用代码证|12-农村集体经济组织登记证|13-宗教活动场所登记证|14-政府部门下发的其他有效证明文件|15-社会服务机构登记证书|16-工会法人资格证书|17-基层法律服务所执业证|18-司法鉴定许可证|19 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| remark | varchar |  | 备注 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
| change_status_time | varchar |  | 状态变更时间 |
