# import sys
import varity_run
sys_argv = {}
sys_argv['action']  = 'init_session'
# sys_argv['action']  = 'plot_hp_weight'
# sys_argv['action']  = 'plot_test_result'
# sys_argv['action']  = 'ldlr_analysis'
# sys_argv['action']  = 'plot_mave_result'
# sys_argv['action']  = 'plot_ldlr_result'
# sys_argv['action']  = 'save_best_hp'
# sys_argv['action']  = 'debug'
# sys_argv['action']  = 'test_hyperopt'
# sys_argv['action']  = 'run_batch_id_jobs'
# sys_argv['action']  = 'plot_feature_shap_interaction'
# sys_argv['action']  = 'target_prediction'
# sys_argv['action']  = 'test_cv_prediction'
# sys_argv['action']  = 'fun_combine_loo_predictions'
# sys_argv['action']  = 'add_loo_predictions'
# sys_argv['action']  = 'add_deepsequence'
# sys_argv['action']  = 'update_data'
# sys_argv['action']  = 'plot_score_versus_probability'
# sys_argv['action']  = 'process_denovo_variants'
# sys_argv['action']  = 'hp_tuning'
# sys_argv['action']  = 'mv_analysis'
# sys_argv['action']  = 'plot_mv_result'
# sys_argv['action']  = 'send_email'
# sys_argv['action'] = 'plot_data_quantity'

sys_argv['session_id'] = 'Revision210704'
sys_argv['predictor'] = 'VARITY_R_CV'
# sys_argv['session_id'] = 'sherloc210915'
# sys_argv['predictor'] = 'VARITY_Sherloc'
sys_argv['run_on_node'] = 0
sys_argv['cluster'] = 0
sys_argv['hp_tune_type'] = 'hyperopt_logistic'
sys_argv['filter_test_score'] = 0
sys_argv['add_deepsequence_scores'] = 0
sys_argv['add_eve_scores'] = 0
sys_argv['add_mpc_mistic_scores'] = 0
sys_argv['add_mutpred_scores'] = 0
sys_argv['add_core_setname'] = 0
sys_argv['add_test_data'] = 0
sys_argv['shrink_data'] = 0
sys_argv['add_no_homozygous_gnomad_data'] = 1
sys_argv['add_complete_sift_provean_scores'] = 0
sys_argv['update_pisa'] = 0
sys_argv['check_data'] = 0
sys_argv['add_loo'] = 0
sys_argv['project_path'] = '/data/varity/'
sys_argv['db_path'] = '/Users/joewu/Dropbox/database/humandb_new/'
sys_argv['pisa_folder'] = 'pisa3'
sys_argv['nucleotide_predictors']=['CADD','MutationTaster','FATHMM','GenoCanyon','DANN','GERP++','phyloP','PhastCons','SiPhy','fitCons'] 
# sys_argv['trials_max_num'] = 300

all_R_CV_preditors = ['VARITY_R_CV','SIFT_R_CV','Polyphen2_HDIV_R_CV','Polyphen2_HVAR_R_CV','PROVEAN_R_CV','CADD_R_CV','PrimateAI_R_CV','Eigen_R_CV',
                 'REVEL_R_CV','M-CAP_R_CV','LRT_R_CV','MutationTaster_R_CV','MutationAssessor_R_CV','FATHMM_R_CV','MetaSVM_R_CV',
                 'MetaLR_R_CV','GenoCanyon_R_CV','DANN_R_CV','GERP++_R_CV','phyloP_R_CV','PhastCons_R_CV','SiPhy_R_CV','fitCons_R_CV']

all_ER_CV_preditors = ['VARITY_ER_CV','SIFT_ER_CV','Polyphen2_HDIV_ER_CV','Polyphen2_HVAR_ER_CV','PROVEAN_ER_CV','CADD_ER_CV','PrimateAI_ER_CV','Eigen_ER_CV',
                 'REVEL_ER_CV','M-CAP_ER_CV','LRT_ER_CV','MutationTaster_ER_CV','MutationAssessor_ER_CV','FATHMM_ER_CV','MetaSVM_ER_CV',
                 'MetaLR_ER_CV','GenoCanyon_ER_CV','DANN_ER_CV','GERP++_ER_CV','phyloP_ER_CV','PhastCons_ER_CV','SiPhy_ER_CV','fitCons_ER_CV']

if sys_argv['action'] == 'mv_analysis':
    sys_argv['mv_qip'] = 'extra_gnomad_af'

if sys_argv['action'] == 'add_loo_predictions':
    sys_argv['no_loo_weight_cutoff'] = 0
#     sys_argv['add_loo_input_file'] = sys_argv['project_path'] + 'output/csv/' + sys_argv['session_id'] + '_P01130_varity_snv_pisa3_predicted.csv'
    sys_argv['add_loo_input_file'] = sys_argv['project_path'] + 'output/csv/' + sys_argv['session_id'] + '_varity_target_denovodb_enriched_negative_added_snv_pisa3_predicted.csv'        
