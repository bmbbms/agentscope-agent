# xacc.t_every_trans (万事网联)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| chn_org_code | varchar |  | 渠道机构号 |
| msg_type | varchar |  | 报文类型指示符 |
| refer_no | varchar |  | 系统参考号 |
| org_code | varchar |  | 处理机构——收单机构或发卡机构 |
| org_id | varchar |  | 处理机构 ID |
| trans_time | varchar |  | 交易时间 |
| account_len | varchar |  | 主账号长度 |
| account_no | varchar |  | 主账号 |
| handle_code | varchar |  | 处理代码 |
| track_no | varchar |  | 系统审核跟踪号 |
| mcc | varchar |  | 商户类型 |
| input_mode | varchar |  | POS 输入模式 |
| refere_code | varchar |  | 参考编号 |
| sett_org_code | varchar |  | 收单机构识别码 |
| term_no | varchar |  | 终端号 |
| auth_ret_code | varchar |  | 授权响应码 |
| brand | varchar |  | 品牌 |
| notify_code | varchar |  | 通知原因码 |
| currency | varchar |  | 币种内协议码 |
| auth_code | varchar |  | 授权码 |
| currency_code | varchar |  | 币种代码-交易币种 |
| currency_str | varchar |  | 隐含小数位数-交易币种 |
| amount | varchar |  | 交易完成金额-交易币种 |
| debit_credit_flag | varchar |  | 借贷记 |
| back_amt | varchar |  | Cash Back 金额-交易币种 |
| pdg | varchar |  | 手续费——交易币种 |
| settle_currency | varchar |  | 币种代码-清算币种 |
| settle_currency_str | varchar |  | 隐含小数位数-清算币种 |
| currency_rate | varchar |  | 货币转换率-清算-货币换算目前不适用于中国境内-该字段取值代表的含义为 1 |
| trans_amt | varchar |  | 交易完成金额-清算币种 |
| exchange_fee | varchar |  | 交换费 |
| indicate | varchar |  | 服务水平指示符 |
| ret_code | varchar |  | 响应码 |
| fill | varchar |  | 填充符 |
| indicate_id | varchar |  | 有效 ID 指示符 |
| atm_id | varchar |  | 无 ATM 附加费计划 ID |
| cross_border | varchar |  | 跨境指示符 |
| cross_border_cur | varchar |  | 跨境币种指示符 |
| visa_fee | varchar |  | Visa 国际服务评估费（ ISA）指示符 |
| trans_req_currency | varchar |  | 交易请求金额-交易币种 |
| fill_one | varchar |  | 填充符 |
| track_code | varchar |  | 跟踪号-调整交易 |
| handle_org | varchar |  | 处理机构 ICA |
| req_time | varchar |  | 传输日期与时间 |
| fill_two | varchar |  |  |
| err_amt | varchar |  | 交易替换金额 |
| err_sett_amt | varchar |  | 交易替换清算金额 |
| ori_sett_date | varchar |  | 原始清算日期 |
| err_refer_no | varchar |  | 争议参考号 |
| arbitrate_id | varchar |  | 仲裁个案 ID |
| reversal | varchar |  | 报文冲正指示符 |
| fill_three | varchar |  | 填充符 |
| recv_amount | varchar |  | 应到账金额 |
| chn_pdg | varchar |  | 渠道手续费 |
| lorder_id | varchar |  | 左端订单号 |
| lmer_no | varchar |  | 左端商户号 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| lmer_name | varchar |  | 左端商户名 |
| lterm_no | varchar |  | 左端终端号 |
| lmer_fee | varchar |  | 左端商户手续费 |
| ctime | varchar |  | 对账时间yyyyMMddHHmmss |
| net_service_fee | varchar |  | 网络服务费 |
| f42 | varchar |  | 右端商户号 |
| merch_en_name | varchar |  | 商户英文名 |
| merch_zh_name | varchar |  | 商户中文名 |
| region_code | varchar |  | 地区代码 |
| dt | integer | partition key |  |
