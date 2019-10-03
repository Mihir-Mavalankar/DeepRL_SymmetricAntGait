num_tm=1e5
algo=ppo2
#python -m baselines.run --alg=$algo --env=RoboschoolAnt-v1 --num_timesteps=$num_tm --save_path=./models/ant_$algo$num_tm
python -m baselines.run --alg=ppo2 --env=RoboschoolAnt-v1 --num_timesteps=0 --load_path=./models/ant_$algo$num_tm --play
