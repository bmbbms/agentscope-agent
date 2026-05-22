# ods_posp.t_f41 (终端表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| f42_id | varchar |  | 客户ID |
| f41 | varchar |  | 终端号 |
| fp41 | varchar |  | 打印终端号 |
| fp43 | varchar |  | 打印商户名称，为空时用客户名称 |
| device_sn | varchar |  | 设备机身号 |
| status | varchar |  | 终端状态：0待启用1启用2停用3注销4闲置 |
| remark | varchar |  | 终端备注 |
| provideform | varchar |  | 机具提供形式 1-租赁 2-购买 |
| region_code | varchar |  | 区域代码（省市区 |
| address | varchar |  | 装机地址 |
| longitude | varchar |  | 经度(根据装机地址算出) |
| latitude | varchar |  | 纬度(根据装机地址算出) |
| f42 | varchar |  |  |
| create_time | varchar |  |  |
| id | varchar |  | 主键 |
| install_time | varchar |  | 装机时间 |
| create_user | varchar |  | 操作人 |
| update_time | varchar |  | 更新时间 |
| action_type | varchar |  | 操作类型 1-新装机；2-加机；3-二维码 |
| terminal_alias | varchar |  | 终端别名 |
| model_id | varchar |  | 机型ID |
| model_name | varchar |  | 机型名称 |
| is_replacement | varchar |  | 是否换机 |
| pieces_num | varchar |  | 打印联数 |
| pieces_seq | varchar |  | 打印顺序 0商户联1银行联2持卡人联 |
| esign_enable | varchar |  | 是否开通电签 0：否1：是 |
| deposit_fee_pack_id | varchar |  | 押金套餐编号，表T_BILL_PACKAGE外键 |
| rent_fee_pack_id | varchar |  | 月租套餐编号，表T_BILL_PACKAGE外键 |
| recv_type | varchar |  | 收取方式：1-线上支付，2-线下支付 |
| auto_active | varchar |  | 商户审核通过后，是否自动激活：1-是，0-否 |
| fp42 | varchar |  | 打印商户号 |
| limit_area | varchar |  | 是否限制交易地区，0 不限制，1 限制 |
| addr_id | varchar |  | 装机地址记录ID |
| cancle_time | varchar |  | 撤机时间 |
| alter_reason | varchar |  | 变更原因 |
| change_status_reason | varchar |  | 终端状态变更原因 |
| change_status_date | varchar |  | 终端状态变更时间 |
| change_status_person | varchar |  | 终端状态变更人 |
| is_push_msg | varchar |  | 是否推送该终端的交易流水  0否1是 |
| nfc_active_flag | varchar |  | NFC激活标志，0：未激活 1已激活 |
| shop_id | varchar |  | 门店ID |
| deposit_amount | varchar |  |  |
| deposit_flag | varchar |  |  |
| reset_manage_pwd | varchar |  |  |
| authorization_pic | varchar |  |  |
| voice_service_fee_id | varchar |  | 音响服务费id |
| voice_communication_fee_id | varchar |  | 音响通讯费id |
