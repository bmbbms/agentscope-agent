# ods_pay_fin.charge_t_activity_fee_statistics (活动手续费汇总表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 汇总ID |
| activity_id | bigint |  | 活动ID |
| merch_no | varchar |  | 商户号 |
| fee_calc_type | varchar |  | 手续费计算类型 |
| begin_time | varchar |  |  |
| end_time | varchar |  |  |
| sum_derate_fee | varchar |  | 总优惠手续费分 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| derate_count | bigint |  | 累计减免次数 |
| body_type | varchar |  | 主体类型1活动2商户 |
| body_value | varchar |  | 主体值 |
| statistics_day | varchar |  | 统计日期yyyyMMdd |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 是否删除(false:否 是:true) |
| meta_output_time | varchar |  | 写入时间 |
| meta_ori_table | varchar |  | 原始表名 |
