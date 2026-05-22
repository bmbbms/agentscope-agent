# 交易金额

**表名**: `edw.region_stat_brch_trd_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | bigint | 统计日期 |
| province | string | 省份 |
| city | string | 城市 |
| belong_branch | string | 业务部门 |
| busi_type | string | 业务大类 |
| amt | decimal |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
