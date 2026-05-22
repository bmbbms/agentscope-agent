# ods_pay_risk.riskctrl_t_nr_monitor_name (数据引入层-信用&风控域-重点监测名单)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| merch_no | varchar |  | 子商户号 |
| monitor_type | varchar |  | 监测类型，逗号分隔，00移机01额度02交易03提现 |
| status | varchar |  | 名单状态0初始1启用2停用 |
| valid_start_time | varchar |  | 有效开始时间，长期2001-01-0123:59:59 |
| valid_end_time | varchar |  | 有效结束时间，长期2099-01-0123:59:59 |
| source | varchar |  | 名单来源 |
| name_desc | varchar |  | 名单描述 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| modified_flag | varchar |  | 可修改标识，0否1是 |
| value_type | varchar |  | 主体类型；merch-商户，cust-客户 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
