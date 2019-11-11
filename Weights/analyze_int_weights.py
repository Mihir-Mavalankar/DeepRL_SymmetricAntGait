import numpy as np
from os import listdir
from os.path import isfile, join

mypath='./'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles[0])
print(onlyfiles[-1])

p1=[]
p2=[]

param_list = np.load('./Ant_ppo2_weights_1.npy',allow_pickle=True)

for p in param_list[:-1]:
    #print(p[0])
    p1.append(p)

param_list = np.load('./Ant_ppo2_weights_40.npy',allow_pickle=True)

for p in param_list[:-1]:
    #print(p[0])
    p2.append(p)

for i in range(len(p1)):
    print(p1[i]-p2[i])
    print('------------------------')
