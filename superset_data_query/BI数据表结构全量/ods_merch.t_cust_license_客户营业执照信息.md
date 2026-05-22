# ods_merch.t_cust_license (客户营业执照信息)

| Column | Type | Extra | Comment |
|---|---|---|---|
| cust_id | varchar |  | 客户号 |
| license_no | varchar |  | 营业执照注册号 |
| credit_no | varchar |  | 统一社会信用代码 |
| nation_tax | varchar |  | 国税登记号 |
| local_tax | varchar |  | 地税登记号 |
| org_license | varchar |  | 组织机构代码证/三证合一前的营业执照号 |
| cert_type | varchar |  | 个人证件类型01-身份证；02-护照；03-港澳通行证；08-军官证；09-港澳居民来往内地通行证（回乡证）；10-台湾同胞来往内地通行证（台胞证）；11-警官证；12-士兵证；13-户口簿；14-临时身份证；15-外国人居留证；99-其他证件 |
| cert_no | varchar |  | 个人证件号码 |
| cert_name | varchar |  | 个人证件姓名 |
| cert_cust_id | varchar |  | 法人客户ID |
| prov_code | varchar |  | 所在省份 |
| city_code | varchar |  | 所在城市 |
| area_code | varchar |  | 所在地区 |
| det_address | varchar |  | 经营详细地址 |
| addr_position | varchar |  | 地址位置信息(json串{ longitude   经度   latitude   纬度 }) |
| busi_scope | varchar |  | 经营范围 |
| corp_property | varchar |  | 企业性质 |
| annex_path | varchar |  | 附件路径 |
| office | varchar |  | 发证机关 |
| regist_date | varchar |  | 核准时间 |
| regist_cny | varchar |  | 币种，默认为：人民币 |
| regist_amt | varchar |  | 注册资金(万元) |
| actual_amt | varchar |  | 实收资本（万元）  |
| regist_stt | varchar |  | 营业执照登记状态  |
| corp_type | varchar |  | 企业类型，1、个体工商户；2、企业 3、其他；4、政府及事业单位  |
| open_date | varchar |  | 开业日期 |
| cancle_date | varchar |  | 注销日期 |
| revoke_date | varchar |  | 吊销日期 |
| last_check_year | varchar |  | 最后年检年度 YYYY  |
| last_report_date | varchar |  | 最近年报报送日期 |
| industry_code | varchar |  | 行业类别代码 |
| industry_name | varchar |  | 行业类别名称 |
| industry_mcc_code | varchar |  | 国民经济行业代码  |
| begin_date | varchar |  | 有效期开始日期 |
| end_date | varchar |  | 有效期截止日期 |
| license_pic | varchar |  | 营业执照照片地址 |
| license_auth_flag | varchar |  | 营业执照OCR认证标志(1 认证一致，0 认证不一致) |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| license_name | varchar |  | 营业执照名称 |
| company_prove_pic | varchar |  | 事业单位证明函 |
| license_region_code | varchar |  | 营业执照上的地区码，可能为省市区任意一级 |
| can_reason | varchar |  | 注销原因 |
| rev_reason | varchar |  | 吊销原因 |
| small_company_flag | varchar |  | 是否为小微企业，1-是小微企业，0-不是小微企业 |
| certification_type | varchar |  | 登记证书类型 |
