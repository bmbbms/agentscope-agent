# ods_pay_risk.measure_t_delay_merch (数据引入层-信用&风控域-延迟处置商户表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| merch_name | varchar |  | 商户名称 |
| product | varchar |  | 产品类型, |
| delay_status | varchar |  | 延迟状态，0-延迟中，1-已解除 |
| delay_measure_keys | varchar |  | 延迟措施列表 |
| delay_amount | bigint |  | 延迟处置金额 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 修改时间 |
| delay_measure_sources | varchar |  |  |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
