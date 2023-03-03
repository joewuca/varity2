#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: UTF-8 -*-
import sys
import os
import traceback
import time
import glob
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib import colors, ticker
from matplotlib.patches import Rectangle
import matplotlib.path as mpath
import matplotlib.patches as patches  
from matplotlib.lines import Line2D  
from matplotlib.gridspec import GridSpec
import matplotlib.collections as collections
# python_path = '/usr/local/projects/ml/python/'
project_path = '/usr/local/projects/varity/gwt/www/'
humandb_path = '/usr/local/database/humandb_new/'
# sys.path.append(python_path)
import alm_fun

#email server related parametes
server_address = 'smtp-relay.gmail.com'
server_port = 587
login_user = 'noreply@varianteffect.org'
from_address = 'noreply@varianteffect.org'
subject = 'No Reply'
for line in open(project_path + 'p.txt','r'):
    login_password = line

def run_varity(run_mode, arguments):
    www_output_path = project_path + 'output/' 
    www_log_path = project_path + 'log/'
    www_upload_path = project_path + 'upload/'
     
    ####*************************************************************************************************************************************************************
    # run for local debug
    ####*************************************************************************************************************************************************************
    if run_mode == 0:
        JSON_varity = run_varity()
        print (JSON_varity)  
        sys.exit()    
             
    ####*************************************************************************************************************************************************************
    # run for web 
    ####*************************************************************************************************************************************************************
    if run_mode == 1:
        queryflag = arguments['queryflag']
        session_id = arguments.get('sessionid',None)
        varity_web_log = open(www_log_path + 'varity_web.log', 'a') 
        varity_web_log.write('\n' + str(datetime.now()) + '\n') 
        varity_web_log.write('queryflag: ' + str(queryflag) + '\n') 
        if session_id is not None:
            varity_web_session_log_file = www_log_path + session_id + '.log'
            varity_web_session_log = open(varity_web_session_log_file, 'a')  
            varity_web_session_log.write('\n' + str(datetime.now()) + '\n') 
            varity_web_session_log.write('queryflag: ' + str(queryflag) + '\n')

    ####*************************************************************************************************************************************************************
    # queryflag -1 : Get the resolution of the user screen  
    ####*************************************************************************************************************************************************************    
        if int(queryflag) == -1:
            image_width = arguments['imagewidth']
            image_height = arguments['imageheight']
            callback = arguments['callback']
            if (int(image_width) < 160) or (int(image_height) < 820):  
                error_msg = "Your browser window size is " + str(image_width) + "*" + str(image_height) + " which is smaller than the minimum browser window size requirement 1600*820 for this web application. " + \
                            "To change your browser window size you could press [CTRL or COMMAND] & [-] in your browser or change screen resolution. Please reload the website after browser window size adjustment."
                varity_web_log.write(error_msg + '\n')                                              
                JSON_Return = str(callback) + '([{"content":"' +  error_msg + '"}])'
            else:
                JSON_Return = str(callback) + '([{"content":"OK"}])' 
    ####*************************************************************************************************************************************************************
    # queryflag 0 : upload user files for varity 
    ####*************************************************************************************************************************************************************      
        if int(queryflag) == 0:
            image_width = arguments['imagewidth']
            image_height = arguments['imageheight']
            session_id = arguments['sessionid']    
        
            dms_landscape_file = arguments['upload_landscape_filename']
            dms_fasta_file = arguments['upload_fasta_filename']
            dms_landscape_file_dest = www_upload_path + session_id + '.txt'
            dms_landscape_content = arguments['upload_landscape']
            dms_fasta_file_dest = www_upload_path + session_id + '.fasta'
            dms_fasta_content = arguments['upload_fasta']
                     
            varity_web_session_log.write('image_width: ' + str(image_width) + '\n')
            varity_web_session_log.write('image_height: ' + str(image_height) + '\n')
            varity_web_session_log.write('landscape file name: ' + str(dms_landscape_file) + '\n')
            varity_web_session_log.write('landscape file dest name: ' + str(dms_landscape_file_dest) + '\n')
            varity_web_session_log.write('fasta file name: ' + str(dms_fasta_file) + '\n')
            varity_web_session_log.write('fasta file dest name: ' + str(dms_fasta_file_dest) + '\n')
        
            uploaded_landscape_file = open(dms_landscape_file_dest, 'wb')
            uploaded_landscape_file.write(dms_landscape_content)
            uploaded_landscape_file.close() 
            uploaded_fasta_file = open(dms_fasta_file_dest, 'wb')
            uploaded_fasta_file.write(dms_fasta_content)
            uploaded_fasta_file.close()
            JSON_Return = "N/A"
#             alm_fun.send_email(server_address,server_port,login_user,login_password,from_address,'joe.wu.ca@gmail.com', 'varity Notification', create_email_notification_msg(session_id))

        ####*************************************************************************************************************************************************************
        # queryflag 1 : Run varity and save the result in JSON format to [sessionid].out and send it back to the broswer 
        ####*************************************************************************************************************************************************************      
        if int(queryflag) == 1: 
            email_address = arguments.get('email_address','')                
            callback = arguments['callback']
            session_id = arguments['sessionid']   
            protein_id = arguments['proteinid']             
            data_name = session_id                
            varity_web_session_log.write(str(arguments) + '\n')                  
            
            if os.path.isfile((humandb_path + 'dms/features/' + protein_id + '_features.csv')  ):
                im_proj = create_varity_instance(arguments,varity_web_session_log)
        #                     varity_web_session_log.write(str(rawdata_init_params) + '\n')
                sessionid_JSON = im_proj.varity_run(session_id)                          
                varity_web_output = open(project_path + 'output/' + session_id + '.out', 'w')
                varity_web_output.write(sessionid_JSON)
                varity_web_output.close()
                JSON_Return = str(callback) + '(' + sessionid_JSON + ')'                       
            else:
                error_msg = "The input Uniprot ID " + protein_id + " is not supported yet , please leave your email address in the box below. We will notify your once this ID is supported."
        #                     error_msg = protein_id                    
                varity_web_session_log.write(error_msg + '\n')                        
                JSON_Return = str(callback) + '([{"content":"' +  error_msg + '"}])'
                return (JSON_Return)
            
            if "@" in email_address:
                alm_fun.send_email(server_address,server_port,login_user,login_password,from_address,email_address, subject, create_email_msg(session_id))
                alm_fun.send_email(server_address,server_port,login_user,login_password,from_address,'joe.wu.ca@gmail.com', 'varity Notification', create_email_notification_msg(session_id))
        ####*************************************************************************************************************************************************************
        # queryflag 2 : Read a list of available landscapes
        ####*************************************************************************************************************************************************************      
        if int(queryflag) == 2: 
            file_list = []
            callback = arguments['callback']
            
            #       varity_web_log.write('callback: ' + str(callback) + '\n')
            varity_web_log.write(str(arguments))  
            for file in glob.glob(project_path + 'output/*.out'):
                file_name = os.path.basename(file)[:-4]
                if (file_name[0] == '*'):
                    file_list.append(file_name)
            file_list.sort();
            landscapes_JSON = '['
            for file_name in file_list:     
                    landscapes_JSON += '{"landscape_name":"' + file_name + '"},'            
            landscapes_JSON += ']'
            JSON_Return = str(callback) + '(' + landscapes_JSON + ')'
            varity_web_log.write(JSON_Return + '\n')
             
        ####*************************************************************************************************************************************************************
        # queryflag 3 : Read JSON from [sessionid].out file and send it back to the broswer 
        ####*************************************************************************************************************************************************************      
        if int(queryflag) == 3: 
            callback = arguments['callback']
            session_id = arguments['sessionid']
            search_type = arguments['search_type']    
            varity_web_session_log.write(str(arguments) + '\n')
        
            [uniprot_id,protein_name,protein_file] = get_protein_file_name (session_id,search_type)
            varity_web_session_log.write("Current protein file: " + protein_file + '\n')  
            #******************************************
            #load protein feature and preidtion result  
            #******************************************            
            cols = ['aa_ref','aa_pos','aa_alt','VARITY_R','VARITY_ER','VARITY_R_LOO','VARITY_ER_LOO',
                    'aa_psipred','ss_end_pos','hmm_id','pfam_end_pos','gnomad_af_log10','asa_mean_normalized','clinvar_clin_sig',
                    'VARITY_R_colorcode','VARITY_R_LOO_colorcode', 'VARITY_ER_colorcode','VARITY_ER_LOO_colorcode','asa_colorcode']                    
            if os.path.isfile(protein_file):                                            
                #******************************************
                #Only Load data for range of positions
                #******************************************      
                varity_protein_df = pd.read_csv(protein_file,sep = '\t',usecols = cols,low_memory = False) [cols]
