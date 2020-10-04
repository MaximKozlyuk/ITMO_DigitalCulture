import matplotlib.pyplot as plt


# defined by equation: y = ax + b
class LineTrend:

    def __init__(self, x, y) -> None:
        if len(x) != len(y):
            raise Exception("Cant create invalid line trend, len(x) != len(y)")
        self.__x = x
        self.__y = y
        super().__init__()

    def plot_trend_line_data(self):
        trend_x, trend_y = self.__trend_coordinates()
        plt.plot(trend_x, trend_y, label="trend")
        plt.plot(self.__x, self.__y, label="data")
        plt.xlabel("time")
        plt.ylabel("coordinate")
        plt.grid()
        plt.show()

    def __trend_coordinates(self) -> ([], []):
        a = self.a()
        b = self.b()
        trend_y = []
        for i in range(len(self.__x)):
            trend_y.append(a * self.__x[i] + b)
        return list(range(len(self.__x))), trend_y

    def n(self) -> float:
        return len(self.__x)

    def a(self) -> float:
        x_sum = sum(self.__x)
        y_sum = sum(self.__y)
        xy = []
        x_squares = []
        for i in range(len(self.__x)):
            xy.append(self.__x[i] * self.__y[i])
            x_squares.append(pow(self.__x[i], 2))
        return (self.n() * sum(xy) - x_sum * y_sum) / (self.n() * sum(x_squares) - pow(x_sum, 2))

    def b(self) -> float:
        y_sum = sum(self.__y)
        x_sum = sum(self.__x)
        return (y_sum - self.a() * x_sum) / self.n()

    # R^2
    def determination(self) -> float:
        trend_x, trend_y = self.__trend_coordinates()
        y_avg = sum(self.__y) / len(self.__y)
        numerator, denominator = 0, 0
        for i in range(len(self.__x)):
            numerator += pow(self.__y[i] - trend_y[i], 2)
            denominator += pow(self.__y[i] - y_avg, 2)
        return 1 - numerator / denominator


series = [41, 48, 53, 40, 51, 50, 39, 38, 47, 55, 46, 52, 49, 61, 64, 54, 67, 65, 63, 70, 62, 58, 72, 74, 57]
line_trend = LineTrend(list(range(0, len(series))), series)
line_trend.plot_trend_line_data()
print("a = ", round(line_trend.a(), 2))
print("b = ", round(line_trend.b(), 3))
print("r = ", round(line_trend.determination(), 3))
