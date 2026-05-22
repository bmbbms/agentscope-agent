# 休眠商户统计

**表名**: `edw.ztrd_merch_list`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| period | string | 统计频率(1-1月,3:3月,6:6月,12:12月),即近多久无交易 |
| merch_no | string | 商户号 |
| status | string | 商户状态 |
| net_date | string | 入网日期 |
| last_trans_time | string | 最后交易时间 |
| last_succ_trans_time | string | 最后成功交易时间 |
| update_time | string | 数据更新时间 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计月份 |
