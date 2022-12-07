from numpy import array_split

f = lambda c: ord(c) - ord("a") + 1 if ord(c) >= ord("a") and ord(c) <= ord("z") else ord(c) - ord("A") + 27
lines = open("input.txt", "r").readlines()
print("p1", sum(sum(f(a) for a in set(line[: (len(line)) // 2]).intersection(set(line[(len(line)) // 2 :]))) for line in lines))
print("p2", sum(sum(map(f, j)) for j in (set(a[:-1]).intersection(b[:-1], c[:-1]) for a,b,c in array_split(lines, len(lines)//3))))
