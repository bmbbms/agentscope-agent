# base_info.t_admusers_info (代理商信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| user_id | varchar |  | 用户ID，此ID在代理商平台通行，所有相关的UserID均为此ID |
| name | varchar |  | 代理商名称 |
| idcard | varchar |  | 身份证号 |
| phone | varchar |  | 代理商手机号 |
| area_province | varchar |  | 省编号，对应t_config表中的area_province配置 |
| glevel | varchar |  | 级别，表示用户级，若用户为代理商，则最大允许3 |
| user_flag | varchar |  | 用户标识，1=代理商，2=人人贷，3=直营，4=渠道商,5=机构,6=子账号,7=嘉联自拓 |
| bank_account | varchar |  | 对私，结算卡 |
| real_name | varchar |  | 对私，真实姓名，用于处理代理商实名认证及提现信息姓名 |
| company_name | varchar |  | 公司名，入网时填写 |
| status | varchar |  | "状态1正常，2禁用，3删除,4必须修改密码，5待审核(1代审核后才允许使用),6=审核未通过，7=待实名" |
| is_blacklist | varchar |  | 是否黑名单，=1表示黑名单用户，黑名单不付款，不审核发票，=0或is null表示非黑名单用户 |
| developer_id | varchar |  | 发展该代理商的子账号或者上级代理商ID；用户标识为1-代理商时有效 |
| create_time | varchar |  | 创建时间 |
| last_update_time | varchar |  | 最后更新时间 |
| parent_user_id | varchar |  | 直属上级代理商id |
| trd_cus_id | varchar |  | 交易系统客户号 |
| path | varchar |  | 层级路径 |
| tax_point | varchar |  | 发票税点，百分比，3-10，默认3，不允许小数；用户标识为6时：薪资 |
| allow_withdraw | varchar |  | 允许提现，1为允许，其它值均为不允许，不允许时分润金额进上级余额 |
| root_user_id | varchar |  | 一级代理商id |
| root_user_name | varchar |  | 一级代理商名称 |
| managername | varchar |  | 渠道经理 |
| channeltype | varchar |  | 是否允许选择渠道  0 不允许   1允许 |
| belong_branch | varchar |  | 业务部门 |
| openname | varchar |  | 对公，开户姓名 |
| account_no | varchar |  | 对公，开户账号 |
| bank_sub_name | varchar |  | 对公，开户银行 |
| bank_union_code | varchar |  | 对公，银联号 |
| accounttype | varchar |  | 账户类型 1 对公账户  0对私账户  |
| legalmancertno | varchar |  | 法人身份证号码 |
| legalmanname | varchar |  | 法人姓名 |
| legalmanphone | varchar |  | 法人联系电话 |
| licenseaddress | varchar |  | 营业执照注册地址 |
| licenseno | varchar |  | 营业执照 |
| bankname | varchar |  | 公司开户行 |
| bankno | varchar |  | 公司开户账号 |
| billno | varchar |  | 公司税号 |
| billtitile | varchar |  | 公司抬头 |
| billtype | varchar |  | 发票类型     0 普通发票   1 专用发票 |
| regisaddress | varchar |  | 公司注册地址 |
| regisphone | varchar |  | 公司注册电话 |
| receaddress | varchar |  | 收货地址 |
| recename | varchar |  | 收货人名称 |
| recephone | varchar |  | 收货人电话 |
| r_agt_acc | varchar |  |  |
| agt_acc | varchar |  |  |
| branch_company | varchar |  | 分公司编号 |
