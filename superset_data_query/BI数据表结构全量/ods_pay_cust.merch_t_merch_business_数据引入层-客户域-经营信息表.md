# ods_pay_cust.merch_t_merch_business (数据引入层-客户域-经营信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| business_code | varchar |  | 经营地区码 |
| business_address | varchar |  | 经营地址 |
| business_name | varchar |  | 经营名称 |
| business_position | varchar |  | 地址位置信息(json串{"longitude":"经度","latitude":"纬度"}) |
| mcc | varchar |  | mcc码 |
| print_merch_no | varchar |  | 打印商户号 |
| print_merch_name | varchar |  | 打印商户名 |
| head_pic | varchar |  | 门头照 |
| body_pic | varchar |  | 经营照 |
| counter_pic | varchar |  | 收银台照片 |
| service_phone | varchar |  | 客服手机号 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| remark | varchar |  | 备注 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
| shop_id | varchar |  | 门店ID |
