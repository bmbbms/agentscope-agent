# 商户收益月统计表

**表名**: `edw.income_stat_mer_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| belong_branch | string | 业务部门 |
| r_agt_id | string | 一级代理商ID |
| r_agt_name | string | 一级代理商名 |
| product_type | string | 产品类型 |
| lmer_no | string | 商户号 |
| lmer_name | string | 商户名 |
| lmer_net_date | string | 商户入网时间 |
| trd_cnt | string | 交易笔数 |
| trd_amt | string | 交易金额 |
| trd_fee | string | 交易手续费 |
| trd_chn_fee | string | 交易成本 |
| trd_profit | string | 交易分润 |
| trd_income | string | 交易收益 |
| card_cnt | string | 刷卡笔数 |
| card_amt | string | 刷卡金额 |
| card_fee | string | 刷卡手续费 |
| card_chn_fee | string | 刷卡成本 |
| card_profit | string | 刷卡分润 |
| card_income | string | 刷卡收益 |
| qr_cnt | string | 码付笔数 |
| qr_amt | string | 码付金额 |
| qr_fee | string | 码付手续费 |
| qr_chn_fee | string | 码付成本 |
| qr_profit | string | 码付分润 |
| qr_income | string | 码付收益 |
| em_cnt | string | 提现笔数 |
| em_amt | string | 提现金额 |
| em_fee | string | 提现手续费 |
| em_chn_fee | string | 提现成本 |
| em_profit | string | 提现分润 |
| em_income | string | 提现收益 |
| serv_cnt | string | 服务费交易笔数 |
| serv_amt | string | 服务费金额 |
| serv_profit | string | 服务费分润 |
| serv_income | string | 服务费收益 |
| act_profit | string | 激活奖励 |
| lsp_vip_profit | string | lsp会员费分润 |
| lsp_dpst_profit | string | lsp押金分润 |
| branch_company | string | 分公司ID |
| lsp_vip_cnt | string | 会员费笔数 |
| lsp_vip_amt | string | 会员费金额 |
| lsp_vip_income | string | 会员费收益 |
| em_no_cost_income | string | 0成本提现收益 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
