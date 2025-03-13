import matplotlib.pyplot as plt


class Parabola:

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def x(self):
        D=self.b**2-4*self.a*self.c
        x1=(-1*self.b+D**0.5)/2*self.a
        x2=(-1*self.b-D**0.5)/2*self.a
        return x1,x2

    def draw_parabola(self):
        x=list(range(-50,51))
        y=[]
        for i in x:
            y.append(self.a*(i**2)+self.b*i+self.c) 
        fig, ax = plt.subplots()
        
        #ax.set_title('График парабола',color='#173544', fontstyle="italic", fontweight="bold") 
        ax.set_xlabel('Ось X',color='#173554', fontweight="bold")
        ax.set_ylabel('Ось Y',color='#173554', fontweight="bold")
        ax.plot(x,y)
    
    def draw(self):
        plt.show()

    def __del__(self):
        pass


class Derivative(Parabola):

    def __init__(self,a, b,c):
        super().__init__(a, b,c)

    def draw_derivative(self):
        x=list(range(-50,51))
        y=[]
        for i in x:
            y.append(2*self.a*i+self.b) 
        fig, ax = plt.subplots()
        super().draw_parabola()
        #ax.set_title('График производной',color='#173544', fontstyle="italic", fontweight="bold") 
        ax.set_xlabel('Ось X',color='#173554', fontweight="bold")
        ax.set_ylabel('Ось Y',color='#173554', fontweight="bold")
        ax.plot(x,y)

    
    
    
    def __del__(self):
        pass



data=input("Введите коэффициенты квадратного уравнения: ")
data=data.split()
a=float(data[0])
b=float(data[1])
c=float(data[2])

f_1=Parabola(a,b,c)
x1,x2=f_1.x()

print(f'Корни квадратного уравнения равны: {x1},{x2}')

f_1=Derivative(a,b,c)

f_1.draw_derivative()
f_1.draw()

