import os
import re
os.chdir("C:/Users/fearg/Documents/advent/5")

seeds, *blocks = open("./input.txt", "r").read().split("\n\n")
# print(seeds)
seeds = list(map(int, seeds.split("seeds: ")[1].split()))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    for x in seeds:
        for a, b, c in ranges:
            if x in range(b, b + c):
                new.append(x - b + a)
                break
        else:
            new.append(x)
    seeds = new

print(min(seeds))