# agt_trd_stat_1m

**表名**: `edw.agt_trd_stat_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| belong_branch | string | 业务部门 |
| r_agt_id | string | 一级代理商ID |
| r_agt_name | string | 一级代理商名称 |
| r_company_name | string | 一级代理商公司名称 |
| s_agt_id | string | 二级代理商名称 |
| s_agt_name | string | 二级代理商名称 |
| s_company_name | string | 二级代理商公司名称 |
| busi_type | string | 业务大类 |
| old_cnt | string | 存量交易笔数 |
| old_amt | string | 存量交易额 |
| new_cnt | string | 新增交易笔数 |
| new_amt | string | 新增交易额 |
| in_cnt | string | 内卡交易笔数 |
| in_amt | string | 内卡交易额 |
| out_cnt | string | 外卡交易笔数 |
| out_amt | string | 外卡交易额 |
| foreign_cnt | string | 外币卡交易笔数 |
| foreign_amt | string | 外币卡交易额 |
| count | string | 交易笔数 |
| amount | string | 交易额 |
| old_dr_cnt | string | 存量借记卡交易笔数 |
| old_dr_amt | string | 存量借记卡交易额 |
| new_dr_cnt | string | 新增借记卡交易笔数 |
| new_dr_amt | string | 新增借记卡交易额 |
| old_cap_cnt | string | 存量借记卡封顶交易笔数 |
| old_cap_amt | string | 存量借记卡封顶交易额 |
| new_cap_cnt | string | 新增借记卡封顶交易笔数 |
| new_cap_amt | string | 新增借记卡封顶交易额 |
| old_cr_cnt | string | 存量贷记卡交易笔数 |
| old_cr_amt | string | 存量贷记卡交易额 |
| new_cr_cnt | string | 新增贷记卡交易笔数 |
| new_cr_amt | string | 新增贷记卡交易额 |
| old_wechat_cnt | string | 存量微信交易笔数 |
| old_wechat_amt | string | 存量微信交易额 |
| new_wechat_cnt | string | 新增微信交易笔数 |
| new_wechat_amt | string | 新增微信交易额 |
| old_alipay_cnt | string | 存量支付宝交易笔数 |
| old_alipay_amt | string | 存量支付宝交易额 |
| new_alipay_cnt | string | 新增支付宝交易笔数 |
| new_alipay_amt | string | 新增支付宝交易额 |
| old_qr_cnt | string | 存量银联二维码交易笔数 |
| old_qr_amt | string | 存量银联二维码交易额 |
| new_qr_cnt | string | 新增银联二维码交易笔数 |
| new_qr_amt | string | 新增银联二维码交易额 |
| mag_cnt | string | 磁条卡笔数 |
| mag_amt | string | 磁条卡金额 |
| ic_cnt | string | IC插卡笔数 |
| ic_amt | string | IC插卡金额 |
| nct_cnt | string | IC非接笔数 |
| nct_amt | string | IC非接金额 |
| dfree_cnt | string | IC双免笔数 |
| dfree_amt | string | IC双免金额 |
| quick_pay_cnt | string | 云闪付笔数 |
| quick_pay_amt | string | 云闪付金额 |
| quick_dfree_cnt | string | 云闪付双免笔数 |
| quick_dfree_amt | string | 云闪付双免金额 |
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
| wechat_c2b_amt | string | 微信C2B金额 |
| wechat_c2b_cnt | string | 微信C2B笔数 |
| alipay_b2c_amt | string | 支付宝B2C金额 |
| alipay_b2c_cnt | string | 支付宝B2C笔数 |
| alipay_c2b_amt | string | 支付宝C2B金额 |
| alipay_c2b_cnt | string | 支付宝C2B笔数 |
| unpay_c2b_amt | string | 银联二维码C2B金额 |
| unpay_c2b_cnt | string | 银联二维码C2B笔数 |
| unpay_b2c_amt | string | 银联二维码B2C金额 |
| unpay_b2c_cnt | string | 银联二维码B2C笔数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
