# ods_pay_cust.merch_t_merch_protocol (数据引入层-客户域-商户收单协议表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| protocol_id | varchar |  | 协议编号 |
| sign_id | varchar |  | 签约编号 |
| sign_mode | varchar |  | 签约模式(P-线下纸质协议,E-线上电子协议,L-签约承诺函,S-签名J-嘉联电子协议) |
| agreement_pic | varchar |  | 协议图片 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| remark | varchar |  | 备注 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
