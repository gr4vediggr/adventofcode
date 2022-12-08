import numpy as np
import time


grid = []
visible = []

max_h = []

with open('input.txt') as file: 
    for line in file.readlines():
        grid.append([])
        visible.append([])
        max_h.append([])
        s = list(map(int, line.strip()))
        grid[-1] += s
        visible[-1]+= [0]*len(s)
        max_h[-1] += [0]*len(s)

grid = np.array(grid)
visible = np.array(visible)
max_h = np.array(max_h)
grid_shape = grid.shape
visible2 = np.zeros(grid_shape)
scores = np.zeros(grid_shape)

def calc_score(x,y, tree_grid, direction): 
    dx, dy = direction

    i = x+dx
    j = y+dy
    h0 = tree_grid[x,y]
    score = 0
    while (0 <= j < tree_grid.shape[1]) and (0 <= i < tree_grid.shape[0]): 
        if tree_grid[x,y] > tree_grid[i,j]:
            score += 1
            i+=dx
            j += dy
        else:
            score += 1
            break

    return score
        
    


ts = time.time()
for i in range(1,grid_shape[0]-1) : 
    
    for j in range(1, grid_shape[1]-1): 
        score = 1
        score *= calc_score(i,j, grid, [-1,0])
        score *= calc_score(i,j, grid, [1,0])
        score *= calc_score(i,j, grid, [0,1])
        score *= calc_score(i,j, grid, [0,-1])
        #print(f"({i},{j}) = {score}")
        scores[i,j]=score
        
        



print("m1", time.time()-ts)
ts = time.time()

for i in range(grid_shape[0]) : 
    pass
      
print("m2", time.time() - ts)

print(visible)
print(visible2)
print(sum(sum(visible)), sum(sum(visible2)))
print(np.max(scores))
print(scores)
print(grid)