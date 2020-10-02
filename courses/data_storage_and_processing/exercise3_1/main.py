# exercise 3.1 solution
from math import exp
import re


def deserialize_data(path: str):
    file = open(path)
    data = {}
    min_distance = ''
    min_stop_count = ''
    min_cost = ''
    for line in file:
        splitted_line = line.split('\t')
        splitted_line[3] = re.sub('\n', ' ', splitted_line[3])
        data[splitted_line[0]] = list(map(float, splitted_line[1:4]))
        if min_distance == '' or data[splitted_line[0]][0] < min_distance:
            min_distance = data[splitted_line[0]][0]
        if min_stop_count == '' or data[splitted_line[0]][1] < min_stop_count:
            min_stop_count = data[splitted_line[0]][1]
        if min_cost == '' or data[splitted_line[0]][2] < min_cost:
            min_cost = data[splitted_line[0]][2]
    return exp_norm(data, min_distance, min_stop_count, min_cost)


def exp_func(x: int, xmin: int):
    return 1 - exp(1 - x / xmin)


def exp_norm(data: dict, min_distance: int, min_stop_count: int, min_cost: int):
    norm_data = {}
    best1 = {}
    best2 = {}
    best3 = {}
    for key in data:
        norm_data[key] = sum([exp_func(data[key][0], min_distance), exp_func(data[key][1], min_stop_count),
                              exp_func(data[key][2], min_cost)])
        if len(best1.keys()) == 0 or norm_data[key] < best1[list(best1.keys())[0]]:
            if len(best1.keys()) != 0:
                if len(best3.keys()) != 0:
                    id3 = list(best3.keys())[0]
                    best3.pop(id3)
                    id3 = list(best2.keys())[0]
                    value3 = best2.pop(list(best2.keys())[0])
                    best3[id3] = value3
                id2 = list(best1.keys())[0]
                value2 = best1.pop(list(best1.keys())[0])
                best2[id2] = value2
                best1[key] = norm_data[key]
            else:
                best1[key] = norm_data[key]
        elif len(best2.keys()) == 0 or norm_data[key] < best2[list(best2.keys())[0]]:
            if len(best2.keys()) != 0:
                if len(best3.keys()) != 0:
                    id3 = list(best3.keys())[0]
                    best3.pop(id3)
                    id3 = list(best2.keys())[0]
                    value3 = best2.pop(list(best2.keys())[0])
                    best3[id3] = value3
                else:
                    id3 = list(best2.keys())[0]
                    value3 = best2.pop(list(best2.keys())[0])
                    best3[id3] = value3
                best2[key] = norm_data[key]
            else:
                best2[key] = norm_data[key]
        elif len(best3.keys()) == 0 or norm_data[key] < best3[list(best3.keys())[0]]:
            if len(best3.keys()) != 0:
                id3 = list(best3.keys())[0]
                best3.pop(id3)
                best3[key] = norm_data[key]
            else:
                best3[key] = norm_data[key]
    result = list(map(int, [list(best1.keys())[0], list(best2.keys())[0], list(best3.keys())[0]]))
    result.sort()
    return result


if __name__ == '__main__':
    print('Copy table without column names to any file and then')
    table = input('Input path to this file: ')
    print(deserialize_data(table))

