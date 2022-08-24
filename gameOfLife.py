#Todays project is simulating conways game of life using python
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#test grid 
# x = np.array([[0,0,255],[255,255,0],[0,255,0]])
x = np.random.choice([0,255],4*4, p =[0.5,0.5]).reshape(4,4)

plt.imshow(x,  interpolation='nearest')
plt.show() #0 == purple 255==yellow