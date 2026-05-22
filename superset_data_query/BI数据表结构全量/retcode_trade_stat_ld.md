# retcode_trade_stat_ld

**表名**: `edw.retcode_trade_stat_ld`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| ret_code | string | 返回码 |
| busi_type | string | 业务大类 |
| fee_calc_type | string | 手续费计算类型 |
| card_type | string | 卡类型 |
| card_flag | string | 卡标志 |
| pwdfree | string | 免密免签标志 |
| cnt | bigint | 笔数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
