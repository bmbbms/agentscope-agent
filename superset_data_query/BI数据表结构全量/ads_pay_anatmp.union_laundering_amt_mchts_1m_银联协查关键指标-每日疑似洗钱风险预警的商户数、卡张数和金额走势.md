# ads_pay_anatmp.union_laundering_amt_mchts_1m (银联协查关键指标-每日疑似洗钱风险预警的商户数、卡张数和金额走势)

| Column | Type | Extra | Comment |
|---|---|---|---|
| dt | varchar(500) |  | 日期 |
| account_type | varchar(500) |  | 预警卡类型 |
| cards | double |  | 疑似洗钱卡张数 |
| cnt | double |  | 疑似洗钱交易笔数 |
| amount | double |  | 疑似洗钱交易金额(万元) |
| l_mchts | integer |  | 关联左端商户数 |
| r_mchts | integer |  | 关联右端商户数 |
