# ods_pay_risk.measure_t_nr_merch_appeal_op (数据引入层-信用&风控域-商户申诉操作记录表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| appeal_id | varchar |  | 申诉记录ID |
| type | varchar |  | 操作类型,00-提交申诉01-风控审核通过02-风控审核拒绝03-清算初审通过04-清算初审拒绝05-清算复审通过06-清算复审拒绝07-系统自动审核拒绝 |
| remark | varchar |  | 备注 |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
