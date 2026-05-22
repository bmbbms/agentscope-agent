# ods_pay_clear.clear_settle_t_clear_delayed_list (数据引入层-清算域-延迟清算流水表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  |  |
| merch_no | varchar |  | 商户号 |
| type | varchar |  | 类型1-止付（单笔）2-止付（商户）-冻结3-止付（商户）-暂不付 |
| expiry_time | varchar |  | 冻结截止日期 |
| free_order_id | varchar |  | 冻结订单号 |
| amount | decimal(22,0) |  | 冻结金额 |
| source | varchar |  | 来源risk-风险管理business-业务运营 |
| platcode | varchar |  |  |
| create_operator | varchar |  | 创建人 |
| update_operator | varchar |  | 修改人 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 修改时间 |
| status | varchar |  | 1-延迟中0:已解除 |
| create_remark | varchar |  | 冻结备注 |
| update_remark | varchar |  | 解除备注 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
