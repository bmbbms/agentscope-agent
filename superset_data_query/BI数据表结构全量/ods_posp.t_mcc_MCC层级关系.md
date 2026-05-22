# ods_posp.t_mcc (MCC层级关系)

| Column | Type | Extra | Comment |
|---|---|---|---|
| mcccode | varchar |  |  |
| mcc_desc | varchar |  |  |
| p_mcccode | varchar |  |  |
| path | varchar |  |  |
| mcc_level | varchar |  |  |
| new_parent | varchar |  | 新上级(价改后) |
| is_free | varchar |  | 是否可开通免签免密，1-是，0-否 |
| small_merchant | varchar |  | 小微商户是否可用，1、可用；0、不可用 |
| deleted | varchar |  | 是否已删除，1、已删除、0、未删除 |
| profession | varchar |  | 自然人行业类别(可疑主体使用) |
| industry_class | varchar |  | 企业行业类别(可疑主体使用) |
| busi_code | varchar |  | 行业类别，见数据字典base_data_user.t_dict.MCC_REL_BUSI_CODE |
| industry_code | varchar |  | 对外行业类型,详细描述查看base_data_user.t_dict.MCC_REL_INDUSTRY_CODE |