#                 varity_protein_df = pd.read_csv(protein_file,sep = '\t')[cols]
#                 varity_protein_df.loc[varity_protein_df['aa_ref'] == varity_protein_df['aa_alt'],'VARITY_R_colorcode'] = '#FDF9CE'  
#                 varity_protein_df.loc[varity_protein_df['aa_ref'] == varity_protein_df['aa_alt'],'VARITY_ER_colorcode'] = '#FDF9CE' 
#                                                                                                            
                #******************************************
                #Retrun the JSON
                #******************************************
#                 print(varity_protein_df.columns)
                varity_protein_df.columns = ['a' + str(i) for i in list(range(varity_protein_df.shape[1]))]
                varity_protein_df_json = varity_protein_df.to_json(orient='records')
                JSON_Return = str(callback) + '(' + varity_protein_df_json + ')'
            else:
                error_msg = "The input protein is incorrect or not supported by VARITY yet, please enter your email address to request this protein. You will be informed when the features and predictions for the preotein is ready!"                                       
                varity_web_session_log.write("ERROR:" + error_msg + '\n')                        
                JSON_Return = str(callback) + '([{"error":"' +  error_msg + '"}])'              

        ####*************************************************************************************************************************************************************
        # queryflag 4 : Return pubmed link of the session id  
        ####*************************************************************************************************************************************************************                     
        if int(queryflag) == 4:     
            callback = arguments['callback']            
            session_id = arguments['sessionid']
            varity_web_session_log.write(str(arguments) + '\n') 
            pubmed_file =  project_path + 'output/' +   session_id + '_pubmed.txt'             
            if os.path.isfile(pubmed_file):
                with open(pubmed_file , 'r') as myfile:
                    pubmed_link = myfile.read().replace('\r', '').replace('\n', '')
                JSON_Return =  str(callback) + '([{"content":' + '"' + pubmed_link  + '"'+ '}])'                  
            else:
                error_msg = "Error! The pubmed link for the variant effect map doesn't exist!"                                       
                varity_web_session_log.write(error_msg + '\n')                        
                JSON_Return = str(callback) + '([{"error":"' +  error_msg + '"}])'
        
        ####*************************************************************************************************************************************************************
        # queryflag 5 : send error email  
        ####*************************************************************************************************************************************************************                     
        if int(queryflag) == 5:     
            callback = arguments['callback']            
            session_id = arguments['sessionid']
            error_email = arguments['email_address']
            varity_web_session_log.write(str(arguments) + '\n')  
            if '@' in error_email:               
                alm_fun.send_email(server_address,server_port,login_user,login_password,from_address,'joe.wu.ca@gmail.com', subject + ' ERROR', create_email_error_msg(error_email,session_id)) 
            JSON_Return = str(callback) + '([{"content":"OK"}])' 
            
        ####*************************************************************************************************************************************************************
        # queryflag 6 : View option async  
        ####*************************************************************************************************************************************************************                     
        if int(queryflag) == 6:     
            callback = arguments['callback']            
            session_id = arguments['sessionid']            
            score_name = arguments['score_name']
            from_pos = arguments['from_pos']
            to_pos = arguments['to_pos']
            varity_web_session_log.write(str(arguments) + '\n')   
            JSON_Return = str(callback) + '([{"content":"' + score_name + "|" + from_pos + "|" + to_pos +'"}])'
#             varity_web_session_log.write(JSON_Return + '\n')  

        ####*************************************************************************************************************************************************************
        # queryflag 7 : Read JSON for single variant
        ####*************************************************************************************************************************************************************      
        if int(queryflag) == 7: 
            callback = arguments['callback']
            session_id = arguments['sessionid']  
            search_type = arguments['search_type']     
            aa_pos = int(arguments['aa_pos'])
            aa_ref = arguments['aa_ref']
            aa_alt = arguments['aa_alt']
            varity_web_session_log.write(str(arguments) + '\n')
           
            #******************************************
            #load variant feature and preidtion result  
            #******************************************
            [uniprot_id,protein_name,protein_file] = get_protein_file_name (session_id,search_type)
            if os.path.isfile(protein_file):                                            
                #******************************************
                #Only Load data for range of positions
                #******************************************      
                cols = open(protein_file, "r").readlines()[0].rstrip().split('\t')
                lst_aa_21 = ["S", "A", "V", "R", "D", "F", "T", "I", "L", "K", "G", "Y", "N", "C", "P", "E", "M", "W", "H", "Q", "*"]
                cur_line = (aa_pos-1) * 21 +  lst_aa_21.index(aa_alt) +1              
                line = open(protein_file, "r").readlines()[cur_line].rstrip().split('\t')
                varity_variant_df  = pd.DataFrame([line],columns = cols)
                #******************************************
                #Retrun the JSON
                #******************************************
                varity_variant_df_json = varity_variant_df.to_json(orient='records')
                JSON_Return = str(callback) + '(' + varity_variant_df_json + ')'
            else:
                error_msg = "The map requested is not avalible!"                                       
                varity_web_session_log.write(error_msg + '\n')                        
                JSON_Return = str(callback) + '([{"error":"' +  error_msg + '"}])'                    

        ####*************************************************************************************************************************************************************
        # queryflag 8 : Create VARITY effect map
        ####*************************************************************************************************************************************************************      
        if int(queryflag) == 8: 
            callback = arguments['callback']            
            session_id = arguments['sessionid']
            search_type = arguments['search_type']
            score_name = arguments['score_name'].split(' ')[0]
            from_pos = arguments['from_pos']
            to_pos = arguments['to_pos']
            varity_web_session_log.write(str(arguments) + '\n')      
            
            [uniprot_id,protein_name,protein_file] = get_protein_file_name (session_id,search_type)      
            map_name = create_varity_effect_map(uniprot_id,protein_name,score_name,int(from_pos),int(to_pos))            
            JSON_Return = str(callback) + '([{"content":"' + map_name  +'"}])'
            
        ####*************************************************************************************************************************************************************
        # queryflag 9 : Create VARITY output file
        ####*************************************************************************************************************************************************************      
        if int(queryflag) == 9: 
            callback = arguments['callback']            
            session_id = arguments['sessionid']
            search_type = arguments['search_type']
            score_name = arguments['score_name'].split(' ')[0]
            from_pos = arguments['from_pos']
            to_pos = arguments['to_pos']
            varity_web_session_log.write(str(arguments) + '\n')      
            
            [uniprot_id,protein_name,protein_file] = get_protein_file_name (session_id,search_type)      
            output_file_name = create_varity_output_file(uniprot_id,protein_name,score_name,int(from_pos),int(to_pos))            
            JSON_Return = str(callback) + '([{"content":"' + output_file_name  +'"}])'
              
  
        varity_web_log.close()
        if session_id is not None:    
            varity_web_session_log.close()

        return (JSON_Return)
