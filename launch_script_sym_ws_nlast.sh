num_tm=6e7
algo=ppo2
svpath=./models_bullet/antbullet_sym_ws_nlast_$algo\_$num_tm

#Model with symmetric weights except last layer
python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=$num_tm --network=mlp_sym_ws_nlast --save_path=$svpath --log_path=./logs/BulletAnt_mlp_sym_ws_nlast/
#python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=0 --network=mlp_sym_ws_nlast --load_path=$svpath --play
