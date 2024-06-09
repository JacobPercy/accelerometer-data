import pandas as pd

filename_1 = "accel_1.csv"
filename_2 = "gyro_1.csv"
df_1 = pd.read_csv(filename_1, delimiter=";")

data_1 = df_1[['AccelerationX', 'AccelerationY', 'AccelerationZ']].values



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

for val in data_1:
    x,y,z = val[0]+x_off,val[1]+y_off,val[2]+z_off

    

    p1.update(x,y,z)
    p1.locate()