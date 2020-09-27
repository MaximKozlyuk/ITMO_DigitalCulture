from courses.data_storage_and_processing.exercise2_2.RoadChart import RoadChart
from courses.data_storage_and_processing.exercise2_2.RoadData import RoadData

# предполагается что выбросы уже убраны в файле
road_data_csv_file_path = \
    "/Users/max/PycharmProjects/ITMO_DigitalCulture/courses/data_storage_and_processing/exercise2_2/data/car113.csv"
road_data = RoadData(road_data_csv_file_path)
car_sensor_records = road_data.read_car_sensor_records()
print("Read ", len(car_sensor_records), " car sensor records.")

chart = RoadChart(car_sensor_records)
chart.plot()
