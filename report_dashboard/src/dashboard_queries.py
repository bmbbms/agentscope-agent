# -*- coding: utf-8 -*-
"""
看板数据配置
定义SQL查询和数据获取逻辑

基于正确的月报数据表:
- edw.agt_stat_mer_1m: 商户月统计(新增商户数inc_mer)
  - SUBSTR(data_from, 1, 1)='1' 大POS, ='2' 小POS
- edw.agt_stat_term_1m: 终端月统计(新增终端数inc_term)
  - SUBSTR(product_type, 1, 1)='1' 大POS, ='2' 小POS
- edw.agt_stat_activity_1m: 活跃度月统计(活跃商户数act_mer_cnt)
  - product_type='POSP' 大POS, LIKE 'MPOS%' 小POS
- edw.agt_trd_stat_1m: 交易月统计(交易额amount单位:分,交易笔数count)
  - SUBSTR(busi_type, 1, 1)='2' 小POS, 其他大POS
- edw.trd_stat_merchant_1m: 商户交易月统计
- base_info.t_dict: 数据字典(业务大类映射)
- base_info.t_admusers_info: 代理商信息表
- ods_posp.t_company: 机构公司表

注意:金额单位为分,需要除以1000000转换为万元
"""

# 字段名映射(英文 -> 中文)
FIELD_MAPPING = {
    'month': '月份',
    'total_amount': '交易总金额（万元）',
    'total_count': '交易总笔数（万笔）',
    'avg_amount': '当月笔均金额（元）',
    'active_merchants': '活跃商户数',
    'new_merchants': '新增商户数',
    'new_terminals': '新增终端数',
    'time': '时间',
    'branch': '归属分公司',
    'business_dept': '业务部门',
    'agent_name': '一级代理商名称',
    'prev_amount': '上月交易额（万元）',
    'curr_amount': '本月交易额（万元）',
    'prev_count': '上月笔数',
    'curr_count': '本月笔数',
    'prev_merchants': '上月商户数',
    'curr_merchants': '本月商户数',
    'prev_terminals': '上月终端数',
    'curr_terminals': '本月终端数',
    'mom': '环比',
    'merch_name': '子商户名',
    'busi_type_name': '业务类型',
    'traditional_pos_amount': '传统POS交易金额（万元）',
    'codepay_guduoyun_amount': '外接码付(咕哚云)交易金额（万元）',
    'finance_pos_amount': '理财POS交易金额（万元）',
    'traditional_pos_count': '传统POS交易笔数（万笔）',
    'codepay_guduoyun_count': '外接码付(咕哚云)交易笔数（万笔）',
    'finance_pos_count': '理财POS交易笔数（万笔）',
    # 小POS产品交易金额（亿元）
    'shangwangbao_amount': '上网宝交易金额（亿元）',
    'laodianqian_amount': '老电签交易金额（亿元）',
    'weidianqian_amount': '微电签交易金额（亿元）',
    'weizhineng_amount': '微智能交易金额（亿元）',
    'changxiangban_amount': '立刷畅享版交易金额（亿元）',
    'qijiban_amount': '骐骥版交易金额（亿元）',
    'xiaolanya_amount': '立刷小蓝牙交易金额（亿元）',
    # 小POS产品新增终端（万台）
    'shangwangbao_terminal': '上网宝新增终端（万台）',
    'laodianqian_terminal': '老电签新增终端（万台）',
    'weidianqian_terminal': '微电签新增终端（万台）',
    'weizhineng_terminal': '微智能新增终端（万台）',
    'changxiangban_terminal': '立刷畅享版新增终端（万台）',
    'qijiban_terminal': '骐骥版新增终端（万台）',
    'xiaolanya_terminal': '立刷小蓝牙新增终端（万台）',
    # 小POS终端绑定、激活、活跃趋势
    'bind_terminals': '新增终端绑定（台）',
    'active_terminals': '一阶段激活数（台）',
    'term_active_merchants': '活跃商户数（台）',
}


# ========== 大POS查询 ==========

# 大POS月度总体数据(金额从分转换为万元)
SQL_LARGE_POS_MONTHLY = """
WITH trd_data AS (
    SELECT
        dt,
        SUM(CAST(amount AS DOUBLE)) / 1000000 as total_amount,
        SUM(CAST(count AS DOUBLE)) / 10000 as total_count
    FROM edw.agt_trd_stat_1m
    WHERE SUBSTR(busi_type, 1, 1) != '2'
      AND dt >= {start_dt} AND dt <= {end_dt}
    GROUP BY dt
),
mer_data AS (
    SELECT
        dt,
        SUM(inc_mer) as new_merchants
    FROM edw.agt_stat_mer_1m
    WHERE SUBSTR(data_from, 1, 1) = '1'
      AND dt >= {start_dt} AND dt <= {end_dt}
    GROUP BY dt
),
act_data AS (
    SELECT
        dt,
        SUM(CAST(act_mer_cnt AS BIGINT)) as active_merchants
    FROM edw.agt_stat_activity_1m
    WHERE product_type = 'POSP'
      AND dt >= {start_dt} AND dt <= {end_dt}
    GROUP BY dt
)
SELECT
    t.dt as month,
    ROUND(t.total_amount) as total_amount,
    ROUND(t.total_count) as total_count,
    ROUND(CASE WHEN t.total_count > 0 THEN t.total_amount / t.total_count ELSE 0 END) as avg_amount,
    a.active_merchants,
    m.new_merchants
FROM trd_data t
LEFT JOIN mer_data m ON t.dt = m.dt
LEFT JOIN act_data a ON t.dt = a.dt
ORDER BY t.dt
"""

