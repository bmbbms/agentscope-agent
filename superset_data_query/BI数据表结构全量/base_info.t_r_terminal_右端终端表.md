# base_info.t_region (行政地区表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| region_id | varchar |  | 区域id |
| region_rank | bigint |  | 地区级别(0全国1省市2地区（市）3县 |
| region_superior_id | varchar |  | 上级区域id |
| region_path | varchar |  | 区域存储路径 |
| region_name_py_en | varchar |  | 区域名称英文 |
| region_name | varchar |  | 区域中文名称 |
| region_tel_area_code | varchar |  | 区域电话区号 |
| status | varchar |  | 状态(1,正常，2,停用，9,删除) |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| region_simple_name | varchar |  | 区域简称 |
