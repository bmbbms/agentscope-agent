# ods_pay_cust.open_t_op_sp_info (服务商(ServiceProvider)信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| sp_id | varchar |  | 服务商ID |
| sp_name | varchar |  | 服务商名称 |
| status | varchar |  | 用户系统状态。0-不可用，1-启用，2-停用 |
| notify_url | varchar |  | 交易结果通知的URL |
| query_url | varchar |  | 用户订单查询的URL |
| public_key_type | varchar |  | 公钥类型 |
| public_key | varchar |  | 服务商设置的公钥 |
| key_pair | varchar |  | 系统为服务商生成的密钥对，需要导出公钥给服务商，该字段需加密 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 记录创建时间 |
| update_time | varchar |  | 最后更新时间 |
| sp_type | varchar |  | 服务商类型。0-商户，1-代理商 |
| sp_busi_type | varchar |  | 服务商业务类型。00-POS+订单支付业务，01-智能终端接入业务，02-智能终端养卡业务，03-理财POS业务，04-保险业务,05-立刷，06-分账业务 |
| agent_no | varchar |  | 代理商编号 |
| sign_architecture | varchar |  | 签名算法 |
| sys_public_key | varchar |  | 系统生成的公钥 |
| update_user | varchar |  | 最后更新人 |
| merch_check_flag | varchar |  | 是否校验商户和SP的对应，0-不校验，1-校验 |
| card_auth_flag | varchar |  | 精养卡业务是否进行银行卡鉴权，0-不鉴权，1-鉴权 |
| app_check_flag | varchar |  | 是否校验APP的版本号/hash值。0-不校验，1-校验 |
| card_num | bigint |  | 养卡业务-机构可报备卡的数量 |
| user_num | bigint |  | 养卡业务-每个商户可报备用户的数量 |
| verify_notify_url | varchar |  | 交易结果通知的URL(生产验证) |
| verify_query_url | varchar |  | 用户订单查询的URL(生产验证) |
| agent_notify_flag | varchar |  | 是否消息通知代理商,默认0-不通知,1-进行通知 |
| facilitator_flag | varchar |  | 服务商标识1-外部服务商,0-内部服务商 |
| refund_switch_flag | varchar |  | 手动退款开关标识0-关闭,1-开启 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 是否删除(false:否 是:true) |
| meta_output_time | varchar |  | 写入时间 |
| meta_ori_table | varchar |  | 原始表名 |
