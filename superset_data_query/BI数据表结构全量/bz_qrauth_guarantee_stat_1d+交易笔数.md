# 交易笔数

**表名**: `edw.bz_qrauth_guarantee_stat_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| accounting_date | bigint | 会计日期 |
| busi_type | string | 交易大类编码 |
| busi_sub_type | string | 交易小类编码 |
| cnt | decimal |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
