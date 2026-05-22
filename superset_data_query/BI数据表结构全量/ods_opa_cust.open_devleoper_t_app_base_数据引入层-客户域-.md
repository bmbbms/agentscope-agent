# ods_opa_cust.open_devleoper_t_app_base (数据引入层-客户域-)

| Column | Type | Extra | Comment |
|---|---|---|---|
| app_id | varchar |  | 应用ID |
| app_name | varchar |  | 应用名 |
| app_alias | varchar |  | 应用别名 |
| developer | varchar |  | 开发者 |
| developer_id | varchar |  | 开发者ID |
| developer_type | varchar |  | 开发者类型 |
| industry | varchar |  | 所属行业 |
| industry_remark | varchar |  | 行业备注 |
| product_type | varchar |  | 产品 |
| status | varchar |  | 状态:0-禁用;1-启用; |
| version | varchar |  | 应用版本 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 修改时间 |
| create_user | varchar |  | 创建者 |
| update_user | varchar |  | 修改者 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
