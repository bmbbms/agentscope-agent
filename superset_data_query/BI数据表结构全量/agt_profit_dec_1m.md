# agt_profit_dec_1m

**表名**: `edw.agt_profit_dec_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| r_agt_id | string | 一级代理商ID |
| r_agt_name | string | 一级代理商名称 |
| source | string | 产品类型 |
| amount | string | 操作金额 |
| remark | string | 备注 |
| status | string | 状态1-初始,2-完成 |
| create_user | string | 申请人 |
| create_time | string | 申请时间 |
| check_user | string | 审核人 |
| check_time | string | 审核时间 |
| process | string | 流程 |
| auto_id | string | 自动ID |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
