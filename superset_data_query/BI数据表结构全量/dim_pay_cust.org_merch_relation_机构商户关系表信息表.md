# dim_pay_cust.org_merch_relation (机构商户关系表信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| merch_name | varchar |  | 商户名 |
| org_code | varchar |  | 机构号 |
| org_name | varchar |  | 机构名 |
| org_type | varchar |  | 项目类型(0-特约商户,1-代理商,2-通用产品,3-商户) |
| branch_company | varchar |  | 分公司ID |
| company_name | varchar |  | 分公司名称 |
| belong_branch | varchar |  | 业务部门ID |
| agt_id | varchar |  | 代理商ID |
| agt_path | varchar |  | 代理商层级 |
| bind_status | varchar |  | 绑定状态(0-停用,1-启用) |
| merch_status | varchar |  | 商户状态(0待启用1启用2停用3注销) |
| net_date | varchar |  | 入网日期 yyyyMMdd |
| net_type | varchar |  | 入网类型 1-营业执照 2-租赁合同 3-小微商户 |
| cancel_date | varchar |  | 注销时间(撤销/停用时间) |
| region_code | varchar |  | 入网地区 |
| region_name | varchar |  | 入网地区名 |
| det_addr | varchar |  | 入网地址 |
| mcc | varchar |  | mcc |
| mcc_desc | varchar |  | mcc 描述 |
| create_time | varchar |  | 入网时间 yyyy-MM-dd HH:mmss |
| update_time | varchar |  | 更新时间 yyyy-MM-dd HH:mmss |
| merch_bind_time | varchar |  | 机构商户绑定时间(yyyy-MM-dd HH:mm:ss) |
