# xdata.t_mer_term_last_trade_detail (最后交易时间)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| term_no | varchar |  | 终端号（无终端号则显示为空） |
| dev_sn | varchar |  | 机身号 |
| product_type | varchar |  | 产品类型(2-MPOS, 5-POSP) |
| last_trade_time | varchar |  | 最后一笔交易时间 |
| last_sus_trade_time | varchar |  | 最后一笔成功交易时间 |
| last_trade_amt | varchar |  | 最后一笔交易金额 |
| last_sus_trade_amt | varchar |  | 最后一笔成功交易金额 |
| dt | integer | partition key |   统计日期 |
| data_source | varchar | partition key |  1 为左端 ，2 为右端 |