#         return (JSON_Return)
#     except:
#         err_msg = traceback.format_exc()
#         err_msg = err_msg.replace('\"',' ');
#         err_msg = err_msg.replace('\'',' ');
#         print (err_msg + '\n')
#         callback = arguments.get('callback','no callback')
#         if arguments.get("sessionid",None) is None:
#             varity_web_log.write(err_msg + '\n')
#             varity_web_log.close()
#         else:
#             varity_web_session_log.write(err_msg + '\n')
#             varity_web_session_log.close()
#         JSON_Return = str(callback) + '([{"error":"varity Error! Please check your inputs or leave your email address on the box below, we will notify you once the problem is found."}])'
        #alm_fun.send_email(server_address,server_port,login_user,login_password,from_address,'joe.wu.ca@gmail.com', subject + ' ERROR', create_email_error_msg('NA',session_id))    
    
def get_protein_file_name (session_id,search_type):
    #******************************************
    # Determine the file name by search_type  
    #******************************************    
    varity_supported_ids_df =  pd.read_csv(project_path + 'downloads/varity_supported_ids.txt', sep = '\t')    
    
    if search_type =='protein_name':
        protein_name = session_id.upper().rstrip()
        if varity_supported_ids_df.loc[varity_supported_ids_df['symbol'] == protein_name,'uniprot_id'].shape[0] > 0:
            uniprot_id = varity_supported_ids_df.loc[varity_supported_ids_df['symbol'] == protein_name,'uniprot_id'].values[0]
        else:
            uniprot_id = 'NULL'
       
    if search_type == 'uniprot_id':
        uniprot_id = session_id.upper().rstrip()
        if varity_supported_ids_df.loc[varity_supported_ids_df['uniprot_id'] == uniprot_id,'symbol'].shape[0] > 0:
            protein_name = varity_supported_ids_df.loc[varity_supported_ids_df['uniprot_id'] == uniprot_id,'symbol'].values[0]
        else:
            protein_name = 'NULL'        
    protein_file = humandb_path + 'varity/bygene/' + uniprot_id + '_' + protein_name + '_varity_web.txt'
    return([uniprot_id,protein_name,protein_file])    
          
def create_varity_instance(arguments,varity_web_session_log):     
    protein_id = arguments['proteinid']
    session_id = arguments.get('sessionid','')
    email_address = arguments.get('email_address','')      
        
    dms_landscape_file = session_id + '.txt'
    dms_fasta_file = session_id + '.fasta'            
    regression_cutoff = float(arguments.get('regression_cutoff','-inf'))
    data_cutoff = float(arguments.get('data_cutoff','-inf'))        
    auto_regression_cutoff = int(arguments['if_auto_cutoff'])
    data_cutoff_flag = int(arguments['if_data_cutoff'])
    normalized_flag = 1 - int(arguments['if_normalization'])   
    regularization_flag = int(arguments['if_regularization'])
    rawprocessed_flag = 1 - int(arguments['if_rawprocessing'])         
    proper_count = int(arguments.get('proper_count',8))  
    synstop_cutoff = float(arguments.get('synstop_cutoff','-inf'))
    stop_exclusion = arguments.get('stop_exclusion','0')  
    
    #alm_project class parameters
    project_params = {}

    
    project_params['project_name'] = 'varity'
    project_params['project_path'] = project_path
    project_params['humandb_path'] = humandb_path
    project_params['log'] = varity_web_session_log 
    project_params['verbose'] = 1

        
    #the reason the following parameters don't belong to data class is we may want to create multiple data instance in one project instance 
    project_params['data_names'] = [] 
    project_params['train_data'] = []        
    project_params['test_data'] = []
    project_params['target_data'] = []
    project_params['extra_train_data'] = []
    project_params['use_extra_train_data'] = []
    project_params['extra_train_data_lst'] = [] 
    project_params['input_data_type'] = []
     
    project_params['run_data_names'] = [session_id]
    project_params['run_estimator_name'] = 'xgb_r'
    project_params['run_estimator_scorename'] = 'rmse'
    project_params['grid_search_on'] = 0
    
    project_params['modes'] = None
    project_params['train_features'] = None
    project_params['train_features_name'] = None
    project_params['start_features'] = None
    project_params['start_features_name'] = None  
    project_params['compare_features'] = None
    project_params['compare_features_name'] = None
    project_params['compare_features_name_forplot'] = None
    project_params['feature_compare_direction'] = 0 
    project_params['compare_methods'] = None 
    
    project_params['plot_columns'] = [0, 1]
    project_params['plot_vmin'] = 0.5
    project_params['plot_vmax'] = 1
    project_params['fig_w'] = 20
    project_params['fig_h'] = 5
        
    #alm_data class parameters
    data_params = {}
    data_params['path'] = project_path 
    data_params['log'] = varity_web_session_log  
    data_params['verbose'] = 1
    
    data_params['name'] = None 
    data_params['target_data_original_df'] = None
    data_params['train_data_original_df'] = None
    data_params['test_data_original_df'] = None                
    data_params['extra_train_data_original_df'] = None 
    data_params['use_extra_train_data'] =  None
    data_params['predicted_target_df'] = None

    data_params['independent_testset'] = 0
    data_params['extra_train_data_original_df_lst'] = [] 
    data_params['extra_data_index'] = 0
    data_params['test_split_method'] = 0
    data_params['test_split_folds'] = 1
    data_params['test_split_ratio'] = 0
    data_params['cv_split_method'] = 2
    data_params['cv_split_folds'] = 1
    data_params['cv_split_ratio'] = 0.1
    data_params['validation_from_testset'] = False
    data_params['percent_min_feature'] = 1
    
    data_params['dependent_variable'] = 'fitness'
    data_params['filter_target'] = 0
    data_params['filter_test'] = 0
    data_params['filter_train'] = 0
    data_params['filter_validation'] = 0
    data_params['prediction_bootstrapping'] = 0
    data_params['bootstrapping_num'] = 3
    
    data_params['if_gradient'] = auto_regression_cutoff
    data_params['if_engineer'] = 0
    data_params['load_from_disk'] = 0
    data_params['save_to_disk'] = 1
    data_params['cur_test_split_fold'] = 0
    data_params['cur_gradient_key'] = 'no_gradient'
    data_params['innerloop_cv_fit_once'] = 0

    data_params['onehot_features'] = []
    data_params['cv_fitonce'] = 0
        
    #alm_ml class parameters
    ml_params = {}
    ml_params['log'] = varity_web_session_log 
    ml_params['verbose'] = 1
    
    ml_params['run_grid_search'] = 0
    ml_params['fs_start_features'] = []
    ml_params['fs_T'] = 0.001
    ml_params['fs_alpha'] = 0.8
    ml_params['fs_K'] = 100
    ml_params['fs_epsilon'] = 0.00001 
    ml_params['tune_tree_nums_before_test'] = 0
    ml_params['tune_tree_nums_during_cv'] = 0    
    
    #es init parameters for es_ml class
    es_params = {}
    es_params['ml_type'] = 'regression'
    es_params['single_feature_as_prediction'] = 1
    es_params['estimator'] = 'xgb_r'
    es_params['name'] = None
    es_params['gs_range'] = None
    es_params['score_name'] = None
    es_params['score_direction'] = None
    es_params['feature_importance_name'] = None
    es_params['round_digits'] = 4 
    es_params['if_feature_engineer'] = 1
    es_params['feature_engineer'] = None
    es_params['shuffle_features'] = []
    es_params['weighted_example'] = 0
    es_params['flip_contamination_train'] = 0
    es_params['flip_contamination_test'] = 0
     
    #data preprocess and update data_params                  
    varity_params = {} 
    varity_params['log'] = varity_web_session_log 
    varity_params['verbose'] = 1
    varity_params['project_path'] = project_path
    varity_params['humandb_path'] = humandb_path
    
    varity_params['project_params'] = project_params
    varity_params['data_params'] = data_params
    varity_params['ml_params'] = ml_params
    varity_params['es_params'] = es_params
       
    #varity class: parameters for data preprocessing
    varity_params['run_data_preprocess'] = 1 
    varity_params['dms_landscape_files'] = [dms_landscape_file]
    varity_params['dms_fasta_files'] = [dms_fasta_file]
    varity_params['dms_protein_ids'] = [protein_id]
    varity_params['data_names'] = [session_id]
    varity_params['remediation'] = [0]
    
    if normalized_flag == 1:
        varity_params['synstop_cutoffs'] = [float("-inf")]
        varity_params['stop_exclusion'] = ["0"]
    else:
        varity_params['synstop_cutoffs'] = [synstop_cutoff]
        varity_params['stop_exclusion'] = [stop_exclusion]
        
    if data_cutoff_flag == 1:
        varity_params['quality_cutoffs'] = [data_cutoff]
    else:
        varity_params['quality_cutoffs'] = [float("-inf")]
    
    if auto_regression_cutoff == 1:
        varity_params['regression_quality_cutoffs'] = [float("-inf")]
    else:
        varity_params['regression_quality_cutoffs'] = [regression_cutoff]
                    
    varity_params['proper_num_replicates'] = [proper_count]
    varity_params['raw_processed'] = [rawprocessed_flag]
    varity_params['normalized_flags'] = [normalized_flag]
    varity_params['regularization_flags'] = [regularization_flag]
    varity_params['reverse_flags'] = [1]
    varity_params['floor_flags'] = [1]
    varity_params['combine_flags'] = [0]

    varity_params['pre_process'] = 1
    varity_params['combine_dms'] = 0
        
    #varity class: parameters for feature engineering
    varity_params['k_range'] = range(3, 5)
    
    
