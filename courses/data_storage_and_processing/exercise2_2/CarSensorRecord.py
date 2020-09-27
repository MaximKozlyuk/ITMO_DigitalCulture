
class CarSensorRecord:

    # structure: LINE_TYPE,LINE,CAR
    def __init__(self, time, line_type, line_coordinate, car) -> None:
        self.__time = time
        self.__line_type = line_type
        self.__line_coordinate = line_coordinate
        self.__car = car
        super().__init__()

    def time(self):
        return self.__time

    def line_type(self):
        return self.__line_type

    def line_coordinate(self):
        return self.__line_coordinate

    def car(self):
        return self.__car
