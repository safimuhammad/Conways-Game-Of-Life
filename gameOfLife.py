#Todays project is simulating conways game of life using python
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#test grid 
ON = 255
OFF = 0
vals=[ON,OFF]
def randomGrid(N):
    randomArray = np.random.choice(vals,N*N, p=[0.2 ,0.8]).reshape(N,N)
    return randomArray



def addGlider(i,j,grid):
    glider = np.array([[0,0,255],
                       [255,0,255],
                       [0,255,255]])
    grid[i:i+3 , j:j+3 ] = glider

    plt.imshow(grid, interpolation='nearest')
    plt.show()


grid = np.zeros(100*100).reshape(100,100)
addGlider(1, 1, grid)