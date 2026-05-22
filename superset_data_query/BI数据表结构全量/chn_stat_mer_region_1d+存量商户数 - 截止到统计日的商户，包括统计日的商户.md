# 存量商户数 - 截止到统计日的商户，包括统计日的商户

**表名**: `edw.chn_stat_mer_region_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | bigint | 统计日期-yyyymmdd |
| product_type | string | 产品类型 2-MPOS，5-POSP |
| city_name | string | 城市名称 |
| prov_name | string | 省份名称 |
| route_paraid | string | 模版ID |
| para_name | string | 模板名称 |
| stock_mer_count | decimal |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计时间 |
