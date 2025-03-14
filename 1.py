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
        
        fig, self.ax = plt.subplots()
        
        # Создание осей координат в центре
        self.ax = plt.gca() 
        self.ax.spines['left'].set_position('center')
        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

        self.ax.set_title('График параболы',color='#173544', fontstyle="italic", fontweight="bold") 
        self.ax.plot(x,y)

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
    
        super().draw_parabola()
        self.ax.set_title('График производной',color='#173544', fontstyle="italic", fontweight="bold") 
        self.ax.plot(x,y)

    def draw_1(self):
        self.ax.set_title('График параболы и её производной',color='#173544', fontstyle="italic", fontweight="bold")
        self.ax.grid(True)
        plt.show()

    def __del__(self):
        pass

class Integral(Parabola):

    def __init__(self,a, b,c,d):
        self.d=d
        super().__init__(a, b,c)
    
    def draw_integral(self):
        x=list(range(-50,51))
        y=[]
        for i in x:
            y.append((1/3)*self.a*i**3+0.5*self.b*i**2+self.c*i+self.d) 
    
        super().draw_parabola()
        self.ax.set_title('График интеграла',color='#173544', fontstyle="italic", fontweight="bold") 
        self.ax.plot(x,y)
    
    def draw_2(self):
        self.ax.set_title('График параболы и её интеграла',color='#173544', fontstyle="italic", fontweight="bold")
        self.ax.grid(True)
        plt.show()

    def __del__(self):
        pass


data=input("Введите коэффициенты квадратного уравнения: ")
data=data.split()
a=float(data[0])
b=float(data[1])
c=float(data[2])

d=float(input('Введиде коэффициент "d" для расчета интеграла: '))

f_1=Parabola(a,b,c)
x1,x2=f_1.x()

print(f'Корни квадратного уравнения равны: {x1},{x2}')

f_1=Derivative(a,b,c)
f_1.draw_derivative()
f_1.draw_1()

f_1=Integral(a,b,c,d)
f_1.draw_integral()
f_1.draw_2()

