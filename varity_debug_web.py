#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys
import numpy as np
import pandas as pd
import random
import codecs
import os
import re
import datetime
import time
import warnings
import pickle
import glob
from scipy import stats
from sklearn import preprocessing
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt 
python_path = '/usr/local/projects/ml/python/'
project_path = '/usr/local/projects/manuscript/funregressor/gwt/www/'
humandb_path = '/usr/local/database/humandb_new/'
sys.path.append(python_path)

import funregressor_web 


#***************************************************************************************************************************************************************
# debug for the web application 
#***************************************************************************************************************************************************************
dict_arg = pickle.load(open(project_path + "output/CALM1_3.pickle", "rb"))
JSON_Return = funregressor_web.run_varity(1,dict_arg) 
print (JSON_Return)   

