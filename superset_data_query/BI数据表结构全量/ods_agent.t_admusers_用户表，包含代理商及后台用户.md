# ods_agent.t_admusers (用户表，包含代理商及后台用户)

| Column | Type | Extra | Comment |
|---|---|---|---|
| user_id | varchar |  | 用户ID，此ID在代理商平台通行，所有相关的UserID均为此ID |
| account | varchar |  | 账号 |
| name | varchar |  |  |
| phone | varchar |  | 代理商手机号 |
| password | varchar |  |  |
| pwd_err_num | varchar |  | 密码错误次数 |
| user_flag | varchar |  | 用户标识，1=代理商，2=人人贷，3=直营，4=渠道商 5=机构 6=子账号 7=嘉联自拓 8=分公司 |
| bank_account | varchar |  | 结算卡 |
| parent_user_id | varchar |  | 父级user_id；用户标识为6时，子账号所属代理商ID |
| glevel | varchar |  | 级别，表示用户级，若用户为代理商，则最大允许3 |
| status | varchar |  | 状态 1正常，2禁用，3删除 4必须修改密码，5待审核(1代审核后才允许使用) 6=审核未通过，7=待实名，8=待审核(1代以外代理商邀请方式添加)，9=审核未通过(1代以外代理商邀请方式添加) |
| last_update_time | varchar |  | 最后更新时间 |
| last_update_user | varchar |  | 最后更新人 |
| last_login_time | varchar |  | 最后登录时间 |
| last_login_ip | varchar |  | 最后登录IP |
| system_customer_id | varchar |  | 交易系统用户ID；用户标识为6时：备注 |
| login_err_date | varchar |  | 最后登录错误时间 |
| roleid | varchar |  | 角色ID，对于代理商来说没意义，所有代理商都一样 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| idcard | varchar |  | 身份证号 |
| allow_withdraw | varchar |  | 允许提现，1为允许，其它值均为不允许，不允许时分润金额进上级余额 |
| tax_point | varchar |  | 发票税点，百分比，3-10，默认3，不允许小数；用户标识为6时：薪资 |
| real_name | varchar |  | 真实姓名，用于处理代理商实名认证及提现信息姓名 |
| company_name | varchar |  | 公司名，入网时填写；用户标识为6时：工号 |
| is_blacklist | varchar |  | 是否黑名单，=1表示黑名单用户，黑名单不付款，不审核发票，=0或is null表示非黑名单用户 |
| area_id | varchar |  | 大区编号，对应t_config表中的Area配置 |
| area_province | varchar |  | 省编号，对应t_config表中的area_province配置 |
| path | varchar |  | 层级路径，格式： user_id user_id  |
| developer_id | varchar |  | 发展该代理商的子账号或者上级代理商ID；用户标识为1-代理商时有效 |
| source | varchar |  | 代理商来源：1=上级代理商添加；2=上级代理商邀请；3=管理平台添加 |
| last_upd_pwd_time | varchar |  | 上次修改密码时间 |
| version | varchar |  | 版本，1旧版本，2新版本 |
| register_type | varchar |  | 入网类型 1营业执照，3个人 |
| tax_type | varchar |  | 缴纳类型，1开票，2扣税 |
| branch_office | varchar |  | 归属分公司编号 |
| jldepartment | varchar |  | 归属业务部门编号 |
| license_no | varchar |  | 营业执照注册号 |
| title | varchar |  | 职称 |
| email | varchar |  | 电子邮箱 |
| permission_type | varchar |  | 数据权限类型:0-公司 1-部门 2-个人 |
| user_type | varchar |  | 账号类型：1-分公司账号 2-部门管理员  3-员工 |
| address | varchar |  | 地址 |
| user_tax_type | varchar |  | 纳税人类型 1-一般纳税人 2-小规模纳税人 |
| link_name | varchar |  | 联系人姓名 |
