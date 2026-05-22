# base_info.t_l_terminal (左端终端表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| rowkey | varchar |  | rowkey |
| lterm_no | varchar |  | 左端终端号 |
| pterm_no | varchar |  | 打印终端号 |
| pmer_no | varchar |  | 打印商户号 |
| pmer_name | varchar |  | 打印商户名 |
| dev_sn | varchar |  | 设备机身号 |
| status | varchar |  | 终端状态 0待启用1启用2停用3注销 |
| prov_form | varchar |  | 机具提供形式 1-租赁 2-购买 |
| region_code | varchar |  | 区域代码(省市区) |
| region_name | varchar |  | 区域名 |
| addr | varchar |  | 装机地址 |
| lon | varchar |  | 经度 |
| lat | varchar |  | 纬度 |
| add_date | varchar |  | 创建时间 |
| install_date | varchar |  | 装机时间 |
| cancel_date | varchar |  | 撤机时间 |
| alias | varchar |  | 终端别名 |
| mod_id | varchar |  | 机型ID |
| mod_name | varchar |  | 机型名称 |
| act_type | varchar |  | 操作类型 1-新装机；2-加机 |
| is_replace | varchar |  | 是否换机 |
| pieces_num | varchar |  | 打印联数 |
| pieces_seq | varchar |  | 打印顺序 0商户联1银行联2持卡人联 |
| esign_enable | varchar |  | 是否开通电签 |
| lmer_no | varchar |  | 商户号 |
| lmer_name | varchar |  | 商户名称 |
| agt_id | varchar |  | 直属代理商ID |
| agt_name | varchar |  | 直属代理商名称 |
| r_agt_id | varchar |  | 一级代理商ID |
| r_agt_name | varchar |  | 一级代理商名称 |
| agt_path | varchar |  | 代理商路径 |
| belong_branch | varchar |  | 业务部门 |
| clerk_id | varchar |  | 业务员编号 |
| clerk | varchar |  | 业务员名称 |
| deposit | varchar |  | 押金 |
| rent | varchar |  | 月租标准 |
| update_time | varchar |  | 更新时间 |
| type_for | varchar |  | 客供类型 |
| rcev_amt | varchar |  | 服务费 |
| rcev_type | varchar |  | 服务费收取方式 |
| rcev_cycle | varchar |  | 服务费收取周期 |
| att_deposit | varchar |  | 押金单据 |
| att_rent | varchar |  | 租金单据 |
| att_rcev | varchar |  | 服务费单据 |
| alter_reason | varchar |  | 变更原因 |
| change_status_reason | varchar |  | 终端状态变更原因 |
| change_status_date | varchar |  | 终端状态变更时间 |
| busi_type | varchar |  | 业务大类 |
| data_update_time | varchar |  | 最大更新时间 |
| data_from | integer | partition key |  |
