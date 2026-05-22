# ads_pay_anatmp.alarm_rule_mernum_accuracy_1y (内部预警关键指标-posp每月预警量和准确率)

| Column | Type | Extra | Comment |
|---|---|---|---|
| dt | varchar(500) |  | 月份 |
| mer_num | integer |  | 预警去重商户数 |
| event_mer_num | integer |  | 预警且推送事件去重商户数 |
| event_mer_accuracy | double |  | 推送风险事件率 |
| mer_num_nocashout | integer |  | 剔除套现-预警去重商户数 |
| event_mer_num_nocashout | integer |  | 剔除套现-预警且推送事件去重商户数 |
| event_mer_accuracy_nocashout | double |  | 剔除套现-推送风险事件率 |
