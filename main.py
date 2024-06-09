import pandas as pd

filename_1 = "accel_2.csv"
filename_2 = "gyro_2.csv"

df_1 = pd.read_csv(filename_1, delimiter=";")
df_2 = pd.read_csv(filename_2, delimiter=";")

data_1 = df_1[['AccelerationX', 'AccelerationY', 'AccelerationZ']].values
data_2 = df_2[['GyroscopeX', 'GyroscopeY', 'GyroscopeZ']].values


class Point():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def update(self,x,y,z):
        self.x += x
        self.y += y
        self.z += z

    def locate(self):
        print(self.x, self.y, self.z)

p1 = Point(0, 0, 0)

x=y=z=0.0 #Initialize starting values of vector

x_off,y_off,z_off = (-data_1[0][0], -data_1[0][1], -data_1[0][2]) #Values of offsets

data_1 = data_1[1:]
data_2 = data_2[1:]

for ac,gy in zip(data_1,data_2):
    x,y,z = ac[0]+x_off,ac[1]+y_off,ac[2]+z_off



    p1.update(x,y,z)
    p1.locate()