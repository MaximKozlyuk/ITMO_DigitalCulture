import math

from courses.data_storage_and_processing.exercise2_1.StockAnalytics import StockAnalytics
from courses.data_storage_and_processing.exercise2_1.StockExchangeData import StockExchangeData

data_file_path = "/courses/data_storage_and_processing/exercise2_1/data/SPFB.RTS-12.18_180901_181231.csv"
stock_dataFile = StockExchangeData(data_file_path)
candles = stock_dataFile.read_candles()
print("Read ", len(candles), " candles records from data file.")

stock_analytics = StockAnalytics(candles)

# 1
# Вычислите суммарный оборот по совершенным сделкам за дату: 26.10.2018. ans=69425054783
# 20181026
sum_volume = stock_analytics.sum_volume_in_date("20181026")
print(sum_volume)


# 2
# Вычислите количество минутных интервалов за дату 12.10.2018,
# когда цена не менялась (цена открытия равна цене закрытия).
# ans - 59
def same_price_in_date_filter(candle):
    if candle.isPriceChanged() and str(candle.date()) == "20181012":
        return candle


price_not_changed_in_date = stock_analytics.filter_candles(same_price_in_date_filter)
print(len(price_not_changed_in_date))


# 3
# Вычислите общий оборот по всем сделкам за все пятницы декабря.
# ans - 116943719078
def friday_of_december_filter(candle):
    date = candle.date()
    if date.weekday() == 4 and date.month() == 12:
        return candle


december_fridays_deals = stock_analytics.filter_candles(friday_of_december_filter)
sum_volume = 0
for c in december_fridays_deals:
    sum_volume += c.sum_volume()
sum_volume = math.ceil(sum_volume)
print(sum_volume)
