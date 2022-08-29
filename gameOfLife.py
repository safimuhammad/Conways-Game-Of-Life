#Todays project is simulating conways game of life using python
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys,argparse

#test grid 
ON = 255
OFF = 0
vals=[ON,OFF]

def randomGrid(N):
    randomArray = np.random.choice(vals,N*N, p=[0.5 ,0.5]).reshape(N,N)
    return randomArray



def addGlider(i,j,grid):
    glider = np.array([[0,0,255],
                       [255,0,255],
                       [0,255,255]])
    grid[i:i+3 , j:j+3 ] = glider



# grid = np.zeros(N*N).reshape(N,150)
# addGlider(1, 1, grid)
def addBar(i,j,grid):
    bar = np.array([[0 , 255 , 0],
                    [0 , 255 , 0],
                    [0 , 255, 0]])
    grid[i:i+3 , j:j+3] =bar

def combined (i1,i2,j1,j2, grid):
     glider = np.array([[0,0,255],
                       [255,0,255],
                       [0,255,255]])
            

     bar = np.array([[0 , 255 , 0],
                    [0 , 255 , 0],
                    [0 , 255, 0]])
     grid[i1:i1+3 , j1:j1+3 ] = glider
     grid[i2:i2+3, j2:j2+3 ] = bar

   




#implementing boundry rules 
def update (framNum, img ,grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i,(j-1)%N]+ grid[i,(j+1)%N]+
                         grid[(i-1)%N,j] + grid[(i+1)%N,j]+
                         grid[(i-1)%N,(j-1)%N]+grid[(i-1)%N,(j+1)%N]+
                         grid[(i+1)%N,(j-1)%N]+grid[(i+1)%N,(j+1)%N])/255)
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

def main():
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
    parser.add_argument('--grid-size' , dest='N' , required=False)
    parser.add_argument('--mov-file' , dest='movfile' , required=False)
    parser.add_argument('--interval' , dest='interval' , required=False)
    parser.add_argument('--glider' , action='store_true' , required=False)
    parser.add_argument('--gosper' , action='store_true', required=False)
    parser.add_argument('--addBar' , action='store_true', required=False)
    parser.add_argument('--combined' , action='store_true', required=False)
    args = parser.parse_args()

    # set grid size
    N = 100 
    if args.N and int(args.N) > 8:
        N = int(args.N)
    #set animation update interval

    updateInterval = 50 
    if args.interval:
        updateInterval = int(args.interval)
    
    # declare grid
    grid = np.array([])
    # check if "glider" demo flag is specified

    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        addGlider(1, 1, grid)
    
    elif args.addBar:
         grid = np.zeros(N*N).reshape(N, N)
         addBar(1, 1, grid)
    elif args.combined:
         grid = np.zeros(N*N).reshape(N, N)
         combined(1,4, 1,4, grid)


    else:
        #populate grid with random on/off 
        grid = randomGrid(N)
    
    #set up the animation 

    fig , ax = plt.subplots()
    img = ax.imshow(grid, interpolation= 'nearest')
    ani = animation.FuncAnimation(fig, update , fargs=(img, grid,N), 
                                  frames=10,
                                  interval=updateInterval,
                                  save_count=50)
    
    # number of frames
    # set the output files
    if args.movfile:
        ani.save(args.movfile , fps=30 , extra_args=['-vcodec', 'libx264'])
    plt.show()

# calling main
if __name__ == '__main__':
    main()