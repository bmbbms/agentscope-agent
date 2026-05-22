# 终端交易日报表

**表名**: `edw.trd_rep_term_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | string | 统计日期 |
| belong_branch | string | 业务部门 |
| busi_type | string | 业务大类 |
| r_agt_id | string | 一级代理商ID |
| r_agt_company_name | string | 一级代理商(公司名称、名称） |
| s_agt_id | string | 二级代理商ID |
| s_agt_company_name | string | 二级代理商(公司名称、名称） |
| agt_id | string | 二级代理商ID |
| agt_company_name | string | 二级代理商(公司名称、名称） |
| term_no | string | 终端号 |
| mer_no | string | 商户号 |
| mer_name | string | 商户名称 |
| net_date | string | 商户入网日期 |
| cnt | bigint | 交易笔数 |
| amt | bigint | 交易金额 |
| fee_amt | bigint | 交易手续费 |
| dr_cnt | bigint | 借记卡笔数 |
| dr_amt | bigint | 借记卡金额 |
| dr_pdg | bigint | 借记卡手续费 |
| dr_cap_cnt | bigint | 借记卡封顶交易笔数 |
| dr_cap_amt | bigint | 借记卡封顶交易金额 |
| dr_cap_pdg | bigint | 借记卡封顶手续费 |
| cr_cnt | bigint | 贷记卡笔数 |
| cr_amt | bigint | 贷记卡金额 |
| cr_pdg | bigint | 贷记卡手续费 |
| wechat_cnt | bigint | 微信笔数 |
| wechat_amt | bigint | 微信金额 |
| wechat_pdg | bigint | 微信手续费 |
| alipay_cnt | bigint | 支付宝笔数 |
| alipay_amt | bigint | 支付宝金额 |
| alipay_pdg | bigint | 支付宝手续费 |
| unpay_cnt | bigint | 银联二维码笔数 |
| unpay_amt | bigint | 银联二维码金额 |
| unpay_pdg | bigint | 银联二维码手续费 |
| branch_company | string | 分公司ID |
| wechat_dr_amt | string | 微信借记卡金额 |
| wechat_dr_cnt | string | 微信借记卡笔数 |
| wechat_dr_pdg | string | 微信借记卡手续费 |
| wechat_cr_amt | string | 微信贷记卡金额 |
| wechat_cr_cnt | string | 微信贷记卡笔数 |
| wechat_cr_pdg | string | 微信贷记卡手续费 |
| alipay_dr_amt | string | 支付宝借记卡金额 |
| alipay_dr_cnt | string | 支付宝借记卡笔数 |
| alipay_dr_pdg | string | 支付宝借记卡手续费 |
| alipay_cr_amt | string | 支付宝贷记卡金额 |
| alipay_cr_cnt | string | 支付宝贷记卡笔数 |
| alipay_cr_pdg | string | 支付宝贷记卡手续费 |
| unpay_dr_amt | string | 银联二维码借记卡金额 |
| unpay_dr_cnt | string | 银联二维码借记卡笔数 |
| unpay_dr_pdg | string | 银联二维码借记卡手续费 |
| unpay_cr_amt | string | 银联二维码贷记卡金额 |
| unpay_cr_cnt | string | 银联二维码贷记卡笔数 |
| unpay_cr_pdg | string | 银联二维码贷记卡手续费 |
| wechat_b2c_amt | string | 微信B2C金额 |
| wechat_b2c_cnt | string | 微信B2C笔数 |
| wechat_b2c_pdg | string | 微信B2C手续费 |
| wechat_c2b_amt | string | 微信C2B金额 |
| wechat_c2b_cnt | string | 微信C2B笔数 |
| wechat_c2b_pdg | string | 微信C2B手续费 |
| alipay_b2c_amt | string | 支付宝B2C金额 |
| alipay_b2c_cnt | string | 支付宝B2C笔数 |
| alipay_b2c_pdg | string | 支付宝B2C手续费 |
| alipay_c2b_amt | string | 支付宝C2B金额 |
| alipay_c2b_cnt | string | 支付宝C2B笔数 |
| alipay_c2b_pdg | string | 支付宝C2B手续费 |
| unpay_b2c_amt | string | 银联二维码B2C金额 |
| unpay_b2c_cnt | string | 银联二维码B2C笔数 |
| unpay_b2c_pdg | string | 银联二维码B2C手续费 |
| unpay_c2b_amt | string | 银联二维码C2B金额 |
| unpay_c2b_cnt | string | 银联二维码C2B笔数 |
| unpay_c2b_pdg | string | 银联二维码C2B手续费 |
| physn_type | string |  |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
