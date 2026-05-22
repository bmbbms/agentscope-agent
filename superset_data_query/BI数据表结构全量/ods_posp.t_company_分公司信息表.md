# ods_posp.t_company (分公司信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| org_id | varchar |  | 分公司ID |
| org_company | varchar |  | 分公司名称 |
| company_address | varchar |  | 分公司地址 |
| company_manage | varchar |  | 分公司负责人 |
| parent_org_id | varchar |  | 父级分公司ID:顶级分公司为0 |
| org_level | varchar |  | 分公司级别 |
| status | varchar |  | 状态(1:正常，2:停用，9:删除) |
| org_path | varchar |  | 总公司到当前公司的ID链 格式：org_id.org_id. |
| remark | varchar |  | 备注 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 修改时间 |
| update_user | varchar |  | 修改人 |
| data_type | varchar |  | 数据类型 0:分公司数据，1:业务部门数据 |
| org_license_no | varchar |  | 分公司统一社会信用代码 |
