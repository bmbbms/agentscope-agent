# 金额

**表名**: `edw.bz_merch_withdraw_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| withdraw_date | string | 会计日期-yyyymmdd |
| group_id | string | 集团ID |
| merch_no | string | 商户号 |
| account_no | string | 入账卡号 |
| cnt | int | 笔数 |
| amount | decimal |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
