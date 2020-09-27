from courses.data_storage_and_processing.exercise2_2.CarSensorRecord import CarSensorRecord
from courses.data_storage_and_processing.exercise2_2.DividingLineType import DividingLineType


class RoadData:

    def __init__(self, road_data_file_path) -> None:
        self.__file_path = road_data_file_path
        super().__init__()

    # structure: LINE_TYPE,LINE,CAR
    def read_car_sensor_records(self) -> []:
        records = []
        time_count = 1
        with open(self.__file_path, 'r') as file:
            for row in file:
                record = row.split(",")
                records.append(
                    CarSensorRecord(
                        time_count,
                        DividingLineType.valueOf(str(record[0])),
                        int(record[1]),
                        int(record[2])
                    )
                )
                time_count += 1
        return records
