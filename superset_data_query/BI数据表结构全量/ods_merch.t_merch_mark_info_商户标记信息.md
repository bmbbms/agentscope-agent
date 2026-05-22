# ods_merch.t_merch_mark_info (商户标记信息)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| ic_mark | varchar |  | 工商信息标记 0.缺失 1 完整，2失效 |
| cert_man_mark | varchar |  | 法人信息标记 0.缺失 1 完整，2失效 |
| compliance_card_mark | varchar |  | 合规结算卡信息标记 0.缺失 1 完整，2失效 |
| master_card_mark | varchar |  | 主结算卡标记 0.缺失 1 完整，2失效 |
| protocol_atta_mark | varchar |  | 协议附件标记 0.缺失 1 完整，2失效 |
| business_atta_mark | varchar |  | 经营附件标记 0.缺失 1 完整，2失效 |
| benefit_man_mark | varchar |  | 受益人信息标记 0.缺失 1 完整，2失效 |
| control_man_mark | varchar |  | 实际控制人信息标记 0.缺失 1 完整，2失效 |
| ic_auth_mark | varchar |  | 四要素结果 0 失败 1 通过 2 未识别 |
| bank_auth_mark | varchar |  | 三要素结果0 失败 1 通过 2 未识别 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| remark | varchar |  | 备注 |
| audit_flag | varchar |  |  |
| evidence_mark | varchar |  | 辅助证明材料标记 0.缺失,1 完整，2失效 |
| auth_card_mark | varchar |  | 授权收款信息标记 0.缺失,1 完整，2失效 |
| face_mark | varchar |  | 人脸识别标记 0.不一致,1 一致 |
| need_rectify | varchar |  | 是否需要资料整改 1是 0否 |
| idcard_two_element_mark | varchar |  | 二要素标记。fail：失败、pass 通过、unidentified 未识别 |
| facticity_mark | varchar |  | 真实性标识。 unknown：未知、yes：是 |
| receipt_protocol_mark | varchar |  | 收单电子协议标记 |
| auth_protocol_mark | varchar |  | 授权电子协议标记 |
| coll_compliance_mark | varchar |  | 收款合规标记 |
| t0_compliance_mark | varchar |  | T0合规标记 |
| chain_merch_mark | varchar |  | 连锁商户标记 |
| fin_merch_mark | varchar |  | 理财商户 |
| account_splitting_mark | varchar |  | 分账商户标记 |
| union_stage_code_mark | varchar |  | 银联分期码商户标记 |
| union_direct_mark | varchar |  | 银联直联商户标记 |
| provide_info_mark | varchar |  | 对外提供资料标记 |
