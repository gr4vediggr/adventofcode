with open("input.txt") as file:
    lines = file.readlines()

# step 1
# find nr columns:
import re

columns = 0
moves = []
init_symbols = []
symbols = []
for line in lines:
    fixed = [l.strip("\n") for l in line.split("[")]
    find = re.findall("(\[[A-Z]\]| \s{3})", line.strip("\n"))
    print(find)
    test = [
        item for sublist in find for item in sublist if (item != "" and item != " ")
    ]

    columns = len(test) if len(test) > columns else columns
    if len(test) == columns:
        init_symbols.append(test)

    move = re.findall("move (\d) from (\d) to (\d)", line.strip("\n"))
    if len(move) > 0:
        moves.append(move[0])

for i in range(columns):
    symbols.append([])

for sym in init_symbols:
    print(sym)

for sym in reversed(init_symbols):

    for i, s in enumerate(sym):
        if s[1] != " ":
            symbols[i].append(s[1])

for s in symbols:
    print(s)


def do_move(from_pile, to_pile, symbols):
    if len(symbols[from_pile]) > 0:
        f = symbols[from_pile].pop()
        symbols[to_pile].append(f)


for move in moves:
    for i in range(int(move[0])):
        do_move(int(move[1]) - 1, int(move[2]) - 1, symbols)

for s in symbols:
    print(s)

print(init_symbols)

s = ""
for c in symbols:
    if len(c) > 0:
        s += c[-1]
print(s)

s = "".join(c[-1] for c in symbols)
print(s)
