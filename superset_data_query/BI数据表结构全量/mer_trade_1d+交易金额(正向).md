# 交易金额(正向)

**表名**: `edw.mer_trade_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| product_type | string | 产品类型(5大pos,2小pos) |
| agt_id | string | 直属代理商 |
| agt_path | string | 代理商层级 |
| merch_no | string | 商户号 |
| cnt | int | 交易笔数(正向) |
| amt | decimal |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
