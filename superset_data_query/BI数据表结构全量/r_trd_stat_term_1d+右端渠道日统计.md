# 笔数

**表名**: `edw.retcode_chn_stat_ld`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | bigint | 统计日期-yyyymmdd |
| rret_code | string | 返回状态吗 |
| ret_code | string | 返回状态吗 |
| chn_no | string | 渠道号 |
| chn_type | string | 渠道类型 |
| busi_type | string | 业务大类 |
| product_type | string | 产品类型 |
| cnt | decimal |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计时间 |
