import matplotlib.pyplot as plt

from courses.data_storage_and_processing.exercise2_2.DividingLineType import DividingLineType


class RoadChart:

    def __init__(self, road_data) -> None:
        self.__road_data = road_data
        super().__init__()

    def plot(self) -> None:
        self.__plot_car_chart()
        self.__plot_split_line_chart()

        plt.xlabel("time")
        plt.ylabel("coordinate")

        plt.grid()
        plt.legend()
        plt.show()
        return

    def __plot_car_chart(self) -> None:
        x, y = [], []
        for record in self.__road_data:
            x.append(record.time())
            y.append(record.car())
        plt.plot(x, y, label="Car", color="#eb4034")

    def __plot_split_line_chart(self) -> None:
        interrupt_x, interrupt_y = [], []
        single_x, single_y = [], []
        double_x, double_y = [], []

        for record in self.__road_data:
            if record.line_type() == DividingLineType.INTERRUPT.name():
                interrupt_x.append(record.time())
                interrupt_y.append(record.line_coordinate())
            if record.line_type() == DividingLineType.SINGLE.name():
                single_x.append(record.time())
                single_y.append(record.line_coordinate())
            if record.line_type() == DividingLineType.DOUBLE.name():
                double_x.append(record.time())
                double_y.append(record.line_coordinate())

        plt.plot(interrupt_x, interrupt_y, label="Interrupt", color="#3474eb")
        plt.plot(single_x, single_y, label="Single", color="#34eb4c")
        plt.plot(double_x, double_y, label="Double", color="#eb34c6")
