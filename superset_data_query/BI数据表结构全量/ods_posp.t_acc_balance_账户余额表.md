# ods_posp.t_accp_profile (会计内部户和内部分户信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| vir_account_no | varchar |  | 虚拟账户号 |
| vir_account_name | varchar |  | 虚拟账户名称 |
| account_type | varchar |  | 账户类型 0-会计内部户 1-备付金分账 2-渠道收单内部分户 3-渠道代付内部分户 4-产品分户 5-中间户 |
| org_code | varchar |  | 所属机构ID |
| ccy_code | varchar |  | 货币代码 |
| subject_code | varchar |  | 科目代码 |
| account_no | varchar |  | 备付金账号 账务类型为1不能为空 |
| channel_no | varchar |  | 渠道编号  账务类型为2和3不能为空 |
| product_no | varchar |  | 产品编号  这里和业务大类关联=BUSI_TYPE 账务类型为4时不能为空 |
| status | varchar |  | 账户状态 ：0-未激活 1-正常 2-冻结；9-已销户 |
| acc_list_flag | varchar |  | 名单标志：0-一般；1-灰名单；2-黑名单；3-红名单 |
| operator | varchar |  | 操作员 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| remarks | varchar |  | 备注 |
