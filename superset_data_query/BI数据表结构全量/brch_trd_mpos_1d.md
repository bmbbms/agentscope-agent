# brch_trd_mpos_1d

**表名**: `edw.brch_trd_mpos_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | bigint | 统计日期 |
| belong_branch | string | 业务部门 |
| product_type | string | 产品类型2-mpos4-立刷商户版 |
| busi_type | string | 业务大类 |
| fee_rate | decimal |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
