# 渠道商户统计-月地区活动商户统计

**表名**: `edw.chn_act_mer_1m`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| source | string | 产品大类 |
| province | string | 省份 |
| city | string | 城市 |
| act_mer_cnt | string | 活动商户数 |
| act_term_cnt | string | 活动终端数 |
| good_mer_cnt | string | 活跃商户数 |
| good_term_cnt | string | 活跃终端数 |
| act_qr_mer_cnt | string | 银联二维码活动商户数 |
| act_qr_term_cnt | string | 银联二维码活动终端数 |
| good_qr_mer_cnt | string | 银联二维码活跃商户数 |
| good_qr_term_cnt | string | 银联二维码活跃终端数 |
| act_nct_mer_cnt | string | 非接活动商户数 |
| act_nct_term_cnt | string | 非接活动终端数 |
| good_nct_mer_cnt | string | 非接活跃商户数 |
| good_nct_term_cnt | string | 非接活跃终端数 |
| act_dfree_mer_cnt | string | 双免活动商户数 |
| act_dfree_term_cnt | string | 双免活动终端数 |
| good_dfree_mer_cnt | string | 双免活跃商户数 |
| good_dfree_term_cnt | string | 双免活跃终端数 |
| act_mer_cnt_3m | string | 近三个月活动商户数 |
| act_term_cnt_3m | string | 近三个月活动终端数 |
| act_qr_mer_cnt_3m | string | 近三个月银联二维码活动商户数 |
| act_qr_term_cnt_3m | string | 近三个月银联二维码活动终端数 |
| act_nct_mer_cnt_3m | string | 近三个月非接活动商户数 |
| act_nct_term_cnt_3m | string | 近三个月非接活动终端数 |
| act_dfree_mer_cnt_3m | string | 近三个月双免活动商户数 |
| act_dfree_term_cnt_3m | string | 近三个月双免活动终端数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int |  |