# 大POS近两年运营数据
SQL_LARGE_POS_TWO_YEAR = """
WITH trd_data AS (
    SELECT
        dt,
        SUM(CAST(amount AS DOUBLE)) / 1000000 as total_amount
    FROM edw.agt_trd_stat_1m
    WHERE SUBSTR(busi_type, 1, 1) != '2'
      AND dt >= {start_dt} AND dt <= {end_dt}
    GROUP BY dt
),
mer_data AS (
    SELECT
        dt,
        SUM(inc_mer) as new_merchants
    FROM edw.agt_stat_mer_1m
    WHERE SUBSTR(data_from, 1, 1) = '1'
      AND dt >= {start_dt} AND dt <= {end_dt}
    GROUP BY dt
),
act_data AS (
    SELECT
        dt,
        SUM(CAST(act_mer_cnt AS BIGINT)) as active_merchants
    FROM edw.agt_stat_activity_1m
    WHERE product_type = 'POSP'
      AND dt >= {start_dt} AND dt <= {end_dt}
    GROUP BY dt
)
SELECT
    t.dt as time,
    ROUND(t.total_amount) as total_amount,
    m.new_merchants,
    a.active_merchants
FROM trd_data t
LEFT JOIN mer_data m ON t.dt = m.dt
LEFT JOIN act_data a ON t.dt = a.dt
ORDER BY t.dt
"""

# 大POS分公司交易环比下降TOP10
# 按差值最小（下降最多或增长最少）取前10名，展示时按环比升序
# 通过agt_trd_stat_1m关联t_admusers_info获取分公司数据
# 过滤条件：业务部门名称='分公司'
# SUBSTR(busi_type, 1, 1) != '2' 对应大POS
SQL_LARGE_POS_BRANCH_DECLINE = """
SELECT
    branch,
    ROUND(prev_amount) as prev_amount,
    ROUND(curr_amount) as curr_amount,
    ROUND(mom * 100, 2) as mom
FROM (
    SELECT
        branch,
        prev_amount,
        curr_amount,
        mom,
        ROW_NUMBER() OVER (ORDER BY diff ASC) as rn
    FROM (
        SELECT
            coalesce(t0.org_company, '其他') as branch,
            p.prev_amount,
            c.curr_amount,
            (c.curr_amount - p.prev_amount) / p.prev_amount as mom,
            c.curr_amount - p.prev_amount as diff
        FROM (
            SELECT
                t.branch_company,
                SUM(CAST(f.amount AS DOUBLE)) / 1000000 as curr_amount
            FROM edw.agt_trd_stat_1m f
            LEFT JOIN base_info.t_admusers_info t ON f.r_agt_id = t.user_id
            LEFT JOIN ods_posp.t_company t1 ON t.belong_branch = t1.org_id
            WHERE f.dt = {current_dt}
              AND SUBSTR(f.busi_type, 1, 1) != '2'
              AND t1.org_company = '分公司'
            GROUP BY t.branch_company
        ) c
        JOIN (
            SELECT
                t.branch_company,
                SUM(CAST(f.amount AS DOUBLE)) / 1000000 as prev_amount
            FROM edw.agt_trd_stat_1m f
            LEFT JOIN base_info.t_admusers_info t ON f.r_agt_id = t.user_id
            LEFT JOIN ods_posp.t_company t1 ON t.belong_branch = t1.org_id
            WHERE f.dt = {previous_dt}
              AND SUBSTR(f.busi_type, 1, 1) != '2'
              AND t1.org_company = '分公司'
            GROUP BY t.branch_company
        ) p ON c.branch_company = p.branch_company
        LEFT JOIN ods_posp.t_company t0 ON c.branch_company = t0.org_id
        WHERE p.prev_amount > 0
          AND t0.org_company IS NOT NULL
          AND t0.data_type = '0'
          AND t0.parent_org_id != '0'
          AND t0.org_company NOT LIKE '%验证%'
    ) ranked
) filtered
WHERE rn <= 10
ORDER BY mom ASC
"""

# 大POS分公司商户环比下降TOP10
# 按差值最小（下降最多或增长最少）取前10名，展示时按环比升序
# 通过agt_stat_mer_1m关联t_admusers_info获取分公司数据
# 过滤条件：业务部门名称='分公司'
# SUBSTR(data_from, 1, 1) = '1' 对应大POS
SQL_LARGE_POS_BRANCH_MERCHANT_DECLINE = """
SELECT
    branch,
    prev_merchants,
    curr_merchants,
    ROUND(mom * 100, 2) as mom
FROM (
    SELECT
        branch,
        prev_merchants,
        curr_merchants,
        mom,
        ROW_NUMBER() OVER (ORDER BY diff ASC) as rn
    FROM (
        SELECT
            coalesce(t0.org_company, '其他') as branch,
            p.prev_merchants,
            c.curr_merchants,
            (c.curr_merchants - p.prev_merchants) / CAST(p.prev_merchants AS DOUBLE) as mom,
            c.curr_merchants - p.prev_merchants as diff
        FROM (
            SELECT
                t.branch_company,
                SUM(f.inc_mer) as curr_merchants
            FROM edw.agt_stat_mer_1m f
            LEFT JOIN base_info.t_admusers_info t ON f.r_agt_id = t.user_id
            LEFT JOIN ods_posp.t_company t1 ON t.belong_branch = t1.org_id
            WHERE f.dt = {current_month}
              AND SUBSTR(f.data_from, 1, 1) = '1'
              AND t1.org_company = '分公司'
            GROUP BY t.branch_company
        ) c
        JOIN (
            SELECT
                t.branch_company,
                SUM(f.inc_mer) as prev_merchants
            FROM edw.agt_stat_mer_1m f
            LEFT JOIN base_info.t_admusers_info t ON f.r_agt_id = t.user_id
            LEFT JOIN ods_posp.t_company t1 ON t.belong_branch = t1.org_id
            WHERE f.dt = {previous_month}
              AND SUBSTR(f.data_from, 1, 1) = '1'
              AND t1.org_company = '分公司'
            GROUP BY t.branch_company
        ) p ON c.branch_company = p.branch_company
        LEFT JOIN ods_posp.t_company t0 ON c.branch_company = t0.org_id
        WHERE p.prev_merchants > 0
          AND t0.org_company IS NOT NULL
          AND t0.data_type = '0'
          AND t0.parent_org_id != '0'
          AND t0.org_company NOT LIKE '%验证%'
    ) ranked
) filtered
WHERE rn <= 10
ORDER BY mom ASC
"""

