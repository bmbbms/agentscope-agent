# brch_stat_mer_netin_1m

**表名**: `edw.brch_stat_mer_netin_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | double |  |
| belong_branch | string |  |
| product_type | string |  |
| net_type | string |  |
| prov_code | string |  |
| city_code | string |  |
| inc_mer_num | double |  |
| stk_mer_num | double |  |
| cancel_mer_num | double |  |
| stop_mer_num | double |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
