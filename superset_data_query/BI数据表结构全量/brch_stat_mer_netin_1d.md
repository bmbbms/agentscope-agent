# brch_stat_mer_netin_1d

**表名**: `edw.brch_stat_mer_netin_1d`

## 表结构

| 字段名 | 类型 | 注释 |
|--------|------|------|
| stat_date | double | 统计月份 |
| belong_branch | string | 业务部门 |
| product_type | string | 产品类型 |
| net_type | string | 入网类型(1营业执照，2租赁合同，3小微) |
| prov_code | string | 省份编码 |
| city_code | string | 城市编码 |
| inc_mer_num | double | 新增商户数 |
| stk_mer_num | double | 存量商户数 |
| cancel_mer_num | double | 注销商户数 |
| stop_mer_num | double | 停用商户数 |

## 分区字段

| 字段名 | 类型 | 注释 |
|--------|------|------|
| dt | int | 分区日期 |
