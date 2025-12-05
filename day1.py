print("Hello Advent of Code")
input = []
with open("inputs/day1.txt") as f:
    for line in f:
        input.append(line.strip()) # removes newline char at end

ans = 0
cur_pos = 50
for rotation in input:
    dir = rotation[0]
    dist = int(rotation[1:])
    if dir == "L":
        cur_pos = (cur_pos - dist) % 100
    else:
        cur_pos = (cur_pos + dist) % 100
    if cur_pos == 0:
        ans += 1

print(ans)
