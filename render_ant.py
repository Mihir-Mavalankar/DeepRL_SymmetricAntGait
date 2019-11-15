import os
import inspect
import pybullet
import gym
import numpy as np
import pybullet_envs
from importlib import import_module
import time
import tensorflow as tf
from argparse import Namespace
from baselines.ppo2.ppo2 import learn
from baselines.common.vec_env import VecFrameStack, VecNormalize, VecEnv
from baselines.common.vec_env.vec_video_recorder import VecVideoRecorder
from baselines.common.cmd_util import common_arg_parser, parse_unknown_args, make_vec_env, make_env
from baselines.common.tf_util import get_session


def get_learn_function_defaults(alg, env_type):
    try:
        alg_defaults = import_module('baselines.ppo2.defaults')
        kwargs = getattr(alg_defaults, env_type)()
    except (ImportError, AttributeError):
        kwargs = {}
    return kwargs


def build_env(alg,seed,nenv):

    env_type="gym_locomotion_envs"
    env_id="AntBulletEnv-v0"

    if env_type in {'atari', 'retro'}:
        if alg == 'deepq':
            env = make_env(env_id, env_type, seed=seed, wrapper_kwargs={'frame_stack': True})
        elif alg == 'trpo_mpi':
            env = make_env(env_id, env_type, seed=seed)
        else:
            frame_stack_size = 4
            env = make_vec_env(env_id, env_type, nenv, seed, gamestate=None, reward_scale=1.0)
            env = VecFrameStack(env, frame_stack_size)

    else:
        config = tf.ConfigProto(allow_soft_placement=True,
                               intra_op_parallelism_threads=1,
                               inter_op_parallelism_threads=1)
        config.gpu_options.allow_growth = True
        get_session(config=config)

        flatten_dict_observations = alg not in {'her'}
        env = make_vec_env(env_id, env_type,1, seed, reward_scale=1.0, flatten_dict_observations=flatten_dict_observations)

        if env_type == 'mujoco':
            env = VecNormalize(env, use_tf=True)

    return env

def main():

  network='mlp'
  pybullet.connect(pybullet.DIRECT)

  env = build_env('ppo2',None,1)
  print("Running pre-trained model")
  env.render(mode='human')
  obs = env.reset()

  alg_kwargs = get_learn_function_defaults('ppo2', 'gym_locomotion_envs')
  alg_kwargs['network'] = network

  model = learn(
      env=env,
      seed=None,
      total_timesteps=0,
      load_path='./models_bullet/antbullet_vanilla_ppo2_6e7',
      **alg_kwargs
  )

  state = model.initial_state if hasattr(model, 'initial_state') else None
  dones = np.zeros((1,))

  episode_rew = np.zeros(env.num_envs) if isinstance(env, VecEnv) else np.zeros(1)

  while True:
      time.sleep(1./60.)
      # a = datetime.datetime.now()
      if state is not None:
          actions, _, state, _ = model.step(obs,S=state, M=dones)
      else:
          actions, _, _, _ = model.step(obs)

      obs, rew, done, _ = env.step(actions)
      episode_rew += rew

      env.render()

      done = done.any() if isinstance(done, np.ndarray) else done
      if done:
          print('episode_rew={}'.format(episode_rew))
          episode_rew = 0
          obs = env.reset()

  env.close()


if __name__ == "__main__":
  main()
