# ods_pay_risk.riskctrl_t_rc_alarm_operate (数据引入层-信用&风控域-规则处理明细表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 操作记录ID |
| operate_type | varchar |  | 操作类型 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| measure | varchar |  | 处理措施 |
| suggestions | varchar |  | 处理意见 |
| remark | varchar |  | 备注 |
| alarm_id | varchar |  | 预警ID |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
