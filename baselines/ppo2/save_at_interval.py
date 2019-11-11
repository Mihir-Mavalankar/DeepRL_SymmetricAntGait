import tensorflow as tf
import numpy as np

def save_weights(model,epoch):
    init = tf.global_variables_initializer()
    param_list = []
    with tf.Session() as sess:
        sess.run(init)
        layers = sess.run(model.var)
        i=0
        for l in layers:
            if('pi' in model.var[i].name):
                param_list.append(l)
            i+=1

    np.save('../../Weights/Ant_ppo2_weights_'+str(epoch), np.asarray(param_list)) #save weights as numpy array
