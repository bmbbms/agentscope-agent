# dws_pay_trd.merch_ord_1d (轻度汇总层--交易域--商户订单流水日统计)

| Column | Type | Extra | Comment |
|---|---|---|---|
| meta_write_service | varchar |  | 写入服务 |
| meta_output_time | varchar |  | 数据更新时间yyyy-MM-dd HH:mm:ss |
| merch_no | varchar |  | 商户号 |
| product | varchar |  | 产品类型（posp-大POS mpos-小POS） |
| ord_cnt_1d | bigint |  | 近1天交易笔数 |
| ord_amt_1d | bigint |  | 近1天交易金额 |
| ord_cnt_1d_suc | bigint |  | 近1天成功交易笔数 |
| ord_amt_1d_suc | bigint |  | 近1天成功交易金额 |
| ord_cnt_1d_qr | bigint |  | 近1天码付交易笔数 |
| ord_amt_1d_qr | bigint |  | 近1天码付交易金额 |
| ord_cnt_1d_qr_suc | bigint |  | 近1天码付成功交易笔数 |
| ord_amt_1d_qr_suc | bigint |  | 近1天码付成功交易金额 |
| ord_cnt_1d_qr_c2b | bigint |  | 近1天码付主扫交易笔数 |
| ord_amt_1d_qr_c2b | bigint |  | 近1天码付主扫交易金额 |
| ord_cnt_1d_qr_c2b_suc | bigint |  | 近1天码付主扫成功交易笔数 |
| ord_amt_1d_qr_c2b_suc | bigint |  | 近1天码付主扫成功交易金额 |
| ord_cnt_1d_qr_b2c | bigint |  | 近1天码付被扫交易笔数 |
| ord_amt_1d_qr_b2c | bigint |  | 近1天码付被扫交易金额 |
| ord_cnt_1d_qr_b2c_suc | bigint |  | 近1天码付被扫成功交易笔数 |
| ord_amt_1d_qr_b2c_suc | bigint |  | 近1天码付被扫成功交易金额 |
| ord_cnt_1d_qr_dr | bigint |  | 近1天码付借记卡交易笔数 |
| ord_amt_1d_qr_dr | bigint |  | 近1天码付借记卡交易金额 |
| ord_cnt_1d_qr_dr_suc | bigint |  | 近1天码付借记卡成功交易笔数 |
| ord_amt_1d_qr_dr_suc | bigint |  | 近1天码付借记卡成功交易金额 |
| ord_cnt_1d_qr_cr | bigint |  | 近1天码付贷记卡交易笔数 |
| ord_amt_1d_qr_cr | bigint |  | 近1天码付贷记卡交易金额 |
| ord_cnt_1d_qr_cr_suc | bigint |  | 近1天码付贷记卡成功交易笔数 |
| ord_amt_1d_qr_cr_suc | bigint |  | 近1天码付贷记卡成功交易金额 |
| ord_cnt_1d_qr_bal | bigint |  | 近1天码付余额交易笔数 |
| ord_amt_1d_qr_bal | bigint |  | 近1天码付余额交易金额 |
| ord_cnt_1d_qr_bal_suc | bigint |  | 近1天码付余额成功交易笔数 |
| ord_amt_1d_qr_bal_suc | bigint |  | 近1天码付余额成功交易金额 |
| ord_cnt_1d_wxpay | bigint |  | 近1天微信支付交易笔数 |
| ord_amt_1d_wxpay | bigint |  | 近1天微信支付交易金额 |
| ord_cnt_1d_wxpay_suc | bigint |  | 近1天微信支付成功交易笔数 |
| ord_amt_1d_wxpay_suc | bigint |  | 近1天微信支付成功交易金额 |
| ord_cnt_1d_alipay | bigint |  | 近1天支付宝交易笔数 |
| ord_amt_1d_alipay | bigint |  | 近1天支付宝交易金额 |
| ord_cnt_1d_alipay_suc | bigint |  | 近1天支付宝成功交易笔数 |
| ord_amt_1d_alipay_suc | bigint |  | 近1天支付宝成功交易金额 |
| ord_cnt_1d_unionpay | bigint |  | 近1天银联二维码交易笔数 |
| ord_amt_1d_unionpay | bigint |  | 近1天银联二维码交易金额 |
| ord_cnt_1d_unionpay_suc | bigint |  | 近1天银联二维码成功交易笔数 |
| ord_amt_1d_unionpay_suc | bigint |  | 近1天银联二维码成功交易金额 |
| ord_cnt_1d_qr_amt_m10 | bigint |  | 近1天金额为10元整倍数的码付交易笔数 |
| ord_amt_1d_qr_amt_m10 | bigint |  | 近1天金额为10元整倍数的码付交易金额 |
| ord_cnt_1d_qr_amt_m10_suc | bigint |  | 近1天金额为10元整倍数的码付成功交易笔数 |
| ord_amt_1d_qr_amt_m10_suc | bigint |  | 近1天金额为10元整倍数的码付成功交易金额 |
| ord_cnt_1d_qr_amt_ge1w | bigint |  | 近1天金额>=1w元的码付交易笔数 |
| ord_amt_1d_qr_amt_ge1w | bigint |  | 近1天金额>=1w元的码付交易金额 |
| ord_cnt_1d_qr_amt_ge1w_suc | bigint |  | 近1天金额>=1w元的码付成功交易笔数 |
| ord_amt_1d_qr_amt_ge1w_suc | bigint |  | 近1天金额>=1w元的码付成功交易金额 |
| ord_cnt_1d_qr_amt_ge100_amt_m100_d5 | bigint |  | 近1天金额>=100元且是100元的整倍数误差5元以内的码付交易笔数 |
| ord_amt_1d_qr_amt_ge100_amt_m100_d5 | bigint |  | 近1天金额>=100元且是100元的整倍数误差5元以内的码付交易金额 |
| ord_cnt_1d_qr_amt_ge100_amt_m100_d5_suc | bigint |  | 近1天金额>=100元且是100元的整倍数误差5元以内的码付成功交易笔数 |
| ord_amt_1d_qr_amt_ge100_amt_m100_d5_suc | bigint |  | 近1天金额>=100元且是100元的整倍数误差5元以内的码付成功交易金额 |
| ord_cnt_1d_qr_amt_not_int | bigint |  | 近1天金额非整数的码付交易笔数 |
| ord_amt_1d_qr_amt_not_int | bigint |  | 近1天金额非整数的码付交易金额 |
| ord_cnt_1d_qr_amt_not_int_suc | bigint |  | 近1天金额非整数的码付成功交易笔数 |
| ord_amt_1d_qr_amt_not_int_suc | bigint |  | 近1天金额非整数的码付成功交易金额 |
| ord_card_num_1d_qr | bigint |  | 近1天码付交易openid去重数 |
| ord_card_num_1d_qr_suc | bigint |  | 近1天码付成功交易openid去重数 |
| ord_cnt_1d_qr_hour_1to5 | bigint |  | 近1天交易时间在[1:00, 5:00)的码付交易笔数 |
| ord_amt_1d_qr_hour_1to5 | bigint |  | 近1天交易时间在[1:00, 5:00)的码付交易金额 |
| ord_cnt_1d_qr_hour_1to5_suc | bigint |  | 近1天交易时间在[1:00, 5:00)的码付成功交易笔数 |
| ord_amt_1d_qr_hour_1to5_suc | bigint |  | 近1天交易时间在[1:00, 5:00)的码付成功交易金额 |
| ord_cnt_1d_qr_hour_0to6 | bigint |  | 近1天交易时间在[0:00, 6:00)的码付交易笔数 |
| ord_amt_1d_qr_hour_0to6 | bigint |  | 近1天交易时间在[0:00, 6:00)的码付交易金额 |
| ord_cnt_1d_qr_hour_0to6_suc | bigint |  | 近1天交易时间在[0:00, 6:00)的码付成功交易笔数 |
| ord_amt_1d_qr_hour_0to6_suc | bigint |  | 近1天交易时间在[0:00, 6:00)的码付成功交易金额 |
| ord_cnt_1d_qr_hour_6to9 | bigint |  | 近1天交易时间在[6:00, 9:00)的码付交易笔数 |
| ord_amt_1d_qr_hour_6to9 | bigint |  | 近1天交易时间在[6:00, 9:00)的码付交易金额 |
| ord_cnt_1d_qr_hour_6to9_suc | bigint |  | 近1天交易时间在[6:00, 9:00)的码付成功交易笔数 |
| ord_amt_1d_qr_hour_6to9_suc | bigint |  | 近1天交易时间在[6:00, 9:00)的码付成功交易金额 |
| ord_cnt_1d_qr_hour_9to11 | bigint |  | 近1天交易时间在[9:00, 11:00)的码付交易笔数 |
| ord_amt_1d_qr_hour_9to11 | bigint |  | 近1天交易时间在[9:00, 11:00)的码付交易金额 |
| ord_cnt_1d_qr_hour_9to11_suc | bigint |  | 近1天交易时间在[9:00, 11:00)的码付成功交易笔数 |
| ord_amt_1d_qr_hour_9to11_suc | bigint |  | 近1天交易时间在[9:00, 11:00)的码付成功交易金额 |
| ord_cnt_1d_qr_hour_11to13 | bigint |  | 近1天交易时间在[11:00, 13:00)的码付交易笔数 |
| ord_amt_1d_qr_hour_11to13 | bigint |  | 近1天交易时间在[11:00, 13:00)的码付交易金额 |
| ord_cnt_1d_qr_hour_11to13_suc | bigint |  | 近1天交易时间在[11:00, 13:00)的码付成功交易笔数 |
| ord_amt_1d_qr_hour_11to13_suc | bigint |  | 近1天交易时间在[11:00, 13:00)的码付成功交易金额 |
| ord_cnt_1d_qr_hour_13to16 | bigint |  | 近1天交易时间在[13:00, 16:00)的码付交易笔数 |
| ord_amt_1d_qr_hour_13to16 | bigint |  | 近1天交易时间在[13:00, 16:00)的码付交易金额 |
| ord_cnt_1d_qr_hour_13to16_suc | bigint |  | 近1天交易时间在[13:00, 16:00)的码付成功交易笔数 |
| ord_amt_1d_qr_hour_13to16_suc | bigint |  | 近1天交易时间在[13:00, 16:00)的码付成功交易金额 |
| ord_cnt_1d_qr_hour_16to20 | bigint |  | 近1天交易时间在[16:00, 20:00)的码付交易笔数 |
| ord_amt_1d_qr_hour_16to20 | bigint |  | 近1天交易时间在[16:00, 20:00)的码付交易金额 |
| ord_cnt_1d_qr_hour_16to20_suc | bigint |  | 近1天交易时间在[16:00, 20:00)的码付成功交易笔数 |
| ord_amt_1d_qr_hour_16to20_suc | bigint |  | 近1天交易时间在[16:00, 20:00)的码付成功交易金额 |
| ord_cnt_1d_qr_hour_20to0 | bigint |  | 近1天交易时间在[20:00, 0:00)的码付交易笔数 |
| ord_amt_1d_qr_hour_20to0 | bigint |  | 近1天交易时间在[20:00, 0:00)的码付交易金额 |
| ord_cnt_1d_qr_hour_20to0_suc | bigint |  | 近1天交易时间在[20:00, 0:00)的码付成功交易笔数 |
| ord_amt_1d_qr_hour_20to0_suc | bigint |  | 近1天交易时间在[20:00, 0:00)的码付成功交易金额 |
| ord_cnt_1d_qr_hour_dine | bigint |  | 近1天交易时间在饭点的码付交易笔数 |
| ord_amt_1d_qr_hour_dine | bigint |  | 近1天交易时间在饭点的码付交易金额 |
| ord_cnt_1d_qr_hour_dine_suc | bigint |  | 近1天交易时间在饭点的码付成功交易笔数 |
| ord_amt_1d_qr_hour_dine_suc | bigint |  | 近1天交易时间在饭点的码付成功交易金额 |
| trd_hours_1d | bigint |  | 近1天交易小时数 |
| trd_hours_1d_suc | bigint |  | 近1天成功交易小时数 |
| ord_cnt_1d_qr_amt_ge100_amt_m50 | bigint |  | 近1天金额>=100元且为50元整倍数的码付交易笔数 |
| ord_amt_1d_qr_amt_ge100_amt_m50 | bigint |  | 近1天金额>=100元且为50元整倍数的码付交易金额 |
| ord_cnt_1d_qr_amt_ge100_amt_m50_suc | bigint |  | 近1天金额>=100元且为50元整倍数的码付成功交易笔数 |
| ord_amt_1d_qr_amt_ge100_amt_m50_suc | bigint |  | 近1天金额>=100元且为50元整倍数的码付成功交易金额 |
| ord_amt_num_1d | bigint |  | 近1天交易金额去重数 |
| ord_amt_num_1d_suc | bigint |  | 近1天成功交易金额去重数 |
| ord_cnt_1d_amt_not_int | bigint |  | 近1天金额非整数的交易笔数 |
| ord_amt_1d_amt_not_int | bigint |  | 近1天金额非整数的交易金额 |
| ord_cnt_1d_amt_not_int_suc | bigint |  | 近1天金额非整数的成功交易笔数 |
| ord_amt_1d_amt_not_int_suc | bigint |  | 近1天金额非整数的成功交易金额 |
| ord_cnt_1d_amt_to_penny | bigint |  | 近1天金额非整数且精确到分的交易笔数 |
| ord_amt_1d_amt_to_penny | bigint |  | 近1天金额非整数且精确到分的交易金额 |
| ord_cnt_1d_amt_to_penny_suc | bigint |  | 近1天金额非整数且精确到分的成功交易笔数 |
| ord_amt_1d_amt_to_penny_suc | bigint |  | 近1天金额非整数且精确到分的成功交易金额 |
| ord_cnt_1d_amt_le1 | bigint |  | 近1天金额<=1元的交易笔数 |
| ord_amt_1d_amt_le1 | bigint |  | 近1天金额<=1元的交易金额 |
| ord_cnt_1d_amt_le1_suc | bigint |  | 近1天金额<=1元的成功交易笔数 |
| ord_amt_1d_amt_le1_suc | bigint |  | 近1天金额<=1元的成功交易金额 |
| ord_cnt_prov_map_1d_qr | map(varchar, bigint) |  | 近1天各省码付交易笔数map |
| ord_cnt_prov_map_1d_qr_suc | map(varchar, bigint) |  | 近1天各省码付成功交易笔数map |
| ord_cnt_prov_entropy_1d_qr_suc | double |  | 近1天码付成功交易笔数省份信息熵 |
| dt | integer | partition key |  |
