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


grid = np.zeros(150*150).reshape(150,150)
# addGlider(1, 1, grid)




#implementing boundry rules 
def update (framNum, img ,grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i,(j-1)%N]+ grid[i,(j+1)%N]+
                         grid[(i-1)%N,j] + grid[(i+1)%N,j]+
                         grid[(i-1)%N,(j-1)%N]+grid[(i-1)%N,(j-1)%N]+
                         grid[(i+1)%N,(j-1)%N]+grid[(i+1)%N,(j-1)%N])/255)
            #applying conway's rules
            if grid[i,j] == ON:
                if(total < 2) or (total>3):
                    newGrid[i,j] = OFF
            else:
                if total  == 3 :
                    newGrid[i,j] = ON
    #update_data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,