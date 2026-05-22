# 休眠终端月统计

**表名**: `edw.ztrd_term_stat_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| period | string | 统计频率(1-1月,3:3月,6:6月,12:12月),即近多久无交易 |
| merch_no | string | 商户号 |
| term_no | string | 终端号 |
| dev_sn | string | 机身号 |
| data_from | string | 数据来源 2-MPOS, 5-POSP |
| term_status | string | 终端状态 |
| add_date | string | 添加时间 |
| install_date | string | 装机时间 |
| cancel_date | string | 撤机时间 |
| last_trans_time | string | 最后交易时间 |
| last_succ_trans_time | string | 最后成功交易时间 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计月份 |
