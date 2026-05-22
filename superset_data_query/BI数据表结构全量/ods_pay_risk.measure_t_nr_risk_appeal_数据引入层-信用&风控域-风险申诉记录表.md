# ods_pay_risk.measure_t_nr_risk_appeal (数据引入层-信用&风控域-风险申诉记录表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | ID |
| merch_no | varchar |  | 商户号 |
| risk_info_id | varchar |  | 风险信息id |
| complete_auth_keys | varchar |  | 完成的申诉要素 |
| appeal_name | varchar |  | 申诉人 |
| phone_number | varchar |  | 申诉手机号 |
| face_score | decimal(6,2) |  | 人脸分数 |
| reason | varchar |  | 申诉理由 |
| verify_reason | varchar |  | 审核原因 |
| status | varchar |  | 申诉状态（00初始，01待审核，02申诉成功，03申诉失败） |
| create_time | varchar |  | 创建时间 |
| remark | varchar |  | 备注 |
| update_time | varchar |  | 更新时间 |
| create_user | varchar |  | 创建人 |
| update_user | varchar |  | 更新人 |
| longitude | double |  | 经度 |
| latitude | double |  | 维度 |
| proc_id | varchar |  | 工作流编号 |
| live_score | decimal(6,2) |  | 活体检测分数 |
| address | varchar |  | 申诉地址 |
| holder_card_no | varchar |  | 持卡人卡号 |
| holder_cert_no | varchar |  | 持卡人证件号 |
| source | varchar |  | 来源：00-商户；01-客服 |
| cur_measure | varchar |  | 当前处置措施 |
| rec_measure | varchar |  | 恢复措施 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