# 大POS商户交易下降TOP10
# 环比下降TOP10:筛选负数结果,按差值最小取前10,再按环比升序展示
# 按商户号汇总所有业务类型的交易额，关联t_merch_info获取标准商户名
SQL_LARGE_POS_MERCHANT_DECLINE = """
WITH current_month AS (
    SELECT
        lmer_no,
        MAX(lmer_name) as lmer_name,
        SUM(CAST(amount AS DOUBLE)) / 1000000 as curr_amount
    FROM edw.trd_stat_merchant_1m
    WHERE dt = {current_month}
    GROUP BY lmer_no
),
previous_month AS (
    SELECT
        lmer_no,
        SUM(CAST(amount AS DOUBLE)) / 1000000 as prev_amount
    FROM edw.trd_stat_merchant_1m
    WHERE dt = {previous_month}
    GROUP BY lmer_no
),
top10 AS (
    SELECT
        c.lmer_no,
        COALESCE(m.merch_name, c.lmer_name) as merch_name,
        p.prev_amount,
        c.curr_amount,
        (c.curr_amount - p.prev_amount) / p.prev_amount as mom
    FROM current_month c
    JOIN previous_month p ON c.lmer_no = p.lmer_no
    LEFT JOIN ods_merch.t_merch_info m ON c.lmer_no = m.merch_no
    WHERE p.prev_amount > 0
      AND c.curr_amount - p.prev_amount < 0
    ORDER BY (c.curr_amount - p.prev_amount) ASC
    LIMIT 10
)
SELECT
    t.merch_name,
    ROUND(t.prev_amount) as prev_amount,
    ROUND(t.curr_amount) as curr_amount,
    ROUND(t.mom * 100, 2) as mom
FROM top10 t
ORDER BY t.mom ASC
"""

# 大POS商户交易上涨TOP10
# 环比上涨TOP10:筛选正数结果,按差值最大取前10,再按环比降序展示
# 按商户号汇总所有业务类型的交易额，关联t_merch_info获取标准商户名
SQL_LARGE_POS_MERCHANT_INCREASE = """
WITH current_month AS (
    SELECT
        lmer_no,
        MAX(lmer_name) as lmer_name,
        SUM(CAST(amount AS DOUBLE)) / 1000000 as curr_amount
    FROM edw.trd_stat_merchant_1m
    WHERE dt = {current_month}
    GROUP BY lmer_no
),
previous_month AS (
    SELECT
        lmer_no,
        SUM(CAST(amount AS DOUBLE)) / 1000000 as prev_amount
    FROM edw.trd_stat_merchant_1m
    WHERE dt = {previous_month}
    GROUP BY lmer_no
),
top10 AS (
    SELECT
        c.lmer_no,
        COALESCE(m.merch_name, c.lmer_name) as merch_name,
        p.prev_amount,
        c.curr_amount,
        (c.curr_amount - p.prev_amount) / p.prev_amount as mom
    FROM current_month c
    JOIN previous_month p ON c.lmer_no = p.lmer_no
    LEFT JOIN ods_merch.t_merch_info m ON c.lmer_no = m.merch_no
    WHERE p.prev_amount > 0
      AND c.curr_amount - p.prev_amount > 0
    ORDER BY (c.curr_amount - p.prev_amount) DESC
    LIMIT 10
)
SELECT
    t.merch_name,
    ROUND(t.prev_amount) as prev_amount,
    ROUND(t.curr_amount) as curr_amount,
    ROUND(t.mom * 100, 2) as mom
FROM top10 t
ORDER BY t.mom DESC
"""

