# xacc.t_master_trans (万事达交易表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| msg_type | varchar |  | 报文类型指示符 |
| trans_time | varchar |  | 交易时间 |
| req_time | varchar |  | 交易时间 |
| amount | varchar |  | 交易金额 |
| f42 | varchar |  | 渠道商户号 |
| term_no | varchar |  | 渠道终端号 |
| mcc | varchar |  | 商户类型 |
| account_no | varchar |  | 卡号 |
| account_len | varchar |  | 卡号长度 |
| refere_code | varchar |  | 参考号 |
| track_code | varchar |  | 跟踪号 |
| input_mode | varchar |  | POS 输入模式 |
| auth_code | varchar |  | 授权码 |
| brand | varchar |  | 账户类型 |
| send_org_code | varchar |  | 发送方机构码 |
| acq_refer_data | varchar |  | 收单方参考数据 |
| present_file_id | varchar |  | 请款文件id |
| busi_activity | varchar |  | Business Activity |
| handle_code | varchar |  | 处理码 |
| fun_code | varchar |  | 功能码 |
| err_amt | varchar |  | 交易金额DE4 |
| check_amt | varchar |  | 对账金额DE5 |
| ori_trans_amt | varchar |  | 原交易金额DE30的1-12 |
| ori_check_amt | varchar |  | 原对账金额 |
| transaction_id | varchar |  | 事务id |
| notify_code | varchar |  | 原因码 |
| ori_sett_date | varchar |  | 原清算日期 |
| trans_curr | varchar |  | 交易币种 |
| check_curr | varchar |  | 对账币种 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| reversal | varchar |  | 报文冲正指示符 |
| rowkey | varchar |  | rowkey |
| chn_org_code | varchar |  | 渠道机构号 |
| exchange_fee | varchar |  | 交换费 |
| debit_credit_flag | varchar |  | 借贷记 |
| recv_amount | varchar |  | 应到账 |
| chn_pdg | varchar |  | 渠道手续费 |
| lorder_id | varchar |  | 左端订单号 |
| lmer_name | varchar |  | 左端商户名 |
| lmer_fee | varchar |  | 左端商户手续费 |
| lmer_no | varchar |  | 左端商户号 |
| lterm_no | varchar |  | 左端终端号 |
| vef_date | varchar |  | 到账日期 |
| dt | integer | partition key |  |
