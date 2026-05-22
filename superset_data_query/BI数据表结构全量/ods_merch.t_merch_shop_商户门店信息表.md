# ods_merch.t_merch_shop (商户门店信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| shop_id | varchar |  | 门店ID |
| merch_id | varchar |  | 商户ID |
| shop_name | varchar |  | 门店经营名称 |
| shop_name_en | varchar |  | 门店英文名称 |
| prov_code | varchar |  | 省份代码 |
| city_code | varchar |  | 城市代码 |
| area_code | varchar |  | 地区代码 |
| det_address | varchar |  | 详细地址 |
| addr_position | varchar |  | 地址位置信息(json串{ longitude   经度   latitude   纬度 }) |
| mcc | varchar |  | MCC码 |
| print_merch_no | varchar |  | 打印商户号 |
| print_merch_name | varchar |  | 打印商户名 |
| shop_head_pic | varchar |  | 门头照 |
| shop_body_pic | varchar |  | 经营照 |
| shop_counter_pic | varchar |  | 收银台照片 |
| shop_counter_pisotion | varchar |  | 拍照位置信息(json串{ longitude   经度   latitude   纬度 }) |
| status | varchar |  | 状态 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 记录创建时间 |
| update_time | varchar |  | 记录更新时间 |
| shop_head_positon | varchar |  | 拍照位置信息(json串{ longitude   经度   latitude   纬度 }) |
| shop_body_position | varchar |  | 拍照位置信息(json串{ longitude   经度   latitude   纬度 }) |
| service_phone | varchar |  | 客服电话 |
| cust_id | varchar |  | 客户ID |
| create_user | varchar |  | 创建人 |
| update_user | varchar |  | 更新人 |
| channel_merch_no | varchar |  | 渠道商户号 |
| channel_attach | varchar |  | 渠道报备图片附件 |
| master_flag | varchar |  | 是否是主/初始门店 1是0否 |
| license_no | varchar |  | 营业执照号 |
| license_pic | varchar |  | 营业执照照片地址 |
| license_name | varchar |  | 营业执照名称 |
| group_id | varchar |  | 门店对应的终端组ID |
