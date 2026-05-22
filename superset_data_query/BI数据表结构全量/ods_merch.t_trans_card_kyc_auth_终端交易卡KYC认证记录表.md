# ods_merch.t_trans_card_kyc_auth (终端交易卡KYC认证记录表)

| Column | Type | Extra | Comment |
|---|---|---|---|
| record_id | varchar |  | 认证记录ID |
| merch_no | varchar |  | 商户号 |
| term_no | varchar |  | 终端号 |
| card_no | varchar |  | 卡号 |
| cert_name | varchar |  | 持卡人姓名 |
| cert_no | varchar |  | 持卡人身份证号 |
| auth_result | varchar |  | 银行卡鉴权结果，0不通过；1通过 |
| status | varchar |  | 人脸认证状态，0未认证；1认证通过；2认证不通过 |
| face_fail_count | bigint |  | 人脸失败次数 |
| create_time | varchar |  | 创建时间 |
| update_time | varchar |  | 更新时间 |
| face_pic | varchar |  | 人脸照片 |
| request_ip | varchar |  | 请求方ip |
| request_location | varchar |  | 请求方位置信息 |
| term_location | varchar |  | 终端位置信息 |
