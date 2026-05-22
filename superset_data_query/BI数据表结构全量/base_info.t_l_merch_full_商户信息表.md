# base_info.t_l_merch_full (商户信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| mer_no | varchar |  | 商户号 |
| mer_name | varchar |  | 商户名称 |
| short_name | varchar |  | 商户简称 |
| email | varchar |  | 商户邮箱 |
| phone | varchar |  | 商户电话 |
| send_code | varchar |  | 发送机构(F33) |
| acqu_code | varchar |  | 收单机构(F32) |
| pmer_no | varchar |  | 打印商户号 |
| en_name | varchar |  | 商户英文名称 |
| status | varchar |  | 商户状态 0-初始 1-启用 2-停用 3-注销 |
| busi_scope | varchar |  | 经营范围 |
| fee_type | varchar |  | 商业类别 01-标准类,02-优惠类 03-减免类 04-特殊计费类 05-其他类 |
| pwdfree | varchar |  | 免签免密标志00-不免签不免疫 01-免签免密 1-免签 |
| agt_id | varchar |  | 直属代理商编号 |
| agt_name | varchar |  | 直属代理商姓名 |
| agt_account | varchar |  | 直属代理商帐号 |
| r_agt_id | varchar |  | 一级代理商编号 |
| r_agt_name | varchar |  | 一级代理商姓名 |
| r_agt_account | varchar |  | 一级代理商帐号 |
| agt_path | varchar |  | 代理商层级路径 |
| sys_customer_id | varchar |  | 系统客户ID |
| net_date | varchar |  | 入网时间 |
| net_type | varchar |  | 入网类型 1-营业执照 2-租赁合同 3-小微商户 |
| net_source | varchar |  | 入网来源 |
| cancel_date | varchar |  | 注销时间 |
| mcc | varchar |  | 商户类型(MCC) |
| mcc_desc | varchar |  | 商户类型描述(MCC) |
| bill_pkg_id | varchar |  | 月租套餐编号，表T_BILL_PACKAGE外键 |
| holdpay | varchar |  | 暂不付标识 |
| holdpay_reason | varchar |  | 暂不付原因 |
| chn_type | varchar |  | 渠道类型 1-间联 2-平台直连 6-终端直连 |
| lic_no | varchar |  | 营业执照编号 |
| legal_name | varchar |  | 法人代表姓名 |
| legal_phone | varchar |  | 法人代表手机号 |
| lic_addr | varchar |  | 营业执照地址 |
| legal_certype | varchar |  | 证件类型01-身份证 02-护照 03-港澳通行证 04-营业执照 05-其它人员、其它业务员 06-代理商、商户 07-代理商业务员 08-军官证；09-港澳居民来往内地通行证(回乡证) 10-台湾同胞来往内地通行证(台胞证) 11-警官证 12-士兵证 13-户口簿 14-临时身份证 15-外国人居留证 99-其他证件 |
| legal_cerno | varchar |  | 法人代表证件号 |
| lic_bdate | varchar |  | 营业执照生效日期 |
| lic_edate | varchar |  | 营业执照失效日期 |
| bord_flag | varchar |  | 境内外标识 |
| legal_cer_bdate | varchar |  | 法人代表证件生效日期 |
| legal_cer_edate | varchar |  | 法人代表证件失效日期 |
| le_contract_no | varchar |  | 租赁合同编号 |
| le_start_date | varchar |  | 租赁开始日期 |
| le_end_date | varchar |  | 租赁结束日期 |
| busi_bdate | varchar |  | 营业起始时间 |
| busi_edate | varchar |  | 营业结束时间 |
| lr_name | varchar |  | 出租方姓名 |
| lr_phone | varchar |  | 出租方联系方式 |
| lr_cer_type | varchar |  | 出租方证件类型 01-身份证 02-护照 03-港澳台身份证 04-军官证 99-其他 |
| lr_cer_no | varchar |  | 出租方证件号码 |
| le_name | varchar |  | 承租方姓名 |
| le_phone | varchar |  | 承租方联系方式 |
| le_cer_type | varchar |  | 承租方证件类型 01-身份证 02-护照 03-港澳台身份证 04-军官证 99-其他 |
| le_cer_no | varchar |  | 承租方证件号码 |
| le_cer_bdate | varchar |  | 承租方证件生效日期 |
| le_cer_edate | varchar |  | 承租方证件失效日期 |
| le_addr | varchar |  | 承租地址 |
| auth_type | varchar |  | 授权类型(1-对公帐号 0-对私法人收款 2-对私授权收款 3-对公授权收款) |
| card_no | varchar |  | 结算账号(卡号/对公账号) |
| card_name | varchar |  | 结算账号户名 |
| bank_no | varchar |  | 开户行 |
| bank_name | varchar |  | 开户行名称 |
| bra_bank_no | varchar |  | 开户行分支行 |
| bra_bank_name | varchar |  | 开户行分支行名称 |
| reg_mobile | varchar |  | 银行预留手机号 |
| card_cer_type | varchar |  | 持卡人证件类型 |
| card_cer_no | varchar |  | 持卡人证件号码 |
| idcard_bdate | varchar |  | 身份证有效开始时间 |
| idcard_edate | varchar |  | 身份证有效结束时间 |
| belong_branch | varchar |  | 业务部门 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| protocol_id | varchar |  | 协议编号 |
| region_code | varchar |  | 区域码 |
| region_name | varchar |  | 区域名 |
| data_integrity | varchar |  | 商户资料(0-完整 1-缺失 2-失效 3-初始) |
| tag_remark | varchar |  | 商户资料备注 |
| report_flag | varchar |  | 报备标志，0：不报备，1：报备，2：未确认 |
| report_remark | varchar |  | 报备备注 |
| busi_type | varchar |  | 商户业务大类 |
| shop_id | varchar |  | 门店id |
| branch_company | varchar |  | 分公司id |
| busi_bank_id | varchar |  | 商户拓展银行号 |
| busi_bank_name | varchar |  | 商户拓展银行名称 |
| busi_bank_path | varchar |  | 商户拓展银行号路径 |
| bank_manager_id | varchar |  | 银行客户经理id |
| bank_manager_name | varchar |  | 银行客户经理名称 |
| bank_work_no | varchar |  | 银行客户经理工号 |
| det_address | varchar |  | 注册地址 |
| busi_address | varchar |  | 主门店地址 |
| audit_status | varchar |  | 审核流程状态，0待审核，1审核通过，2审核拒绝，3审核中 |
| auth_time | varchar |  | 入网审核通过时间 |
| right_flag | varchar |  | 是否报备右端 |
| link_mobile | varchar |  | 主门店联系电话 |
| merch_id | varchar |  | 商户ID |
| pmer_name | varchar |  | 打印商户名 |
| agt_company | varchar |  | 直属代理商公司名 |
| r_agt_company | varchar |  | 一级代理商公司名 |
| s_agt_id | varchar |  | 二级代理商ID |
| s_agt_name | varchar |  | 二级代理商名称 |
| s_agt_account | varchar |  | 二级代理商帐号 |
| s_agt_company | varchar |  | 二级代理商公司名 |
| developer_id | varchar |  | 代理商员工ID |
| developer_name | varchar |  | 代理商员工姓名 |
| developer_acc | varchar |  | 代理商员工帐号 |
| holdpay_user | varchar |  | 暂不付操作人 |
| lic_prov_code | varchar |  | 营业执照省份 ods_merch.t_cust_license的prov_code |
| lic_city_code | varchar |  | 营业执照城市 ods_merch.t_cust_license的city_code |
| lic_area_code | varchar |  | 营业执照地区 ods_merch.t_cust_license的area_code |
| corp_type | varchar |  | 企业类型，1、个体工商户；2、企业 3、其他；4、政府及事业单位 |
| branch_name | varchar |  | 业务部门名称 |
| tag_time | varchar |  | 商户资料标记时间 |
| tag_handle_man | varchar |  | 商户资料变更操作人 |
| tag_handle_name | varchar |  | 资料完整标记处理人 |
| tag_handle_brch_name | varchar |  | 资料完整标记分公司处理人 |
| report_handle_man | varchar |  | 报备人行变更操作人 |
| report_handle_name | varchar |  | 报备标记处理人 |
| report_handle_brch_name | varchar |  | 报备标记分公司处理人 |
| bra_company_name | varchar |  | 所属分公司名称 |
| month_sett_type | varchar |  | 是否月结商户1-是 0-否 |
| settle_type | varchar |  | 清算方式 0-余额提现,1-自动T+1清算,2-笔笔秒到,3-仅T1 |
| change_status_reason | varchar |  | 商户状态变更原因 |
| change_status_time | varchar |  | 商户状态变更时间 |
| change_status_person | varchar |  | 商户状态变更人 |
| contact_man_name | varchar |  | 联系人姓名 |
| contact_man_cert_type | varchar |  | 联系人证件类型 |
| contact_man_cert_no | varchar |  | 联系人证件号码 |
| contact_man_mobile | varchar |  | 联系人电话 |
| holder_name | varchar |  | 股东名称 |
| holder_type | varchar |  | 股东类型0-自然人,1-企业股东,2-机构股东,3-其他 |
| holder_cer_type | varchar |  | 股东证件类型 |
| holder_cer_no | varchar |  | 股东证件号码 |
| holder_cer_bdate | varchar |  | 股东证件生效日期 |
| holder_cer_edate | varchar |  | 股东证件失效日期 |
| regist_proportion | varchar |  | 出资占比 |
| data_update_time | varchar |  | 数据(最大)更新时间 |
| lic_create_time | varchar |  | 营业执照首次入网时间 |
| cust_mcc | varchar |  | 客户号MCC |
| cust_no | varchar |  | 客户号 |
| cust_status | varchar |  | 客户状态 1-启用 2-停用 3-注销 |
| data_from | integer | partition key |  |
