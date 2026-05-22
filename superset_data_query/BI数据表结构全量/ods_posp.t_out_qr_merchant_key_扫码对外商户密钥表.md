# ods_posp.t_out_qr_merchant_key (扫码对外商户密钥表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| org_code | varchar |  | 机构号 |
| merch_no | varchar |  | 商户号 |
| sys_pri_key | varchar |  | 系统私钥 |
| sys_pub_key | varchar |  | 系统公钥 |
| mer_pub_key | varchar |  | 商户公钥 |
| status | varchar |  | 状态，0初始，1正常，2停用，9删除 |
| create_date | varchar |  | 创建时间 |
| sign_key | varchar |  | md5 密钥 |
| group_no | varchar |  | 集团用户 |
| access_type | varchar |  | 1-代理商 0-特约商户 2-设备厂商 |
| org_name | varchar |  | 机构名称 |
| remark | varchar |  | 备注 |
| org_source | varchar |  | 来源 1-外接 0-通行证. |
| update_time | varchar |  | 更新时间 |
| update_user | varchar |  | 更新人 |
| create_user | varchar |  | 创建人 |
| trans_type | varchar |  | 交易类型：微信公众号1 微信扫码2 微信刷卡支付3 支付宝扫码4 支付宝刷卡5 支付宝服务窗6 银联行业码7 银联扫码8 银联刷卡9 微信app支付10 qq扫码11  qq刷卡支付12 |
| if_check_merch | varchar |  | 是否检查商户 0否 1是 |
| sys_version | varchar |  | 系统版本 新外接码付配置1 老外接码付0  |
| if_check_term | varchar |  | 是否检查终端 0否 1是 |
