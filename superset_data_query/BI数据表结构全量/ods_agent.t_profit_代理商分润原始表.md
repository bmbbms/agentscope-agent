# ods_agent.t_profit (代理商分润原始表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| auto_id | varchar |  | 自动编号 |
| user_id | varchar |  | 代理商ID |
| total_date | varchar |  | 分润统计时间 |
| physn | varchar |  | 产品分润的机身号 |
| physn_type | varchar |  | 机具类型 |
| amount | varchar |  | 交易金额 |
| fee | varchar |  | 交易手续费 |
| profit_amount | varchar |  | 分润金额 |
| glevel | varchar |  | 分润等级 |
| trade_list_id | varchar |  | 产生分润的交易流水 |
| type | varchar |  | 分润来源，暂时只用于区分交易还是提现，1=交易，2=提现，3=激活奖励,4=赠送设备,5=服务费,6=订单服务费,8=立刷商户版会员费，9=立刷商户版押金,11=交易分润删除 |
| rule_info | varchar |  | 自己的分润规则：根据分润来源不同，规则不同 |
| next_rule_info | varchar |  | 下级的分润规则，type等于3或4时为激活日期 |
| status | varchar |  | 0=初始需财务审核后展示，1=正常，代理商可查看，2=删除,3=存疑(主要是单笔的分润总金额大于交易的手续费) |
| profit_max_fee | varchar |  | 代理商分润规则的手续费封顶，部分机型可能有手续费封顶的概念，第一次跑分润时填充此值，跑完分润后需要将此值与分润金额和交易手续费对比取小的 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| rate | varchar |  | 交易费率 |
| total_profit_amount | varchar |  | 分润总金额 |
| business_type | varchar |  | 业务类型,1=mpos,2=jj码，3=pos+ |
| card_type | varchar |  | 交易卡类型（0=借记卡，1=贷记卡，3=银联二维码，A=微信，B=支付宝，4=境外银联卡, 5=外卡DCC, 6=外卡EDC-JCB,7=外卡EDC-VISA,111=云闪付) |
| next_user_id | varchar |  | 下级ID |
| dt | integer | partition key |  |
