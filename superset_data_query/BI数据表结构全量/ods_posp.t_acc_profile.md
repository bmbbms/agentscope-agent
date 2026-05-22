# ods_posp.t_acc_profile ()

| Column | Type | Extra | Comment |
|---|---|---|---|
| vir_account_no | varchar |  | 虚拟账户号 |
| vir_account_name | varchar |  | 虚拟账户名称 |
| account_type | varchar |  | 帐户类型：1-个人账户；2-商户账户，３－内部账户 |
| org_code | varchar |  | 所属机构ID |
| ccy_code | varchar |  | 货币代码 |
| subject_code | varchar |  | 科目代码 |
| status | varchar |  | 账户状态 ：0-未激活 1-正常 2-冻结；9-已销户 |
| acc_list_flag | varchar |  | 名单标志：0-一般；1-灰名单；2-黑名单；3-红名单 |
| merch_no | varchar |  | 商户号 |
| property | varchar |  | 账户属性 1：与渠道不相关 2：与交易渠道相关 3：与清算渠道相关 4： 与商户相关 |
| operator | varchar |  | 操作员 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| remark | varchar |  | 备注 |
| settle_type | varchar |  | 清算方式（商户虚户使用）0-余额提现1-自动T+1清算 2-D0秒到 3-仅T+1清算 4-指定账户代付 |
| hold_pay_flag | varchar |  | 暂不付标志，1 暂不付，0 可以付 |
| is_master_acc | varchar |  | 是否子账户，ACCOUNT_TYPE为3 |
| product_type | varchar |  | 产品类型：1-POP+；2-MPOS |
