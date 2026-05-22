# ods_posp.t_withhold_agreement (代扣协议表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| agreement_id | varchar |  | AGREEMENT_ID (S 服务费协议 D 押金协议 R 租金协议 P 购机款协议 DP 租机转购机协议) +协议日期（yyyymmdd）+ 商户号+终端号(费终端填00000000) |
| agreement_type | varchar |  | 协议类型：S 服务费协议 D 押金协议 R 租金协议 O 其他协议  P 购机款协议 DP 租机转购机协议 |
| busi_type | varchar |  | 协议业务大类 |
| busi_sub_type | varchar |  | 协议业务小类 |
| merch_no | varchar |  | 商户号 |
| term_no | varchar |  | 终端号 |
| term_sn | varchar |  | 终端序列号 |
| source | varchar |  | 请求来源 |
| agent_id | varchar |  | 代理商ID |
| start_date | varchar |  | 协议生效日期 |
| stop_date | varchar |  | 协议终止日期，长期协议为空 |
| amount | varchar |  | 协议扣费金额 |
| withhold_type | varchar |  | 扣费类型 0 固定日期(差额扣费) 1 非固定日期 |
| withhold_cycle | varchar |  | 扣费周期 0 一次性 1 按月 2 按季度 3 按年 |
| withhold_mode | varchar |  | 扣费模式 0 周期开始扣 1 周期结束扣 |
| oper_status | varchar |  | 操作状态 0  禁用 1 启用 |
| status | varchar |  | 协议状态 0  正常协议 1  已作废 2 到期终止 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| nera_withhold_date | varchar |  | 最近需要扣费的日期 |
| real_stop_date | varchar |  | 实际协议终止日期 |
| remarks | varchar |  | 备注 |
| real_amount | varchar |  | 实际付款金额 |
| free_amount | varchar |  | 减免金额 |
| merch_name | varchar |  | 商户名 |
| agent_name | varchar |  | 代理商名字 |
| original_agreement_id | varchar |  | 原协议号 |
| cancel_reason | varchar |  | 作废原因 |
| buss_department | varchar |  | 业务部门 |
| audit_status | varchar |  | 审核状态 0：审核中 1：审核通过 2：审核拒绝 |
| withhold_freq | varchar |  | 扣费频次 1：一个周期一次 2：两个周期一次 3：三个周期一次 |
| direct_agent_id | varchar |  | 直属代理商ID |
| first_charge_date | varchar |  | 第一次更改时间 |
