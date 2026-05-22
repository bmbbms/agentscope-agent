# ods_pay_cust.open_t_op_sp_merch (商户参数表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| sp_id | varchar |  | 用户系统id |
| status | varchar |  | 状态。0-不可用，1-可用，2-停用 |
| add_time | varchar |  | 添加时间 |
| update_time | varchar |  | 最后更新时间 |
| add_name | varchar |  | 添加人 |
| update_name | varchar |  | 最后一次更新时间 |
| busi_type | varchar |  | 业务类型。00-POS+订单支付业务，01-智能终端接入业务，02-智能终端养卡业务,03-分账业务 |
| remark | varchar |  | 备注 |
| ledger_num_limit | bigint |  | 分账方数量限制 |
| check_cert_no | varchar |  | 身份证号校验：0-不校验，1-不能为空 |
| check_card_no | varchar |  | 转入转出卡同名校验:0-不校验，1-校验是否同一人名下(身份证号或姓名) |
| org_id | varchar |  | 分公司ID |
| org_path | varchar |  | 分公司ID链 |
| trans_fee | bigint |  | 交易手续费(以分为单位) |
| cancle_trans_flag | varchar |  | 开通撤销交易标记(1:开通，0:不开通) |
| query_bal_flag | varchar |  | 开通余额查询标记(1:开通，0:不开通) |
| merch_emails | varchar |  | 商户联系邮箱(多个邮箱英文逗号分隔) |
| merch_phone | varchar |  | 商户联系电话 |
| audit_status | varchar |  | 审核状态(1:已审核，0:待审核，2:审核拒绝) |
| flow_proc_id | varchar |  | 工作流流程编号 |
| audit_reason | varchar |  | 审核通过/拒绝原因 |
| check_tran_in_card | varchar |  | 转入卡是否鉴权:0-否,1-是(默认) |
| print_remark | varchar |  | 是否打印小票备注:0-否(默认),1-是 |
| print_acquire_bank | varchar |  | 小票是否显示收单行:0-否(默认),1-是 |
| service_hotline | varchar |  | 小票打印服务热线 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 是否删除(false:否 是:true) |
| meta_output_time | varchar |  | 写入时间 |
| meta_ori_table | varchar |  | 原始表名 |
