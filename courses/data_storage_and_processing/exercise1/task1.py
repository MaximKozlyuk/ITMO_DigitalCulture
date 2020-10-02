import csv


def read_table(name: str):
    file = open(name, encoding='windows-1251')
    reader = csv.reader(file, delimiter=';')
    table = []
    for row in reader:
        row.pop(0)
        table.append(row)
    table.pop(0)
    table.pop(0)
    return table


def calculate(table: list):
    time_between_stations = []
    rows_with_empty_time = []
    for row in range(len(table)-1):
        current_station = table[row]
        next_station = table[row+1]
        avg_time = 0
        counter = 0
        for time in range(len(current_station)):
            if current_station[time] != '' and next_station[time] != '':
                current_station_time = current_station[time].split(':')
                next_station_time = next_station[time].split(':')
                avg_time += (int(next_station_time[0]) - int(current_station_time[0])) * 3600 + (int(next_station_time[1]) - int(current_station_time[1])) * 60 + (int(next_station_time[2]) - int(current_station_time[2]))
                counter += 1
            elif current_station[time] == '':
                rows_with_empty_time.append(row)
        time_between_stations.append(avg_time/counter)
    tram_with_empty_times = ''
    for time in range(len(table[rows_with_empty_time[0]])):
        if table[rows_with_empty_time[0]][time] == '':
            tram_with_empty_times = time
    if tram_with_empty_times != '':
        start_time = table[0][tram_with_empty_times].split(':')
        end_time = table[len(table)-1][tram_with_empty_times].split(':')
        time_of_full_road = (int(end_time[0]) - int(start_time[0])) * 3600 + (int(end_time[1]) - int(start_time[1])) * 60 + (int(end_time[2]) - int(start_time[2]))
        values_of_empty_time = []
        for row in rows_with_empty_time:
            empty_time = time_of_full_road * time_between_stations[row - 1]/sum(time_between_stations)
            time_of_prev_station = table[row - 1][tram_with_empty_times].split(':')
            empty_time += int(time_of_prev_station[0]) * 3600 + int(time_of_prev_station[1]) * 60 + int(time_of_prev_station[2])
            hours = int(empty_time // 3600)
            minutes = int((empty_time - hours * 3600) // 60)
            seconds = int(empty_time - hours * 3600 - minutes * 60)
            if hours < 10:
                hours = '0' + str(hours)
            if minutes < 10:
                minutes = '0' + str(minutes)
            if seconds < 10:
                seconds = '0' + str(seconds)
            values_of_empty_time.append(str(hours) + ':' + str(minutes) + ':' + str(seconds))
            table[row][tram_with_empty_times] = str(hours) + ':' + str(minutes) + ':' + str(seconds)
        return values_of_empty_time
    return 0


if __name__ == '__main__':
    print('Input path to csv file: ')
    table_name = input()
    table = read_table(table_name)
    print(calculate(table))