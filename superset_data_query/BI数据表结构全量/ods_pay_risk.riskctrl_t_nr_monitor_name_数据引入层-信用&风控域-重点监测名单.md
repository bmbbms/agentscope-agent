# ods_pay_risk.riskctrl_t_nr_event_audit_detail (数据引入层-信用&风控域-事件审核记录表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| event_id | varchar |  | 事件ID |
| anti_flag | varchar |  | 是否推送反洗钱 |
| exclude_flag | varchar |  | 是否排除可疑 |
| due_flag | varchar |  | 是否下发尽调 |
| due_merch_nos | varchar |  | 尽调子商户号列表 |
| due_over_time | bigint |  | 尽调超时天数 |
| due_reason | varchar |  | 尽调原因 |
| survey_statement | varchar |  | 调查说明 |
| survey_type | varchar |  | 调查类型 |
| due_trade_ids | varchar |  | 尽调交易流水id |
| risk_type | varchar |  | 风险类型 |
| risk_level | varchar |  | 风险等级 |
| measure_deal_body | varchar |  | 处置主体 |
| first_audit_opinion | varchar |  | 初审意见 |
| second_audit_opinion | varchar |  | 复审意见 |
| status | varchar |  | 审核进度,00初审01复审通过02复审拒绝 |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| measure_deal_merch_nos | varchar |  | 处置子商户号列表 |
| risk_ctrl_tag | varchar |  | 风险标签 |
| op_source | varchar |  | 操作来源SYS-系统自动处理，MAN-人工处理 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
