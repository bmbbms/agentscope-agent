# ods_pay_risk.riskctrl_t_rc_merch_param_micro (数据引入层-信用&风控域-MPOS商户风险参数表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| merch_name | varchar |  | 商户名称 |
| risk_rank | varchar |  | 限额等级:1级,2级,3级......,每一级有不同的限额和限笔 |
| net_type | varchar |  | 入网类型 |
| account_type | varchar |  | 结算类型 |
| net_time | varchar |  | 入网时间 |
| mobile | varchar |  | 手机号 |
| det_address | varchar |  | 详细地址 |
| settle_type | varchar |  | 清算方式1:纯T1清算2:纯T0清算3:T0+T1 |
| cert_type | varchar |  | 证件类型，01:身份证 |
| cert_no | varchar |  | 证件号码(法人/个人身份证号) |
| cert_name | varchar |  | 证件人姓名 |
| account_no | varchar |  | 结算账号（卡号） |
| account_name | varchar |  | 结算账户户名 |
| merch_status | varchar |  | 商户状态1-启用2-停用3-注销 |
| verify_status | varchar |  | 审核状态0-待审核1-审核通过2-审核拒绝 |
| area_code | varchar |  | 地区码 |
| province_code | varchar |  | 省编码 |
| city_code | varchar |  | 市编码 |
| create_user | varchar |  | 创建用户 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 更新用户 |
| update_time | varchar |  | 更新时间 |
| final_flag | varchar |  | 入网完成 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
