# base_info.t_tms_device (机具总表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| sn | varchar |  | 机身号 |
| model | varchar |  | 机具型号 |
| app_name | varchar |  | 应用名 |
| ver_id | varchar |  | 终端版本号 |
| ent_time | varchar |  | 入库时间 |
| ext_time | varchar |  | 出库时间 |
| priinamt | varchar |  | 采购价（单位分） |
| prioutamt | varchar |  | 出库价（单位分） |
| sim_card_no | varchar |  | 绑定sim卡卡号 |
| order_id | varchar |  | 订单id |
| agt_map_id | varchar |  | 代理商映射id |
| act_time | varchar |  | 激活时间 |
| unbind_time | varchar |  | 解绑时间 |
| act_status | varchar |  | 激活状态，0未启用，1已启用2、停用 3、注销 |
| inv_status | varchar |  | 库存状态，0－出库，1－入库 |
| physn_status | varchar |  | 机具状态：0、正常、1、返修、2、报废 |
| buy_type | varchar |  | 购买类型（0购机，1租机，2免费） |
| belong_type | varchar |  | 归属类型（代理商映射id类型）06-代理商 05-直营 |
| belong_name | varchar |  | 归属名字 |
| apmac | varchar |  | 路由物理地址 |
| app_type | varchar |  |  应用类型:pos、order_pos |
| trd_host | varchar |  | 交易ip或者域名 |
| trd_port | varchar |  | 交易端口 |
| termsrc | varchar |  | 来源，对外机具入库专有字段 |
| dev_type | varchar |  | 设备类型 |
| xgd_pos | varchar |  | 是否嘉联pos机，1-是，0-不是 |
| vendor_code | varchar |  | 银联给终端厂家分配的6位厂商编号，000004为新国都 |
| update_time | varchar |  | 更新时间 |
| eff_time | varchar |  | 生效时间 |
| inv_time | varchar |  | 失效时间 |
| is_keybord | varchar |  | 是否有键盘 |
| term_keypad | varchar |  | 终端键盘号 |
| is_mer_band | varchar |  | 商户是否已绑定 |
| is_key_down | varchar |  | 主密匙是否下载 |
| br_no | varchar |  | 机构代码 |
| mer_no | varchar |  | 商户号 |
| term_no | varchar |  | 终端号 |
| area_code | varchar |  | 地区代码 |
| bind_time | varchar |  | 绑定时间 |
| bind_agt_time | varchar |  | 绑定代理商的时间 |
| customer_id | varchar |  |  客户id |
