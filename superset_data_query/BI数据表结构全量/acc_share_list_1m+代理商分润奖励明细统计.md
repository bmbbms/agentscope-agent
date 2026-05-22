# 代理商分润奖励明细统计

**表名**: `edw.acc_share_list_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| product_type | string | 产品类型 |
| body_type | string | 主体类型0-嘉联 1-商服 |
| agent_id | string | 代理商ID |
| agent_name | string | 代理商名称 |
| agent_company_name | string | 代理商公司名称 |
| agent_account | string | 代理商注册号 |
| tax_point | string | 税率 |
| share_cost_trade | bigint | 分润成本-1.交易相关奖励 |
| share_cost_active | bigint | 分润成本-2.激活台数相关奖励 |
| share_cost_out | bigint | 分润成本-3.机具出货奖励 |
| share_cost_flow | bigint | 分润成本-4.流量费相关奖励 |
| share_cost_trade_cnt | bigint | 分润成本-5.交易笔数相关奖励 |
| share_cost_desc | bigint | 分润成本-6.本月差额调减 |
| share_cost_month_sett | bigint | 分润成本-7.月结分润项目 |
| share_cost_total | bigint | 分润成本-总计(1+2+3+4+5-6+7) |
| share_adjust_trade | bigint | 分润调整-1.交易相关奖励 |
| share_adjust_active | bigint | 分润调整-2.激活台数相关奖励 |
| share_adjust_out | bigint | 分润调整-3.机具出货奖励 |
| share_adjust_flow | bigint | 分润调整-4.流量费相关奖励 |
| share_adjust_trade_cnt | bigint | 分润调整-5.交易笔数相关奖励 |
| share_adjust_other | bigint | 分润调整-6.其他 |
| share_adjust_total | bigint | 分润调整-总计(1+2+3+4+5+6) |
| share_totalsupp_trade | bigint | 分润总账补录-1.交易 |
| share_totalsupp_active | bigint | 分润总账补录-2.激活 |
| share_totalsupp_out | bigint | 分润总账补录-3.出货 |
| share_totalsupp_flow | bigint | 分润总账补录-4.流量 |
| share_totalsupp_trade_cnt | bigint | 分润总账补录-5.交易笔数 |
| share_totalsupp_other | bigint | 分润总账补录-6.其他 |
| share_totalsupp_total | bigint | 分润总账补录-总计(1+2+3+4+5) |
| accrual_tax_amount | bigint | 计提含税金额(成本总计+调整总计+补录总计) |
| tax_amount | bigint | 税额(计提含税-计提不含税) |
| accrual_notax_amount | bigint | 计提不含税金额(计提含税/(1+税率)) |
| update_time | string | 更新时间(yyyy-MM-dd HH24:mi:ss) |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计月份 |
