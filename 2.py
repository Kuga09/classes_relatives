import matplotlib.pyplot as plt


class Circles:

    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r

    def draw(self):
        fig, self.ax = plt.subplots()

        # Создание осей координат в центре
        self.ax = plt.gca() 
        self.ax.spines['left'].set_position('center')
        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

        circle1=plt.Circle((self.x, self.y), self.r, color='r', fill=False)
        self.ax=plt.gca()
        self.ax.add_patch(circle1)
        plt.axis('scaled')
        plt.show()

    def info(self):
        print(f"Координаты центра и радиус окружности соответственно равны: {x}, {y}, {r}")

    def __del__(self):
        pass

data_first=input("Введите координаты центра и радиус окружности: ")
data_first=data_first.split()
x=float(data_first[0])
y=float(data_first[1])
r=float(data_first[2])

circle_1=Circles(x,y,r)
circle_1.draw()

data_second=input("Введите новые координаты центра и радиус окружности: ")
data_second=data_second.split()
x=float(data_second[0])
y=float(data_second[1])
r=float(data_second[2])

circle_1.info()

