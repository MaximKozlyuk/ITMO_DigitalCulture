class Dot:

    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y
        super().__init__()

    def x(self) -> float:
        return self.__x

    def y(self) -> float:
        return self.__y

    def evklid_dist_to(self, dot) -> float:
        return pow(
            pow(self.x() - dot.x(), 2) + pow(self.y() - dot.y(), 2), 1 / 2
        )

    def manheten_dist_to(self, dot) -> float:
        return abs(self.x() - dot.x()) + abs(self.x() - dot.x())

    def chebisheva_dist_to(self, dot) -> float:
        x_ = abs(self.x() - dot.x())
        y_ = abs(self.y() - dot.y())
        return max([x_, y_])
