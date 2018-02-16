
def get_bottom_program(filename):
    towers = []
    dict_of_towers = {}
    lone_towers = []
    more_towers = {}
    with open(filename, 'r') as f:
        for tower in f.readlines():
            towers.append(tower.strip().split())
    for tower in towers:
        if len(tower) > 2:
            dict_of_towers[tower[0]] = []
            for element in tower[3:]:
                if element[-1] == ",":
                    dict_of_towers[tower[0]].append(element[:element.index(',')])
                else:
                    dict_of_towers[tower[0]].append(element)
        else:
            lone_towers.append(tower[0])
    for tower in dict_of_towers.keys():
        for key in dict_of_towers.keys():
            if tower in dict_of_towers[key]:
                more_towers[key] = dict_of_towers[key]
                more_towers[key][more_towers[key].index(tower)] = dict([(tower, dict_of_towers[tower])])
    for key, value in more_towers.items():
            for element in value:
                if isinstance(element, dict):
                    for tower in element:
                        for item in element[tower]:
                            if isinstance(item, dict):
                                for next_item in item:
                                    for deep in item[next_item]:
                                        if isinstance(deep, dict):
                                            for next_key in deep:
                                                for very_deep in deep[next_key]:
                                                    if isinstance(very_deep, dict):
                                                        for nie_wiem in very_deep:
                                                            for deep_as_fuck in very_deep[nie_wiem]:
                                                                return key


print(get_bottom_program('day7_input.txt'))