#     varity_params['use_funsums'] = ['funsum_fitness_mean']
#     varity_params['use_funsums_name'] = ['fs']  
#     varity_params['value_orderby'] = varity_params['use_funsums']
#     varity_params['value_orderby_name'] = varity_params['use_funsums_name']
    
    varity_params['value_orderby'] = ['blosum100']
    varity_params['value_orderby_name'] = ['bs']
    
    
    varity_params['centrality_names'] = ['mean', 'se', 'count']
    varity_params['dependent_variable'] = 'fitness'
    varity_params['add_funsum_onfly'] = 0 

    #varity class: Jochen's R script related parameters
    varity_params['if_runR'] = 0
    varity_params['R_command'] = '/Library/Frameworks/R.framework/Versions/3.3/Resources/Rscript'
    varity_params['R_wd'] = '/Users/joewu/Google_Drive/Business/AlphaMe/Source_Code/R/R_GI/Jochen/dmspipeline'
    varity_params['R_script_path'] = '/Users/joewu/Google_Drive/Business/AlphaMe/Source_Code/R/R_GI/Jochen/dmspipeline/bin/simpleImpute.R'
    varity_params['R_bend'] = '0'   

    #varity class: email related parameters
    varity_params['email_server_address'] = server_address
    varity_params['email_server_port'] = server_port
    varity_params['email_login_user'] = login_user
    varity_params['email_login_password'] = login_password
    varity_params['email_from_address'] = from_address
    varity_params['email_msg_content'] = create_email_msg(session_id)
    varity_params['email_error_content'] = create_email_error_msg(email_address,session_id)
    varity_params['email_notification_content'] = create_email_notification_msg(session_id)
    
    
    #CBS manuscript
    varity_params['manuscript_cv_predictions'] = 1
    varity_params['manuscript_cv_folds'] = 10
    
        
    im_proj = varity.varity(varity_params)    
    return (im_proj)
    
def create_email_msg(session_id):      
    msg = "*** This is an automatically generated e-mail, please do not reply!\n" + \
    "*** Send your questions and comments to: joe.wu@varianteffect.org\n" + \
    "Your varity session " + "'" + session_id + "'" + " has completed at " + time.ctime() + "(Eastern Time). " + \
    "You can revisit your imputed map by entering your session ID in 'View Landscape' section at impute.varianteffect.org. " + \
    "You also can access the imputed results directly from the following links:\n" + \
    "(1) Original variant effect map: http://impute.varianteffect.org/output/" + session_id + "_fitness_refine.pdf\n" + \
    "(2) Refined variant effect map: http://impute.varianteffect.org/output/" + session_id + "_fitness_org.pdf\n" + \
    "(3) varity results: http://impute.varianteffect.org/output/" + session_id + "_varity.csv\n\n" + \
    "Regards,\nRoth Lab"            
    return(msg)

def create_email_error_msg(user_email,session_id):
    msg = "varity error happened on user " +"[" + user_email + "] session " + "'" + session_id  + "' at " + time.ctime() + "(Eastern Time). " + \
          "Error Log: http://impute.varianteffect.org/log/" + session_id + ".log\n" + \
          "Regards,\nRoth Lab"  
    return(msg)  
    
def create_email_notification_msg(session_id):
    msg = "varity happened with session " + "[" +  session_id  + "] at " + time.ctime() + "(Eastern Time). " + \
          "Check Log at http://impute.varianteffect.org/log/" + session_id + ".log\n" + \
          "Regards,\nRoth Lab"  
    return(msg)
        
def create_varity_effect_map(uniprot_id,protein_name,score_name,from_pos,to_pos):

    cur_log = project_path + 'log/' +  uniprot_id + '_effect_map.log'
    ####*************************************************************************************************************
    # Color Graidents
    ####*************************************************************************************************************     
    v_max_varity = 1
    v_center_varity = 0.5
    v_min_varity = 0
    v_max_varity_color = '#C6172B'
    v_center_varity_color = '#FFFFFF'
    v_min_varity_color = '#3155C6'
    n_gradient_max_varity = 5
    n_gradient_min_varity = 5                
    [lst_max_colors_varity, lst_min_colors_varity] = alm_fun.create_color_gradients(v_max_varity, v_min_varity, v_center_varity, v_max_varity_color, v_min_varity_color, v_center_varity_color, n_gradient_max_varity, n_gradient_min_varity)
    [lst_max_colors_asa, lst_min_colors_asa] = alm_fun.create_color_gradients(1, 0, 0, '#3155C6', '#FFFFFF', '#FFFFFF', 10, 10)
    
    ####*************************************************************************************************************
    # Load the varity effect map data 
    ####*************************************************************************************************************
    protein_file = humandb_path + 'varity/bygene/varity_web_' + protein_name + '[' + uniprot_id + ']' + '.csv'
    if os.path.isfile(protein_file):
        cols = ['aa_ref','aa_pos','aa_alt','VARITY_R','VARITY_ER','VARITY_R_LOO','VARITY_ER_LOO',
                    'aa_psipred','ss_end_pos','hmm_id','pfam_end_pos','gnomad_af_log10','asa_mean_normalized','clinvar_clin_sig',
                    'VARITY_R_colorcode','VARITY_R_LOO_colorcode', 'VARITY_ER_colorcode','VARITY_ER_LOO_colorcode','asa_colorcode']                                                      
        varity_protein_df = pd.read_csv(protein_file,sep = '\t',usecols = cols,low_memory = False) [cols]                                         
        varity_protein_df = varity_protein_df.loc[(varity_protein_df['aa_pos'] >= from_pos) & (varity_protein_df['aa_pos'] <= to_pos),:]
    else:
        return(-1)
    
    ####*************************************************************************************************************
    # plot title 
    ####*************************************************************************************************************
    plot_title = protein_name + '[' + uniprot_id + '] ' + score_name + ' Effect Map [' + str(from_pos) + '-' + str(to_pos) + ']' 
