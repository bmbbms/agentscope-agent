# ods_pay_cust.merch_t_merch_mark_detail_info (数据引入层-客户域-商户标记详细信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键ID |
| merch_no | varchar |  | 子商户号 |
| mark_info_model | varchar |  | 资料模块 |
| mark_value | varchar |  | 标记值 |
| mark_level | varchar |  | 标记层级 |
| mark_detail_id | varchar |  | 标记明细ID |
| parent_mark_id | varchar |  | 上级标记ID |
| mark_status | varchar |  | 标记状态，是否生效 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
