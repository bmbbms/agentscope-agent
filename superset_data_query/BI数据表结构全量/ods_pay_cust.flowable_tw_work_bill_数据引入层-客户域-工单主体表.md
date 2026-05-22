# ods_pay_cust.flowable_tw_work_bill (数据引入层-客户域-工单主体表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| work_id | varchar |  | 工单ID |
| work_def_id | varchar |  | 工单定义ID |
| work_status | varchar |  | 工单状态0待提交1待处理2处理中3已完成4已关闭5已挂起 |
| busi_status | varchar |  | 业务状态0未解决1已解决 |
| merch_no | varchar |  | 商户号 |
| entity_value2 | varchar |  | 实体值2 |
| entity_value3 | varchar |  | 实体值3 |
| entity_value4 | varchar |  | 实体值4 |
| apply_man | varchar |  | 申请人 |
| apply_man_id | varchar |  | 申请人ID |
| create_time | varchar |  | 创建时间 |
| remark | varchar |  | 备注 |
| apply_org_id | varchar |  | 申请人所属平台ID |
| apply_depart_id | varchar |  | 申请人所属部门ID |
| update_time | varchar |  | 更新时间 |
| expire_time | varchar |  | 过期时间 |
| handle_man | varchar |  | 处理人 |
| handle_man_id | varchar |  | 处理人ID |
| end_time | varchar |  | 结束时间 |
| entity_value1 | varchar |  | 实体值1 |
| busi_type | varchar |  | 业务处理方式1电话2短信3线下 |
| urge_time | varchar |  | 催单时间 |
| urge_num | bigint |  | 催单次数 |
| cust_type | varchar |  | 客户类型 |
| cust_no | varchar |  | 客户编号 |
| cust_name | varchar |  | 客户名称 |
| caller_phone | varchar |  | 致电人手机号 |
| caller_name | varchar |  | 致电人姓名 |
| frame_no | varchar |  | 机身号 |
| top_agent | varchar |  | 一级代理商 |
| finish_man | varchar |  | 回访节点之前完结人 |
| finish_time | varchar |  | 非回访节点完结时间 |
| app_version | varchar |  | 创建工单时增加版本号 |
| cust_area_address | varchar |  | 客户所在地址信息 |
| cust_area_code | varchar |  | 客户所在地区码 |
| voucher_phone | varchar |  | 凭证手机号 |
| voucher_upload_time | varchar |  | 凭证上传时间 |
| voucher_upload_status | varchar |  | 凭证上传状态。0-未打开,1-已打开,2-已上传 |
| voucher_sms_time | varchar |  | 发送凭证上传短信时间 |
| product_id | varchar |  | 产品线ID |
| complain_amt | bigint |  | 涉诉金额，单位分 |
| meta_write_service | varchar |  | 写入服务 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_ori_table | varchar |  | 原表 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
