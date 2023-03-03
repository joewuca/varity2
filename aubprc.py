import numpy as np
import matplotlib.pyplot as plt




project_path = '/Users/joewu/Dropbox/projects/varity/'

def fun_byo_precision(bp,prior):
    byo_p = (bp*prior)/(1-bp+prior*(2*bp-1))

    return (byo_p)




# Given balanced precision, how precision changes with respect to prior
bp = 0.8
priors = []
byo_precisions = []

for i in range(1,10001):
    prior = i/10000
    priors.append(prior)
    byo_precisions.append(fun_byo_precision(bp,prior))
    # print ('prior:' + str(prior))
    # print (fun_byo_precision(bp,prior))  
    
    
  
fig = plt.figure(figsize=(10, 10))
plt.clf()
plt.rcParams["font.family"] = "Helvetica"    
ax = plt.subplot()      
for bp in [0.8,0.9,0.95,0.98,0.985]:
# for bp in [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.91,0.92,0.93,0.94,0.95,0.98,0.99]:
# for bp in [0.5,0.8]:
    # bp = i/10000
    priors = []
    byo_precisions1 = []
    byo_precisions2 = []
    byo_precisions_diff = []
        
    for j in range(1,20001):
        prior = j/20000
        priors.append(prior)
        byo_precisions1.append(fun_byo_precision(bp,prior))
        byo_precisions2.append(fun_byo_precision(bp+0.01,prior))
        byo_precisions_diff.append(fun_byo_precision(bp+0.01,prior) - fun_byo_precision(bp,prior))
                                
    # ax.scatter(priors,byo_precisions1 ,s = 5)
    ax.scatter(priors,byo_precisions_diff ,s = 5)
    
    
# ax.set_title('Balanced Precision: ' + str(bp) ,size = 25,pad = 10)
ax.set_xlabel('Prior', size=35,labelpad = 10)
ax.set_xticks(np.arange(0, 1.1, 0.1))
ax.set_ylabel('Precision difference', size=35,labelpad = 10)
ax.tick_params(labelsize=25) 
# ax.set_xticklabels(scores,rotation = 70)
fig.tight_layout()
# fig.savefig(project_path + 'output/img/precisions_versus_prior_BP_' + str(bp) + '.png')
# fig.savefig(project_path + 'output/img/precisions_versus_prior.png')

# fig.savefig(project_path + 'output/img/BYO_precisions_with_different_BP_' + str(bp) + '.png')
fig.savefig(project_path + 'output/img/precision_vs_prior_with_different_bps.png')
# fig.savefig(project_path + 'output/img/precision_vs_prior_with_bps.png')  
#                    