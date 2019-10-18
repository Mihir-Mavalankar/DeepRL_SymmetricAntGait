num_tm=3e4
algo=ppo2
svpath=./models_bullet/antbullet_$algo\_$num_tm
svpathws=./models_bullet/antbullet_mplws_$algo\_$num_tm
#PyBullet-Symmetric Input output######################
#Model without symmetric weights
#python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=$num_tm --network=mlp_sym --nsteps=4096 --noptepochs=15 --save_path=$svpath --log_path=./logs/BulletAnt_mlp/
#python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=0 --network=mlp_sym  --load_path=./models_bullet/antbullet_$algo$num_tm --play


#Model with symmetric weights
#python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=$num_tm --network=mlp_sym_ws --nsteps=4096 --noptepochs=15 --save_path=$svpathws --log_path=./logs/BulletAnt_mlpws/
python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=0 --network=mlp_sym_ws --load_path=./models_bullet/antbullet_mplws_$algo\_$num_tm --play
