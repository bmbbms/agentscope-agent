# ods_pay_cust.partner_t_license_info (数据引入层-客户域-null)

| Column | Type | Extra | Comment |
|---|---|---|---|
| license_id | varchar |  | 营业执照主键ID |
| license_no | varchar |  | 营业执照号码 |
| license_name | varchar |  | 营业执照公司名称 |
| license_begin_date | varchar |  | 营业执照开始日期 |
| license_end_date | varchar |  | 营业执照结束日期 |
| license_address | varchar |  | 营业执照注册地址 |
| user_tax_type | double |  | 纳税人类型 |
| prov_code | varchar |  | 省份代码 |
| city_code | varchar |  | 城市代码 |
| area_code | varchar |  | 区代码 |
| cert_type | varchar |  | 证件类型 |
| cert_no | varchar |  | 证件号码 |
| cert_name | varchar |  | 证件人 |
| cert_begin_date | varchar |  | 证件有效期开始时间 |
| cert_end_date | varchar |  | 证件有效期结束时间 |
| create_time | varchar |  | 创建时间 |
| license_pic | varchar |  | 营业执照图片地址 |
| cert_face_pic | varchar |  | 证件正面照片 |
| cert_back_pic | varchar |  | 证件反面照片 |
| tax_point | double |  | 税点 |
| ent_status | varchar |  | 登记状态 |
| reg_cap | varchar |  | 注册资本 |
| rec_cap | varchar |  | 实收资本 |
| operate_scope | varchar |  | 经营范围 |
| filing_status | varchar |  | 上报状态，1表示已上报 |
| filing_remark | varchar |  | 上报备注 |
| filing_time | varchar |  | 上报修改时间 |
| status | varchar |  | 状态(0:待审核；1:启动；2:停用；3:注销) |
| update_time | varchar |  | 更新时间 |
| audit_status | varchar |  | 审核状态(0:待审核，1:审核通过，2:审核拒绝) |
| legal_name | varchar |  |  |
| operate_address | varchar |  | 经营地址 |
| belong_head_office | varchar |  | 所属总公司 |
| belong_head_office_license_no | varchar |  | 所属总公司营业执照号 |
| cooperation_status | varchar |  | 合作状态，0=待签约、1=已签约、2=待续签、3=已解约 |
| cooperation_begin_date | varchar |  | 合作开始日期 |
| cooperation_end_date | varchar |  | 合作结束日期 |
| cooperation_context | varchar |  | 合作内容 |
| cooperation_area | varchar |  | 合作地域 |
| sign_branch_office_id | varchar |  | 签约分公司id |
| report_status | varchar |  | 备案状态，0=未备案、1=已备案、2=取消备案 |
| report_begin_date | varchar |  | 备案开始日期 |
| report_end_date | varchar |  | 备案结束日期 |
| owner | varchar |  | 实控人 |
| owner_phone | varchar |  | 实控人电话 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
