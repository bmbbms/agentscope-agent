# xacc.clear_fail_msg_report (清算失败按错误原因统计表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| type | varchar |  | 类型 付款失败,退票 |
| reason | varchar |  | 失败原因 |
| amount | varchar |  | 失败金额 |
| total_cnt | varchar |  | 总商户数 |
| dt | integer | partition key |  |
