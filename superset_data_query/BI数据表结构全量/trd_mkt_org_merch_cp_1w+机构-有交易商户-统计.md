# 商户终端交易情况表

**表名**: `edw.t_mer_term_transaction`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| sync_date | string | 同步日期 |
| product_type | string | 产品类型(2-MPOS, 5-POSP) |
| agt_id | string | 直属合伙人ID |
| merch_no | string | 商户号 |
| merch_name | string | 商户名（全名） |
| term_no | string | 终端号（无终端号则显示为空） |
| dev_sn | string | 机身号 |
| last_trade_time | string | 最后交易时间(发生交易的时间,不论交易是否成功) |
| last_succ_trade_time | string | 最后成功交易时间（发生交易额的成功的时间） |
| cy_acc_amt | bigint | 当月累计成功交易金额 |
| cy_acc_cnt | bigint | 当月累计成功交易笔数 |
| cy_acc_dr_amt | bigint | 当月累计借记卡交易额 |
| cy_acc_dr_cnt | bigint | 当月累计借记卡交易笔数 |
| cy_acc_cr_amt | bigint | 当月累计贷记卡交易额 |
| cy_acc_cr_cnt | bigint | 当月累计贷记卡交易笔数 |
| cy_wechat_amt | bigint | 当月累计微信交易额 |
| cy_wechat_cnt | bigint | 当月累计微信交易笔数 |
| cy_wechat_dr_amt | bigint | 当月累计微信借记卡交易额 |
| cy_wechat_dr_cnt | bigint | 当月累计微信借记卡交易笔数 |
| cy_wechat_cr_amt | bigint | 当月累计微信贷记卡交易额 |
| cy_wechat_cr_cnt | bigint | 当月累计微信贷记卡交易笔数 |
| cy_alipay_amt | bigint | 当月累计支付宝交易额 |
| cy_alipay_cnt | bigint | 当月累计支付宝交易笔数 |
| cy_alipay_dr_amt | bigint | 当月累计支付宝借记卡交易额 |
| cy_alipay_dr_cnt | bigint | 当月累计支付宝借记卡交易笔数 |
| cy_alipay_cr_amt | bigint | 当月累计支付宝贷记卡交易额 |
| cy_alipay_cr_cnt | bigint | 当月累计支付宝贷记卡交易笔数 |
| cy_upay_qr_amt | bigint | 当月累计银联二维码交易额 |
| cy_upay_qr_cnt | bigint | 当月累计银联二维码交易笔数 |
| cy_upay_dr_amt | bigint | 当月累计银联二维码借记卡交易额 |
| cy_upay_dr_cnt | bigint | 当月累计银联二维码借记卡交易笔数 |
| cy_upay_cr_amt | bigint | 当月累计银联二维码贷记卡交易额 |
| cy_upay_cr_cnt | bigint | 当月累计银联二维码贷记卡交易笔数 |
| his2now_amt | bigint | 历史至今交易额 |
| his2now_cnt | bigint | 历史至今交易笔数 |
| year2now_amt | bigint | 年度至今交易额 |
| year2now_cnt | bigint | 年度至今交易笔数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | int | 统计月份 |
