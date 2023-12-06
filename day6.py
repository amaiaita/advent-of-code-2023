with open("day6.txt") as f:
    TEST_INPUT = f.read().split("\n")

times = [x for x in TEST_INPUT[0].split(' ') if x != ''][1:]
times = [int(x) for x in times]
distances = [x for x in TEST_INPUT[1].split(' ') if x != ''][1:]
distances = [int(x) for x in distances]

total = 1

for i,time in enumerate(times):
    ways_to_win = 0
    for hold in range(time+1):
        
        distance_travelled = hold * (time-hold)
        if distance_travelled>distances[i]:
            ways_to_win+=1
    total = total * ways_to_win
print(total)

# part 2

with open("day6.txt") as f:
    TEST_INPUT = f.read().split("\n")

# TEST_INPUT = '''Time:      7  15   30
# Distance:  9  40  200'''.split('\n')

times = [x for x in TEST_INPUT[0].split(' ') if x != ''][1:]

time = ''
for t in times:
    time+=t
time = int(time)

distances = [x for x in TEST_INPUT[1].split(' ') if x != ''][1:]

distance = ''
for d in distances:
    distance+=d
distance = int(distance)

total = 1

ways_to_win = 0
for hold in range(time+1):
    
    distance_travelled = hold * (time-hold)
    if distance_travelled>distance:
        ways_to_win+=1
total = total * ways_to_win

print(total)