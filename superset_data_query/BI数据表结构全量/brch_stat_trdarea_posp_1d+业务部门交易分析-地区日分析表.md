# 业务部门日交易统计

**表名**: `edw.brch_stat_trd_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | bigint | 统计日期 |
| belong_branch | string | 业务部门 |
| data_from | string | 产品类型 |
| busi_type | string | 业务大类 |
| amount | bigint | 交易笔数 |
| count | bigint | 交易额 |
| pdg | bigint | 手续费 |
| stk_cnt | bigint | 存量交易笔数 |
| stk_amt | bigint | 存量交易额 |
| stk_pdg | bigint | 存量手续费 |
| stk_dr_cnt | bigint | 存量借记卡笔数 |
| stk_dr_amt | bigint | 存量借记卡金额 |
| stk_dr_cap_cnt | bigint | 存量借记卡封顶笔数 |
| stk_dr_cap_amt | bigint | 存量借记卡封顶金额 |
| stk_cr_cnt | bigint | 存量贷记卡笔数 |
| stk_cr_amt | bigint | 存量贷记卡金额 |
| stk_wechat_cnt | bigint | 存量微信笔数 |
| stk_wechat_amt | bigint | 存量微信金额 |
| stk_alipay_cnt | bigint | 存量支付宝笔数 |
| stk_alipay_amt | bigint | 存量支付宝金额 |
| stk_unpay_cnt | bigint | 存量银联二维码笔数 |
| stk_unpay_amt | bigint | 存量银联二维码金额 |
| inc_cnt | bigint | 新增交易笔数 |
| inc_amt | bigint | 新增交易额 |
| inc_pdg | bigint | 新增手续费 |
| inc_dr_cnt | bigint | 新增借记卡笔数 |
| inc_dr_amt | bigint | 新增借记卡金额 |
| inc_dr_cap_cnt | bigint | 新增借记卡封顶笔数 |
| inc_dr_cap_amt | bigint | 新增借记卡封顶金额 |
| inc_cr_cnt | bigint | 新增贷记卡笔数 |
| inc_cr_amt | bigint | 新增贷记卡金额 |
| inc_wechat_cnt | bigint | 新增微信笔数 |
| inc_wechat_amt | bigint | 新增微信金额 |
| inc_alipay_cnt | bigint | 新增支付宝笔数 |
| inc_alipay_amt | bigint | 新增支付宝金额 |
| inc_unpay_cnt | bigint | 新增银联二维码笔数 |
| inc_unpay_amt | bigint | 新增银联二维码金额 |
| in_cnt | bigint | 内卡笔数 |
| in_amt | bigint | 内卡金额 |
| out_cnt | bigint | 外卡笔数 |
| out_amt | bigint | 外卡金额 |
| dc_cnt | bigint | 外币卡笔数 |
| dc_amt | bigint | 外币卡金额 |
| mag_cnt | bigint | 磁条卡笔数 |
| mag_amt | bigint | 磁条卡金额 |
| ic_ins_cnt | bigint | （IC卡）插卡笔数 |
| ic_ins_amt | bigint | (IC卡)插卡金额 |
| nct_cnt | bigint | (IC卡)非接笔数 |
| nct_amt | bigint | (IC卡)非接金额 |
| ic_dfree_cnt | bigint | (IC卡)双免笔数 |
| ic_dfree_amt | bigint | (IC卡)双免金额 |
| quick_pay_cnt | bigint | 云闪付笔数 |
| quick_pay_amt | bigint | 云闪付金额 |
| quick_pay_dfree_cnt | bigint | 云闪付双免笔数 |
| quick_pay_dfree_amt | bigint | 云闪付双免金额 |
| branch_company | string | 分公司编号 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
