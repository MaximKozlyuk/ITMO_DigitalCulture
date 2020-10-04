# file structure: X;Y;Z;L;R
class CoordinatesDataFile:

    def __init__(self, path_to_coordinates_file) -> None:
        self.__path_to_coordinates_file = path_to_coordinates_file
        super().__init__()

    def read_coordinates(self):
        xy, xz, xl, xr = [[], []], [[], []], [[], []], [[], []]
        with open(self.__path_to_coordinates_file, 'r') as file:
            for row in file:
                coordinate = row.split(";")
                if coordinate[1] != '':
                    xy[0].append(float(coordinate[0]))
                    xy[1].append(coordinate[1])
                elif coordinate[2] != '':
                    xz[0].append(float(coordinate[0]))
                    xz[1].append(float(coordinate[2]))
                elif coordinate[3] != '':
                    xl[0].append(float(coordinate[0]))
                    xl[1].append(float(coordinate[3]))
                elif coordinate[4] != '':
                    xr[0].append(float(coordinate[0]))
                    xr[1].append(float(coordinate[4]))
        return xy, xz, xl, xr
