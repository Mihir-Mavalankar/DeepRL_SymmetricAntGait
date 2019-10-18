import gym
from collections import defaultdict
import numpy as np


def weight_diff(param_list):
    #Unit test to check matrix dimensions are even##########
    for p in param_list[:-1]:
        #print(p.shape)
        if(p.shape[0]%2!=0):
            print("Error: [Unit Test failed] - Matrix dimensions are not even and so the network is not symmetrical!")
            return
    #######################################################

    for p in param_list[:-1]:

        if(len(p.shape)==1):      #reshape if it's a 1D bias vector
            p = p.reshape((1,p.shape[0]))

        half_col = int(p.shape[1]/2)
        diff = np.asarray(p[:,:half_col] - np.flip(p[:,half_col:],axis=1))

        if(diff.shape[1]!=1):
            diff = np.sum(diff, axis = 0).reshape(1,diff.shape[1])

        #Save this to a text file
        #print(p.shape,diff.shape)
