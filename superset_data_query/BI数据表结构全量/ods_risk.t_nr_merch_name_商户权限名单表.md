# ods_risk.t_nr_merch_name (商户权限名单表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 权限名单id |
| value | varchar |  | 权限名单值 |
| type | varchar |  | 权限类型:01-交易权限，02-夜间交易权限，03-大额实名交易，04-大额T0清算权限，05-大额调额权限，06-风控规则权限，07-同卡交易权限 |
| status | varchar |  | 状态: 0-未启用，1-启用,2-停用 |
| descp | varchar |  | 描述 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| valid_start_time | varchar |  | 有效开始时间 |
| valid_end_time | varchar |  | 有效截止时间 |
| proc_id | varchar |  | 流程编号 |
