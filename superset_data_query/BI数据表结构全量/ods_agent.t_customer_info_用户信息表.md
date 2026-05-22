# ods_agent.t_customer_info (用户信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| business_type | varchar |  | 业务类型，用户激活状态跟业务走，同一用户同一业务激活一次 1表示立刷 3=posp  4=立刷商户版 |
| system_customer_id | varchar |  | 交易系统客户号 |
| system_merchno | varchar |  | 交易系统商户号 |
| system_phone | varchar |  | 手机号 |
| system_name | varchar |  | 姓名 |
| activate_status | varchar |  | 激活状态 |
| activate_time | varchar |  | 激活时间 |
| reg_time | varchar |  | 注册时间 |
| auth_time | varchar |  | 认证时间 |
| last_trade_time | varchar |  | 上次交易时间 |
| this_month_amount | varchar |  | 本月交易额 |
| this_month_count | varchar |  | 本月交易笔数 |
| last_month_amount | varchar |  | 最近一个月交易额 |
| last_month_count | varchar |  | 最近一个月交易笔数 |
| all_amount | varchar |  | 交易总金额 |
| all_count | varchar |  | 交易总笔数 |
| user_id | varchar |  | 代理商ID，对应t_admusers表中的user_id |
| activate_cardno | varchar |  | 激活卡号 |
| reg_physn_type | varchar |  | 入网机具类型，同步t_stock_physn表中的机具类型，目前用于标识是否有提现分润 |
| create_time | varchar |  | 插入时间 |
| mer_type | varchar |  | 商户类型，仅pos+有效(1=非标，其它=标准) |
| path | varchar |  | 代理商归属路径 |
| developer_id | varchar |  | 发展者ID |
| activate_amount | varchar |  | 激活金额 |
| tag | varchar |  | 标签 |
| disable_act | varchar |  | 是否可以激活 1--不可激活 |
| update_time | varchar |  | 更新时间 |
| standard_amount | varchar |  | 交易达标总金额 |
| net_type | varchar |  | 入网类型，1-营业执照，3=小微 |
| short_name | varchar |  | 商户简称 |
| group_id | varchar |  | 集团编号 |
| clique_customer_id | varchar |  | 集团客户号 |
| product_type | varchar |  | 产品类型 |
| meta_write_service | varchar |  | 数据写入服务 |
| meta_output_time | varchar |  | 数据写入时间 |
| meta_ori_table | varchar |  | 源数据表 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
