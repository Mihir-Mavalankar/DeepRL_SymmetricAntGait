import numpy as np
from os import listdir
from os.path import isfile, join

network="mlp"
time="2e5"

param_list = np.load('./Ant_ppo2_'+str(network)+'_weights_'+str(time)+'.npy',allow_pickle=True)

for p in param_list[:-1]:
    print(p[0])
    print(p.shape)
    #p1.append(p)
