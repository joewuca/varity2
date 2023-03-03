import numpy as np


db_path = '/Users/joewu/Dropbox/database/humandb_new/pepnn/'


x = np.load(db_path + 'all_data/fragment_data/5ZZ9_A_E.npz')
y = np.load(db_path + 'all_data/receptor_data/5ZZ9_A.npz')
print(x.files)
print(y.files)

y['neighbor_indices']
y['nodes']
y['edges']

x['target_sequence']
x['binding_sites']

print ('OK')