#     sys_argv['add_loo_input_file'] = sys_argv['project_path'] + 'output/csv/' + sys_argv['session_id'] + '_varity_target_mave_pisa3_predicted.csv'
    
    
if sys_argv['action'] == 'add_deepsequence':    
    sys_argv['add_deepsequence_input_file'] = sys_argv['project_path'] + 'output/csv/' + sys_argv['session_id'] + '_varity_target_mave_pisa3_predicted_loo.csv'
    

if sys_argv['action'] == 'plot_feature_shap_interaction':
#     sys_argv['shap_type'] = 'performance'
#     sys_argv['shap_target'] = 'training'
#     sys_argv['shap_target_npy_file'] = sys_argv['project_path'] + 'output/npy/' + sys_argv['session_id'] + '_shap_output_' + sys_argv['predictor'] + '_training.npy'
    
    
    sys_argv['shap_type'] = 'output'
    sys_argv['shap_target'] = 'single-P01130:R:237:P'
    sys_argv['shap_target_npy_file'] = sys_argv['project_path'] + 'output/npy/' + sys_argv['session_id'] + '_target_prediction_VARITY_ER_tf0_Revision1230_1_P01130_varity_snv_pisa3_target_interaction_shap.npy'
    sys_argv['shap_target_csv_file'] = sys_argv['project_path'] + 'output/csv/' + sys_argv['session_id'] + '_P01130_varity_snv_pisa3_VARITY_ER.csv'     
    sys_argv['shap_feature_group'] = 0
    
#     sys_argv['shap_type'] = 'feature'
#     sys_argv['shap_target'] = 'single:P01130_R_350_P'

if sys_argv['action'] == 'init_session':
    sys_argv['reinitiate_session'] = 1
    pass

if sys_argv['action'] == 'mv_analysis':
    sys_argv['qip'] = 'extra_gnomad_af'

if sys_argv['action'] == 'plot_mv_result':
    sys_argv['mv_qip'] = 'extra_gnomad_af'
    sys_argv['fig_x'] = 30
    sys_argv['fig_y'] = 15

if sys_argv['action'] == 'hp_tuning':
    sys_argv['cur_test_fold'] = 0
    
if sys_argv['action'] == 'save_best_hp':    
    sys_argv['cur_test_fold'] = 0
#     sys_argv['trials_mv_size'] = 20
#     sys_argv['trials_max_num'] = 300
#     sys_argv['hp_select_strategy'] = 'selected_tid'
#     sys_argv['selected_tid'] = 259
#     

if sys_argv['action'] == 'plot_hp_weight':    
    
    # sys_argv['plot_qip_titles'] = ['gnomAD Negative add-on sets']                                                          
    # sys_argv['plot_qip_cols_name'] = ['-Log10(AF)']                                                                                                              
    # sys_argv['plot_qip_cols'] = ['log_af']    
    # sys_argv['plot_sets'] = [['extra_gnomad_high','extra_gnomad_low']] 
    
    sys_argv['plot_qip_titles'] = ['gnomAD Negative add-on sets','gnomAD Negative add-on sets']
    sys_argv['plot_qip_cols_name'] = ['Log10(# of homozygotes)','-Log10(MAF)']
    sys_argv['plot_qip_cols'] = ['gnomAD_exomes_nhomalt','log_af']
    sys_argv['plot_sets'] = [['extra_gnomad_high','extra_gnomad_low'],['extra_gnomad_high','extra_gnomad_low']]
    
    # sys_argv['plot_qip_titles'] = ['gnomAD Negative add-on sets']
    # sys_argv['plot_qip_cols_name'] = ['Log10(# of homozygotes)']
    # sys_argv['plot_qip_cols'] = ['gnomAD_exomes_nhomalt']
    # sys_argv['plot_sets'] = [['extra_gnomad_high','extra_gnomad_low']]
            
    # sys_argv['plot_qip_titles'] = ['ClinVar Negative core set','ClinVar Positive core set'] + \
    #                               ['ClinVar Negative add-on set','ClinVar Positive add-on set'] + \
    #                               ['HumsaVar Negative add-on sets (Rare and Common)','HumsaVar Positive add-on sets'] + \
    #                               ['gnomAD Negative add-on sets (Rare and Common)','HGMD Positive add-on sets'] + \
    #                               ['MAVE Negative add-on set','MAVE Positive add-on set']
    #
    #
    # sys_argv['plot_qip_cols_name'] = ['Review Star','Review Star'] + \
    #                                  ['-Log10(AF)','-Log10(AF)'] + \
    #                                  ['-Log10(AF)','-Log10(AF)'] + \
    #                                  ['-Log10(AF)','-Log10(AF)'] + \
    #                                  ['Label Confidence','Label Confidence']
    #
    #
    # sys_argv['plot_qip_cols'] = ['clinvar_review_star','clinvar_review_star'] + \
    #                             ['log_af','log_af'] + \
    #                             ['log_af','log_af'] + \
    #                             ['log_af','log_af'] + \
    #                             ['mave_label_confidence','mave_label_confidence']
    #
    #
    # sys_argv['plot_sets'] = [['core_clinvar_0'],['core_clinvar_1']] + \
    #                         [['extra_clinvar_0_low','extra_clinvar_0_high'],['extra_clinvar_1']] + \
    #                         [['extra_humsavar_0_low','extra_humsavar_0_high'],['extra_humsavar_1']] + \
    #                         [['extra_gnomad_high','extra_gnomad_low'],['extra_hgmd']] + \
    #                         [['extra_mave_0'],['extra_mave_1']]