# 大POS分公司交易上涨TOP10
# 通过agt_trd_stat_1m关联t_admusers_info获取分公司数据
# 过滤条件：业务部门名称='分公司'
# SUBSTR(busi_type, 1, 1) != '2' 对应大POS
SQL_LARGE_POS_BRANCH_INCREASE = """
SELECT
    branch,
    ROUND(prev_amount) as prev_amount,
    ROUND(curr_amount) as curr_amount,
    ROUND(mom * 100, 2) as mom
FROM (
    SELECT
        branch,
        prev_amount,
        curr_amount,
        mom,
        ROW_NUMBER() OVER (ORDER BY diff DESC) as rn
    FROM (
        SELECT
            coalesce(t0.org_company, '其他') as branch,
            p.prev_amount,
            c.curr_amount,
            (c.curr_amount - p.prev_amount) / p.prev_amount as mom,
            c.curr_amount - p.prev_amount as diff
        FROM (
            SELECT
                t.branch_company,
                SUM(CAST(f.amount AS DOUBLE)) / 1000000 as curr_amount
            FROM edw.agt_trd_stat_1m f
            LEFT JOIN base_info.t_admusers_info t ON f.r_agt_id = t.user_id
            LEFT JOIN ods_posp.t_company t1 ON t.belong_branch = t1.org_id
            WHERE f.dt = {current_dt}
              AND SUBSTR(f.busi_type, 1, 1) != '2'
              AND t1.org_company = '分公司'
            GROUP BY t.branch_company
        ) c
        JOIN (
            SELECT
                t.branch_company,
                SUM(CAST(f.amount AS DOUBLE)) / 1000000 as prev_amount
            FROM edw.agt_trd_stat_1m f
            LEFT JOIN base_info.t_admusers_info t ON f.r_agt_id = t.user_id
            LEFT JOIN ods_posp.t_company t1 ON t.belong_branch = t1.org_id
            WHERE f.dt = {previous_dt}
              AND SUBSTR(f.busi_type, 1, 1) != '2'
              AND t1.org_company = '分公司'
            GROUP BY t.branch_company
        ) p ON c.branch_company = p.branch_company
        LEFT JOIN ods_posp.t_company t0 ON c.branch_company = t0.org_id
        WHERE p.prev_amount > 0
          AND t0.org_company IS NOT NULL
          AND t0.data_type = '0'
          AND t0.parent_org_id != '0'
          AND t0.org_company NOT LIKE '%验证%'
    ) ranked
) filtered
WHERE rn <= 10
ORDER BY mom DESC
"""

# 大POS分公司商户上涨TOP10
# 通过agt_stat_mer_1m关联t_admusers_info获取分公司数据
# 过滤条件：业务部门名称='分公司'
# SUBSTR(data_from, 1, 1) = '1' 对应大POS
SQL_LARGE_POS_BRANCH_MERCHANT_INCREASE = """
SELECT
    branch,
    prev_merchants,
    curr_merchants,
    ROUND(mom * 100, 2) as mom
FROM (
    SELECT
        branch,
        prev_merchants,
        curr_merchants,
        mom,
        ROW_NUMBER() OVER (ORDER BY diff DESC) as rn
    FROM (
        SELECT
            coalesce(t0.org_company, '其他') as branch,
            p.prev_merchants,
            c.curr_merchants,
            (c.curr_merchants - p.prev_merchants) / CAST(p.prev_merchants AS DOUBLE) as mom,
            c.curr_merchants - p.prev_merchants as diff
        FROM (
            SELECT
                t.branch_company,
                SUM(f.inc_mer) as curr_merchants
            FROM edw.agt_stat_mer_1m f
            LEFT JOIN base_info.t_admusers_info t ON f.r_agt_id = t.user_id
            LEFT JOIN ods_posp.t_company t1 ON t.belong_branch = t1.org_id
            WHERE f.dt = {current_month}
              AND SUBSTR(f.data_from, 1, 1) = '1'
              AND t1.org_company = '分公司'
            GROUP BY t.branch_company
        ) c
        JOIN (
            SELECT
                t.branch_company,
                SUM(f.inc_mer) as prev_merchants
            FROM edw.agt_stat_mer_1m f
            LEFT JOIN base_info.t_admusers_info t ON f.r_agt_id = t.user_id
            LEFT JOIN ods_posp.t_company t1 ON t.belong_branch = t1.org_id
            WHERE f.dt = {previous_month}
              AND SUBSTR(f.data_from, 1, 1) = '1'
              AND t1.org_company = '分公司'
            GROUP BY t.branch_company
        ) p ON c.branch_company = p.branch_company
        LEFT JOIN ods_posp.t_company t0 ON c.branch_company = t0.org_id
        WHERE p.prev_merchants > 0
          AND t0.org_company IS NOT NULL
          AND t0.data_type = '0'
          AND t0.parent_org_id != '0'
          AND t0.org_company NOT LIKE '%验证%'
    ) ranked
) filtered
WHERE rn <= 10
ORDER BY mom DESC
"""

# 业务类型交易金额趋势(大POS)
# busi_type格式: 第一位区分产品类型(1=大POS, 2=小POS)
# 大POS业务类型代码:
#   1001=传统POS
#   1003=理财POS
#   8001=外接码付(咕哴云)
SQL_BUSINESS_TYPE_AMOUNT = """
SELECT
    dt as month,
    ROUND(SUM(CASE WHEN f.busi_type = '1001' THEN CAST(f.amount AS DOUBLE) ELSE 0 END) / 1000000) as traditional_pos_amount,
    ROUND(SUM(CASE WHEN f.busi_type = '1003' THEN CAST(f.amount AS DOUBLE) ELSE 0 END) / 1000000) as finance_pos_amount,
    ROUND(SUM(CASE WHEN f.busi_type = '8001' THEN CAST(f.amount AS DOUBLE) ELSE 0 END) / 1000000) as codepay_guduoyun_amount
FROM edw.agt_trd_stat_1m f
WHERE SUBSTR(f.busi_type, 1, 1) != '2'
  AND dt >= {start_dt} AND dt <= {end_dt}
GROUP BY dt
ORDER BY dt
"""

