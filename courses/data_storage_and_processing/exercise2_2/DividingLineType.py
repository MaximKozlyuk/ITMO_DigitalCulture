from enum import Enum


class DividingLineType(Enum):
    INTERRUPT = "INTERRUPT"
    SINGLE = "SINGLE"
    DOUBLE = "DOUBLE"

    def __init__(self, name) -> None:
        self.__name = name
        super().__init__()

    def name(self):
        return self.__name

    @staticmethod
    def valueOf(name):
        for member in DividingLineType.__members__:
            if str(member) == name:
                return member
