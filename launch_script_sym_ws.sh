num_tm=6e7
algo=ppo2
svpath=./models_bullet/antbullet_sym_ws_$algo\_$num_tm

#Model with symmetric weights
python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=$num_tm --network=mlp_sym_ws --save_path=$svpath --log_path=./logs/BulletAnt_mlp_sym_ws/
#python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=0 --network=mlp_sym_ws --load_path=$svpath --play
