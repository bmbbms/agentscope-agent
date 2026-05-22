# ods_posp.t_activity (计费活动表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 活动ID |
| activity_name | varchar |  | 活动名称 |
| begin_time | varchar |  | 活动开始时间 yyyy-MM-dd HH mm ss |
| end_time | varchar |  | 活动结束时间 yyyy-MM-dd HH mm ss |
| customer_no | varchar |  | 活动客户编号 |
| customer_name | varchar |  | 活动客户名称 |
| priority | varchar |  | 优先级 |
| status | varchar |  | 状态 1未开始 2已开始 3已结束 |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| account_period | varchar |  | 账单周期 1日 2周 3月(客户/主体账单周期优先级>活动账单周期) |
| project | varchar |  | 项目 activity活动计费 mcc自选MCC计费 |
| use_status | varchar |  | 启用状态  1启用，2停用 |
| set_merch_time | varchar |  | 是否设置商户活动时间0否，1是 |
| sponsor_id | varchar |  | 出资方ID |
| sponsor_name | varchar |  | 出资方名称 |
| disc_type | varchar |  | 减免方式，1全额减免，2优惠费率，3打折，默认为全额减免 |
| statistics_type | varchar |  | 统计方式 all-全额统计 day-按日统计 |
| merch_limit | varchar |  | 是否限制商户限额 1是 0否 |
| activity_title | varchar |  | 活动标题 |
| merch_day_limit | varchar |  | 是否限制商户单日优惠上限，枚举类型：0-不限制，1-限制 |
| bill_type | varchar |  | 0-按活动周期 1-按客户账单周期, 默认为按客户账单周期 |
| merch_quota_warn | varchar |  | 商户额度预警开关,0-关闭,1-开启 |
| merch_settle_cardbin_limit | varchar |  | 商户结算卡bin校验开关,0-关闭,1-开启, 默认关闭 |
