from typing import List

raw: str = ""
with open("day1/input.txt", "r") as f:
    raw = f.read()


calories_elves: List[List[int]] = []
current_elf: List[int] = []

for line in raw.split("\n"):
    if line == "":
        calories_elves.append(current_elf)
        current_elf = []
        continue
    current_elf.append(int(line))

print(max([sum(x) for x in calories_elves]))
