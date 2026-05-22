# ods_merch.t_merch_info (商户信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_id | varchar |  | 商户ID |
| merch_no | varchar |  | 商户号 |
| cust_id | varchar |  | 客户号 |
| merch_name | varchar |  | 商户名称(法定名称) |
| simple_name | varchar |  | 商户经营名称 |
| merch_name_en | varchar |  | 商户英文名称 |
| top_agent_id | varchar |  | 一级代理商编号 |
| direct_agent_id | varchar |  | 直属代理商编号 |
| company_id | varchar |  | 分公司ID |
| company_path | varchar |  | 分公司ID链 |
| depart_id | varchar |  | 业务部门ID |
| depart_path | varchar |  | 业务部门ID链 |
| prov_code | varchar |  | 省份代码 |
| city_code | varchar |  | 城市代码 |
| area_code | varchar |  | 地区代码 |
| det_address | varchar |  | 详细地址 |
| addr_position | varchar |  | 地址位置信息(json串{ longitude   经度   latitude   纬度 }) |
| mcc | varchar |  | MCC码 |
| cert_type | varchar |  | 证件类型(冗余字段方便查询) |
| cert_no | varchar |  | 证件号码(冗余字段方便查询) |
| license_no | varchar |  | 营业执照注册号(冗余字段方便查询) |
| print_merch_no | varchar |  | 打印商户号 |
| print_merch_name | varchar |  | 打印商户名 |
| register_type | varchar |  | 入网类型(1营业执照，2租赁合同，3小微，4立刷电签版) |
| register_src | varchar |  | 入网来源(合伙人、分公司、机构) |
| settle_type | varchar |  | 清算方式 |
| hold_pay_flag | varchar |  | 暂不付标志 |
| hold_pay_reason | varchar |  | 暂不付原因 |
| channel_type | varchar |  | 渠道类型 |
| status | varchar |  | 状态(0初始1正常2停用3注销) |
| audit_status | varchar |  | 审核流程状态，0待审核，1审核通过，2审核拒绝，3审核中 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 记录创建时间 |
| update_time | varchar |  | 记录更新时间 |
| cancle_time | varchar |  | 商户状态变更时间 |
| auth_time | varchar |  | 入网审核通过时间 |
| show_protocol_id | varchar |  | 显示的协议ID(历史数据处理) |
| audit_step | varchar |  | 当前步骤(1 录入商户资料，2 小微人脸识别，3 小微签名/上传承诺函，4 补充经营信息，5 人工审核 6审核结束) |
| client_unique_id | varchar |  | 客户唯一标识 |
| protocol_version | varchar |  | 电子协议版本号 |
| face_flag | varchar |  | 人脸识别通过标志(0 初始，1 通过，2 不通过) |
| face_pic | varchar |  | 人脸识别照片 |
| fail_reasons | varchar |  | 人工审核失败原因(List对象) |
| corp_promise_pic | varchar |  | 承诺函图片地址 |
| promise_position | varchar |  | 上传承诺函时手机定位信息(json串{ longitude   经度   latitude   纬度 }) |
| sign_pic | varchar |  | 法人/小微签名图片地址 |
| sign_position | varchar |  | 签名时手机定位信息 |
| match_percent | varchar |  | 人脸识别相似度 |
| flow_proc_id | varchar |  | 工作流流程编号 |
| paper_protocol_pic_list | varchar |  | 纸质协议列表 |
| busi_scope | varchar |  | 经营范围 |
| service_fee_id | varchar |  | 服务费ID |
| protocol_hash | varchar |  | 协议合同hash(用于判断是否修改协议数据) |
| contact_name | varchar |  | 联系人/经办人姓名 |
| contact_mobile | varchar |  | 联系人/经办人手机号 |
| contact_cert_type | varchar |  | 联系人/经办人证件类型01-身份证；02-护照；03-港澳通行证；08-军官证；09-港澳居民来往内地通行证（回乡证）；10-台湾同胞来往内地通行证（台胞证）；11-警官证；12-士兵证；13-户口簿；14-临时身份证；15-外国人居留证；99-其他证件 |
| contact_cert_no | varchar |  | 联系人/经办人证件号码 |
| wechat_auth_flag | varchar |  | 微信实名认证标志 0 未认证 1 已认证 |
| modify_status | varchar |  | 修改状态(0未修改，1已修改) |
| email | varchar |  | 邮箱 |
| service_mobile | varchar |  | 客服电话 |
| pwd_free | varchar |  | 免密免签  0.不免签不免密 1.免签 2.免签免密 |
| merch_data_flag | varchar |  | 商户资料标志：0.完整 1.缺失 2.失效 3.初始 |
| merch_data_remark | varchar |  | 商户资料备注 |
| allow_settle_flag | varchar |  | 是否允许自主变更结算账号0.否 1.是 |
| auth_collection | varchar |  | 是否允许授权收款 0-禁止 1-允许 |
| register_phone | varchar |  |  |
| reprot_bank_flag | varchar |  | 是否允许报备人行 0-禁止 1-允许 |
| reprot_bank_remark | varchar |  | 是否允许报备人行备注 |
| add_device_flag | varchar |  | 是否允许加机 0否1是 |
| auth_remark | varchar |  | 是否允许授权收款备注 |
| right_flag | varchar |  | 是否报备右端 |
| pay_pwd_set_status | varchar |  | 提现密码设置状态0：未设置，1：已设置 |
| send_agent_id | varchar |  | 上送资料代理商编号 |
| promise_version | varchar |  | 承诺函版本号 |
| staff_id | varchar |  | 员工ID |
| agreement_type | varchar |  | 协议类型(P-线下纸质协议,E-线上电子协议,L-签约承若函,S-法人签名) |
