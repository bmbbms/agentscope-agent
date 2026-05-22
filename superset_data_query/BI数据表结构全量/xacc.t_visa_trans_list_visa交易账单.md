# xacc.t_visa_trans_list (visa交易账单)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| acq_id | varchar |  | 收单机构ID |
| acq_name | varchar |  | 收单机构名称 |
| psp_id | varchar |  | 支付pspid |
| psp_name | varchar |  | 支付psp名称 |
| group_id | varchar |  | 集团号 |
| group_name | varchar |  | 集团名称 |
| mer_id | varchar |  | 商户号 |
| mer_name | varchar |  | 商户名称 |
| store_id | varchar |  | 门店号 |
| store_name | varchar |  | 门店名称 |
| store_mcc | varchar |  | 门店MCC |
| term_id | varchar |  | 终端号 |
| mer_nation | varchar |  | 商户国家 |
| mer_city | varchar |  | 商户城市 |
| mer_txn_time | varchar |  | 商户交易时间 |
| system_txn_time | varchar |  | 讯联系统交易时间 |
| txn_pay_time | varchar |  | psp交易时间 |
| api_type | varchar |  | API类别 |
| txn_type | varchar |  | 交易类型 |
| pay_brand | varchar |  | 支付品牌 |
| pay_method | varchar |  | 付款方式 |
| mer_txn_id | varchar |  | 商户交易号 |
| mer_order_refer | varchar |  | 商户订单参考信息 |
| system_txn_id | varchar |  | 讯联交易号 |
| psp_txn_id | varchar |  | psp交易号 |
| ori_mer_txn_id | varchar |  | 原交易商户交易号 |
| ori_system_txn_id | varchar |  | 原讯联交易号 |
| ori_psp_txn_id | varchar |  | 原交易psp交易号 |
| card_number | varchar |  | 卡号 |
| acc_sett_type | varchar |  | 卡借贷记标识 |
| product_id | varchar |  | 卡产品标识 |
| product_type_id | varchar |  | 卡类别标识 |
| issuer_country | varchar |  | 发卡国家 |
| mer_local_amt | varchar |  | 商户本地金额 |
| local_tips_amt | varchar |  | 小费本地金额 |
| local_surcharge_fee | varchar |  | 额外服务费本地金额 |
| local_capture_amt | varchar |  | 商户确认本地金额 |
| mer_local_curr | varchar |  | 商户本地币种 |
| rate_of_local_to_txn | varchar |  | MCP/DCC汇率 |
| mer_txn_amt | varchar |  | 商户交易金额 |
| tips_amount | varchar |  | 小费交易金额 |
| extra_fee_amt | varchar |  | 额外服务费金额 |
| mer_capture_amt | varchar |  | 商户确认金额 |
| mer_txn_curr | varchar |  | 商户交易币种 |
| user_bill_amt | varchar |  | 用户扣账金额 |
| user_bill_curr | varchar |  | 用户扣账币种 |
| eci | varchar |  | 认证标识 |
| txn_init_mode | varchar |  | 交易发起方式 |
| linkpay_order_id | varchar |  | LinkPay订单号 |
| txn_status | varchar |  | 讯联系统交易状态 |
| system_ret_code | varchar |  | 讯联返回应答码 |
| psp_ret_code | varchar |  | PSP渠道应答码 |
| psp_auth_code | varchar |  | PSP渠道授权码 |
| cross_border_flag | varchar |  | 跨区标识 |
| trans_discount_ind | varchar |  | 交易优惠标识  |
| psp_arn | varchar |  | 双信息请款清算号 |
| psp_settle_date | varchar |  | PSP清算日期  |
| psp_txn_amt | varchar |  | PSP交易金额 |
| psp_txn_curr | varchar |  | PSP交易币种  |
| direct_fx_rate | varchar |  | PSP交易汇率 |
| psp_sttl_amt | varchar |  | PSP清算金额 |
| psp_discount_amt | varchar |  | PSP优惠金额 |
| acq_discount_amt | varchar |  | PSP商户优惠金额  |
| psp_sttl_curr | varchar |  | PSP清算币种 |
| psp_txn_settle_rate | varchar |  | PSP清算汇率  |
| psp_exchange_fee | varchar |  | PSP IC手续费  |
| psp_vat_amount | varchar |  | PSP 增值税费 |
| psp_wht_amount | varchar |  | PSP 预扣税费 |
| psp_net_settle_amt | varchar |  | PSP清算净金额 |
| recv_amount | varchar |  | 应到账金额 |
| chn_pdg | varchar |  | 渠道手续费 |
| chn_org_code | varchar |  | 机构号 |
| file_name | varchar |  | 文件名 |
| file_type | varchar |  | 文件类型 |
| ctime | varchar |  | 清算日期 |
| dt | integer | partition key |  |
