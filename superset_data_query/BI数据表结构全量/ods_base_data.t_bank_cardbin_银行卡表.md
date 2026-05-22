# ods_base_data.t_bank_cardbin (银行卡表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| auto_id | varchar |  | 自动编号 |
| bank_code | varchar |  | 发卡行编号 |
| insuer_name | varchar |  | 发卡行名称 |
| insuer_id | varchar |  | 发卡机构代码 |
| english_cont | varchar |  | 英文名称 |
| fit_track2 | varchar |  | 读取磁道2(磁道信息) |
| fit_offset2 | varchar |  | 起始字节2(磁道信息) |
| fit_length2 | varchar |  | 长度2(磁道信息) |
| fit_track3 | varchar |  | 读取磁道3(磁道信息) |
| fit_offset3 | varchar |  | 起始字节3(磁道信息) |
| fit_length3 | varchar |  | 长度3(磁道信息) |
| pan_length | varchar |  | 长度(主账号) |
| pan_ctt | varchar |  | 主账号 |
| pan_offset2 | varchar |  | 起始字节2(主账号) |
| pan_track2 | varchar |  | 读取磁道2(主账号) |
| pan_offset3 | varchar |  | 起始字节3(主账号) |
| pan_track3 | varchar |  | 读取磁道3(主账号) |
| bin_ctt | varchar |  | 发卡行标识取值(发卡行)卡bin,通过crm_user.pkg_bankcard.f_GetCardBin获取 |
| bin_length | varchar |  | 长度(发卡行) |
| bin_offset2 | varchar |  | 起始字节2(发卡行) |
| bin_track2 | varchar |  | 读取磁道2(发卡行) |
| bin_offset3 | varchar |  | 起始字节3(发卡行) |
| bin_track3 | varchar |  | 读取磁道3(发卡行 |
| card_type | varchar |  |  |
| remark | varchar |  | 备注 |
| addname | varchar |  | 新增人 |
| addtime | varchar |  | 新增时间 |
| uptname | varchar |  | 最后修改人 |
| upttime | varchar |  | 最后修改时间 |
| card_name | varchar |  |  |
| card_flag | varchar |  | 卡类型，0-借记卡，1贷记卡，2预付费卡 |
| org_code | varchar |  | 卡组织标识UnionPay-银联AmEx-美国运通 |
