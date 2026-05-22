# 客户经理交易月统计

**表名**: `edw.bz_manager_stat_trd_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | bigint | 统计月份 |
| type | string | 客户类型0-客户经理1-银行 |
| id | string | ID(银行ID/客户经理ID) |
| name | string | 名称(银行名/客户经理名) |
| parent_id | string | 归属父级银行 |
| parent_name | string | 归属父级银行名称 |
| bank_id_path | string | 银行层级路径 |
| inc_mer_num | bigint | 新增商户数 |
| amt | bigint | 交易额(正+1,反-1) |
| cnt | bigint | 交易笔数(正+1,反+1) |
| meta_write_service | string | 写入服务 |
| meta_output_time | string | 数据更新时间yyyy-MM-dd HH:mm:ss |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
