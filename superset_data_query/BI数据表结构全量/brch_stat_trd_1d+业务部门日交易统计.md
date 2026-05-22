# 业务部门交易分析-日图标展示

**表名**: `edw.brch_stat_trd_posp_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | bigint | 统计日期(yyyyMMdd) |
| belong_branch | string | 业务部门 |
| busi_type | string | 业务大类 |
| cnt | bigint | 交易笔数 |
| amt | bigint | 交易金额 |
| fee_amt | bigint | 交易手续费 |
| dr_cnt | bigint | 借记卡笔数 |
| dr_amt | bigint | 借记卡金额 |
| cr_cnt | bigint | 贷记卡笔数 |
| cr_amt | bigint | 贷记卡金额 |
| wechat_cnt | bigint | 微信笔数 |
| wechat_amt | bigint | 微信金额 |
| alipay_cnt | bigint | 支付宝笔数 |
| alipay_amt | bigint | 支付宝金额 |
| unpay_cnt | bigint | 银联二维码笔数 |
| unpay_amt | bigint | 银联二维码金额 |
| foreign_cnt | bigint | 外币卡交易笔数 |
| foreign_amt | bigint | 外币卡交易额 |
| quick_pay_cnt | bigint | 云闪付交易笔数 |
| quick_pay_amt | bigint | 云闪付交易额 |
| quick_pay_dfree_cnt | bigint | 云闪付双免交易笔数 |
| quick_pay_dfree_amt | bigint | 云闪付双免交易额 |
| oth_cnt | bigint | 其他交易笔数 |
| oth_amt | bigint | 其他交易额 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
