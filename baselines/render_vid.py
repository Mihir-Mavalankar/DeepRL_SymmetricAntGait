
import os
import inspect
import pybullet
import gym
import numpy as np
import pybullet_envs
import time
from baselines.ppo2.model import Model
model_fn = Model

def main():
      pybullet.connect(pybullet.DIRECT)
      env = gym.make("AntBulletEnv-v0")
      env.render(mode="human")
      nenvs = env.num_envs 

      ob_space = env.observation_space
      ac_space = env.action_space

      # Calculate the batch_size
      nbatch = nenvs * nsteps
      nbatch_train = nbatch // nminibatches
      ent_coef=0.0
      lr=3e-4
      vf_coef=0.5
      max_grad_norm=0.5
      model = model_fn(policy=policy, ob_space=ob_space, ac_space=ac_space, nbatch_act=nenvs, nbatch_train=nbatch_train,
                      nsteps=nsteps, ent_coef=ent_coef, vf_coef=vf_coef,
                      max_grad_norm=max_grad_norm, comm=comm, mpi_rank_weight=mpi_rank_weight)
      model.load('./models_bullet/antbullet_vanilla_ppo2_6e7')


      env.reset()

      while 1:
        frame = 0
        score = 0
        restart_delay = 0
        obs = env.reset()

        while 1:
          time.sleep(1. / 60.)
          a = pi.act(obs)
          obs, r, done, _ = env.step(a)
          #print("reward")
          #print(r)
          score += r
          frame += 1
          distance = 5
          yaw = 0

          still_open = env.render("human")
          if still_open == False:
            return
          if not done: continue
          if restart_delay == 0:
            print("score=%0.2f in %i frames" % (score, frame))
            restart_delay = 60 * 2  # 2 sec at 60 fps
          else:
            restart_delay -= 1
            if restart_delay == 0: break

if __name__ == "__main__":
  main()
