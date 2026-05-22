# 客户商户交易月统计表

**表名**: `edw.t_cus_merch_trd_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| cust_id | string | 客户号 |
| legal_name | string | 法人名称 |
| legal_certype | string | 法人证件类型 |
| legal_cerno | string | 法人证件号码 |
| is_extra | string | 域内商户1-是0-域外 |
| extra_mer_no | string | 域外商户号 |
| mer_no | string | 商户号 |
| mer_name | string | 商户名 |
| pri_industry | string | 一级行业 |
| sec_industry | string | 二级行业 |
| mcc | string | mcc |
| net_date | string | 入网日期 |
| deal_month | bigint | 交易月份 |
| trans_infos | string | 交易信息json |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
