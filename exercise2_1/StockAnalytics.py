import math


class StockAnalytics:

    def __init__(self, candles) -> None:
        self.__candles = candles
        super().__init__()

    # "20181026" - input date format
    def __candles_of_date(self, date_of_deals) -> []:
        candles_of_date = []
        for c in self.__candles:
            if str(c.date()) == date_of_deals:
                candles_of_date.append(c)
        return candles_of_date

    def sum_volume_in_date(self, date) -> float:
        candles_of_date = self.__candles_of_date(date)
        sum_volume = 0
        for c in candles_of_date:
            sum_volume += c.sum_volume()
        return math.ceil(sum_volume)

    def filter_candles(self, predicate) -> []:
        satisfying_candles = []
        for c in self.__candles:
            if predicate(c) is not None:
                satisfying_candles.append(c)
        return satisfying_candles
