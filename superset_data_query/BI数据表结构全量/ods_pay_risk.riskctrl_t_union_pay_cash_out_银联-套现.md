# ods_pay_risk.riskctrl_t_nr_merch_due (数据引入层-信用&风控域-门店尽调表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 尽调ID |
| merch_no | varchar |  | 门店号 |
| merch_name | varchar |  | 门店名称 |
| cust_due_id | varchar |  | 客户尽调关联ID |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| work_id | varchar |  | 工单编号 |
| out_id | varchar |  | 门店尽调外部ID |
| meta_write_service | varchar |  | 写入服务 |
| meta_ori_table | varchar |  | 原表 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
