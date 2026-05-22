# ERP首页统计

**表名**: `edw.trd_erp_stat_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | bigint | 统计日期 |
| busi_type | string | 业务大类 |
| amt | bigint | 交易额 |
| cnt | bigint | 交易笔数 |
| card_amt | bigint | 刷卡交易额 |
| card_cnt | bigint | 刷卡交易笔数 |
| qr_amt | bigint | 码付交易额 |
| qr_cnt | bigint | 码付交易笔数 |
| wechat_amt | bigint | 微信交易额 |
| wechat_cnt | bigint | 微信交易笔数 |
| alipay_amt | bigint | 支付宝交易额 |
| alipay_cnt | bigint | 支付宝交易笔数 |
| net_mer_num | bigint | 入网商户数（新增） |
| belong_branch | string | 业务部门 |
| branch_company | string | 分公司ID |
| meta_write_service | string | 数据写入来源 |
| meta_output_time | string | 数据写入时间 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 统计时间 |