#     
#     sys_argv['plot_weight_type'] = [1,0]
    sys_argv['plot_weight_type'] = [0]
    sys_argv['plot_final_weight'] = 0
    
    
#     sys_argv['plot_qip_titles'] = ['ClinVar Negative core set','ClinVar Positive core set'] + \
#                                   ['ClinVar Negative add-on set','ClinVar Positive add-on set'] + \
#                                   ['ClinVar Negative add-on set','ClinVar Positive add-on set'] + \
#                                   ['HumsaVar Negative add-on sets','HumsaVar Positive add-on sets'] + \
#                                   ['MAVE Negative add-on set','MAVE Positive add-on set'] + \
#                                   ['MAVE Negative add-on set','MAVE Positive add-on set'] + \
#                                   ['gnomAD Negative add-on sets','gnomAD Negative add-on sets'] + \
#                                   ['HGMD Positive add-on sets']                                  
#                                             
#     sys_argv['plot_qip_cols_name'] = ['Review Star','Review Star'] + \
#                                      ['-Log10(MAF)','-Log10(MAF)'] + \
#                                      ['Review Star','Review Star'] + \
#                                      ['-Log10(MAF)','-Log10(MAF)'] + \
#                                      ['Label Confidence','Label Confidence'] + \
#                                      ['Mutational Accessibility','Mutational Accessibility'] + \
#                                      ['Log10(# of homozygotes)','-Log10(MAF)'] + \
#                                      ['-Log10(MAF)']
#                                                                                                                   
#     sys_argv['plot_qip_cols'] = ['clinvar_review_star','clinvar_review_star'] + \
#                                 ['log_af','log_af'] + \
#                                 ['clinvar_review_star','clinvar_review_star'] + \
#                                 ['log_af','log_af'] + \
#                                 ['mave_label_confidence','mave_label_confidence'] + \
#                                 ['accessibility','accessibility'] + \
#                                 ['gnomAD_exomes_nhomalt','log_af'] + \
#                                 ['log_af']
#         
#     sys_argv['plot_sets'] = [['core_clinvar_0'],['core_clinvar_1']] + \
#                             [['extra_clinvar_0_low','extra_clinvar_0_high'],['extra_clinvar_1']] + \
#                             [['extra_clinvar_0_low','extra_clinvar_0_high'],['extra_clinvar_1']] + \
#                             [['extra_humsavar_0_low','extra_humsavar_0_high'],['extra_humsavar_1']] + \
#                             [['extra_mave_0'],['extra_mave_1']] + \
#                             [['extra_mave_0'],['extra_mave_1']] + \
#                             [['extra_gnomad_high','extra_gnomad_low'],['extra_gnomad_high','extra_gnomad_low']] + \
#                             [['extra_hgmd']]                                                        

    sys_argv['cur_test_fold'] = 0 
    
if sys_argv['action'] == 'test_cv_prediction':   

    sys_argv['predictors']=['SIFT_R_CV','Polyphen2_HDIV_R_CV','Polyphen2_HVAR_R_CV','PROVEAN_R_CV','CADD_R_CV','PrimateAI_R_CV','Eigen_R_CV',
                                    'REVEL_R_CV','M-CAP_R_CV','MetaSVM_R_CV','MetaLR_R_CV','MISTIC_R_CV','MPC_R_CV']
    
    sys_argv['predictors'] = ['VARITY_Naive_R_CV'] 

if sys_argv['action'] == 'plot_ldlr_result':
    sys_argv['ldlr_correlation_file'] = sys_argv['project_path'] + 'output/csv/ldlr_variants_remove_circularity_0_maf_0.005_spc_pisa3.csv'
    sys_argv['correlation_type'] = 'Spearman' 
    sys_argv['compare_to_predictor']='VARITY_R'
#     sys_argv['ldlr_correlation_file'] = sys_argv['project_path'] + 'output/csv/ldlr_variants_remove_circularity_0_maf_0.005_pcc_pisa3.csv'
#     sys_argv['correlation_type'] = 'Pearson'
#     sys_argv['compare_to_predictor']='VARITY_ER_LOO'   
    sys_argv['plot_title'] = 'Performance on LDLR variants'
    sys_argv['correlation_key_col'] = ''
    

    sys_argv['compare_predictors']=['VARITY_R','VARITY_ER','VARITY_R_LOO','VARITY_ER_LOO','SIFT','Polyphen2_HDIV','Polyphen2_HVAR','PROVEAN','CADD','PrimateAI','Eigen',
                                    'REVEL','M-CAP','LRT','MutationTaster','MutationAssessor','FATHMM','MetaSVM',
                                    'MetaLR','GenoCanyon','DANN','GERP++','phyloP','PhastCons','SiPhy','fitCons','MISTIC','MPC']   
    sys_argv['no_plot_predictors'] = ['MutationTaster','fitCons','GenoCanyon']      
    
