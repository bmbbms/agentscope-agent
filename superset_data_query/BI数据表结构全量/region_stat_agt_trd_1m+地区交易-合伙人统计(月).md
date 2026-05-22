# 右端渠道月统计

**表名**: `edw.r_trd_stat_term_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| rmerch_no | string | 右端商户号 |
| product_type | string |  |
| rterm_no | string |  |
| acc_amt | bigint | 成功交易金额 |
| acc_cnt | bigint | 成功交易笔数 |
| acc_dr_amt | bigint | 借记卡交易额 |
| acc_dr_cnt | bigint | 借记卡交易笔数 |
| acc_cr_amt | bigint | 贷记卡交易额 |
| acc_cr_cnt | bigint | 贷记卡交易笔数 |
| wechat_amt | bigint | 微信交易额 |
| wechat_cnt | bigint | 微信交易笔数 |
| wechat_dr_amt | bigint | 微信借记卡交易额 |
| wechat_dr_cnt | bigint | 微信借记卡交易笔数 |
| wechat_cr_amt | bigint | 微信贷记卡交易额 |
| wechat_cr_cnt | bigint | 微信贷记卡交易笔数 |
| alipay_amt | bigint | 支付宝交易额 |
| alipay_cnt | bigint | 支付宝交易笔数 |
| alipay_dr_amt | bigint | 支付宝借记卡交易额 |
| alipay_dr_cnt | bigint | 支付宝借记卡交易笔数 |
| alipay_cr_amt | bigint | 支付宝贷记卡交易额 |
| alipay_cr_cnt | bigint | 支付宝贷记卡交易笔数 |
| upay_qr_amt | bigint | 银联二维码交易额 |
| upay_qr_cnt | bigint | 银联二维码交易笔数 |
| upay_dr_amt | bigint | 银联二维码借记卡交易额 |
| upay_dr_cnt | bigint | 银联二维码借记卡交易笔数 |
| upay_cr_amt | bigint | 银联二维码贷记卡交易额 |
| upay_cr_cnt | bigint | 银联二维码贷记卡交易笔数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
