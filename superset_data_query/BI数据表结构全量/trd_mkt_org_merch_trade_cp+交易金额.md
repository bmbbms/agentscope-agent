# 商户终端累计交易统计

**表名**: `edw.trd_accu_merch_term`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| busi_type | string | 业务大类 |
| mer_no | string | 商户号 |
| mer_name | string | 商户名 |
| term_no | string | 终端号 |
| term_sn | string | 机身号 |
| rts_begin_time | string | 交服务费时间 |
| rts_end_time | string | 达标截止时间 |
| cnt | bigint | 累计交易笔数 |
| amt | bigint | 累计交易金额 |
| fee | bigint | 累计交易手续费 |
| rts_cnt | bigint | 累计达标笔数(剔除首笔免手续费) |
| rts_amt | bigint | 累计达标金额(剔除首笔免手续费) |
| cr_cnt | bigint | 累计贷记卡笔数 |
| cr_amt | bigint | 累计贷记卡金额 |
| dr_cnt | bigint | 累计借记卡笔数 |
| dr_amt | bigint | 累计借记卡金额 |
| qrcr_cnt | bigint | 累计码付贷记卡笔数 |
| qrcr_amt | bigint | 累计码付贷记卡金额 |
| qrdr_cnt | bigint | 累计码付借记卡笔数 |
| qrdr_amt | bigint | 累计码付借记卡金额 |
| update_time | string | 更新时间 |
| cap_cnt | bigint | 累计封顶交易笔数 |
| cap_amt | bigint | 累计封顶交易笔数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
