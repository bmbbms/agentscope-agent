# 渠道商户统计-月商户统计

**表名**: `edw.chn_mer_stat_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| source | string | 产品类型 |
| province | string | 省份 |
| city | string | 城市 |
| region_code | string | 行政代码 |
| inc_mer_cnt | string | 新增商户数 |
| inc_term_cnt | string | 新增终端书 |
| stk_mer_cnt | string | 存量商户数 |
| stk_term_cnt | string | 存量终端数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
