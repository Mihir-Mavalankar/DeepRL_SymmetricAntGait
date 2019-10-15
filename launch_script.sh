num_tm=2e4
algo=ppo2
#Roboschool####################
#Model without symmetric weights
#python -m baselines.run --alg=$algo --env=RoboschoolAnt-v1 --num_timesteps=$num_tm  --nsteps=4096 --noptepochs=15 --save_path=./models/ant_$algo$num_tm
#python -m baselines.run --alg=ppo2 --env=RoboschoolAnt-v1 --num_timesteps=0  -load_path=./models/ant_$algo\_$num_tm --play

#Model with symmetric weights
#python -m baselines.run --alg=$algo --env=RoboschoolAnt-v1 --num_timesteps=$num_tm  --nsteps=4096 --noptepochs=15 --network=mlp_ws --save_path=./models/ant_mplws_$algo$num_tm
#python -m baselines.run --alg=$algo --env=RoboschoolAnt-v1 --num_timesteps=0 --network=mlp_ws --load_path=./models/ant_mplws_$algo$num_tm --play

#PyBullet######################
#Model without symmetric weights
# python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=$num_tm  --nsteps=4096 --noptepochs=15 --save_path=./models_bullet/antbullet_$algo$num_tm --log_path=./logs/BulletAnt_mlp/
# python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=0 --load_path=./models_bullet/antbullet_mplws_$algo$num_tm --play


#Model with symmetric weights
python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=$num_tm  --nsteps=4096 --noptepochs=15 --network=mlp_ws --save_path=./models_bullet/antbullet_mplws_$algo$num_tm --log_path=./logs/BulletAnt_mlpws/
python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=0 --network=mlp_ws --load_path=./models_bullet/antbullet_mplws_$algo$num_tm --play
