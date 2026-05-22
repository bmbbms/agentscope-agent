# 商户交易(金额笔数)月排名

**表名**: `edw.mer_stat_trade_rank_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| merch_no | string | 商户号 |
| merch_name | string | 商户名称 |
| mcc | string | mcc |
| product_type | string | 产品类型(2-MPOS,5-MPOS) |
| busi_type | string | 业务大类(1001/2001) |
| agt_id | string | 代理商ID |
| agt_name | string | 代理商名称 |
| r_agt_id | string | 一级代理商ID |
| r_agt_name | string | 一级代理商名称 |
| s_agt_id | string | 二级代理商ID |
| s_agt_name | string | 二级代理商名称 |
| belong_branch | string | 业务部门ID  |
| branch_company | string | 分公司ID |
| agt_path | string | 代理商层级路径 |
| trans_amt | bigint | 交易额 |
| trans_cnt | bigint | 交易笔数 |
| pri_trans_amt | bigint | 上期交易额 |
| pri_trans_cnt | bigint | 上期交易笔数 |
| end_date | string | 统计截止日期 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
