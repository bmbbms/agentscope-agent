# ods_risk.t_rc_name_list (各种名单表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| value | varchar |  | 名单信息 |
| type | varchar |  | 名单类型(00-卡号，01-卡Bin，02-商户号，03-营业执照，04-身份证号，05-手机号，07-工商白名单，08-进件银行卡白名单,09-境外移机,10-营业执照名称,11-商户名称,12-移机,13-移码,14-结算卡号,15-境外交易,16-通用,17-IP地址,18-地区,19-经纬度,20-移机检测,21-结算法人年龄,22-禁止交易地区商户,23-对公账户,24-终端,25-境内移机,26-进件二要素,28-POSP地区,30-境内移机(特殊)) |
| flag | varchar |  | 名单标志:00-白名单，01-入网白名单，02-交易白名单，03-提现白名单，04-代付白名单；10.代理商入网黑名单，11-入网黑名单，12-交易黑名单，13-提现黑名单，14-代付黑名单，15-预警白名单，17-代付白名单，20-移机检测名单，21-可疑商户名单，22-D0提现黑名单，25-提现白名单，26-借记卡快提白名单，27-交易灰名单，29-提现灰名单 |
| source | varchar |  | 名单来源：00.系统自动，01.手工录入，02.银联提供，03.公安部提供，04-其他机构提供，05.人行提供 06.支付清算协会  07.银联可疑名单 08.入网黑名单回溯 |
| status | varchar |  | 状态，0-未启用,1-启用,2-停用 |
| descp | varchar |  | 描述 |
| start_time | varchar |  | 启用时间 yyyy-MM-dd hh24:mi:ss |
| create_time | varchar |  | 创建时间 yyyy-MM-dd hh24:mi:ss |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 yyyy-MM-dd hh24:mi:ss |
| update_user | varchar |  | 更新人 |
| id | bigint |  |  |
| verify_status | varchar |  | 审核状态 0-待审核 1-审核通过 2-审核拒绝 |
| deal_record | varchar |  | 处理记录 |
| valid_start_time | varchar |  | 有效开始时间 yyyy-MM-dd hh24:mi:ss |
| valid_end_time | varchar |  | 有效截止时间 yyyy-MM-dd hh24:mi:ss |
| verify_record | varchar |  |  |
| verify_user | varchar |  |  |
| verify_time | varchar |  | yyyy-MM-dd hh24:mi:ss |
| modify_status | varchar |  | 修改状态 0-可修改 1-不可修改 |
| is_trace | varchar |  | 是否回溯生成，1-是，0-否 |
| nation_code | varchar |  | 国籍代码 DEFAULT CHN |
| nation_name | varchar |  | 国籍名称 DEFAULT 中国 |
| is_frms | varchar |  | 推送到反洗钱状态，0-未推送或不成功，1-推送成功 |
