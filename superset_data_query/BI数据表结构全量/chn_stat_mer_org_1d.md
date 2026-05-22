# chn_stat_mer_org_1d

**表名**: `edw.chn_stat_mer_org_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| product_type | string | 产品类型 |
| city_code | string | 城市编号 |
| city_name | string | 城市名称 |
| prov_code | string | 省份编号 |
| prov_name | string | 省份名称 |
| org_code | string | 机构编号 |
| org_name | string | 机构名称 |
| route_paraid | string | 模版ID |
| para_name | string | 模板名称 |
| stock_mer_count | string | 存量商户数 |
| new_mer_count | string | 新增商户数 |
| fixation_rount | string | 是否固定路由(0 否 1是) |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
