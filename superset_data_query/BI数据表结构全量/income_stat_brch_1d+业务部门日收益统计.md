# 业务部门日收益统计

**表名**: `edw.income_stat_brch_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | bigint | 统计日期 |
| belong_branch | string | 业务部门 |
| product_type | string | 产品类型 |
| trd_cnt | bigint | 交易笔数 |
| trd_amt | bigint | 交易金额 |
| trd_fee | bigint | 交易手续费 |
| trd_chn_fee | bigint | 交易成本 |
| trd_profit | bigint | 交易分润 |
| trd_income | bigint | 交易收益 |
| card_cnt | bigint | 刷卡笔数 |
| card_amt | bigint | 刷卡金额 |
| card_fee | bigint | 刷卡手续费 |
| card_chn_fee | bigint | 刷卡成本 |
| card_profit | bigint | 刷卡分润 |
| card_income | bigint | 刷卡收益 |
| qr_cnt | bigint | 码付笔数 |
| qr_amt | bigint | 码付金额 |
| qr_fee | bigint | 码付手续费 |
| qr_chn_fee | bigint | 码付成本 |
| qr_profit | bigint | 码付分润 |
| qr_income | bigint | 码付收益 |
| em_cnt | bigint | 提现笔数 |
| em_amt | bigint | 提现金额 |
| em_fee | bigint | 提现手续费 |
| em_chn_fee | bigint | 提现成本 |
| em_profit | bigint | 提现分润 |
| em_income | bigint | 提现收益 |
| serv_cnt | bigint | 服务费交易笔数 |
| serv_amt | bigint | 服务费金额 |
| serv_profit | bigint | 服务费分润 |
| serv_income | bigint | 服务费收益 |
| act_profit | bigint | 激活奖励 |
| lsp_vip_profit | bigint | lsp会员费分润 |
| lsp_dpst_profit | bigint | lsp押金分润 |
| lsp_vip_amt | bigint | 会员费金额 |
| lsp_vip_income | bigint | 会员费收益 |
| lsp_vip_cnt | bigint | 会员费笔数 |
| em_no_cost_income | bigint | 0成本提现收益 |
| branch_company | string | 分公司编号 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