# 业务类型交易笔数趋势(大POS)
# busi_type格式: 第一位区分产品类型(1=大POS, 2=小POS)
# 大POS业务类型代码:
#   1001=传统POS
#   1003=理财POS
#   8001=外接码付(咕哴云)
SQL_BUSINESS_TYPE_COUNT = """
SELECT
    dt as month,
    ROUND(SUM(CASE WHEN f.busi_type = '1001' THEN CAST(f.count AS DOUBLE) ELSE 0 END) / 10000,1) as traditional_pos_count,
    ROUND(SUM(CASE WHEN f.busi_type = '1003' THEN CAST(f.count AS DOUBLE) ELSE 0 END) / 10000,1) as finance_pos_count,
    ROUND(SUM(CASE WHEN f.busi_type = '8001' THEN CAST(f.count AS DOUBLE) ELSE 0 END) / 10000) as codepay_guduoyun_count
FROM edw.agt_trd_stat_1m f
WHERE SUBSTR(f.busi_type, 1, 1) != '2'
  AND dt >= {start_dt} AND dt <= {end_dt}
GROUP BY dt
ORDER BY dt
"""


# ========== 小POS(立刷)查询 ==========

# 小POS月度总体数据
SQL_SMALL_POS_MONTHLY = """
WITH trd_data AS (
    SELECT
        dt,
        SUM(CAST(amount AS DOUBLE)) / 1000000 as total_amount,
        SUM(CAST(count AS DOUBLE)) / 10000 as total_count
    FROM edw.agt_trd_stat_1m
    WHERE SUBSTR(busi_type, 1, 1) = '2'
      AND dt >= {start_dt} AND dt <= {end_dt}
    GROUP BY dt
),
mer_data AS (
    SELECT
        dt,
        SUM(inc_mer) as new_merchants
    FROM edw.agt_stat_mer_1m
    WHERE SUBSTR(data_from, 1, 1) = '2'
      AND dt >= {start_dt} AND dt <= {end_dt}
    GROUP BY dt
),
act_data AS (
    SELECT
        dt,
        SUM(CAST(act_mer_cnt AS BIGINT)) as active_merchants
    FROM edw.agt_stat_activity_1m
    WHERE product_type LIKE 'MPOS%'
      AND dt >= {start_dt} AND dt <= {end_dt}
    GROUP BY dt
),
term_data AS (
    SELECT
        dt,
        SUM(CAST(inc_term AS BIGINT)) as new_terminals
    FROM edw.agt_stat_term_1m
    WHERE SUBSTR(product_type, 1, 1) = '2'
      AND dt >= {start_dt} AND dt <= {end_dt}
    GROUP BY dt
)
SELECT
    t.dt as month,
    ROUND(t.total_amount) as total_amount,
    ROUND(t.total_count) as total_count,
    ROUND(CASE WHEN t.total_count > 0 THEN t.total_amount / t.total_count ELSE 0 END) as avg_amount,
    a.active_merchants,
    m.new_merchants,
    te.new_terminals
FROM trd_data t
LEFT JOIN mer_data m ON t.dt = m.dt
LEFT JOIN act_data a ON t.dt = a.dt
LEFT JOIN term_data te ON t.dt = te.dt
ORDER BY t.dt
"""

# 小POS近两年运营数据
SQL_SMALL_POS_TWO_YEAR = """
WITH trd_data AS (
    SELECT
        dt,
        SUM(CAST(amount AS DOUBLE)) / 1000000 as total_amount
    FROM edw.agt_trd_stat_1m
    WHERE SUBSTR(busi_type, 1, 1) = '2'
      AND dt >= {start_dt} AND dt <= {end_dt}
    GROUP BY dt
),
mer_data AS (
    SELECT
        dt,
        SUM(inc_mer) as new_merchants
    FROM edw.agt_stat_mer_1m
    WHERE SUBSTR(data_from, 1, 1) = '2'
      AND dt >= {start_dt} AND dt <= {end_dt}
    GROUP BY dt
)
SELECT
    t.dt as time,
    ROUND(t.total_amount) as total_amount,
    m.new_merchants
FROM trd_data t
LEFT JOIN mer_data m ON t.dt = m.dt
ORDER BY t.dt
"""

# 小POS服务商交易下降TOP10(一级代理商)
# 环比下降TOP10:筛选负数结果,按差值最小取前10,再按环比升序展示
# 排除服务商名称为"其他"的记录,按公司名称汇总(一个公司可能有多个代理商ID)
SQL_SMALL_POS_AGENT_DECLINE = """
SELECT
    agent_name,
    ROUND(prev_amount) as prev_amount,
    ROUND(curr_amount) as curr_amount,
    ROUND(mom * 100, 2) as mom
FROM (
    SELECT
        agent_name,
        prev_amount,
        curr_amount,
        mom,
        ROW_NUMBER() OVER (ORDER BY diff ASC) as rn
    FROM (
        SELECT
            c.agent_name,
            p.prev_amount,
            c.curr_amount,
            (c.curr_amount - p.prev_amount) / p.prev_amount as mom,
            c.curr_amount - p.prev_amount as diff
        FROM (
            SELECT
                COALESCE(t.company_name, t.name) as agent_name,
                SUM(CAST(f.amount AS DOUBLE)) / 1000000 as curr_amount
            FROM edw.agt_trd_stat_1m f
            LEFT JOIN base_info.t_admusers_info t ON f.r_agt_id = t.user_id
            WHERE SUBSTR(f.busi_type, 1, 1) = '2'
              AND f.dt = {current_dt}
              AND COALESCE(t.company_name, t.name) IS NOT NULL
            GROUP BY COALESCE(t.company_name, t.name)
        ) c
        JOIN (
            SELECT
                COALESCE(t.company_name, t.name) as agent_name,
                SUM(CAST(f.amount AS DOUBLE)) / 1000000 as prev_amount
            FROM edw.agt_trd_stat_1m f
            LEFT JOIN base_info.t_admusers_info t ON f.r_agt_id = t.user_id
            WHERE SUBSTR(f.busi_type, 1, 1) = '2'
              AND f.dt = {previous_dt}
              AND COALESCE(t.company_name, t.name) IS NOT NULL
            GROUP BY COALESCE(t.company_name, t.name)
        ) p ON c.agent_name = p.agent_name
        WHERE p.prev_amount > 0
          AND c.curr_amount - p.prev_amount < 0
    ) ranked
) filtered
WHERE rn <= 10
ORDER BY mom ASC
"""

