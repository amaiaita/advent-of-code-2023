with open("day5.txt") as f:
    TEST_INPUT = f.read().split("\n\n")

seeds = [int(x) for x in TEST_INPUT[0].split(' ')[1:]]


maps_formatted = {}

for i in range(1,len(TEST_INPUT)):
    map_list = TEST_INPUT[i].splitlines()
    maps_formatted[map_list[0]] = {}
    for j, code in enumerate(map_list):
        
        if j !=0:
            code = code.split(' ')
            maps_formatted[map_list[0]]['destinations'].append(int(code[0]))
            maps_formatted[map_list[0]]['sources'].append(int(code[1]))
            maps_formatted[map_list[0]]['ranges'].append(int(code[2]))
        else:
            maps_formatted[map_list[0]]['destinations'] = []
            maps_formatted[map_list[0]]['sources'] = []
            maps_formatted[map_list[0]]['ranges'] = []

def mapping_process(map_to_use,source_to_use):
    destination = []
    for j,seed in enumerate(source_to_use):
        current_map = maps_formatted[map_to_use]
        for i, source in enumerate(current_map['sources']):
            if ((seed>=source) & (seed<source+current_map['ranges'][i])):
                destination.append(current_map['destinations'][i] + (seed-source))
                break
        
        if len(destination)<j+1:
            destination.append(seed)
    return destination

soils = mapping_process('seed-to-soil map:',seeds)
fertilizers = mapping_process('soil-to-fertilizer map:',soils)
waters = mapping_process('fertilizer-to-water map:',fertilizers)
lights = mapping_process('water-to-light map:',waters)
temperatures = mapping_process('light-to-temperature map:',lights)
humidities = mapping_process('temperature-to-humidity map:',temperatures)
locations = mapping_process('humidity-to-location map:',humidities)

print(min(locations))