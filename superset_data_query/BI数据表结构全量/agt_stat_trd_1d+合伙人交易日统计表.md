# 合伙人交易日统计表

**表名**: `edw.agt_stat_trd_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | string | 统计日期 |
| belong_branch | string | 业务部门 |
| r_agt_id | string | 一级代理商 |
| r_agt_name | string | 一级代理商名 |
| r_agt_company_name | string | 一级代理商公司名称 |
| r_agt_acc | string | 一级代理商账号 |
| s_agt_id | string | 二级代理商 |
| s_agt_name | string | 二级代理商名 |
| s_agt_company_name | string | 二级代理商公司名称 |
| s_agt_acc | string | 二级代理商账号 |
| agt_id | string | 直属代理商 |
| agt_name | string | 直属代理商名 |
| agt_company_name | string | 直属代理商公司名称 |
| agt_acc | string | 直属代理商账号 |
| agt_path | string | 代理商路径 |
| data_from | string | 产品类型 |
| busi_type | string | 业务大类 |
| amount | string | 交易笔数 |
| count | string | 交易额 |
| pdg | string | 手续费 |
| stk_cnt | string | 存量交易笔数 |
| stk_amt | string | 存量交易额 |
| stk_pdg | string | 存量手续费 |
| stk_dr_cnt | string | 存量借记卡笔数 |
| stk_dr_amt | string | 存量借记卡金额 |
| stk_dr_cap_cnt | string | 存量借记卡封顶笔数 |
| stk_dr_cap_amt | string | 存量借记卡封顶金额 |
| stk_cr_cnt | string | 存量贷记卡笔数 |
| stk_cr_amt | string | 存量贷记卡金额 |
| stk_wechat_cnt | string | 存量微信笔数 |
| stk_wechat_amt | string | 存量微信金额 |
| stk_alipay_cnt | string | 存量支付宝笔数 |
| stk_alipay_amt | string | 存量支付宝金额 |
| stk_unpay_cnt | string | 存量银联二维码笔数 |
| stk_unpay_amt | string | 存量银联二维码金额 |
| inc_cnt | string | 新增交易笔数 |
| inc_amt | string | 新增交易额 |
| inc_pdg | string | 新增手续费 |
| inc_dr_cnt | string | 新增借记卡笔数 |
| inc_dr_amt | string | 新增借记卡金额 |
| inc_dr_cap_cnt | string | 新增借记卡封顶笔数 |
| inc_dr_cap_amt | string | 新增借记卡封顶金额 |
| inc_cr_cnt | string | 新增贷记卡笔数 |
| inc_cr_amt | string | 新增贷记卡金额 |
| inc_wechat_cnt | string | 新增微信笔数 |
| inc_wechat_amt | string | 新增微信金额 |
| inc_alipay_cnt | string | 新增支付宝笔数 |
| inc_alipay_amt | string | 新增支付宝金额 |
| inc_unpay_cnt | string | 新增银联二维码笔数 |
| inc_unpay_amt | string | 新增银联二维码金额 |
| in_cnt | string | 内卡笔数 |
| in_amt | string | 内卡金额 |
| out_cnt | string | 外卡笔数 |
| out_amt | string | 外卡金额 |
| dc_cnt | string | 外币卡笔数 |
| dc_amt | string | 外币卡金额 |
| mag_cnt | string | 磁条卡笔数 |
| mag_amt | string | 磁条卡金额 |
| ic_ins_cnt | string | （IC卡）插卡笔数 |
| ic_ins_amt | string | (IC卡)插卡金额 |
| nct_cnt | string | (IC卡)非接笔数 |
| nct_amt | string | (IC卡)非接金额 |
| ic_dfree_cnt | string | (IC卡)双免笔数 |
| ic_dfree_amt | string | (IC卡)双免金额 |
| quick_pay_cnt | string | 云闪付笔数 |
| quick_pay_amt | string | 云闪付金额 |
| quick_pay_dfree_cnt | string | 云闪付双免笔数 |
| quick_pay_dfree_amt | string | 云闪付双免金额 |
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
| branch_company | string | 分公司编号 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
