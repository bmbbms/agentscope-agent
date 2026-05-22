# ods_pay_cust.merch_t_cust_attachment (数据引入层-客户域-客户附件信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| cust_no | varchar |  | 客户号 |
| type | varchar |  | 附件类型 |
| file_type | varchar |  | 文件类型1-图片2-pdf3-视频 |
| path | varchar |  | 附件地址 |
| video_path | varchar |  | 视频地址 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| remark | varchar |  | 备注 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
