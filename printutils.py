import matplotlib.pyplot as plt
import numpy as np
moves = [[0, 1], [1, 0], [0, -1], [-1, 0], [0, 0]]
def initIm(N,env=None,goal_img=None):
    plt.grid()
    plt.xticks(np.arange(-.5, N, int(N/10)),np.arange(0, N, int(N/10)))
    plt.yticks(np.arange(-.5, N, int(N/10)),np.arange(0, N, int(N/10)))
    if env is not None:
        plt.imshow(env.reshape(len(env),len(env)),cmap='gray_r', origin="lower")#obstacles
    if goal_img is not None: 
        plt.imshow(goal_img.reshape(len(env),len(env)),cmap='Purples',alpha=0.6,origin="lower")

def print_grid(grid, N, cmap='gray_r',filename=None):
    initIm(N)
    plt.imshow(grid.reshape(N,N),cmap=cmap, origin="lower")
    if filename:
        plt.savefig(filename)
    else:
        plt.show()

def printMoveAndBeliefOnEnv(env,belief,goal_img,state,action):
    N = len(env)
    move = moves[action]
    
    im1 = plt.arrow(state[1],state[0],move[1],move[0],ec ='green',head_width = 0.2,animated=True) #transition
    im2 = plt.imshow(belief.reshape(len(env),len(env)),cmap='OrRd',origin="lower",alpha=0.5,animated =True) #belief  
    return [im1,im2]

