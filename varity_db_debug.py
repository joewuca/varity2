import sys
import alm_humandb

sys_argv = {}
sys_argv['python_path']  = '/Users/joewu/Dropbox/projects/varity/python'
sys_argv['project_path']  = '/Users/joewu/Dropbox/projects/humandb/'
sys_argv['varity_project_path']  = '/Users/joewu/Dropbox/projects/varity/'
sys_argv['db_path']  = '/Users/joewu/Dropbox/database/humandb_new/'
# sys_argv['db_action']  = 'create_accsum_data'
sys_argv['db_action']  = 'create_sherloc_training_data'
sys_argv['db_action']  = 'create_sherloc_data'
# sys_argv['db_action']  = 'process_sherloc_test_results'
sys_argv['db_action']  = 'assemble_final_sherloc_results'


sys_argv['db_action']  = 'create_eve_data'



# sys_argv['db_action'] = 'debug'
# sys_argv['session_id']  = 'Revision1230_1'
sys_argv['varity_session_id']  = 'Revision1230_1'

sys_argv['run_on_node'] = 0
sys_argv['parallel_id']  = 1
sys_argv['parallel_num']  = 1
sys_argv['single_id'] = ''
sys_argv['single_id_chr'] = ''
sys_argv['assembly'] = 'GRCh37'
sys_argv['uniprot_id'] = 'P01130'
sys_argv['uniprot_ids'] = ['P01009']
sys_argv['pdb_ids'] = ['6ah0','4nho','3jcr']
sys_argv['target_data_type'] = 'uniprot_ids'
sys_argv['target_data_name'] = 'B_TEST'
sys_argv['varity_batch_id'] = 'test'
sys_argv['pisa_folder'] = 'pisa3'


#***************************************************************************************************************************************************************
# Run db commnad  
#***************************************************************************************************************************************************************
db_obj = alm_humandb.alm_humandb(sys_argv)
db_obj.humandb_action(db_obj.runtime)
