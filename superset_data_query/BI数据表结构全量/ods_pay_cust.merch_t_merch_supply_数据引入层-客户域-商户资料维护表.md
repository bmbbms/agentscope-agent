# ods_pay_cust.merch_t_merch_supply (数据引入层-客户域-商户资料维护表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| merch_no | varchar |  | 子商户号 |
| cust_id | varchar |  | 商户号 |
| merch_name | varchar |  | 商户名 |
| dept_id | varchar |  | 业务部门ID |
| company_id | varchar |  | 分公司ID |
| type | varchar |  | 维护类型，多个用逗号分开 |
| expire_time | varchar |  | 过期时间 |
| object_type | varchar |  | 通知对象，1商户，2代理商 |
| notice_type | varchar |  | 通知方式，1APP，2短信 |
| status | varchar |  | 状态，0待完成，1审核中，2审核打回，3已完成，4已取消，其中已完成，已取消为最终状态 |
| create_user | varchar |  | 创建人 |
| update_user | varchar |  | 更新人 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| issue_type | varchar |  | 问题类型 |
| issue_desc | varchar |  | 问题描述 |
| merch_type | varchar |  | 商户类型1POS+商户，2MPOS商户 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
| plan_deal_time | varchar |  | 计划处置时间 |
| remark | varchar |  | 备注 |
