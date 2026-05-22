# ods_mpos.t_member_refund_rent (转账流水表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| order_id | varchar |  | 订单号 |
| ori_order_id | varchar |  | 原始订单号 |
| busi_type | varchar |  | 业务大类 |
| busi_sub_type | varchar |  | 业务小类 |
| trans_time | varchar |  | 交易时间 |
| amount | varchar |  | 转账金额 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| out_fund_merch_no | varchar |  | 出账商户号 |
| in_fund_merch_no | varchar |  | 入账商户号 |
| out_fund_status | varchar |  | 出账状态0-初始1-成功2-失败 |
| update_out_fund_status | varchar |  | 更新出账状态0-初始 1-冲正成功 2-冲正失败 |
| in_fund_status | varchar |  | 入账状态0-初始1-成功2-失败 |
| update_in_fund_status | varchar |  | 更新入账状态0-初始 1-冲正成功 2-冲正失败 |
| product | varchar |  | 产品 LSP 立刷商户版  LS 立刷  FS 飞刷 |
| purchase_status | varchar |  | 是否冲销购机款，0，否  1，是 |
