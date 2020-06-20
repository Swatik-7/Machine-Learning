import random
from itertools import count
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt

x_vals=[]
y_vals=[]
index=count()
def animate(i):
	x_vals.append(next(index))
	y_vals.append(random.randint(0,5))
	plt.cla()
	plt.plot(x_vals,y_vals)
    

#passing (fig, function, interval of repetition in ms)
an=FuncAnimation(plt.gcf(),animate, interval=1000)  
plt.tight_layout()
plt.show()

