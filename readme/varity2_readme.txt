
VARITY2 Readme

**********************************************************************************
Project setup
**********************************************************************************
1) Run "git clone https://github.com/joewuca/varity2.git" under YPF (Your Project Folder), this will create a folder called "varity2" that contains all VARITY2 script, readme, and config files.
2) Download VARITY2_startfolders.zip from (), and unzip under YPF, this will create "varity2_project" (results output folder) and "varity2_data" (data input folder)


**********************************************************************************
Environment setup
**********************************************************************************
1) Install Conda with python3.9 (https://docs.conda.io/en/latest/miniconda.html) 
2) Create Conda environment for VARITY2 ( using YPF/varity2/varity2.yaml)


**********************************************************************************
Run VARITY2 commands
**********************************************************************************

1) init_session -- Initialize the session 'VARITY2' based on the config file named VARITY2.vsc

python3 /home/rothlab/jwu/projects/varity2/varity_run.py action=init_session session_id=VARITY2 mem=20480 run_on_node=0 cluster=0 project_path=/home/rothlab/jwu/projects/varity2_project/ config_path=/home/rothlab/jwu/projects/varity2/config/ db_path=/home/rothlab/jwu/projects/varity2_project/ db_path=/home/rothlab/jwu/projects/varity2_database/humandb_new/

2) hp_tuning -- Tune the hyper-parameters in the nested CV setting for VARITY2_R_CV

python3 /home/rothlab/jwu/projects/varity2/varity_run.py action=hp_tuning session_id=VARITY2 predictor=VARITY2_R_CV cur_test_fold=0 mem=20480 run_on_node=0 cluster=0 project_path=/home/rothlab/jwu/projects/varity2_project/ config_path=/home/rothlab/jwu/projects/varity2/config/ db_path=/home/rothlab/jwu/projects/varity2_project/ db_path=/home/rothlab/jwu/projects/varity2_database/humandb_new/
python3 /home/rothlab/jwu/projects/varity2/varity_run.py action=hp_tuning session_id=VARITY2 predictor=VARITY2_R_CV cur_test_fold=1 mem=20480 run_on_node=0 cluster=0 project_path=/home/rothlab/jwu/projects/varity2_project/ config_path=/home/rothlab/jwu/projects/varity2/config/ db_path=/home/rothlab/jwu/projects/varity2_project/ db_path=/home/rothlab/jwu/projects/varity2_database/humandb_new/
python3 /home/rothlab/jwu/projects/varity2/varity_run.py action=hp_tuning session_id=VARITY2 predictor=VARITY2_R_CV cur_test_fold=2 mem=20480 run_on_node=0 cluster=0 project_path=/home/rothlab/jwu/projects/varity2_project/ config_path=/home/rothlab/jwu/projects/varity2/config/ db_path=/home/rothlab/jwu/projects/varity2_project/ db_path=/home/rothlab/jwu/projects/varity2_database/humandb_new/
python3 /home/rothlab/jwu/projects/varity2/varity_run.py action=hp_tuning session_id=VARITY2 predictor=VARITY2_R_CV cur_test_fold=3 mem=20480 run_on_node=0 cluster=0 project_path=/home/rothlab/jwu/projects/varity2_project/ config_path=/home/rothlab/jwu/projects/varity2/config/ db_path=/home/rothlab/jwu/projects/varity2_project/ db_path=/home/rothlab/jwu/projects/varity2_database/humandb_new/
python3 /home/rothlab/jwu/projects/varity2/varity_run.py action=hp_tuning session_id=VARITY2 predictor=VARITY2_R_CV cur_test_fold=4 mem=20480 run_on_node=0 cluster=0 project_path=/home/rothlab/jwu/projects/varity2_project/ config_path=/home/rothlab/jwu/projects/varity2/config/ db_path=/home/rothlab/jwu/projects/varity2_project/ db_path=/home/rothlab/jwu/projects/varity2_database/humandb_new/
python3 /home/rothlab/jwu/projects/varity2/varity_run.py action=hp_tuning session_id=VARITY2 predictor=VARITY2_R_CV cur_test_fold=5 mem=20480 run_on_node=0 cluster=0 project_path=/home/rothlab/jwu/projects/varity2_project/ config_path=/home/rothlab/jwu/projects/varity2/config/ db_path=/home/rothlab/jwu/projects/varity2_project/ db_path=/home/rothlab/jwu/projects/varity2_database/humandb_new/
python3 /home/rothlab/jwu/projects/varity2/varity_run.py action=hp_tuning session_id=VARITY2 predictor=VARITY2_R_CV cur_test_fold=6 mem=20480 run_on_node=0 cluster=0 project_path=/home/rothlab/jwu/projects/varity2_project/ config_path=/home/rothlab/jwu/projects/varity2/config/ db_path=/home/rothlab/jwu/projects/varity2_project/ db_path=/home/rothlab/jwu/projects/varity2_database/humandb_new/
python3 /home/rothlab/jwu/projects/varity2/varity_run.py action=hp_tuning session_id=VARITY2 predictor=VARITY2_R_CV cur_test_fold=7 mem=20480 run_on_node=0 cluster=0 project_path=/home/rothlab/jwu/projects/varity2_project/ config_path=/home/rothlab/jwu/projects/varity2/config/ db_path=/home/rothlab/jwu/projects/varity2_project/ db_path=/home/rothlab/jwu/projects/varity2_database/humandb_new/
python3 /home/rothlab/jwu/projects/varity2/varity_run.py action=hp_tuning session_id=VARITY2 predictor=VARITY2_R_CV cur_test_fold=8 mem=20480 run_on_node=0 cluster=0 project_path=/home/rothlab/jwu/projects/varity2_project/ config_path=/home/rothlab/jwu/projects/varity2/config/ db_path=/home/rothlab/jwu/projects/varity2_project/ db_path=/home/rothlab/jwu/projects/varity2_database/humandb_new/
python3 /home/rothlab/jwu/projects/varity2/varity_run.py action=hp_tuning session_id=VARITY2 predictor=VARITY2_R_CV cur_test_fold=9 mem=20480 run_on_node=0 cluster=0 project_path=/home/rothlab/jwu/projects/varity2_project/ config_path=/home/rothlab/jwu/projects/varity2/config/ db_path=/home/rothlab/jwu/projects/varity2_project/ db_path=/home/rothlab/jwu/projects/varity2_database/humandb_new/