# 小POS服务商商户下降TOP10(一级代理商)
# 环比下降TOP10:筛选负数结果,按差值最小取前10,再按环比升序展示
# 排除服务商名称为"其他"的记录,按公司名称汇总(一个公司可能有多个代理商ID)
SQL_SMALL_POS_AGENT_MERCHANT_DECLINE = """
SELECT
    agent_name,
    prev_merchants,
    curr_merchants,
    ROUND(mom * 100, 2) as mom
FROM (
    SELECT
        agent_name,
        prev_merchants,
        curr_merchants,
        mom,
        ROW_NUMBER() OVER (ORDER BY diff ASC) as rn
    FROM (
        SELECT
            c.agent_name,
            p.prev_merchants,
            c.curr_merchants,
            (c.curr_merchants - p.prev_merchants) / CAST(p.prev_merchants AS DOUBLE) as mom,
            c.curr_merchants - p.prev_merchants as diff
        FROM (
            SELECT
                COALESCE(t.company_name, t.name) as agent_name,
                SUM(m.inc_mer) as curr_merchants
            FROM edw.agt_stat_mer_1m m
            LEFT JOIN base_info.t_admusers_info t ON m.r_agt_id = t.user_id
            WHERE SUBSTR(m.data_from, 1, 1) = '2'
              AND m.dt = {current_month}
              AND COALESCE(t.company_name, t.name) IS NOT NULL
            GROUP BY COALESCE(t.company_name, t.name)
        ) c
        JOIN (
            SELECT
                COALESCE(t.company_name, t.name) as agent_name,
                SUM(m.inc_mer) as prev_merchants
            FROM edw.agt_stat_mer_1m m
            LEFT JOIN base_info.t_admusers_info t ON m.r_agt_id = t.user_id
            WHERE SUBSTR(m.data_from, 1, 1) = '2'
              AND m.dt = {previous_month}
              AND COALESCE(t.company_name, t.name) IS NOT NULL
            GROUP BY COALESCE(t.company_name, t.name)
        ) p ON c.agent_name = p.agent_name
        WHERE p.prev_merchants > 0
          AND c.curr_merchants - p.prev_merchants < 0
    ) ranked
) filtered
WHERE rn <= 10
ORDER BY mom ASC
"""

# 小POS服务商交易上涨TOP10(一级代理商)
# 环比上涨TOP10:筛选正数结果,按差值最大取前10,再按环比降序展示
# 排除服务商名称为"其他"的记录,按公司名称汇总(一个公司可能有多个代理商ID)
SQL_SMALL_POS_AGENT_INCREASE = """
SELECT
    agent_name,
    ROUND(prev_amount) as prev_amount,
    ROUND(curr_amount) as curr_amount,
    ROUND(mom * 100, 2) as mom
FROM (
    SELECT
        agent_name,
        prev_amount,
        curr_amount,
        mom,
        ROW_NUMBER() OVER (ORDER BY diff DESC) as rn
    FROM (
        SELECT
            c.agent_name,
            p.prev_amount,
            c.curr_amount,
            (c.curr_amount - p.prev_amount) / p.prev_amount as mom,
            c.curr_amount - p.prev_amount as diff
        FROM (
            SELECT
                COALESCE(t.company_name, t.name) as agent_name,
                SUM(CAST(f.amount AS DOUBLE)) / 1000000 as curr_amount
            FROM edw.agt_trd_stat_1m f
            LEFT JOIN base_info.t_admusers_info t ON f.r_agt_id = t.user_id
            WHERE SUBSTR(f.busi_type, 1, 1) = '2'
              AND f.dt = {current_dt}
              AND COALESCE(t.company_name, t.name) IS NOT NULL
            GROUP BY COALESCE(t.company_name, t.name)
        ) c
        JOIN (
            SELECT
                COALESCE(t.company_name, t.name) as agent_name,
                SUM(CAST(f.amount AS DOUBLE)) / 1000000 as prev_amount
            FROM edw.agt_trd_stat_1m f
            LEFT JOIN base_info.t_admusers_info t ON f.r_agt_id = t.user_id
            WHERE SUBSTR(f.busi_type, 1, 1) = '2'
              AND f.dt = {previous_dt}
              AND COALESCE(t.company_name, t.name) IS NOT NULL
            GROUP BY COALESCE(t.company_name, t.name)
        ) p ON c.agent_name = p.agent_name
        WHERE p.prev_amount > 0
          AND c.curr_amount - p.prev_amount > 0
    ) ranked
) filtered
WHERE rn <= 10
ORDER BY mom DESC
"""

