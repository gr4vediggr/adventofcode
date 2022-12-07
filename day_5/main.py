import re

import numpy as np

mode = 'stacks'
skips = 0
moves = []
stacks = []
with open('input.txt') as file: 
    lines = file.readlines()

    for line in lines:
        line = line.strip("\n")
        
        if mode == 'stacks': 
            # (4 n ) - 1 = len


            n = int((len(line) + 1)//4)
            crates = []
            for i in range(0, n):
                a = line[i*4: (i+1)*4].strip(" []")
                
                if a.isdigit():
                    mode = 'skip'
                    break
                
                crates.append(a)
            if len(crates)>0:
                stacks.append(crates)
            
            
        if mode == 'skip':
            skips += 1
            if skips == 3:
                mode = 'moves'
        if mode == 'moves':
            #print(line.strip())
            a = [int(i) for i in re.findall(r"move (\d+) from (\d+) to (\d+)", line.strip())[0]]
            moves.append(a)

stacks = np.transpose(np.array(list(reversed(stacks)), dtype=object)).tolist()
for i in range(len(stacks)):
    while stacks[i][-1] == "":
        stacks[i].pop()


def mover_9000(move_list, stackies):

    from_stack = move_list[1]-1
    to_stack = move_list[2]-1
    amount = move_list[0]
    for i in range(amount): 
        crate = stackies[from_stack].pop()
        stackies[to_stack].append(crate)

def mover_9001(move_list, stackies): 
    from_stack = move_list[1]-1
    to_stack = move_list[2]-1
    amount = move_list[0]

    craties = stackies[from_stack][-amount:]
    stackies[from_stack] = stackies[from_stack][0:-amount]
    stackies[to_stack] = stackies[to_stack] + craties
    
    



    


for move in moves: 
    print(stacks)
    mover_9001(move, stacks)




answer = ""
for i in range(n):

    answer += stacks[i][-1]
print(answer)

