# 商户年龄分布-日统计

**表名**: `edw.brch_mer_ages_distribution_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | string | 统计日期 |
| belong_branch | string | 业务部门 |
| product_type | string | 产品类型 |
| net_type | string | 入网类型1-营业执照2-租赁合同3-小微商户 |
| age | double | 法人年龄 |
| increate_num | double | 增量商户数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
