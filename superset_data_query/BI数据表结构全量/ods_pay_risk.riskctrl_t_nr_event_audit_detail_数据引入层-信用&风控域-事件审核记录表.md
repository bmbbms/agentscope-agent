# ods_pay_risk.risk_tag_t_merch_tag_op (数据引入层-信用&风控域-商户标签操作记录)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| merch_no | varchar |  | 商户号 |
| tag_id | varchar |  | 标签id |
| tag_name | varchar |  | 标签名称 |
| op_type | varchar |  | 1 绑定, 2 解绑； |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| meta_write_service | varchar |  | 写入服务 |
| meta_ori_table | varchar |  | 原表 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
| dt | integer | partition key | 分区日期 create_time |