if sys_argv['action'] == 'plot_mave_result':
    sys_argv['test_result_type'] = 'correlation'
    sys_argv['cur_test_fold'] = -1    
    sys_argv['correlation_key_col'] = 'symbol'
    sys_argv['correlation_type'] = 'Pearson' 
    sys_argv['compare_to_predictor']='VARITY_ER_LOO'
#     sys_argv['correlation_type'] = 'Spearman' 
#     sys_argv['compare_to_predictor']='VARITY_R_LOO'        
    sys_argv['plot_title'] = 'Performance on experimental variant effect maps'
    sys_argv['t_value'] = 2.015 
    sys_argv['independent_test_file'] = sys_argv['project_path'] + 'output/csv/' + sys_argv['session_id'] + '_varity_target_mave_pisa3_predicted_loo_with_deepsequence.csv'
    sys_argv['independent_test_name'] = 'MAVE'
    sys_argv['filter_test_score'] = 'MAF_0.005'
    sys_argv['dependent_variable'] = 'mave_score'
    sys_argv['mave_label_confidence_cutoff'] = 0.5
    sys_argv['mave_weight_cutoff'] = 1

#     sys_argv['compare_predictors']=['VARITY_R','VARITY_ER','VARITY_R_LOO','VARITY_ER_LOO','SIFT','Polyphen2_HDIV','Polyphen2_HVAR','PROVEAN','CADD','PrimateAI','Eigen',
#                                     'REVEL','M-CAP','LRT','MutationTaster','MutationAssessor','FATHMM','MetaSVM',
#                                     'MetaLR','GenoCanyon','DANN','GERP++','phyloP','PhastCons','SiPhy','fitCons','MISTIC','MPC']   
#     sys_argv['no_plot_predictors'] = ['MutationTaster','fitCons','PhastCons','GenoCanyon']
    
    
    #'MutationAssessor','SIFT','Polyphen2_HDIV','Polyphen2_HVAR' removed due to no scores on some of the mave genes
    
    sys_argv['compare_predictors']=['VARITY_R','VARITY_ER','VARITY_R_LOO','VARITY_ER_LOO','PROVEAN','CADD','PrimateAI','Eigen',
                                'REVEL','M-CAP','LRT','MutationTaster','FATHMM','MetaSVM',
                                'MetaLR','GenoCanyon','DANN','GERP++','phyloP','PhastCons','SiPhy','fitCons','MISTIC','MPC']   
    sys_argv['no_plot_predictors'] = ['MutationTaster','fitCons','PhastCons','GenoCanyon','MISTIC']
    
