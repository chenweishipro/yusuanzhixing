# 基础数据
detail_sql = """
SELECT
            bm.BUSINESS_ID as budgetMaintainBusinessId,
            bm.DISPLAY_CODE as displayCode,
            bm.PERIOD_ID as periodId,
            bm.MAINTAIN_NAME as maintainName,
            bm.SUBJECT_ID as subjectId,
            bm.ITEM_ID as itemId,
            bm.SEGMENT as segment,
            bm.COST_CENTER as costCenter,
            bm.PROJECT as project,
            bm.SERVICE_LINE as serviceLine,
            bm.BUDGET_AMOUNT as budgetAmount,
            bm.BUDGET_REMAINING_SUM as budgetRemainingSum,
            bm.TOLERANCE as tolerance,
            bm.CONTROL_STRATEGY as controlStrategy,
            bm.BUDGET_CARRY_OVER as budgetCarryOver,
            bm.CARRY_OVER_PERIOD as carryOverPeriod,
            bm.RELATED_YEAR_BUDGET as relatedYearBudget,
            bm.ACTIVE_DATE as activeDate,
            bm.INACTIVE_DATE as inactiveDate,
            bm.DIMENSION1 as dimension1,
            bm.DIMENSION2 as dimension2,
            bs.SUBJECT_NAME as subjectNameLocal,
            bp.PERIOD_NAME as periodNameLocal,
            bm.BUDGET_DEDUCTION_SUM AS budgetDeductionSum,
            bm.SEGMENT_CATEGORY as segmentCategory,
            bm.BUDGET_FREEZE_SUM AS budgetFreezeSum,
            bm.CREATE_DATE

                ,bad.PLATFORM as platform
                ,bad.BUDGET_TYPE as budgetType
                ,bad.DISPLAY_CODE as documentNum
                ,bad.DOCUMENT_TYPE_CODE as documentTypeCode
                ,bad.DOCUMENT_TYPE_NAME as documentTypeName
                ,bad.APPLICANT as applicant
                ,bad.CURRENCY as currency
                ,bad.EXCHANGE_RATE as exchangeRate
                ,bad.ORIGINAL_CURRENCY_AMOUNT as originalCurrencyAmount
                ,bad.BUDGET_AMOUNT as budgetAmountDetail
                ,bad.DESCRIPTION as description
                ,bad.CREATE_DATE as operateDate
                ,case when bad.DOCUMENT_TYPE_NAME = '税务报账单' then str.application_date
                    when bad.DOCUMENT_TYPE_NAME = '薪酬计提单' then gsc.application_date
                    when bad.DOCUMENT_TYPE_NAME = '对公报销申请' then spe.application_date
                    when bad.DOCUMENT_TYPE_NAME = '会议费用报销单' then smce.application_date
                    when bad.DOCUMENT_TYPE_NAME = '营销费用报销单' then smr.application_date
                    when bad.DOCUMENT_TYPE_NAME = '员工费用报销单' then ter.application_date
                    when bad.DOCUMENT_TYPE_NAME = '员工借款申请' then loan.application_date
                else null
                end as applicationDate
                ,case when bad.DOCUMENT_TYPE_NAME = '税务报账单' then str.total_date
                    when bad.DOCUMENT_TYPE_NAME = '薪酬计提单' then gsc.total_date
                    when bad.DOCUMENT_TYPE_NAME = '对公报销申请' then spe.total_date
                    when bad.DOCUMENT_TYPE_NAME = '会议费用报销单' then smce.total_date
                    when bad.DOCUMENT_TYPE_NAME = '营销费用报销单' then smr.total_date
                    when bad.DOCUMENT_TYPE_NAME = '员工费用报销单' then ter.total_date
                    when bad.DOCUMENT_TYPE_NAME = '员工借款申请' then loan.total_date
                else null
                end as glDate
                ,case when bad.DOCUMENT_TYPE_NAME = '税务报账单' then str.department_id
                    when bad.DOCUMENT_TYPE_NAME = '薪酬计提单' then gsc.department_id
                    when bad.DOCUMENT_TYPE_NAME = '对公报销申请' then spe.department_id
                    when bad.DOCUMENT_TYPE_NAME = '会议费用报销单' then smce.department_id
                    when bad.DOCUMENT_TYPE_NAME = '营销费用报销单' then smr.department_id
                    when bad.DOCUMENT_TYPE_NAME = '员工费用报销单' then ter.department_id
                    when bad.DOCUMENT_TYPE_NAME = '员工借款申请' then loan.department_id
                else null
                end as APPLICATION_DEPT
                ,smce.CONFERENCE_NAME
                ,case when bad.DOCUMENT_TYPE_NAME = '税务报账单' then str.STATUS
                when bad.DOCUMENT_TYPE_NAME = '薪酬计提单' then gsc.STATUS
                when bad.DOCUMENT_TYPE_NAME = '对公报销申请' then spe.STATUS
                when bad.DOCUMENT_TYPE_NAME = '会议费用报销单' then smce.STATUS
                when bad.DOCUMENT_TYPE_NAME = '营销费用报销单' then smr.STATUS
                when bad.DOCUMENT_TYPE_NAME = '员工费用报销单' then ter.STATUS
                when bad.DOCUMENT_TYPE_NAME = '员工借款申请' then loan.STATUS
                else null
                end as STATUS
                ,case when bad.DOCUMENT_TYPE_NAME = '税务报账单' then str.BUSINESS_ID
                when bad.DOCUMENT_TYPE_NAME = '薪酬计提单' then gsc.BUSINESS_ID
                when bad.DOCUMENT_TYPE_NAME = '对公报销申请' then spe.BUSINESS_ID
                when bad.DOCUMENT_TYPE_NAME = '会议费用报销单' then smce.BUSINESS_ID
                when bad.DOCUMENT_TYPE_NAME = '营销费用报销单' then smr.BUSINESS_ID
                when bad.DOCUMENT_TYPE_NAME = '员工费用报销单' then ter.BUSINESS_ID
                when bad.DOCUMENT_TYPE_NAME = '员工借款申请' then loan.BUSINESS_ID
                else null
                end as docId
                ,case when bad.DOCUMENT_TYPE_NAME = '税务报账单' then ''
                when bad.DOCUMENT_TYPE_NAME = '薪酬计提单' then ''
                when bad.DOCUMENT_TYPE_NAME = '对公报销申请' then sped.remark
                when bad.DOCUMENT_TYPE_NAME = '会议费用报销单' then smcec.remark
                when bad.DOCUMENT_TYPE_NAME = '营销费用报销单' then smrc.remark
                when bad.DOCUMENT_TYPE_NAME = '员工费用报销单' then tref.remark
                when bad.DOCUMENT_TYPE_NAME = '员工借款申请' then ''
                else null
                end as remark

        FROM
            budget_maintain bm
        LEFT JOIN budget_subject bs ON bm.SUBJECT_ID = bs.BUSINESS_ID
        LEFT JOIN budget_period bp ON bm.PERIOD_ID = bp.BUSINESS_ID

            LEFT JOIN budget_amount_detail bad ON bm.BUSINESS_ID = bad.BUDGET_MAINTAIN_ID
            left join ssc_tax_reporting str on bad.DISPLAY_CODE = str.document_number
            left join gl_salary_calculation gsc on bad.DISPLAY_CODE = gsc.document_number
            left join ssc_public_expense spe on bad.DISPLAY_CODE = spe.document_number
            left join ssc_meeting_costing_expense smce on bad.DISPLAY_CODE = smce.document_number
            left join ssc_marketing_reimbursement smr on bad.DISPLAY_CODE = smr.document_number
            left join te_emp_reimbursement ter on bad.DISPLAY_CODE = ter.document_number
            left join te_loan_information loan on bad.DISPLAY_CODE = loan.document_number
            left join te_emp_reimbursement_fees tref on bad.DOCUMENT_LINE_NUM = tref.budget_line_id
            left join ssc_public_expense_detail sped on bad.DOCUMENT_LINE_NUM = sped.budget_line_id
            left join ssc_meeting_costing_expense_cost smcec on bad.DOCUMENT_LINE_NUM = smcec.budget_line_id
            left join ssc_marketing_reimbursement_cost smrc on bad.DOCUMENT_LINE_NUM = smrc.budget_line_id

"""


