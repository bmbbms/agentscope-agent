# base_info.t_r_merch_term (右端商户-终端表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rmer_no | varchar |  | 右端商户号 |
| rmer_name | varchar |  | 右端商户名 |
| channel | varchar |  | 渠道编号 |
| channel_name | varchar |  | 渠道名称 |
| region_code | varchar |  | 商户地区码 |
| province_code | varchar |  | 商户所在省份 |
| province_name | varchar |  | 商户所在省份-名称 |
| city_code | varchar |  | 商户所在城市 |
| city_name | varchar |  | 商户所在城市-名称 |
| mcc_code | varchar |  | 商户MCC码 |
| standard | varchar |  | 标准类别，0-标准类，1-优惠类，2-特技类，3-减免类 |
| mer_status | varchar |  | 商户状态，0停用，1 正常 , 3 注销 |
| charge_class | varchar |  | 特殊计费档次 |
| charge_type | varchar |  | 特殊计费类型 |
| mer_create_time | varchar |  | 商户新增时间 |
| mer_update_time | varchar |  | 商户更新时间 |
| mer_create_name | varchar |  | 商户添加人 |
| mer_update_name | varchar |  | 商户修改人 |
| mer_remark | varchar |  | 商户备注 |
| auto_flag | varchar |  | 商户自动报备标志，0：否，1：是 |
| report_time | varchar |  | 商户报备时间 |
| fix_route | varchar |  | 是否固定路由(0:否,1:是) |
| dyn_route | varchar |  | 是否动态路由(0:否,1:是) |
| dyn_route_status | varchar |  | 动态路由状态，0-停用，1-启用 |
| product_type | varchar |  | 产品类型：1-POP+；2-MPOS |
| rterm_no | varchar |  | 右端终端号 |
| term_sn | varchar |  | 机身号 |
| stock_flag | varchar |  | 存量标识，Y-存量，N-新增 |
| term_device_type | varchar |  | 终端设备类型 01 ATM,02 传统POS,03 MPOS,04 智能POS,05 II型固定电话POS |
| term_status | varchar |  | 终端状态，0-停用，1-启用，2-注销 |
| term_create_time | varchar |  | 终端新增时间 |
| term_update_time | varchar |  | 终端更新时间 |
| shop_id | varchar |  | 门店id |
