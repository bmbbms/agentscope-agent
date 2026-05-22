# ods_pay_cust.merch_t_merch_info (数据引入层-客户域-商户信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_id | varchar |  | 商户ID |
| merch_no | varchar |  | 商户号 |
| cust_id | varchar |  | 客户ID |
| merch_name | varchar |  | 商户名称 |
| merch_english_name | varchar |  | 商户英文名称 |
| top_agent_id | varchar |  | 一级代理商ID |
| direct_agent_id | varchar |  | 直属代理商ID |
| company_id | varchar |  | 分公司ID |
| company_path | varchar |  | 分公司路径 |
| depart_id | varchar |  | 业务部门ID |
| depart_path | varchar |  | 业务部门路径 |
| register_type | varchar |  | 入网类型(1营业执照，3小微) |
| product_type | varchar |  | 产品类型(01-标准POS，02-扫码POS，03-SAAS，04-场景POS) |
| register_source | varchar |  | 入网来源(5-自主进件7-合伙人进件8-渠道9-码付渠道10-POS渠道12-SDK进件C-分公司V4-商户系统4.0) |
| channel_type | varchar |  | 渠道类型(1-间连2-平台直连6-终端直连) |
| email | varchar |  | 商户邮箱 |
| register_phone | varchar |  | 注册手机号 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| remark | varchar |  | 备注 |
| status | varchar |  | 商户状态1-启用2-停用3-注销 |
| change_status_time | varchar |  | 状态变更时间 |
| auth_time | varchar |  | 审核时间 |
| audit_status | varchar |  | 审核状态0-待审核，1-审核通过，2-审核拒绝，3-审核中，4-流程终止 |
| audit_step | varchar |  | 审核步骤1-录入商户资料，2-小微人脸识别，3-小微签名/上传承诺函，4-补充经营信息，5-人工审核,6-审核结束 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
| change_status_type | varchar |  | 变更状态类型 |
