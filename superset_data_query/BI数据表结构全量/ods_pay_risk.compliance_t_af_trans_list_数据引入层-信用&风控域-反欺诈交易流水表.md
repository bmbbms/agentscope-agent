# ods_pay_risk.compliance_t_af_trans_list (数据引入层-信用&风控域-反欺诈交易流水表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| trans_serial | varchar |  | 传输报文流水号 |
| tx_code | varchar |  | 交易类型编码A00105-止付A00107-止付延期/解除A00205-冻结A00207-冻结延期/解除A00311-单笔查询 |
| acqins_org_code | varchar |  | 受理机构编号:对应请求报文是发送机构，对应应答报文是接收结构 |
| feedback_trans_serial | varchar |  | 反馈报文流水号 |
| app_id | varchar |  | 业务申请编号 |
| ori_app_id | varchar |  | 原业务申请编号(与第一次止付业务申请编号相同) |
| app_time | varchar |  | 业务申请时间 |
| app_type | varchar |  | 业务类型(A00205/A00207:00-冻结延期,01-冻结解除,02-冻结)(A00105/A00107:00-止付延期,01-止付解除,02-止付) |
| app_org_code | varchar |  | 业务申请机构编号 |
| app_org_name | varchar |  | 业务申请机构名称 |
| case_no | varchar |  | 案件编号 |
| case_doc_id | varchar |  | 法律文书号 |
| case_type | varchar |  | 案件类型（0000-电信诈骗） |
| feedback_org_code | varchar |  | 反馈支付机构编号 |
| feedback_org_name | varchar |  | 反馈支付机构名称 |
| account_type | varchar |  | 账号类别（01-个人；02-商户） |
| feature_code | varchar |  | 事件特征码:9999-支付机构自定义异常事件 |
| feature_desc | varchar |  | 异常事件描述(<FeatureCode>=9999时，必填) |
| param_type | varchar |  | 参数类型(A1-按外部银行流水号止付；A2-支付机构订单号；A3-收单POS刷卡流水号) |
| param_data | varchar |  | 传入参数（param_type=A1时，传入外部银行流水号，要求止付进入止付机构内的该笔交易，中止结算；param_type=A2时，传入支付订单号，要求止付进入止付机构内的该笔交易，中止结算,param_type=A3时，传入收单POS流水号，要求止付该POS机结算业务，中止结算) |
| trans_time | varchar |  | 交易时间(精确到日) |
| amount | bigint |  | 金额 |
| req_reason | varchar |  | 事由 |
| req_remark | varchar |  | 说明 |
| start_time | varchar |  | 起始时间 |
| expire_time | varchar |  | 截止时间 |
| operator_id_type | varchar |  | 经办人证件类型 |
| operator_id | varchar |  | 经办人证件号码 |
| operator_name | varchar |  | 经办人姓名 |
| operator_phone | varchar |  | 经办人电话 |
| investigator_id_type | varchar |  | 协查人证件类型 |
| investigator_id | varchar |  | 协查人证件号码 |
| investigator_name | varchar |  | 协查人证件姓名 |
| result_code | varchar |  | 结果 |
| term_no | varchar |  | 消费POS机编号 |
| merch_no | varchar |  | 商户号 |
| merch_name | varchar |  | 开户主体姓名或企业名称 |
| merch_id_type | varchar |  | 开户主体证件类型 |
| merch_id | varchar |  | 开户主体证件号 |
| merch_id_period | varchar |  | 证照有效期（格式：YYYYMMDD-YYYYMMDD） |
| merch_phone | varchar |  | 开户主体电话号码 |
| merch_addr | varchar |  | 开户主体绑定地址 |
| feedback_reason | varchar |  | 反馈原因 |
| feedback_remark | varchar |  | 反馈说明 |
| status | varchar |  | 状态:1-已受理，2-已反馈，3-反馈成功，4-反馈失败 |
| ret_code | varchar |  | 返回码 |
| ret_msg | varchar |  | 返回消息 |
| feedback_operator_name | varchar |  | 反馈经办人姓名 |
| feedback_operator_phone | varchar |  | 反馈经办人电话 |
| feedback_time | varchar |  | 反馈时间 |
| ret_time | varchar |  | 反馈应答时间 |
| ret_trans_serial | varchar |  | 应答报文流水号 |
| freeze_order_id | varchar |  | 冻结订单号 |
| hold | varchar |  | 保留字段，存储一些不支持的报文信息 |
| create_time | varchar |  |  |
| update_time | varchar |  |  |
| feedback_packet | varchar |  | 反馈报文 |
| event_id | varchar |  | 风险事件编号 |
| deal_status | varchar |  | 处理状态：00-初始；01-待处理；02-处理中；03-已处理 |
| cust_no | varchar |  | 客户号 |
| cust_name | varchar |  | 客户名称 |
| meta_write_service | varchar |  | 写入服务 |
| meta_ori_table | varchar |  | 原表 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
