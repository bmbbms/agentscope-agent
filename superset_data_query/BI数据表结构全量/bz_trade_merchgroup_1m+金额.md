# 金额

**表名**: `edw.bz_trade_merchgroup_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| trans_month | string | 会计日期-yyyymm |
| group_id | string | 集团ID |
| merch_group_id | string | 商户组ID |
| merch_no | string | 商户号 |
| fee_calc_type | string | 手续费计算类型 |
| update_time | string | 更新时间 |
| stroke_count | int | 笔数 |
| amount_sum | decimal |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
