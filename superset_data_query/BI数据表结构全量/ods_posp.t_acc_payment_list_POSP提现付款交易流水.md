# ods_posp.t_accp_subject (会计科目表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| subject_code | varchar |  | 科目代码 |
| subject_name | varchar |  | 科目名称 |
| subject_type | varchar |  | 0-资产类；1-负债类；3-共同类；4-权益类；5-损益类；6-表外科目(保留) |
| subject_level | varchar |  | 科目级别 |
| balance_dir_flag | varchar |  | 余额方向 D-借方；C-贷方；B-轧差(按借方，允许未负数) |
| ccy_code | varchar |  | 货币代码 |
| acc_periodl | varchar |  | 会计分期，天为单位 |
| total_check_flag | varchar |  | 是否需要进行总分核对：Y-是；N-否 |
| red_acc_flag | varchar |  | 红账标志：0-非红账，1-红账 |
| channel_flag | varchar |  | 账户类型 1-备付金分户 2-渠道收单内部分户 3-渠道代付内部分户 4产品分户 |
| up_subject_code | varchar |  | 上级科目代码 |
| is_manual | varchar |  | 是否允许手工记账：0-不允许 1-允许 |
| is_minus | varchar |  | 是否允许值为负数: 0-否 1-是 |
| effective_date | varchar |  | 生效日期 |
| expired_date | varchar |  | 失效日期 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人员 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人员 |
| is_lead_node | varchar |  | 是否叶子节点，Y：叶子节点 N：不是叶子节点 |
| exter_flag | varchar |  | 是否关联外部户，Y-是，N-否 |
| sediment_flag | varchar |  | 属于沉淀资金Y-是N-否 |
