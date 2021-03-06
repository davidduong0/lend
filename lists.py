# (01/09/20) Original list of variables to use. Note that this list has redundant vars that won't be used at all (e.g. id, sec_ secondary bureau vars etc.), but it's basically the list of vars that are both in old data (up to 2018) and in data to score in 2020+

print("Loading lists of vars and printing out some list sizes...")

# List of numeric variables in model (same name before and after processing)
numeric_cols_4_model = ['loan_amnt',
 'int_rate',
 'installment',
 'annual_inc',
 'acc_now_delinq',
 'acc_open_past_24mths',
 'bc_open_to_buy',
 'percent_bc_gt_75',
 'bc_util',
 'dti',
 'delinq_2yrs',
 'delinq_amnt',
 'fico_range_low',
 'fico_range_high',
 'inq_last_6mths',
 'mths_since_last_delinq',
 'mths_since_last_record',
 'mths_since_recent_inq',
 'mths_since_recent_revol_delinq',
 'mths_since_recent_bc',
 'mort_acc',
 'open_acc',
 'pub_rec',
 'total_bal_ex_mort',
 'revol_bal',
 'revol_util',
 'total_bc_limit',
 'total_acc',
 'total_il_high_credit_limit',
 'num_rev_accts',
 'mths_since_recent_bc_dlq',
 'pub_rec_bankruptcies',
 'num_accts_ever_120_pd',
 'chargeoff_within_12_mths',
 'collections_12_mths_ex_med',
 'tax_liens',
 'mths_since_last_major_derog',
 'num_sats',
 'num_tl_op_past_12m',
 'mo_sin_rcnt_tl',
 'tot_hi_cred_lim',
 'tot_cur_bal',
 'avg_cur_bal',
 'num_bc_tl',
 'num_actv_bc_tl',
 'num_bc_sats',
 'pct_tl_nvr_dlq',
 'num_tl_90g_dpd_24m',
 'num_tl_30dpd',
 'num_tl_120dpd_2m',
 'num_il_tl',
 'mo_sin_old_il_acct',
 'num_actv_rev_tl',
 'mo_sin_old_rev_tl_op',
 'mo_sin_rcnt_rev_tl_op',
 'total_rev_hi_lim',
 'num_rev_tl_bal_gt_0',
 'num_op_rev_tl',
 'tot_coll_amt',
 'annual_inc_joint',
 'dti_joint',
 'open_acc_6m',
 'open_act_il',
 'open_il_12m',
 'open_il_24m',
 'mths_since_rcnt_il',
 'total_bal_il',
 'il_util',
 'open_rv_12m',
 'open_rv_24m',
 'max_bal_bc',
 'all_util',
 'inq_fi',
 'total_cu_tl',
 'inq_last_12m']
print(len(numeric_cols_4_model))

# List of cat vars to KEEP AFTER feature engineering
CAT_NAMES_TO_KEEP = ['highRiskZip','major_derog_NA','bc_dlq_NA', 'revol_delinq_NA',
                     'grade_a','grade_b','grade_c','grade_d','emp_length_1 year',
                     'emp_length_10+ years','emp_length_2 years','emp_length_3 years',
                     'emp_length_4 years','emp_length_5 years','emp_length_6 years',
                     'emp_length_7 years','emp_length_8 years','emp_length_9 years',
                     'emp_length_less 1 year','home_ownership_mortgage','home_ownership_own',
                     'home_ownership_rent','verification_status_not verified',
                     'verification_status_source verified','verification_status_verified',
                     'purpose_car','purpose_credit card','purpose_debt consolidation',
                     'purpose_educational','purpose_home improvement','purpose_house',
                     'purpose_other',
                     'purpose_major purchase','purpose_medical','purpose_moving',
                     'purpose_renewable energy','purpose_small business',
                     'purpose_vacation','purpose_wedding','initial_list_status_f',
                     'initial_list_status_w','application_type_individual',
                     'application_type_joint app','disbursement_method_cash',
                     'disbursement_method_directpay']

print(len(CAT_NAMES_TO_KEEP))

###########
# APPENDIX:

# (01/09/20) Below list is for later reference/ review (vars in new dataset but not in old dataset, cannot train with those)
new_vars_not_in_training = ['exp_default_rate',
 'service_fee_rate',
 'accept_d',
 'exp_d',
 'list_d',
 'credit_pull_d',
 'review_status_d',
 'review_status',
 'msa',
 'ils_exp_d',
 'effective_int_rate',
 'verified_status_joint',
 'mtg_payment',
 'housing_payment']