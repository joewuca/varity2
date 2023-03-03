from liftover import get_lifter
import pandas as pd
import numpy as np

#lift over
# varity_38_df =  pd.read_csv("../varity_all_predictions.txt",sep = '\t')
# varity_38_df.head(10).to_csv("../varity_all_predictions_test.txt",index = False)
# converter = get_lifter('hg19', 'hg38')
#
# def get_chr_38(chr_37,pos_37):
#
#     x = converter[chr_37][pos_37]
#     if len(x) != 0: 
#         return x[0][0]
#     else:
#         return np.nan
#
# def get_pos_38(chr_37,pos_37):
#
#     x = converter[chr_37][pos_37]
#     if len(x) != 0: 
#         return x[0][1]
#     else:
#         return np.nan
#
# varity_38_df['chr_38'] = varity_38_df.apply(lambda x: get_chr_38(x['chr'],x['nt_pos']),axis = 1)
# varity_38_df['nt_pos_38'] = varity_38_df.apply(lambda x: get_pos_38(x['chr'],x['nt_pos']),axis = 1)
#
# varity_38_df.to_csv("../varity_all_predictions_38.csv",index = False)

# # varity_38_df = 
# chrom = '1'
# pos = 103786442
#
#
# x = converter[chrom][pos][0][0]
# y = converter[chrom][pos][0][1]



varity_38_df =  pd.read_csv("../varity_all_predictions_38.csv")
varity_38_df.loc[varity_38_df['nt_pos_38'].isnull(),'nt_pos_38'] = -1
varity_38_df['nt_pos_38'] = varity_38_df['nt_pos_38'].astype(int)
varity_38_df.to_csv("../varity_all_predictions_new_38.csv",index = False)

print("OK")