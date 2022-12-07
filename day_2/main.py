# first read input

from enum import Enum


class Hand(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


def calculate_score(us, them):
    score = 0
    if us == them:
        score = 3
    elif (us.value - them.value) % 3 == 1:
        score = 6
    else:
        score = 0

    return score + us.value + 1


def to_hand_shape(c):
    match c:
        case "A":
            return Hand.ROCK
        case "B":
            return Hand.PAPER
        case "C":
            return Hand.SCISSORS
        case "X":
            return Hand.ROCK
        case "Y":
            return Hand.PAPER
        case "Z":
            return Hand.SCISSORS


def choose_strategy(them, us):
    if us == "X":
        return Hand((them.value - 1) % 3)

    if us == "Y":
        return them
    if us == "Z":

        return Hand((them.value + 1) % 3)


total_score = 0
count_lines = 0
with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        count_lines += 1
        inputs = line.split(" ")
        them = inputs[0]
        us = inputs[1].strip()
        them = to_hand_shape(them)

        us = choose_strategy(them, us)
        score = calculate_score(us, them)
        print(count_lines, us, them, score)
        total_score += score

print(total_score)