#     vmax = np.nanmax(list(varity_gene_figure_df[score_name]))
#     vmin = np.nanmin(list(varity_gene_figure_df[score_name]))
         
    ####*************************************************************************************************************
    # SYN variants color , and set score to 
    ####*************************************************************************************************************    
    syn_color = '#fdf9ce'        
    varity_protein_df.loc[varity_protein_df['aa_ref'] == varity_protein_df['aa_alt'], score_name] = np.nan
    varity_protein_df.loc[varity_protein_df['aa_ref'] == varity_protein_df['aa_alt'], score_name + '_colorcode'] = syn_color
    
    ####*************************************************************************************************************
    # Score standard error (set to 0 in this case as VARITY score has no standard error currently)
    ####*************************************************************************************************************
    se_name = score_name + '_se'
    varity_protein_df[se_name] = 0
    varity_protein_df.loc[varity_protein_df[score_name].isnull(), se_name] = np.nan        

    ####*************************************************************************************************************
    # Create data sets for [score,asa,ss,pfam,colorcode,se,colorcode_ordered] 
    ####*************************************************************************************************************
    varity_gene_figure_df = varity_protein_df.copy()
    #score     
    landscape_score = varity_protein_df.pivot(index='aa_alt', columns='aa_pos', values=score_name)
    #asa
    landscape_asa = varity_protein_df.loc[varity_protein_df['asa_mean_normalized'].notnull(), ['aa_pos', 'asa_colorcode']].drop_duplicates()
    #ss
    landscape_ss = varity_protein_df.loc[varity_protein_df['ss_end_pos'].notnull(), ['aa_pos', 'aa_psipred', 'ss_end_pos']]
    landscape_ss = landscape_ss.drop_duplicates()
    #pfam
    landscape_pfam = varity_protein_df.loc[varity_gene_figure_df['hmm_id'].notnull() & varity_protein_df['pfam_end_pos'].notnull(), ['aa_pos', 'hmm_id', 'pfam_end_pos']]
    landscape_pfam = landscape_pfam.drop_duplicates()
    #colorcode
    landscape_colorcode = varity_protein_df.pivot(index='aa_alt', columns='aa_pos', values=score_name + '_colorcode')
    #se
    landscape_se = varity_protein_df.pivot(index='aa_alt', columns='aa_pos', values=se_name)
    #colorcode_ordered    
    landscape_score_copy = landscape_score.copy()            
    landscape_score_copy.drop('*', axis=0, inplace=True)
    landscape_score_copy.fillna(np.nanmax(landscape_score_copy) + 1, inplace=True)
    landscape_score_orderindex = landscape_score_copy.apply(lambda x: np.argsort(x), axis=0)    
    landscape_colorcode_copy = landscape_colorcode.copy()
    landscape_colorcode_copy.drop('*', axis=0, inplace=True)
    landscape_colorcode_copy.replace(syn_color, '#C0C0C0', inplace=True)
    landscape_colorcode_ordered = landscape_colorcode_copy.apply(lambda x: np.array(x)[landscape_score_orderindex[x.name]], axis=0)
    landscape_colorcode_ordered.index = range(20)
    
    ####*************************************************************************************************************
    # Start to plot figures
    ####*************************************************************************************************************    
