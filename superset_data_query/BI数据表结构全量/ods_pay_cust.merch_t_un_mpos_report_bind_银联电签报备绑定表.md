# ods_pay_cust.merch_t_un_mpos_report_bind (银联电签报备绑定表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 子商户号 |
| term_no | varchar |  | 终端号 |
| device_sn | varchar |  | 机身号 |
| channel_merch_no | varchar |  | 渠道商户号 |
| shop_name | varchar |  | 渠道经营名称 |
| bind_status | varchar |  | 绑定状态0-未绑定1-已绑定2-绑定失败 |
| fail_reason | varchar |  | 失败原因 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 是否删除(false:否 是:true) |
| meta_output_time | varchar |  | 写入时间 |
| meta_ori_table | varchar |  | 原始表名 |
| bind_type | varchar |  | 绑定类型。1：管理后台人工绑定，2：电签升级企业类型营业执照 |
