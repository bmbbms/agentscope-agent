# ods_pay_risk.risk_tag_t_tag_info (数据引入层-信用&风控域-标签定义表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| tag_id | varchar |  | 标签ID,一级标签分类编码+_+二级标签分类编码+_+顺序号 |
| tag_name | varchar |  | 标签名称 |
| rel_body_type | varchar |  | 标签所属主体类型,00:商户，01:子商户，02:代理商 |
| item_id | varchar |  | 所属标签分类ID |
| expire_flag | varchar |  | 是否临时标签,0:永久标签，1:临时标签 |
| expire_value | bigint |  | 标签有效期值,正整数 |
| expire_unit | varchar |  | 标签有效期单位,1:分钟，2:小时，3:天，4:月 |
| value_type | varchar |  | 标签值类型,1:String,2:Json |
| trans_flag | varchar |  | 是否影响交易,0:不影响，1:影响 |
| analysis_flag | varchar |  | 是否影响事后分析,0:不影响，1:影响 |
| tag_desc | varchar |  | 标签说明 |
| status | varchar |  | 状态,1:正常，2:停用，9:删除 |
| remark | varchar |  | 备注 |
| create_user | varchar |  | 创建人 |
| create_time | varchar |  | 创建时间 |
| update_user | varchar |  | 更新人 |
| update_time | varchar |  | 更新时间 |
| meta_write_service | varchar |  | 写入服务 |
| meta_ori_table | varchar |  | 原表 |
| meta_is_delete | boolean |  | 主表是否物理删除 true-是, false-否 |
| meta_output_time | timestamp(3) |  | 记录更新时间yyyy-MM-dd HH:mm:ss.SSS |
