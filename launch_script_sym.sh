num_tm=1e5
algo=ppo2
svpath=./models_bullet/antbullet_sym_$algo\_$num_tm

#PyBullet-Symmetric Input output######################
python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=$num_tm --network=mlp_sym --save_path=$svpath --log_path=./logs/BulletAnt_mlp_sym/
#python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=0 --network=mlp_sym  --load_path=$svpath --play
