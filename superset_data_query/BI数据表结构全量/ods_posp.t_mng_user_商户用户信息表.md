# ods_posp.t_mng_user (商户用户信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| user_id | varchar |  | 用户ID |
| user_type | varchar |  | 用户类型(1平台自动生成，2管理人员添加) |
| user_code | varchar |  | 员工编号 |
| login_name | varchar |  | 登录名 |
| login_pwd | varchar |  | 登录密码 |
| user_name | varchar |  | 用户名 |
| mobile | varchar |  | 手机号 |
| email | varchar |  | 邮箱 |
| status | varchar |  | 状态(1 正常，2 停用，3 临时锁定，9 删除) |
| remark | varchar |  | 备注 |
| owner_plat | varchar |  | 所属平台(取T_PLAT_PROJECT.PLAT_CODE) |
| owner_id | varchar |  | 所属平台客户ID |
| create_time | varchar |  | 记录创建时间 |
| create_user | varchar |  | 记录创建人 |
| update_time | varchar |  | 修改时间 |
| update_user | varchar |  | 修改人 |
| login_ip | varchar |  | 最近登录IP |
| login_time | varchar |  | 最近登录时间 |
| crm_user_id | varchar |  | CRM系统userid |
| personal_info | varchar |  | 预留信息 |
| update_pwd_time | varchar |  | 最后修改密码时间 |
| force_pwd_update | varchar |  | 强制修改密码 1- 强制修改 0-不强制修改 |
| login_type | varchar |  | 登陆类型 P-账密登陆 T-账密+token登陆 |
| cert_type | varchar |  | 证件类型 01-身份证；02-护照；03-港澳通行证；05-其它人员、其它业务员；06-代理商、商户；07-代理商业务员；08-军官证；09-港澳居民来往内地通行证（回乡证）；10-台湾同胞来往内地通行证（台胞证）；11-警官证；12-士兵证；13-户口簿；14-临时身份证；15-外国人居留证；99-其他证件 |
| cert_no | varchar |  | 证件号码 |
| user_alias | varchar |  | 用户昵称 |
| force_pay_pwd_reset | varchar |  | 强制修改支付密码密码 1- 强制修改 0-不强制修改 |
| mbp_flag | varchar |  | 是否开通手机pos，1是0否 |
| last_login_device | varchar |  | 最近登录设备号，APP登录取device_no字段 |
| check_val | varchar |  | gm包字段加密校验值，通过sm3的hashmac 计算得到，长度44 |
