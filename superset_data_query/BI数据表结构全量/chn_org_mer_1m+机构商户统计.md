# 机构商户统计

**表名**: `edw.chn_org_mer_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | bigint | 统计日期-yyyymm |
| source | string | 产品类型(2小pos/5大pos) |
| org_code | string | 机构代码 |
| inc_mer_cnt | bigint | 新增商户数 |
| stk_mer_cnt | bigint | 存量商户数 |
| inc_term_cnt | bigint | 新增终端数 |
| stk_term_cnt | bigint | 存量终端数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
