# ods_merch.t_cust_detail (客户详情表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| cust_no | varchar |  | 客户号 |
| cust_id | varchar |  | 客户关联号 |
| state | varchar |  | 客户状态 1-启用 2-停用 3-注销 |
| region_code | varchar |  | 行政地区码 |
| union_code | varchar |  | 银联地区码 |
| cust_name | varchar |  | 客户姓名 |
| cust_type | varchar |  | 客户证件类型 01-身份证; 02-护照; 03-港澳通行证; 04-营业执照;08-军官证; 09-港澳居民来往内地通行证(回乡证); 10-台湾同胞来往内地通行证(台胞证); 11-警官证; 12-士兵证; 13-户口簿; 14-临时身份证; 15-外国人居留证; 99-其他证件 |
| cust_cert_no | varchar |  | 客户证件号 |
| create_time | varchar |  | 创建时间, yyyy-MM-dd HH:mm:ss |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间, yyyy-MM-dd HH:mm:ss |
| update_user | varchar |  | 更新人 |
| remark | varchar |  | 备注 |
| mcc | varchar |  | MCC码 |
| license_no | varchar |  | 营业执照号 |
| type | varchar |  | 客户类型(个人/企业)  C-营业执照, P-小微 |
| merch_id | varchar |  | 商户ID |
| merch_no | varchar |  | 左端商户号 |
| account_no | varchar |  | 结算账号 |
| change_status_time | varchar |  | 客户状态变更时间, yyyy-MM-dd HH:mm:ss |
| merch_name | varchar |  | 商户名称 |
| register_time | varchar |  | 客户入网时间, yyyy-MM-dd HH:mm:ss |
| shop_name | varchar |  | 经营名称 |
| det_address | varchar |  | 详细地址 |
| merch_en_name | varchar |  | 商户英文名称 |
| mobile | varchar |  | 手机号 |
| cust_class | varchar |  | 客户类别 1-标准类 2-非标类 3-理财类 |
| account_name | varchar |  | 结算户名 |
| union_bank_name | varchar |  | 开户行 |
| union_bank_no | varchar |  | 开户行号 |
| account_pic | varchar |  | 结算照片 |
| addr_position | varchar |  | 地区码 |
| register_settle_flag | varchar |  | 是否允许入网变更结算卡标识 0-不允许 1-允许 |
| account_type | varchar |  | 0-对私法人收款 1-对公收款 2-对私授权收款 3-对公授权收款 4-对公特殊账户收款 |
| settle_mode | varchar |  | 结算模式 0 - 统一结算 , 1 - 独立结算 |
| corp_type | varchar |  | 企业类型 |
| pwd_free | varchar |  | 免密免签: 0.不免签不免密 1.免签 2.免签免密 |
| state_change_type | varchar |  | 状态变更类型 1-风险停用/注销；2-无交易停用/注销；3-正常停用/注销 4-资料整改停用/注销 |