if sys_argv['action'] == 'plot_test_result':

    sys_argv['plot_test_with_saved_data'] = 0
    sys_argv['plot_show_size'] = 0
    sys_argv['t_value'] = 1.833113
    #     sys_argv['plot_metric']= ['interp_aubprc','org_auroc']
    #     sys_argv['plot_metric_order']= ['interp_aubprc','org_auroc']
    #
    #     sys_argv['plot_metric']= ['interp_aubprc']
    #     sys_argv['plot_metric_order']= ['interp_aubprc']
    
    #     sys_argv['plot_metric']= ['org_auroc']
    #     sys_argv['plot_metric_order']= ['org_auroc']
    #
    
    #     aubprc and roc for nested cross-validation
    sys_argv['size_factor'] = 1.13
    sys_argv['table_scale_factor'] = 2.83
    
    # aubprc for denovo
    sys_argv['size_factor'] = 1.03
    sys_argv['table_scale_factor'] = 2.8
    # #
    #     auroc for denovo
    #     sys_argv['size_factor'] = 1.07
    #     sys_argv['table_scale_factor'] = 2.8
    
    # (only VARITY_ER,VARITY_R and MutationAccessor)
    #     sys_argv['size_factor'] = 1.5
    #     sys_argv['table_scale_factor'] = 3.5
    
    ####***************************************************************************************************************************************************************
    # Performance comparison on variants on core set (measure impact of structure features and imbalanced training set )
    ####***************************************************************************************************************************************************************
    
    #     sys_argv['independent_test_file'] =  sys_argv['project_path'] + 'output/csv/VARITY_R_core_data_predicted.csv'
    #     sys_argv['independent_test_name'] = 'VARITY_R_CORE'
    #     sys_argv['filter_test_score'] = '0'
    #     sys_argv['dependent_variable'] = 'label'
    #     sys_argv['compare_to_predictor']='VARITY_R'
    #     sys_argv['compare_predictors']=['VARITY_R','PrimateAI','MISTIC','MPC','REVEL','M-CAP','MutationAssessor']
    #
    #
    
    ####***************************************************************************************************************************************************************
    # Performance comparison on LDLR variants (x% as cases , y% as controls)
    ####***************************************************************************************************************************************************************
    
    #     sys_argv['independent_test_file'] =  sys_argv['db_path'] + 'ukb/csv/ldlr_validation_set.csv'
    #     sys_argv['independent_test_name'] = 'LDL'
    #     sys_argv['filter_test_score'] = 0
    #     sys_argv['dependent_variable'] = 'LDL_label'
    #     sys_argv['compare_to_predictor']='VARITY_ER'
    #     sys_argv['compare_predictors']=['VARITY_R','VARITY_ER','SIFT','Polyphen2_HDIV','Polyphen2_HVAR','PROVEAN','CADD','PrimateAI','Eigen',
    #                                     'REVEL','M-CAP','LRT','MutationTaster','MutationAssessor','FATHMM','MetaSVM',
    #                                     'MetaLR','GenoCanyon','DANN','GERP++','phyloP','PhastCons','SiPhy','fitCons','MISTIC','MPC']
    #     sys_argv['no_plot_predictors'] = []
    
    
    ####***************************************************************************************************************************************************************
    # Performance comparison on denovodb (with coe et al enrichement annotation) variants in NueroDevelopment case control studies
    ####***************************************************************************************************************************************************************
    
    #     sys_argv['independent_test_file'] =  sys_argv['db_path'] + 'varity/all/varity_target_denovodb_coe_snv.csv'
    #     sys_argv['independent_test_name'] = 'coe_denovo'
    #     sys_argv['filter_test_score'] = 'coedn1'
    #     sys_argv['dependent_variable'] = 'denovo_label'
    #     sys_argv['predictor'] = 'VARITY_ER'
    #     sys_argv['compare_to_predictor']='VARITY_ER'
    #
    # #
    #     sys_argv['compare_predictors']=['VARITY_R','VARITY_ER',
    #                                     'SIFT','Polyphen2_HDIV','Polyphen2_HVAR','PROVEAN','CADD','PrimateAI','Eigen',
    #                                     'REVEL','M-CAP','LRT','MutationTaster','MutationAssessor','FATHMM','MetaSVM',
    #                                     'MetaLR','GenoCanyon','DANN','GERP++','phyloP','PhastCons','SiPhy','fitCons','MPC']
    #     sys_argv['no_plot_predictors'] = []
    
    ####***************************************************************************************************************************************************************
    # Performance comparison on MPC denovo variants in NueroDevelopment case control studies
    ####***************************************************************************************************************************************************************
    
    #     sys_argv['independent_test_file'] =  sys_argv['db_path'] + 'varity/all/varity_target_mpc_denovodb_snv.csv'
    #     sys_argv['independent_test_name'] = 'mpc_denovo'
    #     sys_argv['filter_test_score'] = 'mpcdn1'
    #     sys_argv['dependent_variable'] = 'denovo_label'
    #     sys_argv['predictor'] = 'VARITY_ER'
    #     sys_argv['compare_to_predictor']='VARITY_ER'
    #
    # #
    #     sys_argv['compare_predictors']=['VARITY_R','VARITY_ER',
    #                                     'SIFT','Polyphen2_HDIV','Polyphen2_HVAR','PROVEAN','CADD','PrimateAI','Eigen',
    #                                     'REVEL','M-CAP','LRT','MutationTaster','MutationAssessor','FATHMM','MetaSVM',
    #                                     'MetaLR','GenoCanyon','DANN','GERP++','phyloP','PhastCons','SiPhy','fitCons','MPC']
    #     sys_argv['no_plot_predictors'] = []
    #
    
    # #
    #     sys_argv['compare_predictors']=['VARITY_R','VARITY_ER','VARITY_Naive_R','VARITY_Naive_ER','VARITY_NoPPI_R','VARITY_NoPPI_ER']
    #     sys_argv['no_plot_predictors'] = []
    # #
    #     sys_argv['compare_predictors']=['VARITY_R','VARITY_ER','VARITY_Naive_R','VARITY_Naive_ER','VARITY_NoPPI_R','VARITY_NoPPI_ER',
    #                                     'SIFT','Polyphen2_HDIV','Polyphen2_HVAR','PROVEAN','CADD','PrimateAI','Eigen',
    #                                     'REVEL','M-CAP','LRT','MutationTaster','MutationAssessor','FATHMM','MetaSVM',
    #                                     'MetaLR','GenoCanyon','DANN','GERP++','phyloP','PhastCons','SiPhy','fitCons','MPC']
    #
    #     sys_argv['no_plot_predictors'] = ['SIFT','Polyphen2_HDIV','Polyphen2_HVAR','PROVEAN','CADD','PrimateAI','Eigen',
    #                                     'LRT','MutationTaster','FATHMM','MetaSVM',
    #                                     'MetaLR','GenoCanyon','DANN','GERP++','phyloP','PhastCons','SiPhy','fitCons','MPC']
    #
    #
    #     sys_argv['compare_predictors'] = ['VARITY_R','VARITY_ER']
    
    #     sys_argv['filter_test_score'] = 'dn1_MPC'
    #     sys_argv['compare_predictors'] = ['VARITY_R','VARITY_ER','MPC']
    # #
    #     sys_argv['filter_test_score'] = 'dn1_M-CAP'
    #     sys_argv['compare_predictors'] = ['VARITY_R','VARITY_ER','M-CAP']
    #
    #     sys_argv['filter_test_score'] = 'denovo_test'
    #     sys_argv['compare_predictors'] = ['VARITY_R','VARITY_ER','MISTIC']
    
    ####***************************************************************************************************************************************************************
    # Performance comparison on Denovo variants in NueroDevelopment case control studies
    ####***************************************************************************************************************************************************************
    # sys_argv['independent_test_file'] = sys_argv['project_path'] + 'output/csv/' + sys_argv[
    #     'session_id'] + '_varity_target_denovodb_enriched_negative_added_snv_pisa3_predicted_loo_not_tuned.csv'
    # sys_argv['independent_test_name'] = 'Denovodb'
    # sys_argv['filter_test_score'] = 'dn1'
    # sys_argv['dependent_variable'] = 'denovo_label'
    # sys_argv['compare_to_predictor'] = 'VARITY_ER'
    #
    # #     sys_argv['compare_predictors']=['VARITY_R','VARITY_ER']
    # #     sys_argv['no_plot_predictors'] = []
    #
    # sys_argv['compare_predictors'] = ['VARITY_R', 'VARITY_ER',
    #                                   'SIFT', 'Polyphen2_HDIV', 'Polyphen2_HVAR', 'PROVEAN', 'CADD', 'PrimateAI', 'Eigen',
    #                                   'REVEL', 'M-CAP', 'LRT', 'MutationTaster', 'MutationAssessor', 'FATHMM', 'MetaSVM',
    #                                   'MetaLR', 'GenoCanyon', 'DANN', 'GERP++', 'phyloP', 'PhastCons', 'SiPhy', 'fitCons',
    #                                   'MPC']
    #
    # sys_argv['no_plot_predictors'] = []
    
    #     sys_argv['compare_predictors'] = ['VARITY_R','VARITY_ER']
    #       
    #     sys_argv['filter_test_score'] = 'dn1_MPC'
    #     sys_argv['compare_predictors'] = ['VARITY_R','VARITY_ER','MPC']
    # #     
    #     sys_argv['filter_test_score'] = 'dn1_M-CAP'
    #     sys_argv['compare_predictors'] = ['VARITY_R','VARITY_ER','M-CAP']
    #       
    #     sys_argv['filter_test_score'] = 'denovo_test'
    #     sys_argv['compare_predictors'] = ['VARITY_R','VARITY_ER','MISTIC']
    
    
    
    
    
        ####***************************************************************************************************************************************************************
        #Performance comparison on variants in UKB genes
        ####***************************************************************************************************************************************************************
        
    #     sys_argv['independent_test_file'] =  sys_argv['project_path'] + 'output/csv/varity_target_ukb_predicted.csv'
    #     sys_argv['independent_test_name'] = 'UKB'
    #     sys_argv['filter_test_score'] = 0
    #     sys_argv['dependent_variable'] = 'label'
    #     sys_argv['compare_to_predictor']='Revision1106_100_VARITY_R'     
    #     sys_argv['compare_predictors']=['Revision1106_25_VARITY_R','Revision1106_25_VARITY_ER',
    #                                     'Revision1106_50_VARITY_R','Revision1106_50_VARITY_ER',
    #                                     'Revision1106_75_VARITY_R','Revision1106_75_VARITY_ER',                                    
    #                                     'Revision1106_100_VARITY_R','Revision1106_100_VARITY_ER',
    #                                     'Revision1106_125_VARITY_R','Revision1106_125_VARITY_ER',
    #                                     'MutationAssessor','Polyphen2_HVAR','CADD',
    #                                     'SIFT','PROVEAN','PrimateAI','REVEL','M-CAP','MISTIC','MPC','MutationTaster',
    #                                     'MetaSVM','MetaLR']                                     
    
    
    
        ####***************************************************************************************************************************************************************
        #Performance comparison using nested cross-validation (ER)
        ####***************************************************************************************************************************************************************                                                                      
    #     sys_argv['cur_test_fold'] = -1
    #     sys_argv['filter_test_score'] = 1
    #     sys_argv['predictor']='VARITY_ER_CV'
    #     sys_argv['compare_to_predictor']='VARITY_ER_CV'                
    #     sys_argv['compare_predictors'] = ['VARITY_ER_CV','VARITY_Naive_ER_CV']
    #     
    # #     sys_argv['compare_predictors'] = ['VARITY_ER_CV','VARITY_Naive_ER_CV','VARITY_NoPPI_ER_CV','VARITY_NoCS_ER_CV','VARITY_NoPPI-CS_ER_CV']      
    # #     sys_argv['compare_predictors']=['VARITY_ER_CV','VARITY_Naive_ER_CV','VARITY_NoPPI_ER_CV','SIFT_ER_CV','Polyphen2_HDIV_ER_CV','Polyphen2_HVAR_ER_CV','PROVEAN_ER_CV','CADD_ER_CV','PrimateAI_ER_CV','Eigen_ER_CV',
    # #                                    'REVEL_ER_CV','M-CAP_ER_CV','LRT_ER_CV','MutationTaster_ER_CV','MutationAssessor_ER_CV','FATHMM_ER_CV','MetaSVM_ER_CV',
    # #                                    'MetaLR_ER_CV','GenoCanyon_ER_CV','DANN_ER_CV','GERP++_ER_CV','phyloP_ER_CV','PhastCons_ER_CV','SiPhy_ER_CV','fitCons_ER_CV','MPC_ER_CV']
    # #             
    #     sys_argv['no_plot_predictors'] = []
    #     sys_argv['no_plot_predictors'] = ['VARITY_Naive_ER_CV','VARITY_NoPPI_ER_CV','fitCons_ER_CV']
    #     sys_argv['no_plot_predictors'] = ['VARITY_Naive_ER_CV','VARITY_NoPPI_ER_CV','SIFT_ER_CV','Polyphen2_HDIV_ER_CV','Polyphen2_HVAR_ER_CV','PROVEAN_ER_CV','CADD_ER_CV','PrimateAI_ER_CV',
    #                                    'M-CAP_ER_CV','LRT_ER_CV','MutationTaster_ER_CV','MutationAssessor_ER_CV','FATHMM_ER_CV','MetaSVM_ER_CV',
    #                                    'MetaLR_ER_CV','GenoCanyon_ER_CV','DANN_ER_CV','GERP++_ER_CV','phyloP_ER_CV','PhastCons_ER_CV','SiPhy_ER_CV','fitCons_ER_CV','MPC_ER_CV']
    # #         
    
    
                
    #     sys_argv['compare_predictors']=['VARITY_ER_CV','DeepSequence_ER_CV']
    #     sys_argv['compare_predictors']=['VARITY_ER_CV','EVMutation_ER_CV']  
    #     sys_argv['compare_predictors']=['VARITY_ER_CV','MISTIC_ER_CV']
    #     sys_argv['compare_predictors']=['VARITY_ER_CV','MPC_ER_CV']          
               
    ###***************************************************************************************************************************************************************
    #Performance comparison using nested cross-validation (R)
    ###***************************************************************************************************************************************************************                                                                      
    sys_argv['cur_test_fold'] = -1
    sys_argv['filter_test_score'] = 1
    sys_argv['compare_to_predictor']='VARITY_R_CV'    
            

    sys_argv['compare_predictors']=['VARITY_R_CV','VARITY_WithEve_R_CV','SIFT_R_CV','Polyphen2_HDIV_R_CV','Polyphen2_HVAR_R_CV','PROVEAN_R_CV','CADD_R_CV','PrimateAI_R_CV','Eigen_R_CV',
                           'REVEL_R_CV','M-CAP_R_CV','LRT_R_CV','MutationTaster_R_CV','MutationAssessor_R_CV','FATHMM_R_CV','MetaSVM_R_CV',
                           'MetaLR_R_CV','GenoCanyon_R_CV','DANN_R_CV','GERP++_R_CV','phyloP_R_CV','PhastCons_R_CV','SiPhy_R_CV','eve_R_CV','MPC_R_CV']
    
    
    sys_argv['compare_predictors']=['VARITY_R_CV','VARITY_WithEve_R_CV','SIFT_R_CV','Polyphen2_HDIV_R_CV','Polyphen2_HVAR_R_CV','PROVEAN_R_CV','CADD_R_CV','PrimateAI_R_CV','Eigen_R_CV',
                       'REVEL_R_CV','M-CAP_R_CV','LRT_R_CV','MutationTaster_R_CV','MutationAssessor_R_CV','FATHMM_R_CV','MetaSVM_R_CV',
                       'MetaLR_R_CV','GenoCanyon_R_CV','DANN_R_CV','GERP++_R_CV','phyloP_R_CV','PhastCons_R_CV','SiPhy_R_CV','MPC_R_CV'] 
 
           
    # sys_argv['no_plot_predictors'] = ['VARITY_R_CV','SIFT_R_CV','Polyphen2_HDIV_R_CV','Polyphen2_HVAR_R_CV','PROVEAN_R_CV','CADD_R_CV','PrimateAI_R_CV','Eigen_R_CV',
    #                        'M-CAP_R_CV','LRT_R_CV','MutationTaster_R_CV','MutationAssessor_R_CV','FATHMM_R_CV','MetaSVM_R_CV',
    #                        'MetaLR_R_CV','GenoCanyon_R_CV','DANN_R_CV','GERP++_R_CV','phyloP_R_CV','PhastCons_R_CV','SiPhy_R_CV','fitCons_R_CV','MPC_R_CV']
    sys_argv['no_plot_predictors'] = []         
    #
    #
    # sys_argv['compare_predictors']=['VARITY_R_CV','VARITY_Naive_R_CV','VARITY_NoPPI_R_CV','SIFT_R_CV','Polyphen2_HDIV_R_CV','Polyphen2_HVAR_R_CV','PROVEAN_R_CV','CADD_R_CV','PrimateAI_R_CV','Eigen_R_CV',
    #                                'REVEL_R_CV','M-CAP_R_CV','LRT_R_CV','MutationTaster_R_CV','MutationAssessor_R_CV','FATHMM_R_CV','MetaSVM_R_CV',
    #                                'MetaLR_R_CV','GenoCanyon_R_CV','DANN_R_CV','GERP++_R_CV','phyloP_R_CV','PhastCons_R_CV','SiPhy_R_CV','fitCons_R_CV','MPC_R_CV','MISTIC_R_CV']
    #
    # sys_argv['no_plot_predictors'] = ['SIFT_R_CV','Polyphen2_HDIV_R_CV','Polyphen2_HVAR_R_CV','PROVEAN_R_CV','CADD_R_CV','PrimateAI_R_CV',
    #                                'M-CAP_R_CV','LRT_R_CV','MutationTaster_R_CV','MutationAssessor_R_CV','FATHMM_R_CV','MetaSVM_R_CV',
    #                                'MetaLR_R_CV','GenoCanyon_R_CV','DANN_R_CV','GERP++_R_CV','phyloP_R_CV','PhastCons_R_CV','SiPhy_R_CV','fitCons_R_CV','MPC_R_CV','MISTIC_R_CV']
    #
    # sys_argv['compare_predictors']=['VARITY_R_CV','DeepSequence_R_CV']
    # sys_argv['compare_predictors']=['VARITY_R_CV','EVMutation_R_CV']  
    # sys_argv['compare_predictors']=['VARITY_R_CV','MISTIC_R_CV']
    # sys_argv['compare_predictors']=['VARITY_R_CV','MPC_R_CV']   
    #
    # sys_argv['compare_predictors']=['VARITY_R_CV','VARITY_R_LOO_CV']       
                         

