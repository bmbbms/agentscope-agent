# ods_pay_trd.charge_t_fee_merch_rate (数据引入层-交易域-商户费率信息)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键 |
| merch_no | varchar |  | 商户号 |
| fee_type | varchar |  | 计费类型 |
| min_amount | decimal(22,0) |  | 最小金额，单位分 |
| max_amount | decimal(22,0) |  | 最大金额，单位分 |
| fee_bottom | decimal(22,0) |  | 保底手续费，单位分 |
| fee_top | decimal(22,0) |  | 封顶手续费，单位分 |
| rate | varchar |  | 费率 |
| fix_flag | varchar |  | 费率标识，0：固定费率，1：固定手续费 |
| step | decimal(22,0) |  | 阶梯手续费，单位分 |
| base_amount | decimal(22,0) |  | 阶梯基础金额，单位分 |
| base_fee | decimal(22,0) |  | 阶梯基础金额以下收费金额，单位分 |
| des | varchar |  | 费率描述 |
| start_time | varchar |  | 生效起始日期，为空表示不限制(yyyy-MM-dd HH:mm:ss.SSS) |
| end_time | varchar |  | 生效起始日期，为空表示不限制(yyyy-MM-dd HH:mm:ss.SSS) |
| create_time | varchar |  | 创建时间(yyyy-MM-dd HH:mm:ss.SSS) |
| update_time | varchar |  | 更新时间(yyyy-MM-dd HH:mm:ss.SSS) |
| create_name | varchar |  | 创建人员 |
| update_name | varchar |  | 更新人员 |
| status | varchar |  | 启用状态,1:启用,0:禁用 |
| meta_write_service | varchar |  | 数据写入服务 |
| meta_output_time | timestamp(3) |  | 数据写入时间(yyyy-MM-dd HH:mm:ss.SSS) |
| meta_is_delete | boolean |  | 源数据是否删除 true:删除, false:不删除 |
| meta_ori_table | varchar |  | 源数据表 |
