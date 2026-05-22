# 商户无交易统计

**表名**: `edw.ztrd_merch_stat_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| merch_no | string | 商户号 |
| net_type | string | 入网类型 1-营业执照 2-租赁合同 3-小微商户 4-电签 5-小pos |
| first_sus_date | string | 首次成功交易日期 |
| last_sus_date | string | 最后一笔成功交易日期 |
| no_trd_days | int | 无交易天数 |
| is_new_sleep | boolean | 是否是今天休眠 |
| is_new_start | boolean | 是否是今天重启用 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
