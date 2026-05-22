# ods_agent.t_profit_amount_log (代理商分润金额变化历史表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| user_id | varchar |  | 用户ID |
| val1 | varchar |  | 变化前 |
| val2 | varchar |  | 变化值 |
| val3 | varchar |  | 变化后 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人，type=2时此值为审核人的ID type=1时此值为system |
| type | varchar |  | 类型，MPOS(1=分润，2=提现，3=提现未通过退回 4分润扣税 5扣税加给上级 6运营扣除(MPOS)，7运营增加(MPOS)(6、7、306、307用于处理分润分润出错的情况，此时key为修改依据) 1001 MPOS抵扣 108=营销费用申请 120=分润撤销 121=已撤销 122=会员领取冲销嘉联 123=押金奖励冲销嘉联) POS+(8pos+分润，9扣服务费，10激活奖励(MPOS)，11扣工资包 306=运营扣除(POS+) 3001POS抵扣307=运营增加(POS+) 12=数据服务费 |
| profit_total_date | varchar |  | type=1时使用，表示分润的统计日期，type=2时此值与create_date相等 |
| key | varchar |  | 键，type等于2或者3时有效，存储提现的id，对应t_withdraw表中的withdraw_id type=1时无效；type为运营调整类，值为管理平台T_Gm_Operate主键；type=215/216，值为营销活动表主键；type=221 值为代扣订单ID；type=225/226/6时，值为退押金/会员费交易流水ID |
| auto_id | varchar |  | 自动编号 |
| subject | varchar |  | 科目代码，1001--分润金额，2001--直接提现余额，3001--立刷商户版分润金额，2002--营销活动账户金额，2003-卡券活动户 |
| time_stamp | varchar |  | 记账时间戳 |
| dt | integer | partition key | 分区日期字段 |
