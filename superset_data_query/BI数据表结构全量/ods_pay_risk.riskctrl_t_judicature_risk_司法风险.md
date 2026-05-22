# ods_pay_risk.risk_merch_t_cust_level_op (客户评级操作记录表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| level_op_id | varchar |  | 评级操作记录ID |
| cust_no | varchar |  | 客户号 |
| merch_no | varchar |  | 商户号,评级取商户信息的商户号 |
| cust_name | varchar |  | 客户姓名 |
| cust_level | varchar |  | 评级级别 |
| cust_score | varchar |  | 评级分数 |
| level_version | varchar |  | 评级版本 |
| status | varchar |  | 状态,0:待审核，1:审核通过，2:审核拒绝，3:待复审，4:初审通过 |
| op_source | varchar |  | 操作来源,A:商户进件，B:商户变更，C:人工排查，D:定时重评，E:风险事件，F:渠道风险 |
| op_event_id | varchar |  | 风险事件ID,操作来源为风险事件时记录风险事件ID |
| op_type | varchar |  | 操作类型,1系统评级2初审通过3复审通过4定时重评5初审退回6复审退回7人工修改8变更重评9人工重评10风险重评 |
| flow_proc_id | varchar |  | 工作流流程编号 |
| remark | varchar |  | 备注 |
| op_time | varchar |  | 操作时间 |
| op_user | varchar |  | 操作人 |
| update_time | varchar |  | 更新时间 |
| del_flag | varchar |  | 删除标志,1:未删除，0:已删除 |
| cust_type | varchar |  | 客户类型(P个人客户，C企业客户) |
| score_index_id | varchar |  | 评分指标ID(1.0上使用) |
| audit_type | varchar |  | 审核类型(0人工审核,1自动审核) |
| register_type | varchar |  | 入网类型(1:营业执照入网,2:租赁合同入网,3:小微商户入网,4:立刷电签商户,5:立刷商户) |
| index_version | varchar |  | 指标版本 |
| corp_type | varchar |  | 企业类型(1:个体工商户,2:企业,3:其他,4:政府及事业单位) |
| level_op_source | varchar |  | 执行的评级类型 |
| case_id | varchar |  | 例外情形ID |
| cust_status | varchar |  | 客户状态(1:启用,2:停用,3:注销) |
| index_busi | varchar |  | 评级指标所属业务,MPOS:立刷/电签，POSP:POS+业务，SMALL:小微商户 |
