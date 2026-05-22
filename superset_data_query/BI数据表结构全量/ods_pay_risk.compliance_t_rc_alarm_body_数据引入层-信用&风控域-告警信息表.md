# ods_pay_risk.compliance_t_rc_alarm_body (数据引入层-信用&风控域-告警信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | id |
| body_value | varchar |  | 预警主体:右端商户号 |
| merch_no_left | varchar |  | 左端商户号 |
| body_name | varchar |  | 右端商户名称 |
| deal_measure | varchar |  | 处理措施:03-交易黑名单,04-提现黑名单,01-排除可疑,08-冻结账户,16-风险停用,17-风险注销,99-其他 |
| status | varchar |  | 处理状态0待初审1待复审2已处理 |
| report_status | varchar |  | 上报状态0初始1待上报2已上报 |
| alarm_types | varchar |  | 预警类型，|分隔 |
| warn_codes | varchar |  | 触发的预警规则列表，|分隔 |
| trigger_times | decimal(22,0) |  | 触发次数 |
| is_test | varchar |  | 是否为测试规则，1是0否 |
| is_show | varchar |  | 是否显示1是0否 |
| trade_count | bigint |  | 交易次数 |
| trade_amount | bigint |  | 交易金额分 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 最后更新人 |
| remark | varchar |  | 备注 |
| risk_status | varchar |  | 风险状态 |
| merch_warn_is_show | varchar |  | 一对一是否显示1是0否 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
