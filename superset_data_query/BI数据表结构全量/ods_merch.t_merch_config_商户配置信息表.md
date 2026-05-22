# ods_merch.t_merch_config (商户配置信息表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| merch_no | varchar |  | 商户号 |
| config_key | varchar |  | 配置的键(merch_logo_url 商户logo链接，merch_advertise_url 商户广告链接) |
| config_scope | varchar |  | 配置分类(WHITE 白名单类型，PROP 商户属性) |
| config_val | varchar |  | 配置的值 |
| reverse_field | varchar |  | 配置保留字段，各个配置key可以自定义该字段的内容(商户广告链接 该字段存广告结束时间yyyyMMddHH24miss) |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 修改时间 |
| create_user | varchar |  | 创建人 |
| update_user | varchar |  | 修改人 |
| remark | varchar |  | 备注 |
