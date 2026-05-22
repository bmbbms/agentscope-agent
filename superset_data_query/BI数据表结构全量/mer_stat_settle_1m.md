# mer_stat_settle_1m

**表名**: `edw.mer_stat_settle_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| belong_branch | string | 业务部门 |
| r_agt_id | string | 一级代理商ID |
| r_agt_name | string | 一级代理商名 |
| r_agt_company | string | 一级代理商公司名 |
| lmer_no | string | 商户号 |
| lmer_name | string | 商户名 |
| should_amount | string | 应付金额 |
| ori_amount | string | 原始交易金额 |
| amount | string | 交易金额 |
| count | string | 交易笔数 |
| fee | string | 交易手续费 |
| discount_amount | string | 优惠金额 |
| discount_count | string | 优惠笔数 |
| discount_fee | string | 优惠手续费 |
| cost | string | 费用 |
| adjust_amount | string | 调整金额 |
| quick_em_amt | string | 快速提现金额 |
| quick_em_cnt | string | 快速提现笔数 |
| quick_em_fee | string | 快速提现手续费 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
