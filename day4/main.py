with open("input.txt") as file:
    lines = file.readlines()
    count = 0
    count2 = 0
    for line in lines:
        elf1, elf2 = line.strip().split(",")

        a = elf1.split("-")
        elf1_set = set(range(int(a[0]), int(a[1]) + 1))

        b = elf2.split("-")
        elf2_set = set(range(int(b[0]), int(b[1]) + 1))
        if elf1_set.issubset(elf2_set) or elf1_set.issuperset(elf2_set):
            count += 1

        if len(elf2_set.intersection(elf1_set)) > 0:
            count2 += 1

print(count, count2)
