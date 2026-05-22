# base_info.t_r_terminal (右端终端表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| rterm_no | varchar |  | 右端终端号 |
| rmer_no | varchar |  | 右端商户号 |
| channel | varchar |  | 归属渠道 |
| channel_name | varchar |  | 渠道名称 |
| rsn | varchar |  | 右端序列号 |
| rdev_sn | varchar |  | 右端机身号(深银联要求) |
| term_pool_type | varchar |  | 终端管理池类型 |
| term_route_flag | varchar |  | 合规终端是否路由 |
| start_time | varchar |  | 允许交易的起始时间 |
| end_time | varchar |  | 允许交易的结束时间 |
| min_amt | varchar |  | 允许交易最小金额 |
| max_amt | varchar |  | 允许交易最大金额 |
| cap_amt | varchar |  | 封顶交易金额 |
| status | varchar |  | 终端状态(1:启用 2:停用 3:注销) |
| limit | varchar |  | 免签免密额度(数据库默认0) |
| pwdfree | varchar |  | 免密标识01免密?00不免密?(数据库默认00) |
| rdev_type | varchar |  | 终端设备类型(01:ATM,02:传统POS,03:MPOS,04:智能POS,05:II型固定电话POS) |
| remark | varchar |  | 备注信息 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| is_allot | varchar |  | 是否调拨专用,0-否，1-是 |
| is_new | varchar |  | 是否存量(Y:存量,N:新增) |
| u_user | varchar |  | 修改人 |
| is_export | varchar |  | 导出状态 1已导出 0未导出 |
| report_time | varchar |  | 应上报时间 |
| report_flag | varchar |  | 自动上报操作标志，1-新增2-修改3-删除 |
| auto_flag | varchar |  | 自动报备标志，0：否，1：是 |
| region_code | varchar |  | 区域 |
| region_name | varchar |  | 区域名 |
| rmer_name | varchar |  | 商户名称 |
| product_type | varchar |  | 产品类型(1-POP+；2-MPOS) |
| model | varchar |  | 终端机具型号 |