if sys_argv['action'] == 'target_prediction':
    sys_argv['target_file'] = sys_argv['db_path'] + 'varity/all/varity_target_denovodb_enriched_negative_added_snv_pisa3.csv'
#     sys_argv['target_file'] = sys_argv['db_path'] + 'varity/all/varity_target_denovodb_enriched_negative_added_snv_pisa1.csv'
#     sys_argv['target_file'] = sys_argv['db_path'] + 'varity/all/varity_target_denovodb_enriched_negative_added_snv_pisa2.csv'
    sys_argv['target_dependent_variable'] = 'denovo_label'
#     sys_argv['target_file'] = sys_argv['db_path'] + 'varity/bygene/P01130_varity_snv.csv'
#     sys_argv['target_file'] = sys_argv['db_path'] + 'ukb/csv/ldlr_missense_variants.csv'
    
#     sys_argv['trials_mv_size'] = 200
#     sys_argv['save_target_csv_name'] = sys_argv['project_path'] + 'output/csv/varity_target_ukb_VARITY_R_100.csv'

    sys_argv['prediction_ouput_with_input_cols'] = 0
    sys_argv['additional_features'] = []
    sys_argv['loo'] = 0
    sys_argv['shap_test_interaction'] = 0
    sys_argv['shap_train_interaction'] = 0
    
