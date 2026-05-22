# ods_pay_clear.clear_t_clearing_up_log (数据引入层-清算域-更新日志表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| log_id | varchar |  | 记录id |
| up_table | varchar |  | 变更表名称 |
| up_column | varchar |  | 变更字段 |
| ori_value | varchar |  | 原记录 |
| new_value | varchar |  | 新记录 |
| operator | varchar |  | 操作人 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| source | varchar |  | 来源1-入网进件2-新增立牌/静态码3-立刷机型变更4-开通理财业务5-开通秒到6-手工调整7-管理平台设置8-分公司管理平台 |
| busi_id | varchar |  | 业务端id |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
