# 分润成本核对表

**表名**: `edw.t_profit_cost_check_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| check_month | bigint | 核对月份(yyyyMM) |
| period | string | 周期类型(DAY-日返MONTH-月返NORMAL-正常) |
| src_busi_sub_type | string | 成本小类 |
| dest_busi_sub_type | string | 发放小类 |
| src_amt | bigint | 成本金额 |
| dest_amt | bigint | 发放金额 |
| update_time | string | 更新时间 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
