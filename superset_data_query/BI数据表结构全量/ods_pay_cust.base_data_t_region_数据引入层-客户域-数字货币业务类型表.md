# ods_pay_cust.base_data_t_region (数据引入层-客户域-数字货币业务类型表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| region_id | varchar |  | 区域id |
| region_rank | bigint |  | 地区级别(0全国1省市2地区（市）3县 |
| region_superior_id | varchar |  | 上级区域id |
| region_path | varchar |  | 区域存储路径 |
| region_name_py_en | varchar |  | 区域名称英文 |
| region_name | varchar |  | 区域中文名称 |
| region_tel_area_code | varchar |  | 区域电话区号 |
| status | varchar |  | 状态(1:正常，2:停用，9:删除) |
| region_simple_name | varchar |  | 地区简称 |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
