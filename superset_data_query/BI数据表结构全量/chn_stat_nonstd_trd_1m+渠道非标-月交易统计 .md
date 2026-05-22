# 渠道非标-月交易统计 

**表名**: `edw.chn_stat_nonstd_trd_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | string | 统计日期(yyyyMMdd) |
| product_type | string | 产品大类           |
| province | string | 省份             |
| city | string | 城市             |
| region_code | string | 地区码            |
| total_cnt | string | 总交易笔数         |
| total_amt | string | 总交易金额         |
| nonstd_cnt | string | 非标笔数           |
| nonstd_amt | string | 非标金额           |
| nonstd_pdg | string | 非标手续费         |
| nonstd_income | string | 非标收益           |
| nonstd_der_cnt | string | 减免类非标笔数     |
| nonstd_der_amt | string | 减免类非标金额     |
| nonstd_der_income | string | 减免类非标收益     |
| nonstd_dr_cnt | string | 非标借记卡笔数     |
| nonstd_dr_amt | string | 非标借记卡金额     |
| nonstd_dr_pdg | string | 非标借记卡手续费   |
| nonstd_dr_income | string | 非标借记卡收益     |
| nonstd_cr_cnt | string | 非标贷记卡笔数     |
| nonstd_cr_amt | string | 非标贷记卡金额     |
| nonstd_cr_pdg | string | 非标贷记卡手续费   |
| nonstd_cr_income | string | 非标贷记卡收益     |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
