# 机构-有交易商户-统计

**表名**: `edw.trd_mkt_org_merch_cp_1w`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| start_date | date | 统计开始日期 |
| end_date | date | 统计结束日期 |
| period | string | 统计周期-W |
| org_code | string | 机构号 |
| org_name | string | 项目(机构名称) |
| branch_company | string | 所属分公司 |
| org_type | string | 项目类型(0-特约商户,1-代理商,2-通用产品,3-商户) |
| merch_no | string | 商户号 |
| merch_name | string | 商户名 |
| org_trade | string | 是否机构交易 Y/N |
| meta_write_service | string | 数据写入来源 |
| meta_output_time | string | 数据写入时间 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计时间 |
