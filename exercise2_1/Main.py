from exercise2_1.StockAnalytics import StockAnalytics
from exercise2_1.StockExchangeData import StockExchangeData

data_file_path = "/Users/max/PycharmProjects/ITMO_DigitalCulture/exercise2_1/data/SPFB.RTS-12.18_180901_181231.csv"
stock_dataFile = StockExchangeData(data_file_path)
candles = stock_dataFile.read_candles()
print("Read ", len(candles), " candles records from data file.")

stock_analytics = StockAnalytics(candles)

# 1
# Вычислите суммарный оборот по совершенным сделкам за дату: 26.10.2018.


# 2
# Вычислите количество минутных интервалов за дату 12.10.2018,
# когда цена не менялась (цена открытия равна цене закрытия).


# 3
# Вычислите общий оборот по всем сделкам за все пятницы декабря.

