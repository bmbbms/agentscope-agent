# 活动交易流水-刷单日统计表

**表名**: `edw.charge_activity_record_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| activity_id | string | 活动ID |
| activity_name | string | 活动名称 |
| merch_no | string | 商户号 |
| fee_calc_type | string | 计费类型01内卡借记卡02内卡贷记卡03银联二维码04云闪付优惠11外卡借记卡12外卡贷记卡20外币DCC21外币EDC22外币卡EDC-VM30微信31支付宝D0D0交易T1T1交易 |
| account | string | 账号 |
| swip_count | int | 刷单次数 |
| swip_date | string | 刷单日期 |
| create_time | string | 创建时间 |
| group_id | string | 分组聚合ID |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
