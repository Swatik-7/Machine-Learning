import random
from itertools import count
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
import pandas as pd

x_vals=[]
y_vals=[]
index=count()
def animate(i):
	df=pd.read_csv('data4.csv')
	x=df['x_value']
	y1=df['total_1']
	y2=df['total_2']

	plt.cla()
	plt.plot(x,y1,label='Channel1')
	plt.plot(x,y2,label='Channel2')

	plt.legend()

#passing (fig, function, interval of repetition in ms)
an=FuncAnimation(plt.gcf(),animate, interval=1000)  
plt.tight_layout()
plt.show()


