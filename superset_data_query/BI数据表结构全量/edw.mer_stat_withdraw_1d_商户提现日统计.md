# edw.mer_stat_withdraw_1d (商户提现日统计)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| belong_branch | varchar |  | 业务部门 |
| r_agt_id | varchar |  | 一级代理商 |
| r_agt_name | varchar |  | 一级代理商名(公司名称/名称) |
| product_type | varchar |  | 产品类型 |
| mer_no | varchar |  | 商户号 |
| mer_name | varchar |  | 商户名称 |
| net_date | varchar |  | 商户入网时间(yyyyMMdd) |
| cnt | varchar |  | 提现笔数 |
| amt | varchar |  | 提现金额 |
| fee_amt | varchar |  | 提现手续费 |
| d0_cnt | varchar |  | 快速提现笔数 |
| d0_amt | varchar |  | 快速提现金额 |
| t1_cnt | varchar |  | 一般提现笔数 |
| t1_amt | varchar |  | 一般提现金额 |
| priv_cnt | varchar |  | 对私提现笔数 |
| priv_amt | varchar |  | 对私提现金额 |
| pub_cnt | varchar |  | 对公提现笔数 |
| pub_amt | varchar |  | 对公提现金额 |
| branch_company | varchar |  | 分公司ID |
| dt | integer | partition key |  |
