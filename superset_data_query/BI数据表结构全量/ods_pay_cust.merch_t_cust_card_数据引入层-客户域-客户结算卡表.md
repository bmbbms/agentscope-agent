# ods_pay_cust.merch_t_cust_card (数据引入层-客户域-客户结算卡表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| cust_no | varchar |  | 客户号 |
| account_no | varchar |  | 结算账号 |
| account_type | varchar |  | 结算类型0-对私法人收款1-对公收款2-对私授权收款3-对公授权收款4-对公特殊账户收款 |
| account_name | varchar |  | 结算户名 |
| union_bank_name | varchar |  | 开户行名称 |
| union_bank_no | varchar |  | 开户行号 |
| account_pic | varchar |  | 结算照片 |
| merch_id | varchar |  | 商户协议ID，结算信息来源子商户 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| remark | varchar |  | 备注 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
