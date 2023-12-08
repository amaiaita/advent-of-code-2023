with open("day8.txt") as f:
    TEST_INPUT = f.read().split("\n\n")

instructions = TEST_INPUT[0]
nodes = TEST_INPUT[1].split('\n')
node = {}

for n in nodes:
    split = n.split(' = ')
    node[split[0]] = split[1]

for key,value in node.items():
    node[key] = value.strip('()').split(', ')

instructions = instructions.replace("L","0")
instructions = instructions.replace("R","1")

steps = 0 
next_step=''

while next_step != 'ZZZ':
    for i,instruction in enumerate(instructions):
        instruction = int(instruction)
        if steps == 0:
            next_step = node['AAA'][instruction]
        else: 
            next_step = node[next_step][instruction]
        steps+=1
        if next_step == 'ZZZ':
            break

