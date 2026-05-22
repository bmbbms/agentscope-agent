# ods_opa_cust.open_devleoper_t_developer (数据引入层-客户域-开发者表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | integer |  | 开发者id |
| devp_type | varchar |  | 开发者类型 |
| legal_name | varchar |  | 法定名称 |
| credit_no | varchar |  | 统一社会信用代码 |
| cert_name | varchar |  | 法人姓名 |
| cert_no | varchar |  | 法人证件号码 |
| contact_name | varchar |  | 联系人姓名 |
| contact_phone | varchar |  | 联系人手机号 |
| contact_email | varchar |  | 联系人邮箱 |
| expand_department | varchar |  | 拓展部门 |
| company_id | varchar |  | 所属分公司 |
| direct_agent_name | varchar |  | 业务员 |
| license_no | varchar |  | 营业执照 |
| cert_face_pic | varchar |  | 法人证件人像面 |
| cert_back_pic | varchar |  | 法人证件国徽面 |
| due_diligence_report | varchar |  | 尽职调查报告 |
| tec_commit_letter | varchar |  | 技术对接承诺函 |
| bank_card_pic | varchar |  | 结算卡照片 |
| head_pic | varchar |  | 经营门头照 |
| body_pic | varchar |  | 经营场所照 |
| status | varchar |  | 状态 |
| project_initial_date | varchar |  | 立项日期 |
| project_release_date | varchar |  | 上线日期 |
| project_retire_date | varchar |  | 下线日期 |
| project_remark | varchar |  | 项目备注 |
| process_ids | varchar |  | 流程编号 |
| special_approve | varchar |  | 是否特批 |
| chargeable | varchar |  | 是否收费 |
| charge_amount | varchar |  | 收费金额 |
| charge_remark | varchar |  | 收费备注 |
| payment_proofs | varchar |  | 打款凭证 |
| ka_flag | varchar |  | 是否KA商户 |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 修改人 |
| update_time | varchar |  | 修改时间 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
