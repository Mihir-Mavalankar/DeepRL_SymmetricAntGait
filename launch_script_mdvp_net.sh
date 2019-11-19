num_tm=1e5
algo=ppo2
svpath=./models_bullet/antbullet_mvdp_net_$algo\_$num_tm

#MDVP NET for Ant
python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=$num_tm --network=mvdp_net --save_path=$svpath --log_path=./logs/BulletAnt_mvdp_net/
#python -m baselines.run --alg=$algo --env=AntBulletEnv-v0 --num_timesteps=0 --network=mvdp_net --load_path=$svpath --play
