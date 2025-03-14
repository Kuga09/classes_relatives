import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


class Circles:

    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r

    def draw_circle(self):
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
circle_1.draw_circle()

data_second=input("Введите новые координаты центра и радиус окружности: ")
data_second=data_second.split()
x=float(data_second[0])
y=float(data_second[1])
r=float(data_second[2])

circle_1.info()

class Sphere(Circles):

    def __init__(self,x,y,z,r):
        super().__init__(x,y,r)
        self.z=z
    
    def draw_sphere(self):

        u = np.linspace(0, 2 * np.pi, 100) 
        v = np.linspace(0, np.pi, 100)     
        X = self.x + self.r * np.outer(np.cos(u), np.sin(v))  
        Y = self.y + self.r * np.outer(np.sin(u), np.sin(v))  
        Z = self.z + self.r * np.outer(np.ones(np.size(u)), np.cos(v))  

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, color='b', alpha=0.6)  

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Sphere')

        plt.show()  

z=float(input('Введите координату центра сферы по оси Z: '))

Sphere_1=Sphere(x,r,z,r)

Sphere_1.draw_sphere()