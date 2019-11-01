num_tm=2e4
algo=ppo2
svpath=./models_bullet/antbullet_vanilla_$algo\_$num_tm

#Vanilla PPO for Ant
python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=$num_tm --save_path=$svpath --log_path=./logs/BulletAnt_vanilla/
#python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=0 --load_path=$svpath --play
