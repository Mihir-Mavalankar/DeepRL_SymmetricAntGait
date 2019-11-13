import gym
import numpy as np
import pybullet
import pybullet_envs
import time
import gym.envs

env = gym.make('AntBulletEnv-v0')
env.render(mode='human')
done = False
state = env.reset()
for step in range(5000):
    time.sleep(1. / 60.)
    if done:
        state = env.reset()
    action = env.action_space.sample()
    #print(state.shape)
    state, reward, done, info = env.step(action)
    #print(info)
    env.render(mode='human')
