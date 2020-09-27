from exercise2_1.Candle import PriceInfo, Candle


class StockExchangeData:

    def __init__(self, csv_stock_data_file) -> None:
        self.__csv_stock_data_file = csv_stock_data_file
        super().__init__()

    # method assumes that there is NO structure description in first string like the following one:
    # <TICKER>;<PER>;<DATE>;<TIME>;<OPEN>;<HIGH>;<LOW>;<CLOSE>;<VOL>
    def read_candles(self):
        candles = []
        with open(self.__csv_stock_data_file, 'r') as file:
            for row in file:
                records = row.split(";")
                # records[8] = records[8][:1]
                price_info = PriceInfo(
                    float(records[4]),  # 109870.0000000
                    float(records[5]),  # 109920.0000000
                    float(records[6]),  # 109830.0000000
                    float(records[7]),  # 109910.0000000
                    int(records[8]),    # 16
                )
                candle = Candle(
                    records[0],         # SPFB.RTS-12.18
                    int(records[1]),    # 1
                    int(records[2]),    # 20181128
                    int(records[3]),    # 115400
                    price_info
                )
                candles.append(candle)
        return candles