# 小POS服务商商户上涨TOP10(一级代理商)
# 环比上涨TOP10:筛选正数结果,按差值最大取前10,再按环比降序展示
# 排除服务商名称为"其他"的记录,按公司名称汇总(一个公司可能有多个代理商ID)
SQL_SMALL_POS_AGENT_MERCHANT_INCREASE = """
SELECT
    agent_name,
    prev_merchants,
    curr_merchants,
    ROUND(mom * 100, 2) as mom
FROM (
    SELECT
        agent_name,
        prev_merchants,
        curr_merchants,
        mom,
        ROW_NUMBER() OVER (ORDER BY diff DESC) as rn
    FROM (
        SELECT
            c.agent_name,
            p.prev_merchants,
            c.curr_merchants,
            (c.curr_merchants - p.prev_merchants) / CAST(p.prev_merchants AS DOUBLE) as mom,
            c.curr_merchants - p.prev_merchants as diff
        FROM (
            SELECT
                COALESCE(t.company_name, t.name) as agent_name,
                SUM(m.inc_mer) as curr_merchants
            FROM edw.agt_stat_mer_1m m
            LEFT JOIN base_info.t_admusers_info t ON m.r_agt_id = t.user_id
            WHERE SUBSTR(m.data_from, 1, 1) = '2'
              AND m.dt = {current_month}
              AND COALESCE(t.company_name, t.name) IS NOT NULL
            GROUP BY COALESCE(t.company_name, t.name)
        ) c
        JOIN (
            SELECT
                COALESCE(t.company_name, t.name) as agent_name,
                SUM(m.inc_mer) as prev_merchants
            FROM edw.agt_stat_mer_1m m
            LEFT JOIN base_info.t_admusers_info t ON m.r_agt_id = t.user_id
            WHERE SUBSTR(m.data_from, 1, 1) = '2'
              AND m.dt = {previous_month}
              AND COALESCE(t.company_name, t.name) IS NOT NULL
            GROUP BY COALESCE(t.company_name, t.name)
        ) p ON c.agent_name = p.agent_name
        WHERE p.prev_merchants > 0
          AND c.curr_merchants - p.prev_merchants > 0
    ) ranked
) filtered
WHERE rn <= 10
ORDER BY mom DESC
"""

# 小POS各产品交易金额趋势
# 使用edw.trd_stat_term_model_1m表，通过physn_type关联产品信息
# 产品映射：通过product_type映射到mpos_type
SQL_SMALL_POS_PRODUCT_AMOUNT = """
SELECT
    dt as month,
    ROUND(SUM(CASE WHEN mpos_type = '上网宝' THEN CAST(amt AS DOUBLE) ELSE 0 END) / 10000000000, 1) as shangwangbao_amount,
    ROUND(SUM(CASE WHEN mpos_type = '老电签' THEN CAST(amt AS DOUBLE) ELSE 0 END) / 10000000000, 1) as laodianqian_amount,
    ROUND(SUM(CASE WHEN mpos_type = '微电签' THEN CAST(amt AS DOUBLE) ELSE 0 END) / 10000000000, 1) as weidianqian_amount,
    ROUND(SUM(CASE WHEN mpos_type = '微智能' THEN CAST(amt AS DOUBLE) ELSE 0 END) / 10000000000, 1) as weizhineng_amount,
    ROUND(SUM(CASE WHEN mpos_type = '立刷畅享版' THEN CAST(amt AS DOUBLE) ELSE 0 END) / 10000000000, 1) as changxiangban_amount,
    ROUND(SUM(CASE WHEN mpos_type = '骐骥版' THEN CAST(amt AS DOUBLE) ELSE 0 END) / 10000000000, 1) as qijiban_amount,
    ROUND(SUM(CASE WHEN mpos_type = '立刷小蓝牙' THEN CAST(amt AS DOUBLE) ELSE 0 END) / 10000000000, 1) as xiaolanya_amount
FROM (
    SELECT
        f.dt,
        f.amt,
        CASE
            WHEN t.product_type IN ('2', '3') THEN '老电签'
            WHEN t.product_type IN ('8', '9', '11') THEN '立刷畅享版'
            WHEN t.product_type IN ('1000010', '1000011', '1000012') THEN '骐骥版'
            WHEN t.product_type IN ('1', '7') THEN '上网宝'
            WHEN t.product_type IN ('4', '6', '14', '1000013') THEN '微电签'
            WHEN t.product_type IN ('5', '10') THEN '微智能'
            ELSE '立刷小蓝牙'
        END as mpos_type
    FROM edw.trd_stat_term_model_1m f
    LEFT JOIN ods_pay_cust.micro_pos_t_device_product_info t ON f.physn_type = t.device_type
    WHERE SUBSTR(f.busi_type, 1, 1) = '2'
      AND f.dt >= {start_dt} AND f.dt <= {end_dt}
) product_data
GROUP BY dt
ORDER BY dt
"""