# 匹配成本中心
zdbc_sql ="""
select VALUE_SET_CODE,VALUE_SET_NAME from mdm_section_value v
left join mdm_section_value_set s on s.SECTION_ID = v.BUSINESS_ID
where SECTION_CODE = 'BUDGET_COST_CENTER'
"""

# 预算科目名称
zdbc_sql1 ="""
select VALUE_SET_CODE,VALUE_SET_NAME from mdm_section_value v
left join mdm_section_value_set s on s.SECTION_ID = v.BUSINESS_ID
where SECTION_CODE = 'SSC_BUDGET_ACCOUNT'
"""


# 项目阶段名称
zdbc_sql2 = """
select VALUE_SET_CODE,VALUE_SET_NAME from mdm_section_value v
left join mdm_section_value_set s on s.SECTION_ID = v.BUSINESS_ID
where SECTION_CODE = 'SSC_PROJECT_PHASE'
"""

# 匹配产品名称
zdbc_sql3 = """
select VALUE_SET_CODE,VALUE_SET_NAME from mdm_section_value v
left join mdm_section_value_set s on s.SECTION_ID = v.BUSINESS_ID
where SECTION_CODE = 'SSC_PRODUCT'
"""

# 科目类别名称
zdbc_sql4 = """
select VALUE_SET_CODE,VALUE_SET_NAME from mdm_section_value v
left join mdm_section_value_set s on s.SECTION_ID = v.BUSINESS_ID
where SECTION_CODE = 'SSC_ACCOUNT_CATEGORY'
"""

