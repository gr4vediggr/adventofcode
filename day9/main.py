import numpy as np

tail = np.array([0,0])
head = np.array([0,0])

visited = set()

directions = { 
    "R" : np.array([1,0]),
    "L" : np.array([-1,0]),
    "U" : np.array([0,1]),
    "D" : np.array([0,-1])
}

with open('input.txt') as file : 
    lines = file.readlines()

for line in lines: 
    direction, amount = line.strip().split(" ")
    amount = int(amount)

    for _ in range(amount): 
        head += directions[direction]

        d_pos = head-tail
        if np.any( (np.abs(d_pos) - np.array([1,1])) > 0):
            d_tail = np.clip(d_pos, -1, 1 )
        
        
            tail += d_tail
        x, y = tail
        visited.add((x,y))

print(visited, len(visited) )
        