3) test_cv_prediction -- Run prediction on the nested CV using VARITY2_R_CV and other predictors

python3 /home/rothlab/jwu/projects/varity2/varity_run.py action=test_cv_prediction session_id=VARITY2 predictors=[VARITY2_R_CV,SIFT_R_CV,Polyphen2_HDIV_R_CV,Polyphen2_HVAR_R_CV,PROVEAN_R_CV] mem=20480 run_on_node=0 cluster=0 project_path=/home/rothlab/jwu/projects/varity2_project/ config_path=/home/rothlab/jwu/projects/varity2/config/ db_path=/home/rothlab/jwu/projects/varity2_project/ db_path=/home/rothlab/jwu/projects/varity2_database/humandb_new/

4) plot_test_result -- Plot the nested CV performance comparison figure 

python3 /home/rothlab/jwu/projects/varity2/varity_run.py action=plot_test_result session_id=VARITY2 plot_test_with_saved_data=0 plot_show_size=0 t_value=1.833113 filter_test_score=0 cur_test_fold=-1 size_factor=1.13 table_scale_factor=2.83 predictor=VARITY2_R_CV compare_predictors=[VARITY2_R_CV,SIFT_R_CV,Polyphen2_HDIV_R_CV,Polyphen2_HVAR_R_CV,PROVEAN_R_CV] no_plot_predictors=[] nucleotide_predictors=[] compare_to_predictor=VARITY2_R_CV mem=20480 run_on_node=0 cluster=0 project_path=/home/rothlab/jwu/projects/varity2_project/ config_path=/home/rothlab/jwu/projects/varity2/config/ db_path=/home/rothlab/jwu/projects/varity2_project/ db_path=/home/rothlab/jwu/projects/varity2_database/humandb_new/


[common commands used on cluster]
scp jwu@galenus.mshri.on.ca:/home/rothlab/jwu/projects/varity2_project/output/img/*.* ./
squeue -o "%.10i %.100j %.8u %.8T %.10M %.9l %.6D %R %m %C" -u jwu --sort=+i
sinfo -N -o "%10N %a %25E %15C %10m %10e"