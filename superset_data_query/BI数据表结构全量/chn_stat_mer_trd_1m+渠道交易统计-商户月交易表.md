# 渠道交易统计-商户月交易表

**表名**: `edw.chn_stat_mer_trd_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | string | 统计月份yyyyMM |
| product_type | string | 产品大类 |
| province | string | 省份 |
| city | string | 城市 |
| adm_code | string | 行政代码 |
| merch_no | string | 商户号 |
| merch_name | string | 商户名 |
| mcc | string | MCC |
| trd_cnt | string | 总交易笔数 |
| trd_amt | string | 总交易金额 |
| fee_amt | string | 手续费 |
| nonstd_trd_cnt | string | 非标笔数 |
| nonstd_trd_amt | string | 非标金额 |
| nonstd_trd_fee | string | 非标手续费 |
| dr_trd_cnt | string | 借记卡笔数 |
| dr_trd_amt | string | 借记卡金额 |
| cr_trd_cnt | string | 贷记卡笔数 |
| cr_trd_amt | string | 贷记卡金额 |
| ir_trd_cnt | string | 内卡笔数 |
| ir_trd_amt | string | 内卡金额 |
| or_trd_cnt | string | 外卡笔数 |
| or_trd_amt | string | 外卡金额 |
| ic_nct_cnt | string | (IC卡)非接笔数 |
| ic_nct_amt | string | (IC卡)非接金额 |
| quick_cnt | string | 云闪付笔数 |
| quick_amt | string | 云闪付金额 |
| ic_dfee_cnt | string | (IC卡)双免笔数 |
| ic_dfee_amt | string | (IC卡)双免金额 |
| quick_dfree_cnt | string | 云闪付双免笔数 |
| quick_dfree_amt | string | 云闪付双免金额 |
| unqrcode_cnt | string | 银联二维码笔数 |
| unqrcode_amt | string | 银联二维码金额 |
| charge_type | string | 交易方式 |
| mag_amt | string | 磁条卡金额 |
| mag_cnt | string | 磁条卡笔数 |
| ic_ins_amt | string | IC插卡金额 |
| ic_ins_cnt | string | IC插卡笔数 |
| unpay_c2b_amt | string | 银联二维码主扫金额 |
| unpay_c2b_cnt | string | 银联二维码主扫笔数 |
| unpay_b2c_amt | string | 银联二维码被扫金额 |
| unpay_b2c_cnt | string | 银联二维码被扫笔数 |
| oth_mod_amt | string | 其他受理方式金额 |
| oth_mod_cnt | string | 其他受理方式笔数 |
| ic_lt1000_amt | string | 1000元以下IC卡金额 |
| ic_lt1000_cnt | string | 1000元以下IC卡笔数 |
| quickpay_lt1000_amt | string | 1000元以下云闪付金额 |
| quickpay_lt1000_cnt | string | 1000元以下云闪付笔数 |
| fav_amt | string | 优惠金额 |
| fav_cnt | string | 优惠笔数 |
| fav_pdg | string | 优惠手续费 |
| union_dr_cnt | string | 银联二维码借记卡交易笔数 |
| union_dr_amt | string | 银联二维码借记卡交易金额 |
| union_cr_cnt | string | 银联二维码贷记卡交易笔数 |
| union_cr_amt | string | 银联二维码贷记卡交易笔数 |
| qr_dr_cnt | string | 码付借记卡交易笔数 |
| qr_dr_amt | string | 码付借记卡交易金额 |
| qr_cr_cnt | string | 码付贷记卡交易笔数 |
| qr_cr_amt | string | 码付贷记卡交易笔数 |
| conn_cnt | string | 连通笔数 |
| conn_amt | string | 连通金额 |
| conn_fee | string | 连通手续费 |
| dr_fee | string | 借记卡手续费 |
| cr_fee | string | 贷记卡手续费 |
| unqrcode_fee | string | 银联二维码手续费 |
| ex_conn_amt | string | 连通外卡金额 |
| ex_conn_cnt | string | 连通外卡笔数 |
| mastercard_trd_amt | string | 万事网联金额 |
| mastercard_trd_fee | string | 万事网联手续费 |
| mastercard_trd_cnt | string | 万事网联笔数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
