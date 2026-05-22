# xacc.clear_fail_org_compay_report (清算失败按公司维度统计表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| company | varchar |  | 分公司 |
| depart_id | varchar |  | 部门 |
| amount | varchar |  | 失败金额 |
| type | varchar |  | 类型 付款失败,退票 |
| level | varchar |  | 级别 1千以内,1千-1万,1万-10万,10万-50万,50万以上 |
| total_cnt | varchar |  | 总商户数 |
| high_quality_cnt | varchar |  | 优质商户数 |
| financial_cnt | varchar |  | 理财商户数 |
| corporate_cnt | varchar |  | 对公商户数 |
| manay_cnt | varchar |  | 失败次数大于5商户数 |
| first_cnt | varchar |  | 首次失败商户数 |
| dt | integer | partition key |  |
