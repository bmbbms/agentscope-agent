# ods_agent.t_stock_physn (机具库存表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| physn | varchar |  | 机身号 |
| status | varchar |  | 状态，此状态用于标识机具的状态，可能的状态有： 1：正常，2：报废，3：删除，4：撤机； |
| type | varchar |  | 机具类型  对应t_config表中的physn_type配置 |
| import_time | varchar |  | 导入时间，机具导入这个表的时间 |
| import_user | varchar |  | 导入人 |
| rate | varchar |  | 机具费率 |
| rate_update_user | varchar |  | 费率修改人 |
| rate_update_time | varchar |  | 费率修改时间 |
| min_price | varchar |  | 结算底价 |
| source | varchar |  | 机具来源，1=购买，2=激活赠送 3--存量入库 4--携机入库 |
| clerk | varchar |  | 业务员 |
| bind_status | varchar |  | 机具绑定状态 |
| bind_time | varchar |  | 绑定时间 |
| activate_status | varchar |  | 用户激活状态 |
| activate_time | varchar |  | 用户激活时间 |
| user_system_cid | varchar |  | 对应t_admusers的那个system_customer_id字段 |
| buy_machine_order_no | varchar |  | 购机订单号，用于营销周期的机具筛选 |
| user_id | varchar |  | 用户ID |
| parent_user_id | varchar |  | 上级代理商ID |
| root_user_id | varchar |  | 顶级代理商ID |
| glevel | varchar |  | 级别 |
| first_bind_time | varchar |  | 首次绑定商户时间，用于POS+机器服务费计算 |
| path | varchar |  | 代理商路径 |
| owner_ship | varchar |  | 产权归属 0-嘉联，1-新国都商服  |
| update_time | varchar |  | 更新时间 |
| model | varchar |  | 型号，用于特殊处理某些机器 |
