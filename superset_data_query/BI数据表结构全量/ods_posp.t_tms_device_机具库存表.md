# ods_posp.t_tms_device (机具库存表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| sn | varchar |  | 机身号 |
| model | varchar |  | 机具型号 |
| app_name | varchar |  | 应用名 |
| ver_id | varchar |  | 终端版本号 |
| entdate | varchar |  | 入库日期 |
| extdate | varchar |  | 出库日期 |
| priinamt | varchar |  | 采购价（单位分） |
| prioutamt | varchar |  | 出库价（单位分） |
| simcadno | varchar |  | 绑定SIM卡卡号 |
| inoprid | varchar |  | 入库操作员编号 |
| inoprname | varchar |  | 入库操作员姓名 |
| outoprid | varchar |  | 出库操作员编号 |
| outoprname | varchar |  | 出库操作员姓名 |
| order_id | varchar |  | 订单ID |
| agent_map_id | varchar |  | 代理商映射ID |
| activate_date | varchar |  | 激活日期 |
| unbind_date | varchar |  | 解绑的日期 |
| activate_status | varchar |  | 激活状态，0未启用，1已启用2、停用 3、注销 |
| inventory_status | varchar |  | 库存状态，0－出库，1－入库 |
| machine_status | varchar |  | 机具状态：0、正常、1、返修、2、报废 |
| buy_type | varchar |  | 购买类型（0购机，1租机，2免费） |
| update_time | varchar |  | 更新时间 |
| affiliation_type | varchar |  | 归属类型（代理商映射ID类型）06-代理商 05-直营 04-嘉联 |
| affiliation_name | varchar |  | 归属名字（冗余字段，可根据AGENT_MAP_ID以及AFFILIATION_TYPE查询） |
| apmac | varchar |  | 路由物理地址 |
| app_type | varchar |  | 应用类型 POS+、ORDER_POS |
| trade_host | varchar |  | 交易IP或者域名 |
| trade_port | varchar |  | 交易端口 |
| source | varchar |  | 来源，对外机具入库专有字段 |
| device_type | varchar |  | 设备类型(01：ATM 02：传统POS 03：MPOS 04：智能POS 05：MISPOS 06 II型固定电话POS 立牌：SP 电子码牌：EP 音箱：AD 意锐收银台：YR) |
| xgd_pos | varchar |  | 是否嘉联POS机，1-是，0-不是，2-新国都商服（预留） |
| vendor_code | varchar |  | 银联给终端厂家分配的6位厂商编号，000004为新国都 |
| virtual | varchar |  | 是否为虚拟机器，1-是；0-否 |
| tusn_flag | varchar |  | 银联21号文安全域标志，1-新机器，0-存量机器，默认值为：1 |
| tmk_gene_type | varchar |  | 终端主密钥下发方式 1.下发 2.不下发 |
| direct_agent_id | varchar |  | 直属代理商编号 |
| nfc_chip_id | varchar |  | NFC芯片ID |
| un_cut_machine_id | varchar |  | 防切机ID |
| machine_source | varchar |  | 机具来源，1-嘉联，0-客供，2-新国都商服，3-分公司 |
| ent_flag | varchar |  |  |
| assign_agent_batch_no | varchar |  |  |
| auth_no | varchar |  |  |
| suplier_no | varchar |  |  |
| suplier_name | varchar |  |  |