# 小POS各产品新增终端趋势
# 使用edw.agt_stat_term_1m表，通过product_type关联产品信息
SQL_SMALL_POS_PRODUCT_TERMINAL = """
SELECT
    dt as month,
    ROUND(SUM(CASE WHEN mpos_type = '上网宝' THEN inc_term ELSE 0 END) / 10000, 2) as shangwangbao_terminal,
    ROUND(SUM(CASE WHEN mpos_type = '老电签' THEN inc_term ELSE 0 END) / 10000, 2) as laodianqian_terminal,
    ROUND(SUM(CASE WHEN mpos_type = '微电签' THEN inc_term ELSE 0 END) / 10000, 1) as weidianqian_terminal,
    ROUND(SUM(CASE WHEN mpos_type = '微智能' THEN inc_term ELSE 0 END) / 10000, 1) as weizhineng_terminal,
    ROUND(SUM(CASE WHEN mpos_type = '立刷畅享版' THEN inc_term ELSE 0 END) / 10000, 1) as changxiangban_terminal,
    ROUND(SUM(CASE WHEN mpos_type = '骐骥版' THEN inc_term ELSE 0 END) / 10000, 2) as qijiban_terminal,
    ROUND(SUM(CASE WHEN mpos_type = '立刷小蓝牙' THEN inc_term ELSE 0 END) / 10000, 2) as xiaolanya_terminal
FROM (
    SELECT
        f.dt,
        CAST(f.inc_term AS DOUBLE) as inc_term,
        CASE
            WHEN t.product_type IN ('2', '3') THEN '老电签'
            WHEN t.product_type IN ('8', '9', '11') THEN '立刷畅享版'
            WHEN t.product_type IN ('1000010', '1000011', '1000012') THEN '骐骥版'
            WHEN t.product_type IN ('1', '7') THEN '上网宝'
            WHEN t.product_type IN ('4', '6', '14', '1000013') THEN '微电签'
            WHEN t.product_type IN ('5', '10') THEN '微智能'
            ELSE '立刷小蓝牙'
        END as mpos_type
    FROM edw.agt_stat_term_1m f
    LEFT JOIN ods_pay_cust.micro_pos_t_device_product_info t ON f.model = t.device_type
    WHERE SUBSTR(f.product_type, 1, 1) = '2'
      AND f.dt >= {start_dt} AND f.dt <= {end_dt}
) product_data
GROUP BY dt
ORDER BY dt
"""

# 小POS终端绑定、激活、活跃趋势（近25个月）
SQL_SMALL_POS_TERM_TREND = """
WITH term_data AS (
    SELECT
        dt,
        SUM(CAST(inc_term AS BIGINT)) as bind_terminals,
        SUM(CAST(inc_act_term AS BIGINT)) as active_terminals
    FROM edw.agt_stat_term_1m
    WHERE SUBSTR(product_type, 1, 1) = '2'
      AND dt >= {start_dt} AND dt <= {end_dt}
    GROUP BY dt
),
act_data AS (
    SELECT
        dt,
        SUM(CAST(act_mer_cnt AS BIGINT)) as term_active_merchants
    FROM edw.agt_stat_activity_1m
    WHERE product_type LIKE 'MPOS%'
      AND dt >= {start_dt} AND dt <= {end_dt}
    GROUP BY dt
)
SELECT
    t.dt as month,
    t.bind_terminals as bind_terminals,
    t.active_terminals as active_terminals,
    a.term_active_merchants as term_active_merchants
FROM term_data t
LEFT JOIN act_data a ON t.dt = a.dt
ORDER BY t.dt
"""


def get_date_params(stat_month: str = None):
    """
    获取日期参数

    Args:
        stat_month: 统计月份, 格式YYYYMM, 默认为上个月

    Returns:
        dict: 包含各种日期格式参数(均为整数, 用于dt分区字段比较)
    """
    from datetime import datetime, timedelta
    from calendar import monthrange

    if stat_month is None:
        today = datetime.now()
        last_month = today.replace(day=1) - timedelta(days=1)
        stat_month = last_month.strftime('%Y%m')

    # 解析月份
    year = int(stat_month[:4])
    month = int(stat_month[4:6])

    # 当月(整数格式)
    current_month_int = int(stat_month)

    # 上个月
    if month == 1:
        prev_year = year - 1
        prev_month = 12
    else:
        prev_year = year
        prev_month = month - 1
    prev_stat_month = f"{prev_year}{prev_month:02d}"
    previous_month_int = int(prev_stat_month)

    # 计算25个月前的日期（近2年趋势：最新月往前25个月至最新月）
    def calc_months_ago(y, m, n):
        """计算n个月前的年月"""
        total_months = y * 12 + m - 1 - n
        new_y = total_months // 12
        new_m = total_months % 12 + 1
        return new_y, new_m

    # 近25个月起始（用于近2年趋势图）
    start_year_25m, start_month_25m = calc_months_ago(year, month, 24)  # 往前24个月+当月=25个月
    start_dt_2year = int(f"{start_year_25m}{start_month_25m:02d}")

    # 近13个月起始（用于近1年趋势图）
    start_year_13m, start_month_13m = calc_months_ago(year, month, 12)  # 往前12个月+当月=13个月
    start_dt_1year = int(f"{start_year_13m}{start_month_13m:02d}")

    # 当前月份作为end_dt
    end_dt = current_month_int

    return {
        'stat_month': stat_month,
        'current_dt': current_month_int,
        'current_month': current_month_int,
        'previous_dt': previous_month_int,
        'previous_month': previous_month_int,
        'start_dt': start_dt_2year,  # 近25个月起始
        'start_dt_2year': start_dt_2year,  # 近25个月起始
        'start_dt_1year': start_dt_1year,  # 近13个月起始
        'end_dt': end_dt,
    }


def translate_fields(data: list) -> list:
    """
    将英文字段名转换为中文

    Args:
        data: 数据列表(字典格式)

    Returns:
        转换后的数据列表
    """
    if not data:
        return data

    result = []
    for row in data:
        new_row = {}
        for key, value in row.items():
            chinese_key = FIELD_MAPPING.get(key, key)
            new_row[chinese_key] = value
        result.append(new_row)
    return result


def format_number(value, decimal_places=0):
    """
    格式化数字为千分位格式

    Args:
        value: 数值
        decimal_places: 小数位数

    Returns:
        格式化后的字符串
    """
    try:
        if value is None:
            return '0'
        num = float(value)
        if decimal_places > 0:
            return f"{num:,.{decimal_places}f}"
        else:
            return f"{int(round(num)):,}"
    except:
        return '0'