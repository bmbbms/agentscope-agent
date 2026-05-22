# 业务部门交易分析-地区日分析表

**表名**: `edw.brch_stat_trdarea_posp_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | bigint | 统计日期yyyyMMdd会计日期 |
| belong_branch | string | 业务部门 |
| product_type | string | 产品类型2-mpos,5-posp |
| busi_type | string | 业务大类 |
| prov_code | string | 省份编码 |
| prov_name | string | 省份名称 |
| city_code | string | 市区编码 |
| city_name | string | 市区名称 |
| amt | bigint | 交易额 |
| cnt | bigint | 交易笔数 |
| unqr_amt | bigint | 银联二维码金额 |
| unqr_cnt | bigint | 银联二维码笔数 |
| dr_amt | bigint | 借记卡金额 |
| dr_cnt | bigint | 借记卡笔数 |
| cr_amt | bigint | 贷记卡金额 |
| cr_cnt | bigint | 贷记卡笔数 |
| alipay_amt | bigint | 支付宝金额 |
| alipay_cnt | bigint | 支付宝笔数 |
| wechat_amt | bigint | 微信金额 |
| wechat_cnt | bigint | 微信笔数 |
| fcc_amt | bigint | 外币卡金额 |
| fcc_cnt | bigint | 外币卡笔数 |
| other_amt | bigint | 其他金额 |
| other_cnt | bigint | 其他笔数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
