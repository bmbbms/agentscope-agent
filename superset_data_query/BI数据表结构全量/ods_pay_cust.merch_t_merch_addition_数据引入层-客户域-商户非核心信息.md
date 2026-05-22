# ods_pay_cust.merch_t_merch_addition (数据引入层-客户域-商户非核心信息)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_id | varchar |  | 商户ID |
| merch_no | varchar |  | 商户号 |
| simple_name | varchar |  | 商户经营名称 |
| mcc | varchar |  | MCC码 |
| settle_type | varchar |  | 清算方式 |
| hold_pay_flag | varchar |  | 暂不付标志 |
| hold_pay_reason | varchar |  | 暂不付原因 |
| protocol_version | varchar |  | 电子协议版本号 |
| face_flag | varchar |  | 人脸识别通过标志(0:初始，1:通过，2:不通过) |
| face_pic | varchar |  | 人脸识别照片 |
| match_percent | varchar |  | 人脸识别相似度 |
| fail_reasons | varchar |  | 人工审核失败原因(List对象) |
| flow_proc_id | varchar |  | 工作流流程编号 |
| busi_scope | varchar |  | 经营范围 |
| service_fee_id | varchar |  | 服务费ID |
| protocol_hash | varchar |  | 协议合同hash(用于判断是否修改协议数据) |
| service_mobile | varchar |  | 客服电话 |
| pwd_free | varchar |  | 免密免签:0.不免签不免密1.免签2.免签免密 |
| merch_data_flag | varchar |  | 商户资料标志：0.完整1.缺失2.失效3.初始 |
| merch_data_remark | varchar |  | 商户资料备注 |
| auth_collection | varchar |  | 是否允许授权收款0-禁止1-允许 |
| auth_remark | varchar |  | 是否允许授权收款备注 |
| reprot_bank_flag | varchar |  | 是否允许报备人行0-禁止1-允许 |
| reprot_bank_remark | varchar |  | 是否允许报备人行备注 |
| add_device_flag | varchar |  | 是否允许加机0否1是 |
| promise_version | varchar |  | 承诺函版本号 |
| area_no | varchar |  | 地区代码 |
| det_address | varchar |  | 详细地址 |
| addr_position | varchar |  | 地址位置信息(json串{"longitude":"经度","latitude":"纬度"}) |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
| client_unique_id | varchar |  | 客户唯一标识 |
