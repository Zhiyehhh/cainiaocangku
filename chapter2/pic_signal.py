import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-5,5,1000)

# gate signal
def g(x):
    return np.piecewise(x,
                        [x<(-0.5),x==(-0.5),(x>(-0.5)) & (x<0.5),x==0.5,x>0.5],
                        [0,0.5,1,0.5,0])

# sinc signal
def sinc(x):
    return np.piecewise(x,
                        [x != 0,x==0],
                        [lambda x:np.sin(np.pi*x)/(np.pi*x),0])

# sgn signal
def sgn(x):
    return np.piecewise(x,
                        [x<0,x==0,x>0],
                        [-1,0,1])

# Lambda signal
def Lambda(x):
    return np.piecewise(x,
                        [x<-1,(x>=-1)&(x<0),(x>=0) & (x<1),x>=1],
                        [0,lambda x:x+1,lambda x:-x+1,0])

# u_(-1) signal
def u(x):
    return np.piecewise(x,
                        [x<0,x==0,x>0],
                        [0,0.5,1])

functions = {
    'g(x)': g,
    'sinc(x)': sinc,
    'sgn(x)': sgn,
    'Lambda(x)': Lambda,
    'u(x)': u
}

for name,func in functions.items():
    y=func(x)
    plt.figure()
    plt.plot(x,y)
    plt.title(f'y={name}')
    plt.grid(True)
    filename=f'{name}.png'
    plt.savefig(filename,dpi=150)
