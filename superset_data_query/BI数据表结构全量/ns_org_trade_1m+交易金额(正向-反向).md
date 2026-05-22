# 交易金额(正向-反向)

**表名**: `edw.ns_org_trade_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| org_id | string | 大机构ID(一级合作商) |
| org_id2 | string | 小机构ID(二级合作商) |
| r_agt_id | string | 一级代理商 |
| product_type | string | 产品类型(5大pos,2小pos) |
| cnt | int | 交易笔数(正向) |
| ne_cnt | int | 交易笔数(反向) |
| amt | decimal |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
