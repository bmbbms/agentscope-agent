# ods_pay_fin.fund_check_t_stat_trans_day (数据引入层-财务域-交易日统计)

| Column | Type | Extra | Comment |
|---|---|---|---|
| check_date | varchar |  | 对账时间 |
| chn_org_code | varchar |  | 渠道机构号 |
| in_responsibility | varchar |  | 入账责任方,通过自己划拨对账文件获取 |
| trans_type | varchar |  | 交易类型0-刷卡-1,-二维码 |
| trans_count | decimal(22,0) |  | 交易笔数 |
| trans_amt | decimal(22,0) |  | 交易金额 |
| recv_fee | decimal(22,0) |  | 应收手续费 |
| actual_recv_amt | decimal(22,0) |  | 实收手续费 |
| chn_fee | decimal(22,0) |  | 渠道手续费 |
| brand_serve_fee | decimal(22,0) |  | 品牌服务费 |
| fee_profit | decimal(22,0) |  | 手续费利润 |
| utime | varchar |  | 更新时间 |
| chn_org_code_name | varchar |  | 渠道机构名称 |
| chn_no | varchar |  | 渠道号 |
| chn_name | varchar |  | 渠道名称 |
| busi_type | varchar |  | 业务平台 |
| busi_type_name | varchar |  | 业务平台名称 |
| discount_fee | decimal(22,0) |  | 优惠金额 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
