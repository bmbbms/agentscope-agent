# base_info.t_r_merchant (右端商户表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| rmer_no | varchar |  | 右端商户号 |
| rmer_name | varchar |  | 右端商户名 |
| status | varchar |  | 商户状态(1:启用 2:停用 3:已注销) |
| cup_oprstate | varchar |  | 渠道审核状态 |
| charge_type | varchar |  | 特殊计费类型 |
| charge_class | varchar |  | 特殊计费档次 |
| outflag | varchar |  | EDC/DCC标识(00002001 EDC 00002002 DCC) |
| merproper | varchar |  | 渠道机构代码(受理机构代码) |
| rmer_name_en | varchar |  | 英文名称 |
| std_fee | varchar |  | 商户类别(0:标准类/其他 1:优惠类 2:特计类 3:减免类) |
| fee_pkgs | varchar |  | 计费套餐编号(可存多个逗号分隔) |
| channel | varchar |  | 渠道编号 |
| channel_name | varchar |  | 渠道名称 |
| mcc | varchar |  | 商户类型(code) |
| mcctype | varchar |  | 商户类型 0401政府服务 0402铁路客运 0403公共交通 0404公共事业缴费 0405保险 0406农资收购 0501:信用卡还款 0502:助农取款 |
| region_code | varchar |  | 四位行政地区编码 |
| region_name | varchar |  | 区域名称 |
| region_code_bak | varchar |  | 四位行政地区编码备份 20180801-20181029 |
| chn_type | varchar |  | 渠道类型，1:间联 2:直连 |
| create_time | varchar |  | 创建时间(启用时间/添加时间) |
| update_time | varchar |  | 更新时间(停用时间) |
| report_time | varchar |  | 应上报时间(报备时间) |
| auto_flag | varchar |  | 自动报备标志 |
| buss_address | varchar |  | 商户经营地址 |
| register_address | varchar |  | 商户注册地址 |
| post_address | varchar |  | 商户通讯地址 |
| fixation_rount | varchar |  | 是否固定路由(0:否,1:是) |
| dynamic_rount | varchar |  | 是否动态路由(0:否,1:是) |
| data_from | varchar |  | 数据来源,已不存值 |
| product_type | varchar |  | 产品类型(1-POP+；2-MPOS) |
| channel_operate_name | varchar |  | 渠道经营名称 |
| en_merch_name | varchar |  | 商户英文名称 |
| left_merch_no | varchar |  | 左端商户号 |
| change_status_time | varchar |  | 商户状态变更时间 |
| cust_no | varchar |  | 客户号 |
