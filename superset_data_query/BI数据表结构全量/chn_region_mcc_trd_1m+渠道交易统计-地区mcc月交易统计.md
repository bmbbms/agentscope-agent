# 渠道交易统计-地区mcc月交易统计

**表名**: `edw.chn_region_mcc_trd_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_month | string | 统计月份yyyymm |
| product_type | string | 业务大类(2-小pos 5-大pos) |
| province | string | 省份 |
| city | string | 城市 |
| adm_code | string | 行政代码 |
| mcc | string | mcc |
| trd_cnt | string | 总交易笔数 |
| trd_amt | string | 总交易金额 |
| fee_amt | string | 手续费 |
| unpay_cnt | string | 银联笔数 |
| unpay_amt | string | 银联金额 |
| unpay_pdg | string | 银联手续费 |
| dr_trd_cnt | string | 借记卡笔数 |
| dr_trd_amt | string | 借记卡金额 |
| cr_trd_cnt | string | 贷记卡笔数 |
| cr_trd_amt | string | 贷记卡金额 |
| ir_trd_cnt | string | 内卡笔数 |
| ir_trd_amt | string | 内卡金额 |
| or_trd_cnt | string | 外卡笔数 |
| or_trd_amt | string | 外卡金额 |
| foreign_cnt | string | 外币卡笔数 |
| foreign_amt | string | 外币卡金额 |
| mag_cnt | string | 磁条卡笔数 |
| mag_amt | string | 磁条卡金额 |
| ic_ins_cnt | string | ic插卡笔数 |
| ic_ins_amt | string | ic插卡金额 |
| ic_nct_cnt | string | (ic卡)非接笔数 |
| ic_nct_amt | string | (ic卡)非接金额 |
| ic_dfee_cnt | string | (ic卡)双免笔数 |
| ic_dfee_amt | string | (ic卡)双免金额 |
| quick_cnt | string | 云闪付笔数 |
| quick_amt | string | 云闪付金额 |
| quick_dfree_cnt | string | 云闪付双免笔数 |
| quick_dfree_amt | string | 云闪付双免金额 |
| unqrcode_cnt | string | 银联二维码笔数 |
| unqrcode_amt | string | 银联二维码金额 |
| unpay_c2b_cnt | string | 银联二维码主扫笔数 |
| unpay_c2b_amt | string | 银联二维码主扫金额 |
| unpay_b2c_cnt | string | 银联二维码被扫笔数 |
| unpay_b2c_amt | string | 银联二维码被扫金额 |
| oth_mod_cnt | string | 其他受理方式笔数 |
| oth_mod_amt | string | 其他受理方式金额 |
| wechat_cnt | string | 微信笔数 |
| wechat_amt | string | 微信金额 |
| wechat_fee | string | 微信手续费 |
| alipay_cnt | string | 支付宝笔数 |
| alipay_amt | string | 支付宝金额 |
| alipay_fee | string | 支付宝手续费 |
| ic_lt1000_cnt | string | 1000元以下ic卡笔数 |
| ic_lt1000_amt | string | 1000元以下ic卡金额 |
| quickpay_lt1000_cnt | string | 1000元以下云闪付笔数 |
| quickpay_lt1000_amt | string | 1000元以下云闪付金额 |
| fav_cnt | string | 优惠笔数 |
| fav_amt | string | 优惠金额 |
| fav_pdg | string | 优惠手续费 |
| qr_dr_cnt | string | 码付借记卡交易笔数 |
| qr_dr_amt | string | 码付借记卡交易金额 |
| qr_cr_cnt | string | 码付贷记卡交易笔数 |
| qr_cr_amt | string | 码付贷记卡交易笔数 |
| conn_cnt | string | 连通笔数 |
| conn_amt | string | 连通金额 |
| conn_fee | string | 连通手续费 |
| ex_conn_amt | string | 连通外卡金额 |
| ex_conn_cnt | string | 连通外卡笔数 |
| mastercard_trd_amt | string | 万事网联金额 |
| mastercard_trd_fee | string | 万事网联手续费 |
| mastercard_trd_cnt | string | 万事网联笔数 |
| dc_amt | string | 条码直连金额 |
| dc_cnt | string | 条码直连笔数 |
| dc_fee | string | 条码直连手续费 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
