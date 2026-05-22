# 批次号,int类型

**表名**: `edw.t_activity_order_stat_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| sponsor_id | string | 活动id |
| activity_id | string |  |
| mchnt_code | string | 商户号 |
| mchnt_name | string | 商户名 |
| card_no | string | 卡号 |
| card_type | string | 卡类型,0-借记卡1-贷记卡2-对公账户3-借贷混合4-电子账户5-其他 |
| trans_amt | bigint | 交易金额 |
| trans_time | string | 交易时间 |
| total_fee | bigint | 原始手续费 |
| cur_fee | bigint | 实付手续费 |
| point_use | bigint | 使用优惠金 |
| cybermoney_type | string | 权益类型,填默认值07 |
| trans_seq_no | string | 业务主键,即交易流水号 |
| batch_code | decimal |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
