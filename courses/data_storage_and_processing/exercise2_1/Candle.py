# <TICKER>;<PER>;<DATE>;<TIME>;<OPEN>;<HIGH>;<LOW>;<CLOSE>;<VOL>
import datetime


class Candle:

    def __init__(self, ticker, per, date, time, price_info) -> None:
        self.__ticker = ticker
        self.__per = per
        self.__date = date
        self.__time = time
        self.__price_info = price_info
        super().__init__()

    def __str__(self) -> str:
        return str([
            self.__ticker, self.__per, self.__date, self.__time, str(self.__price_info)
        ])

    def date(self):
        return self.__date

    def isPriceChanged(self) -> bool:
        return self.__price_info.isPriceChanged()

    def sum_volume(self) -> float:
        return self.__price_info.sum_volume()


class PriceInfo:

    def __init__(self, price_open, high, low, close, vol) -> None:
        self.__price_open = price_open
        self.__high = high
        self.__low = low
        self.__close = close
        self.__vol = vol
        super().__init__()

    def __str__(self) -> str:
        return str(
            [self.__price_open, self.__high, self.__low, self.__close, self.__vol]
        )

    def avg_price(self) -> float:
        return (self.__price_open + self.__high + self.__low + self.__close) / 4

    def sum_volume(self) -> float:
        return self.__vol * self.avg_price()

    def isPriceChanged(self) -> bool:
        return self.__price_open == self.__close


class CandleDate:

    # e.g. 20181012
    def __init__(self, date) -> None:
        self.__date = date
        super().__init__()

    def __str__(self) -> str:
        return str(self.__date)

    def weekday(self) -> int:
        this_datetime = datetime.datetime(
            int(self.__date[:4]),
            int(self.__date[4:6]),
            int(self.__date[6:])
        )
        return this_datetime.weekday()

    def month(self) -> int:
        return int(self.__date[4:6])
