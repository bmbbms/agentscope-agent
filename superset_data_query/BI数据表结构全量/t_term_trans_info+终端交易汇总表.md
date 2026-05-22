# 机型交易月统计表

**表名**: `edw.trd_stat_term_model_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | string | 统计月份 |
| physn_type | string | 机型 |
| belong_branch | string | 归属机构 |
| branch_company | string | 分公司ID |
| busi_type | string | 业务大类 |
| amt | bigint | 交易金额 |
| cnt | bigint | 交易笔数 |
| fee_amt | bigint | 交易手续费 |
| in_dr_cap_amt | bigint | 内卡借记卡封顶交易额 |
| in_dr_cap_cnt | bigint | 内卡借记卡封顶交易笔数 |
| in_dr_cap_pdg | bigint | 内卡借记卡封顶手续费 |
| card_amt | bigint | 刷卡交易金额 |
| card_cnt | bigint | 刷卡交易笔数 |
| card_fee | bigint | 刷卡交易手续费 |
| qr_amt | bigint | 码付交易金额 |
| qr_cnt | bigint | 码付交易笔数 |
| qr_fee | bigint | 码付交易手续费 |
| dr_amt | bigint | 借记卡交易额 |
| dr_cnt | bigint | 借记卡交易笔数 |
| dr_pdg | bigint | 借记卡交易手续费 |
| cr_amt | bigint | 贷记卡交易额 |
| cr_cnt | bigint | 贷记卡交易笔数 |
| cr_pdg | bigint | 贷记卡交易手续费 |
| wechat_amt | bigint | 微信交易额 |
| wechat_cnt | bigint | 微信交易笔数 |
| wechat_pdg | bigint | 微信交易手续费 |
| alipay_amt | bigint | 支付宝交易额 |
| alipay_cnt | bigint | 支付宝交易笔数 |
| alipay_pdg | bigint | 支付宝交易手续费 |
| unpay_amt | bigint | 银联二维码交易额 |
| unpay_cnt | bigint | 银联二维码交易笔数 |
| unpay_pdg | bigint | 银联二维码交易手续费 |
| unpay_c2b_amt | bigint | 银联二维码主扫交易额 |
| unpay_c2b_cnt | bigint | 银联二维码主扫交易笔数 |
| unpay_c2b_pdg | bigint | 银联二维码主扫交易手续费 |
| unpay_b2c_amt | bigint | 银联二维码被扫交易额 |
| unpay_b2c_cnt | bigint | 银联二维码被扫交易笔数 |
| unpay_b2c_pdg | bigint | 银联二维码被扫交易手续费 |
| wechat_b2c_amt | bigint | 微信B2C金额 |
| wechat_b2c_cnt | bigint | 微信B2C笔数 |
| wechat_b2c_pdg | bigint | 微信B2C手续费 |
| wechat_c2b_amt | bigint | 微信C2B金额 |
| wechat_c2b_cnt | bigint | 微信C2B笔数 |
| wechat_c2b_pdg | bigint | 微信C2B手续费 |
| alipay_b2c_amt | bigint | 支付宝B2C金额 |
| alipay_b2c_cnt | bigint | 支付宝B2C笔数 |
| alipay_b2c_pdg | bigint | 支付宝B2C手续费 |
| alipay_c2b_amt | bigint | 支付宝C2B金额 |
| alipay_c2b_cnt | bigint | 支付宝C2B笔数 |
| alipay_c2b_pdg | bigint | 支付宝C2B手续费 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
