elves = []

with open("input.txt") as file:
    lines = file.readlines()

    elf = 0
    elves.append(0)
    for line in lines:
        line = line.strip("\n")
        if line:
            elves[elf] += int(line)
        else:
            elf += 1
            elves.append(0)


elves = sorted(elves, key=lambda x: -x)
print(sum(elves[0:3]))
