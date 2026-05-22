# 客户无交易统计推送

**表名**: `edw.push_ztrd_cust_stat_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| cust_no | string | 客户号(商户号) |
| dormancy_day | int | 多少天定义为休眠 |
| push_type | string | 消息系统类型 |
| push_topic | string | 推送主题 |
| dormancy_status | tinyint | 休眠状态:1-休眠 2-休眠唤醒 3-结束休眠 |
| reason | tinyint | 休眠原因:1 - 连续>=90天无交易 2 - 连续>=180天无交易 3 - 连续>=270天无交易 4 - 连续>=360天无交易 5、商户被停用 6、商户被注销 |
| change_status | tinyint | 商户状态 1-启用 2-停用 3-注销 |
| last_time | string | 最后一笔成功交易日期:yyyyMMdd |
| meta_output_time | string | 数据更新时间yyyy-MM-dd HH:mm:ss.SSS |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
