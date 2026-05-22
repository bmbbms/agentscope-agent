# ods_pay_cust.merch_t_attachment_oracle (数据引入层-客户域-商户附件信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | ID |
| merch_id | varchar |  | 商户ID |
| type | varchar |  | 附件类型 |
| path | varchar |  | 附件地址 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| cust_id | varchar |  | 客户ID |
| shop_id | varchar |  | 门店ID |
| file_type | varchar |  | 1图片2pdf3视频 |
| video_path | varchar |  | 视频地址 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
