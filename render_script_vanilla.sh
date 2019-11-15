num_tm=1e5
algo=ppo2
svpath=./models_bullet/antbullet_vanilla_$algo\_$num_tm

python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=0 --load_path=$svpath --play
