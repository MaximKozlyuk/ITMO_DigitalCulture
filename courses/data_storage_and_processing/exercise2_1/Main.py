import math

from courses.data_storage_and_processing.exercise2_1.StockAnalytics import StockAnalytics
from courses.data_storage_and_processing.exercise2_1.StockExchangeData import StockExchangeData

data_file_path = "/Users/max/PycharmProjects/ITMO_DigitalCulture/courses/data_storage_and_processing/" \
                 "exercise2_1/data/SPFB.RTS-12.18_180901_181231.csv"
stock_dataFile = StockExchangeData(data_file_path)
candles = stock_dataFile.read_candles()
print("Read ", len(candles), " candles records from data file.")

stock_analytics = StockAnalytics(candles)

# 1
# Вычислите суммарный оборот по совершенным сделкам за дату: <put your date>.
sum_volume = stock_analytics.sum_volume_in_date("20181008")
print(sum_volume)


# 2
# Вычислите количество минутных интервалов за дату <put your date>,
# когда цена не менялась (цена открытия равна цене закрытия).
def same_price_in_date_filter(candle):
    if candle.is_price_grow() and str(candle.date()) == "20181019":
        return candle


price_not_changed_in_date = stock_analytics.filter_candles(same_price_in_date_filter)
print(len(price_not_changed_in_date))


# 3
# Вычислите общий оборот по всем сделкам за все пятницы декабря.
def friday_of_december_filter(candle):
    date = candle.date()
    if date.weekday() == 4 and date.month() == 12:
        return candle


def monday_of_october_filter(candle):
    date = candle.date()
    if date.weekday() == 0 and date.month() == 10:
        return candle


december_fridays_deals = stock_analytics.filter_candles(monday_of_october_filter)
sum_volume = 0
for c in december_fridays_deals:
    sum_volume += c.sum_volume()
sum_volume = math.ceil(sum_volume)
print(sum_volume)
