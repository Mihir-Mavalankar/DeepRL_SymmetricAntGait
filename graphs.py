import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import csv

y=[]
x=[]
files=['./logs/BulletAnt_vanilla/progress_mlp_vanilla_6e7.csv','./logs/BulletAnt_mvdp_net/progress_mvdp_net_6e7.csv',
        './logs/BulletAnt_mlp_sym_ws/progress_mlp_sym_ws_6e7.csv']

i=0
for f in files:
    temp=[]
    c=True

    with open(f, 'r') as csvfile:
        plots= csv.reader(csvfile, delimiter=',')
        for row in plots:
            if(c):
                c=False
                continue

            if(i==0):
                x.append(int(row[12]))
            temp.append(float(row[1]))

    y.append(temp)
    i+=1

#for j in range(3):
print(len(y))
print(len(x),len(y[0]),len(y[1]),len(y[2]))
# temp_y2=[]
# for i in range(len(y[2])):
#     temp_y2.append(y[2][i])
#     temp_y2.append(y[2][i])
#
# print(len(temp_y2))

plt.plot(x,y[0],label="PPO_vanilla")
plt.plot(x,y[1],label="PPO_mvdp_net")
plt.plot(x,y[2],label="PPO_sym_ws")

plt.title('Results')
plt.xlabel('Timesteps')
plt.ylabel('Average reward over last 100 epsisodes')
plt.legend()
plt.savefig('Res.png')
plt.show()