#     fig_width = int(len(landscape_colorcode.columns) / 5)
    f = len(landscape_colorcode.columns) / 550             
    fig_width = 30
    aa_plot = ['*', 'P', 'C', 'G', 'Q', 'N', 'T', 'S', 'E', 'D', 'K', 'H', 'R', 'W', 'Y', 'F', 'M', 'I', 'L', 'V', 'A']            
    fig = plt.figure(figsize=(fig_width, 12)) 
    font_scale_factor = 1.5
    fig.patch.set_facecolor('white')
    gs = GridSpec(10, 1, hspace=0.3)
        
    ####************************************************************************************************************************************************************* 
    # Top additional tracks (secondary structure, accessible surface area, pfam etc) [ax_1]
    ####*************************************************************************************************************************************************************
    stime = time.time()
    n_tracks = 3
    ax_1 = plt.subplot(gs[1:3, :])                                                 
    x = [1] * (n_tracks + 1) + list(range(1, landscape_colorcode.shape[1] + 1))
    y = list(range(1, n_tracks + 2)) + [1] * landscape_colorcode.shape[1]                        
    ax_1.plot(x, y, alpha=0)
    
    ####**************************
    # asa tracks
    ####**************************
    asa_patches = []
    for idx in landscape_asa.index:                
        x = landscape_asa.loc[idx, 'aa_pos'] - from_pos +1
        xy_color = landscape_asa.loc[idx, 'asa_colorcode']
        rect = patches.Rectangle((x, 1), 1, 1, linewidth=1, edgecolor=xy_color, facecolor=xy_color, fill=True, clip_on=False)
        asa_patches.append(rect)
    pass
    ax_1.add_collection(collections.PatchCollection(asa_patches, match_original=True))
    
    ####**************************
    # ss tracks
    ####**************************
    ss_patches = []
    for idx in landscape_ss.index:                
        x = landscape_ss.loc[idx, 'aa_pos'] - from_pos +1
        if landscape_ss.loc[idx, 'aa_psipred'] == 'C':
            width = int(landscape_ss.loc[idx, 'ss_end_pos'] - landscape_ss.loc[idx, 'aa_pos'] + 1)
            ss_patch_C = patches.Rectangle((x, 2), width, 1, linewidth=1, edgecolor='#FFFFFF', facecolor='#FFFFFF', fill=True, clip_on=False)
            ss_patches.append(ss_patch_C)
             
        if landscape_ss.loc[idx, 'aa_psipred'] == 'E':  # beat sheets
            width = int(landscape_ss.loc[idx, 'ss_end_pos'] - landscape_ss.loc[idx, 'aa_pos'] + 1)
            ss_patch_E = patches.Arrow(x, 2.5, width, 0, linewidth=1, edgecolor='#000000', facecolor='#000000', fill=True, clip_on=False)
            ss_patches.append(ss_patch_E)
             
        if landscape_ss.loc[idx, 'aa_psipred'] == 'H':  # alpha helix
            for i in range(x, int(landscape_ss.loc[idx, 'ss_end_pos'] - from_pos + 2)):
                cur_path = mpath.Path
                cur_path_data = [(cur_path.MOVETO, (i, 2)), (cur_path.CURVE4, (i + 1, 2.5)), (cur_path.CURVE4, (i + 1, 2.9)), (cur_path.CURVE4, (i + 0.5, 2.9)), (cur_path.CURVE4, (i - 0.5, 2.9)), (cur_path.CURVE4, (i, 2.5)), (cur_path.CURVE4, (i + 1, 2))]
                codes, verts = zip(*cur_path_data)
                cur_path = mpath.Path(verts, codes)                        
                ss_patch_H = patches.PathPatch(cur_path, linewidth=1, edgecolor='#4D4D4D', facecolor='#4D4D4D', fill=False, clip_on=False)
                ss_patches.append(ss_patch_H)                     
    pass  
    ax_1.add_collection(collections.PatchCollection(ss_patches, match_original=True))
     
    ####************************** 
    # pfam track
    ####**************************
    pfam_patches = []
    pfam_patch = patches.Rectangle((1, 3), landscape_colorcode.shape[1], 1, linewidth=1, edgecolor='#C0C0C0', facecolor='#C0C0C0', fill=True, clip_on=False)
    pfam_patches.append(pfam_patch)
    for idx in landscape_pfam.index:                
        x = landscape_pfam.loc[idx, 'aa_pos'] - from_pos +1
        x_end = np.min([to_pos,int(landscape_pfam.loc[idx, 'pfam_end_pos'])]) - from_pos +1
        width = x_end - x + 1
        ax_1.text(x + width / 2, 3.3, landscape_pfam.loc[idx, 'hmm_id'], fontstyle='italic', fontweight='bold', fontsize=font_scale_factor*12,)                    
        pfam_patch = patches.Rectangle((x, 3), width, 1, linewidth=1, edgecolor='#FFD700', facecolor='#FFD700', fill=True, clip_on=False)
        pfam_patches.append(pfam_patch)
    pass
    ax_1.add_collection(collections.PatchCollection(pfam_patches, match_original=True))
    

    ax_1.yaxis.set_ticks([1, 2.5, 4])
    ax_1.yaxis.set_ticklabels(['ASA', 'SS', 'Domain'])
    ax_1.patch.set_facecolor('white')
    ax_1.set_xbound(1, landscape_colorcode.shape[1] + 1)
    for loc, spine in ax_1.spines.items():
        spine.set_linestyle('-')
        spine.set_smart_bounds(True)
        spine.set_linewidth(2.0)
        spine.set_color('black')
        spine.set_visible(False)
    pass 
    ax_1.tick_params(direction='out', length=6, width=2, colors='black', grid_color='b', grid_alpha=0.0)
    ax_1.xaxis.set_visible(False)
    ax_1.yaxis.set_visible(False)

    ####****************************************
    # legend (right side) for additional tracks
    ####****************************************    
    l = landscape_colorcode.shape[1]
    x2 = 33
    step = 2 / len(lst_max_colors_asa)
    for i in range(len(lst_max_colors_asa)):
        y2 = step * i + 1.5
        xy_color = lst_max_colors_asa[len(lst_max_colors_asa) - i - 1] 
        rect = patches.Rectangle((x2 * f + l, y2), 10 * f, step, linewidth=1, edgecolor=xy_color, facecolor=xy_color, fill=True, clip_on=False)
        ax_1.add_patch(rect)
    legend_fitness = []            
    legend_fitness.append((((x2 + 13) * f + l, 1.5), ((x2 + 13) * f + l, 3.5)))
    legend_fitness.append((((x2 + 13) * f + l, 1.5), ((x2 + 17) * f + l, 1.5)))
    legend_fitness.append((((x2 + 13) * f + l, 2.5), ((x2 + 17) * f + l, 2.5)))
    legend_fitness.append((((x2 + 13) * f + l, 3.5), ((x2 + 17) * f + l, 3.5)))
    lc = collections.LineCollection(legend_fitness, linewidth=2, color='black', clip_on=False)
    ax_1.add_collection(lc) 
    ax_1.text((x2 + 25) * f + l, 2.5, "ASA", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    ax_1.text((x2 + 19) * f + l, 1.5, "0", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    ax_1.text((x2 + 19) * f + l, 2.5, "0.5", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    ax_1.text((x2 + 19) * f + l, 3.5, "1", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    
    ####****************************************
    # legend (left side) for additional tracks
    ####****************************************
    x = -40    
    ax_1.text((x - 5) * f, 1.5, "ASA", fontsize=font_scale_factor*10, va='center', weight='bold')
    ax_1.text((x - 5) * f, 2.5, "SS", fontsize=font_scale_factor*10, va='center', weight='bold')
    ax_1.text((x - 5) * f, 3.5, "Pfam", fontsize=font_scale_factor*10, va='center', weight='bold')
    x1 = x + 11
    left_legend_lines = []        
    left_legend_lines.append(((x1 * f, 1.5), ((x1 + 3) * f, 1.5)))
    left_legend_lines.append(((x1 * f, 2.5), ((x1 + 3) * f, 2.5)))
    left_legend_lines.append(((x1 * f, 3.5), ((x1 + 3) * f, 3.5)))
    left_legend_lines.append((((x1 + 3) * f, 1.5), ((x1 + 3) * f, 3.5)))            
    lc = collections.LineCollection(left_legend_lines, linewidth=2, color='black', clip_on=False)
    ax_1.add_collection(lc) 
    
    etime = time.time()    
    alm_fun.show_msg (cur_log,1,"additional tracks running time was %g seconds" % (etime - stime))  

    ####************************************************************************************************************************************************************* 
    # column ordered genophenogram [ax_2]
    ####*************************************************************************************************************************************************************
    stime = time.time()
    ax_2 = plt.subplot(gs[3:5, :])                                                 
    x = [1] * landscape_colorcode_ordered.shape[0] + list(range(1, landscape_colorcode_ordered.shape[1] + 1))
    y = list(range(1, landscape_colorcode_ordered.shape[0] + 1)) + [1] * landscape_colorcode_ordered.shape[1]                        
    ax_2.plot(x, y, alpha=0)
    rectangle_patches = []
    for x_pos in landscape_colorcode_ordered.columns:
        for y_pos in landscape_colorcode_ordered.index:
            x = x_pos - from_pos +1 
            y = y_pos + 1
            xy_color = landscape_colorcode_ordered.loc[y_pos, x_pos]
            rect = patches.Rectangle((x, y), 1, 1, linewidth=1, edgecolor=xy_color, facecolor=xy_color, fill=True, clip_on=False)
            rectangle_patches.append(rect) 
    pass           
    ax_2.add_collection(collections.PatchCollection(rectangle_patches, match_original=True))

    ax_2.patch.set_facecolor('white')  
    ax_2.yaxis.set_ticks([1, 5, 10, 15, 20])
    ax_2.yaxis.set_ticklabels([0, 0.25, 0.5, 0.75, 1])
    ax_2.set_ybound(1, 21)
    ax_2.set_xbound(1, landscape_colorcode.shape[1] + 1)  
    
    ax_2.xaxis.set_visible(False)
    ax_2.yaxis.set_visible(False)
    for loc, spine in ax_2.spines.items():
        spine.set_linestyle('-')
        spine.set_smart_bounds(True)
        spine.set_linewidth(2.0)
        spine.set_color('black')
        spine.set_visible(False)
    pass 
#     ax_2.tick_params(direction='out', length=6, width=2, colors='black', grid_color='b', grid_alpha=0.0)
     
    ####***********************************************
    # legend for the ordered genophenogram (right side)
    ####***********************************************
    x2 = 33

    lst_colors_varity_new = lst_max_colors_varity + lst_min_colors_varity  
    step = 19 / len(lst_colors_varity_new)
    for i in range(len(lst_colors_varity_new)):
        y2 = step * i + 1.5
        xy_color = lst_colors_varity_new[len(lst_colors_varity_new) - i - 1] 
        rect = patches.Rectangle((x2 * f + l, y2), 10 * f, step, linewidth=1, edgecolor=xy_color, facecolor=xy_color, fill=True, clip_on=False)
        ax_2.add_patch(rect)
    pass
    se_legend_fitness = []     

    se_legend_fitness.append((((x2 + 13) * f + l, 1.5), ((x2 + 13) * f + l, 21.5)))
    se_legend_fitness.append((((x2 + 13) * f + l, 1.5), ((x2 + 17) * f + l, 1.5)))
    se_legend_fitness.append((((x2 + 13) * f + l, 21.5), ((x2 + 17) * f + l, 21.5)))
    lc = collections.LineCollection(se_legend_fitness, linewidth=2, color='black', clip_on=False)
    ax_2.add_collection(lc) 
    ax_2.text((x2 + 25) * f + l, 11.5, "Pahtogenicity", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    ax_2.text((x2 + 19) * f + l, 1.5, "0", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    ax_2.text((x2 + 19) * f + l, 11.5, "0.5", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    ax_2.text((x2 + 19) * f + l, 21.5, "1", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    
    ####***********************************************   
    # legend for the ordered genophenogram (left side)
    ####***********************************************       
#     x = -40    
#     ax_2.text((x - 5) * f, 12, "pos/neu/neg", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
#     left_legend_lines = []                        
#     x1 = x + 11
#     for i in range(6):                
#         y1 = i * (19 / 5) + 1.5
#         left_legend_lines.append(((x1 * f, y1), ((x1 + 3) * f, y1)))
#         if i % 2 == 0:
#             ax_2.text((x + 6) * f, y1, i * 0.2, fontsize=font_scale_factor*10, ha='center', weight='bold')
#     pass 
#     left_legend_lines.append((((x1 + 3) * f, 1.5), ((x1 + 3) * f, 20.5)))
#     lc = collections.LineCollection(left_legend_lines, linewidth=2, color='black', clip_on=False)
#     ax_2.add_collection(lc) 
    
    etime = time.time()   
    alm_fun.show_msg (cur_log,1,"ordered genophenogram running time was %g seconds" % (etime - stime)) 
    
    ####************************************************************************************************************************************************************* 
    # Main Landscape [ax_3]
    ####*************************************************************************************************************************************************************
    stime = time.time()
    ax_3 = plt.subplot(gs[5:, :])                                                 
    x = [1] * landscape_colorcode.shape[0] + list(range(1, landscape_colorcode.shape[1] + 1))
    y = list(range(1, landscape_colorcode.shape[0] + 1)) + [1] * (landscape_colorcode.shape[1])                        
    ax_3.plot(x, y, alpha=0)
    ax_3.xaxis.set_visible(True)
    ax_3.yaxis.set_visible(False)
    ax_3.patch.set_facecolor('white')    
    
    rectangle_patches = []
    for x_pos in landscape_colorcode.columns:
        for y_aa in landscape_colorcode.index:
            x = x_pos - from_pos +1 
            y = aa_plot.index(y_aa) + 1
            xy_color = landscape_colorcode.loc[y_aa, x_pos]
            rect = patches.Rectangle((x, y), 1, 1, linewidth=1, edgecolor=xy_color, facecolor=xy_color, fill=True, clip_on=False)
            rectangle_patches.append(rect)
    pass
    ax_3.add_collection(collections.PatchCollection(rectangle_patches, match_original=True))
    
    ####************************                     
    # Draw the standard error
    ####************************
    stime = time.time()
    se_lines = []
    for x_pos in landscape_se.columns:
        for y_aa in landscape_se.index:
            x = x_pos
            y = aa_plot.index(y_aa) + 1
            se = landscape_se.loc[y_aa, x_pos]
            if se !=0 : 
                se_lines.append(((x + (1 - se) / 2, y + (1 - se) / 2), (x + (1 + se) / 2, y + (1 + se) / 2)))  
    pass
    ax_3.add_collection(collections.LineCollection(se_lines, linewidth=1, color='black'))  
    
    ####*****************************************
    # legends for main landscape (AA , left side)   
    ####*****************************************
    x = -40   
    ax_3.text((x - 5) * f, 12, "AA residue", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold') 
    aa_legend_lines = []            
    x1 = x + 11
    for i in range(21):
        y1 = i + 1.5
        aa_legend_lines.append(((x1 * f, y1), ((x1 + 3) * f, y1)))  
        ax_3.text((x + 6) * f, y1, aa_plot[i], fontsize=font_scale_factor*10, va='center', weight='bold')
    pass 
    aa_legend_lines.append((((x1 + 3) * f, 1.5), ((x1 + 3) * f, 21.5)))
    
    aa_legend_lines.append((((x1 + 7) * f, 11.5), ((x1 + 9) * f, 11.5)))
    aa_legend_lines.append((((x1 + 7) * f, 13.5), ((x1 + 9) * f, 13.5)))
    aa_legend_lines.append((((x1 + 8) * f, 11.5), ((x1 + 8) * f, 13.5)))
    ax_3.text((x1 + 10) * f, 12.5, '+', fontsize=font_scale_factor*10, va='center', weight='bold')
    
    aa_legend_lines.append((((x1 + 7) * f, 9.5), ((x1 + 9) * f, 9.5)))
    aa_legend_lines.append((((x1 + 7) * f, 10.5), ((x1 + 9) * f, 10.5)))
    aa_legend_lines.append((((x1 + 8) * f, 9.5), ((x1 + 8) * f, 10.5)))
    ax_3.text((x1 + 10) * f, 10, '-', fontsize=font_scale_factor*10, va='center', weight='bold')
    
    aa_legend_lines.append((((x1 + 13) * f, 14.5), ((x1 + 15) * f, 14.5)))
    aa_legend_lines.append((((x1 + 13) * f, 21.5), ((x1 + 15) * f, 21.5)))
    aa_legend_lines.append((((x1 + 14) * f, 14.5), ((x1 + 14) * f, 21.5)))
    ax_3.text((x1 + 17) * f, 18, 'hydrophobic', rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    
    aa_legend_lines.append((((x1 + 13) * f, 5.5), ((x1 + 15) * f, 5.5)))
    aa_legend_lines.append((((x1 + 13) * f, 13.5), ((x1 + 15) * f, 13.5)))
    aa_legend_lines.append((((x1 + 14) * f, 5.5), ((x1 + 14) * f, 13.5)))
    ax_3.text((x1 + 17) * f, 9, 'polar', rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    
    lc = collections.LineCollection(aa_legend_lines, linewidth=2, color='black', clip_on=False)
    ax_3.add_collection(lc) 

    ####***************************************
    # legends for the standard error (right side)        
    ####***************************************    
    se_legend_lines = []
    x = 10
    ax_3.text(x * f + l, 12, "stderr", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    ax_3.text((x + 6) * f + l, 1.5, "0", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    ax_3.text((x + 6) * f + l, 11.5, "0.5", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    ax_3.text((x + 6) * f + l, 21.5, "1", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    
    x1 = 21
    for i in range(11):
        se = (i) / 10  
        y1 = i * 2 + 1.5
        se_legend_lines.append(((x1 * f + l, y1), ((x1 + 3) * f + l, y1)))  
        
        y = i * 2 + 1              
        se_legend_lines.append((((x1 + 7 + (1 - se) / 2) * f + l, y + (1 - se) / 2), ((x1 + 7 + (1 + se) / 2) * f + l, y + (1 + se) / 2)))
    pass 
    se_legend_lines.append((((x1 + 3) * f + l, 1.5), ((x1 + 3) * f + l, 21.5)))
    lc = collections.LineCollection(se_legend_lines, linewidth=2, color='black', clip_on=False)
    ax_3.add_collection(lc) 

   ####***************************************
    # legends for the score (right side)        
    ####***************************************  
    x2 = 33
    lst_colors_varity_new = [syn_color] + lst_max_colors_varity + lst_min_colors_varity    
    step = 20 / len(lst_colors_varity_new)
    for i in range(len(lst_colors_varity_new)):
        y2 = step * i + 1.5
        xy_color = lst_colors_varity_new[len(lst_colors_varity_new) - i - 1] 
        rect = patches.Rectangle((x2 * f + l, y2), 10 * f, step, linewidth=1, edgecolor=xy_color, facecolor=xy_color, fill=True, clip_on=False)
        ax_3.add_patch(rect)
    pass

    se_legend_fitness = []  
    se_legend_fitness.append((((x2 + 13) * f + l, 1.5), ((x2 + 13) * f + l, 21.5)))
    se_legend_fitness.append((((x2 + 13) * f + l, 1.5), ((x2 + 17) * f + l, 1.5)))
    se_legend_fitness.append((((x2 + 13) * f + l, (20 - step) / 2 + 1.5), ((x2 + 17) * f + l, (20 - step) / 2 + 1.5)))
    se_legend_fitness.append((((x2 + 13) * f + l, 21.5 - step), ((x2 + 17) * f + l, 21.5 - step)))
    se_legend_fitness.append((((x2 + 13) * f + l, 21.5), ((x2 + 17) * f + l, 21.5)))
    lc = collections.LineCollection(se_legend_fitness, linewidth=2, color='black', clip_on=False)
    ax_3.add_collection(lc) 
    ax_3.text((x2 + 25) * f + l, 11.5, "Pathogenicity", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    ax_3.text((x2 + 19) * f + l, 1.5, "0", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    ax_3.text((x2 + 19) * f + l, (20 - step) / 2 + 1.5, "0.5", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')
    ax_3.text((x2 + 19) * f + l, 21.5 - step, "1", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold')  
    ax_3.text((x2 + 19) * f + l, 21.5, "wt", rotation=90, fontsize=font_scale_factor*10, va='center', weight='bold') 

    ####***************************************
    # take care of the ticks of the main landscape
    ####***************************************  
    ax_3.set_ybound(1, 22)    
    ax_3.yaxis.set_ticks(np.arange(1.5, 22.5, 1))
    ax_3.yaxis.set_ticklabels(aa_plot)  

                            
    lst_xaxis = list(range(0,landscape_colorcode.shape[1]+1,10))
    lst_xaxis[0] = 1
        
    uniprot_seq_dict = np.load(humandb_path + 'uniprot/npy/uniprot_seq_dict.npy',allow_pickle=True).item()
    pvid_seq = uniprot_seq_dict[uniprot_id]
    lst_xaxis_lables = [str(from_pos-1+i) + '\n' + pvid_seq[from_pos-2+i] for i in lst_xaxis ]
    
    ax_3.set_xbound(1, landscape_colorcode.shape[1] + 1)  
    ax_3.xaxis.set_ticks(lst_xaxis)
    ax_3.xaxis.set_ticklabels(lst_xaxis_lables) 
    
    #automatically determine the tick label font size (20 labels fontsize: 10 , 100 labels fontsize:5)
    x_axis_label_fontsize = 10 - (5/80)*(len(lst_xaxis_lables)-20)        
    ax_3.tick_params(labelsize=font_scale_factor*x_axis_label_fontsize)

    for loc, spine in ax_3.spines.items():
        spine.set_linestyle('-')
        spine.set_linewidth(2.0)
        spine.set_color('black')
        spine.set_visible(False)
        if loc in ['bottom']:
            spine.set_position(('axes', -0.03))  # outward by 10 points
            spine.set_visible(True)
    pass        
    ax_3.tick_params(direction='out', length=6, width=2, colors='black', grid_color='b', grid_alpha=0.0)
    
#     if (to_pos - from_pos+1) > 100:
#         ax_3.xaxis.set_visible(False)
#         ax_3.yaxis.set_visible(False)
#         for loc, spine in ax_3.spines.items():
#             spine.set_visible(False)
#         pass
     
    etime = time.time()
    alm_fun.show_msg (cur_log,1,"main landscape running time was %g seconds" % (etime - stime))        
    alm_fun.show_msg (cur_log,1,"size:" + str(len(se_lines)))

    ####***************************************
    # save the map 
    ####***************************************                  
    plt.suptitle(plot_title, fontsize=font_scale_factor*30, y =0.9)
    str_time = str(datetime.now())
    str_time = str_time.replace(' ','')
    str_time = str_time.replace('-','')
    str_time = str_time.replace(':','')
    str_time = str_time.replace('.','')
    map_name = protein_name + '[' + uniprot_id + ']' + '_' + str(from_pos) + '-' + str(to_pos) + '_' +  score_name + '_' +  str_time
    plt.savefig(project_path + 'output/' + map_name + '.pdf')    
    alm_fun.show_msg (cur_log,1,map_name + '.pdf was saved.')
    plt.close()
    return (map_name)

def create_varity_output_file(uniprot_id,protein_name,score_name,from_pos,to_pos):
    ####*************************************************************************************************************
    # Load the varity  data for the uniprot_id 
    ####*************************************************************************************************************
    key_cols = ['p_vid','aa_pos','aa_ref','aa_alt']
    feature_cols = ['provean_score','sift_score','evm_epistatic_score','integrated_fitCons_score','LRT_score','GERP_RS',
                        'phyloP30way_mammalian','phastCons30way_mammalian','SiPhy_29way_logOdds','blosum100','in_domain','asa_mean','aa_psipred_E',
                        'aa_psipred_H','aa_psipred_C','bsa_max','h_bond_max','salt_bridge_max','disulfide_bond_max','covelent_bond_max','solv_ne_abs_max',
                        'mw_delta','pka_delta','pkb_delta','pi_delta','hi_delta','pbr_delta','avbr_delta','vadw_delta','asa_delta','cyclic_delta','charge_delta',
                        'positive_delta','negative_delta','hydrophobic_delta','polar_delta','ionizable_delta','aromatic_delta','aliphatic_delta','hbond_delta',
                        'sulfur_delta','essential_delta','size_delta']
    score_cols = ['VARITY_R','VARITY_R_LOO','VARITY_ER','VARITY_ER_LOO']
    
    output_cols = key_cols + score_cols + feature_cols
    
    protein_file = humandb_path + 'varity/bygene/'+ uniprot_id + '_' + protein_name + '_varity_web.txt'
    if os.path.isfile(protein_file):                                            
        varity_protein_df = pd.read_csv(protein_file,sep = '\t')                                              
        varity_protein_df = varity_protein_df.loc[(varity_protein_df['aa_pos'] >= from_pos) & (varity_protein_df['aa_pos'] <= to_pos)  & (varity_protein_df['p_vid'] == uniprot_id),:]
        str_time = str(datetime.now())
        str_time = str_time.replace(' ','')
        str_time = str_time.replace('-','')
        str_time = str_time.replace(':','')
        str_time = str_time.replace('.','')
        output_filename = protein_name + '[' + uniprot_id + ']' + '_' + str(from_pos) + '-' + str(to_pos) + '_' +  score_name + '_' +  str_time
        varity_protein_df[output_cols].to_csv(project_path + 'output/' + output_filename + '.csv',index = False)     
        return(output_filename)   
    else:
        return(-1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    