# <TICKER>;<PER>;<DATE>;<TIME>;<OPEN>;<HIGH>;<LOW>;<CLOSE>;<VOL>
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

    def avg_price(self):
        return (self.__price_open + self.__high + self.__low + self.__close) / 4

    def sum_volume(self):
        return self.__vol * self.avg_price()
