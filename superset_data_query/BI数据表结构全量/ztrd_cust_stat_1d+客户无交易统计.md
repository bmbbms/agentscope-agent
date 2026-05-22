# 客户无交易统计

**表名**: `edw.ztrd_cust_stat_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| cust_no | string | 客户号(商户号) |
| first_sus_date | string | 首次成功交易日期 |
| last_sus_date | string | 最后一笔成功交易日期 |
| no_trd_days | int | 无交易天数 |
| is_new_sleep | boolean | 是否是今天休眠 |
| is_new_start | boolean | 是否是今天重启用 |
| is_new_stop | boolean | 是否是今天停用/注销 |
| change_status | tinyint | 客户状态 1-启用 2-停用 3-注销 |
| is_dormancy | boolean | 曾今是否休眠 |
| meta_output_time | string | 数据更新时间yyyy-MM-dd HH:mm:ss.SSS |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
