# ods_pay_cust.micro_pos_t_device_product_info (数据引入层-客户域-设备产品表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| device_type | varchar |  | 机型 |
| product_type | varchar |  | 产品类型:1-上网宝,2-云电签,3-电签,4-微电签,5-微智能,6-嘉联优客 |
| firm_flag | varchar |  | 厂商标识 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| equity_package_id | varchar |  | 权益包id |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
