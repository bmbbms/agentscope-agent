# ods_pay_cust.agent_t_merch_act_tag (数据引入层-客户域-商户达标标记表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| act_tag_id | varchar |  | 主键id，规则生成 |
| business_type | varchar |  | 业务类型 |
| merch_no | varchar |  | 商户号 |
| act_status | varchar |  | 达标状态 |
| act_type | varchar |  | 达标类型 |
| act_physn_type | varchar |  | 达标机型 |
| act_date | varchar |  | 达标日期 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| act_key_1 | varchar |  | 达标参数1，保存达标需要的参数 |
| act_key_2 | varchar |  | 达标参数2，保存达标需要的参数 |
| act_key_3 | varchar |  | 达标参数3，保存达标需要的参数 |
| physn | varchar |  | 机身号 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
