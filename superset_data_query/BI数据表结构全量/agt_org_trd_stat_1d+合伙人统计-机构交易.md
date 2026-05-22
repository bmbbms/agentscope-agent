# 合伙人统计-机构交易

**表名**: `edw.agt_org_trd_stat_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| trans_time | string | 交易日期(yyyyMMdd) |
| trans_month | string | 交易月份(yyyyMM) |
| org_name | string | 机构名称 |
| org_code | string | 机构号 |
| access_type | string | 机构类型 |
| belong_branch | string | 业务部门 |
| branch_company | string | 分公司名称 |
| count_out | bigint | 外部笔数 |
| amount_out | bigint | 外部交易额 |
| count_in | bigint | 内部笔数 |
| amount_in | bigint | 内部交易额 |
| count_all | bigint | 内外总笔数 |
| amount_all | bigint | 内外总交易额 |
| qr_version | string | 版本号 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
