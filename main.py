import pandas as pd

filename = "data.csv"
df = pd.read_csv(filename)

data = df.iloc[:, [3, 4, 5]].values

print(data)

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

p1 = Point(0,0,0)
p1.locate()