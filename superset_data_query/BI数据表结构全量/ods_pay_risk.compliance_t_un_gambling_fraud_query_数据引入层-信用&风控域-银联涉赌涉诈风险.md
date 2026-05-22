# ods_pay_risk.compliance_t_un_gambling_fraud_query (数据引入层-信用&风控域-银联涉赌涉诈风险	)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 主键ID,查询序列号 |
| query_value | varchar |  | 查询信息 |
| query_type | varchar |  | 信息类型00-手机号，01身份证号，02-银行卡号 |
| query_source | varchar |  | 查询来源数据字典UN_RISK_QUERY_SOURCE |
| rsp_code | varchar |  | 渠道响应码 |
| rsp_msg | varchar |  | 响应信息 |
| trace_no | varchar |  | 交易序列号 |
| fraud_risk_score | double |  | 欺诈风险得分，riskCode-100 |
| fraud_risk_level | varchar |  | 欺诈风险等级1低2中3中高，4高 |
| banker_risk_score | double |  | 赌博庄家101 |
| banker_risk_level | varchar |  | 赌博庄家 |
| player_risk_score | double |  | 赌博玩家102 |
| player_risk_level | varchar |  | 赌博玩家等级 |
| launder_risk_score | double |  | 洗钱风险得分103 |
| launder_risk_level | varchar |  | 洗钱风险等级 |
| other_risk_score | double |  | 其它风险得分999 |
| other_risk_level | varchar |  | 其它风险等级 |
| query_result | varchar |  | 01-命中02-未命中03查询失败 |
| create_time | varchar |  | 查询时间 |
| create_user | varchar |  | 查询人 |
| update_time | varchar |  | 更新时间 |
| meta_write_service | varchar |  | 写入服务 |
| meta_ori_table | varchar |  | 原表 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
