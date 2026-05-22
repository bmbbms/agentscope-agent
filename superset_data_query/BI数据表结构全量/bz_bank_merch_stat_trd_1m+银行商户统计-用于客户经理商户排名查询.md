# 银行商户统计-用于客户经理商户排名查询

**表名**: `edw.bz_bank_merch_stat_trd_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | bigint | 统计月份(yyyyMM) |
| mer_no | string | 商户号 |
| mer_name | string | 商户名 |
| manager_id | string | 客户经理ID |
| manager_name | string | 客户经理名 |
| bank_id | string | 所属银行ID |
| bank_name | string | 所属银行名称 |
| bank_id_path | string | 银行层级路径 |
| amt | bigint | 交易额(正+1,反-1) |
| cnt | bigint | 交易笔数(正+1,反+1) |
| amt_rank | bigint | 当前交易额排名 |
| cnt_rank | bigint | 当前交易笔数排名 |
| meta_write_service | string | 写入服务 |
| meta_output_time | string | 数据更新时间yyyy-MM-dd HH:mm:ss |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
