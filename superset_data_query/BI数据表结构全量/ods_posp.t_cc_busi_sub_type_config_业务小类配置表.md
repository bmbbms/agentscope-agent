# ods_posp.t_cc_busi_sub_type_config (业务小类配置表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| busi_sub_type | varchar |  | 业务小类 |
| busi_sub_type_name | varchar |  | 业务小类名称 |
| message_type | varchar |  | 报文类型：0域 |
| trans_code | varchar |  | 交易类型码：3域 |
| service_code | varchar |  | 服务点条件码：25域 |
| is_reversal | varchar |  | 是否是冲正类的交易 N ：否， Y ：是 O 其他 |
| debit_credit_flag | varchar |  | 借贷方向D -1 C 1  消费 ：C  退货：D |
| is_check_account | varchar |  | 是否对账 Y 对账，N：不对账 |
| is_qrcode | varchar |  | 是否二维码Y 是，N 不是 |
| busi_sub_type_key | varchar |  | 业务小类key-用于代码映射key |
| operation_name | varchar |  |  |
| operation_time | varchar |  |  |
