# ods_pay_risk.compliance_t_rc_report (数据引入层-信用&风控域-可疑报告)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 报告号 |
| merch_nos | varchar |  | 商户号列表 |
| merch_names | varchar |  | 商户名称列表 |
| source | varchar |  | 来源warn-预警event-风险事件 |
| out_id | varchar |  | 外部ID-关联预警/风险事件等 |
| org_branch_id | varchar |  | 报告分支机构ID |
| status | varchar |  | 报告状态0-审核中1-待处理2-待上报3-上报中4-已上报5-待重报6-排除可疑 |
| org_name | varchar |  | 报告机构名称-RINM |
| risk_standard | varchar |  | 机构自定可疑交易标准编号-UDSI |
| deal_measure | varchar |  | 可疑交易处理情况-SSTM |
| risk_feature | varchar |  | 可疑交易特征-STCR |
| risk_desc | varchar |  | 可疑交易描述-SSDS |
| pre_report_name | varchar |  | 初次报送的可疑交易报文名称-ORXN |
| trans_count | bigint |  | 可疑交易数量-TTNM |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| merch_count | bigint |  | 可疑主体（商户）数量-SCTN |
| amount | bigint |  | 可疑金额 |
| org_area_code | varchar |  | 报告机构地区编码 |
| sent_times_flag | bigint |  | 报送次数标志 |
| type | varchar |  | 报告类型 |
| lei | varchar |  | LEI编码 |
| urgency | varchar |  | 报告紧急程度 |
| trigger_point | varchar |  | 报告触发点 |
| transaction_behavior | varchar |  | 资金交易及客户行为情况 |
| err_msg | varchar |  | 错误信息 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
