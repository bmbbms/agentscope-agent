# ods_pay_risk.risk_monitor_t_scene_body (场景主体表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| id | varchar |  | 场景ID |
| name | varchar |  | 场景名称 |
| scale | varchar |  | 场景规模 |
| status | varchar |  | 状态 |
| verify_status | varchar |  | 审核状态 |
| modify_status | varchar |  | 可修改状态 |
| body_type | varchar |  | 主体类型1-代理商2-分公司 |
| body_id | varchar |  | 应用主体编号 |
| body_name | varchar |  | 应用主体名称 |
| industry_type | varchar |  | 行业类别 |
| business_time | varchar |  | 营业时间段 |
| trade_address | varchar |  | 交易位置 |
| trade_address_code | varchar |  | 交易位置省市区编码 |
| trade_scale | varchar |  | 交易规模 |
| remark | varchar |  | 场景说明 |
| detail_request | varchar |  | 资质要求 |
| control_desc | varchar |  | 管控策略说明 |
| create_time | varchar |  | 创建时间 |
| create_user | varchar |  | 创建人 |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| verify_advice | varchar |  | 审核意见 |
| agent_auth_list | varchar |  | 业务团队权限（BODY_TYPE+AUTH_FLAG）列表，格式示例：1-0,2-1 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 是否删除(false:否 是:true) |
| meta_output_time | varchar |  | 写入时间 |
| meta_ori_table | varchar |  | 原始表名 |
