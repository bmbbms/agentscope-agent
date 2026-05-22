# edw.ztrd_merch_list (休眠商户统计)

| Column | Type | Extra | Comment |
|---|---|---|---|
| period | varchar |  | 统计频率(1-1月,3:3月,6:6月,12:12月),即近多久无交易 |
| merch_no | varchar |  | 商户号 |
| status | varchar |  | 商户状态 |
| net_date | varchar |  | 入网日期 |
| last_trans_time | varchar |  | 最后交易时间 |
| last_succ_trans_time | varchar |  | 最后成功交易时间 |
| update_time | varchar |  | 数据更新时间 |
| dt | integer | partition key | 统计月份 |
| source | varchar | partition key | 来源(L:左端R:右端) |