if sys_argv['action'] == 'merge_prediction':
    sys_argv['target_file'] = sys_argv['db_path'] + 'varity/all/varity_target_denovodb_enriched_negative_added_snv_pisa.csv'
    sys_argv['target_predicted_files']= ['Revision1213_varity_target_denovodb_enriched_negative_added_snv_pisa_VARITY_ER.csv','Revision1213_varity_target_denovodb_enriched_negative_added_snv_pisa_VARITY_R.csv']
#     
#     sys_argv['target_file'] = sys_argv['db_path'] + 'varity/all/varity_target_denovodb_enriched_negative_added_snv_pisa1.csv' 
#     sys_argv['target_predicted_files']= ['Revision1213_pisa1_varity_target_denovodb_enriched_negative_added_snv_pisa1_VARITY_ER.csv','Revision1213_pisa1_varity_target_denovodb_enriched_negative_added_snv_pisa1_VARITY_R.csv']
#     
#     sys_argv['target_file'] = sys_argv['db_path'] + 'varity/all/varity_target_denovodb_enriched_negative_added_snv_pisa2.csv' 
#     sys_argv['target_predicted_files']= ['Revision1213_pisa2_varity_target_denovodb_enriched_negative_added_snv_pisa2_VARITY_ER.csv','Revision1213_pisa2_varity_target_denovodb_enriched_negative_added_snv_pisa2_VARITY_R.csv']
          
    
if sys_argv['action'] == 'test_hyperopt':
    sys_argv['target_file'] = sys_argv['project_path'] + 'output/csv/denovodb_snv_dn1_pisa3.csv'
    sys_argv['target_type'] = 'file'
    sys_argv['target_dependent_variable'] = 'denovo_label'
    
    

# 
# for i in range(10):
#     sys_argv['cur_test_fold'] = i
#     varity_run.varity_run(sys_argv)



if sys_argv['action'] == 'run_batch_id_jobs':
    sys_argv['batch_id_file'] = sys_argv['project_path'] + 'output/csv/' + sys_argv['session_id'] +  '_' + sys_argv['predictor'] + '_loo_indices.csv'       
    sys_argv['batch_id_name'] = 'target_index'
    sys_argv['varity_action'] = 'fun_loo_predictions'
    sys_argv['batch_id_exist_files']= sys_argv['project_path'] + 'output/loo_temp/' + '*' + sys_argv['predictor'] + '.txt'
    sys_argv['parallel_batches'] = 100
    
varity_run.varity_run(sys_argv)

