# ods_pay_trd.insurance_t_customer_white_name (数据引入层-交易域-保险白名单)

| Column | Type | Extra | Comment |
|---|---|---|---|
| customer_id | varchar |  | 消费者ID |
| status | varchar |  | 状态(0.不显示保险,1.显示且默认勾选,2.显示且默认不勾选，9删除) |
| ctime | varchar |  | 创建时间 |
| utime | varchar |  | 更新时间 |
| merch_no | varchar |  | 商户号 |
| white_type | varchar |  | 白名单类型:1-商户(默认),2-代理商 |
| use_status | varchar |  | 启用状态:0-停用,1-启用(默认) |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
