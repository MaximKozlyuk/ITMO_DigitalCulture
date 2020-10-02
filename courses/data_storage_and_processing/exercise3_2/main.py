# exercise 3.2 solution
# 40,43,52,44,47,39,50,54,45,41,58,56,63,64,57,49,48,51,66,60


def exp_smooth(row: list, alpha: float):
    result = []
    for i in range(len(row)):
        if i == 0:
            result.append(row[i])
        else:
            s = alpha * row[i] + (1 - alpha) * result[len(result) - 1]
            result.append(round(s, 2))
    return result


if __name__ == '__main__':
    row = input('Input your row: ')
    alpha = float(input('Input your alpha: '))
    row = row.split(',')
    row = list(map(int, row))
    print(exp_smooth(row, alpha))