# 匹配项目名称
sql_text_project_name = """
SELECT
            BUSINESS_ID AS businessId
            ,ORGANIZATION_NAME AS organizationName
            ,PROJECT_ID AS projectId
            ,PROJECT_NAME AS projectName
            ,START_TIME AS startTime
            ,END_TIME AS endTime
            ,DELETE_FLAG AS deleteFlag
            ,PROPERTY AS property
            ,ERP_FLAG AS erpFlag
        FROM te_project_management
        WHERE 1 = 1 AND delete_flag = 0	
        ORDER BY modified_date DESC
"""

# 员工信息
sql_text_employee ="""
  select * from mdm_employee
"""

# 部门信息
sql_text_department = "select * from mdm_organization"


# 业务小类
sql_bs_small_kind = f"""
select
        t1.business_id docId,
        t2.invoice_subcategory_code categoryCode,
        t2.segment_value_id segment,
        t1.document_number docNum
        from te_emp_reimbursement t1 inner join
        te_emp_reimbursement_fees t2 on t1.business_id = t2.parent_id

        union all
        select
        t1.business_id docId,
        t2.invoice_subcategory_code categoryCode,
        t2.segment_value_id segment,
        t1.document_number docNum
        from ssc_meeting_costing_expense t1 inner join
        ssc_meeting_costing_expense_cost t2 on t1.business_id = t2.expense_id

        union all
        select
        t1.business_id docId,
        t2.invoice_subcategory_code categoryCode,
        t2.segment_value_id segment,
        t1.document_number docNum
        from ssc_public_expense t1 inner join
        ssc_public_expense_detail t2 on t1.business_id = t2.expense_id

        union all
        select
        t1.business_id docId,
        t2.invoice_subcategory_code categoryCode,
        t2.segment_value_id segment,
        t1.document_number docNum
        from ssc_marketing_reimbursement t1 inner join
        ssc_marketing_reimbursement_cost t2 on t1.business_id = t2.expense_id

"""

