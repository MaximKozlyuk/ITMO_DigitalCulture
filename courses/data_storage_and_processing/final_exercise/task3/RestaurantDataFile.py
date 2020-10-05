# колонки:
# Ресторан|Количество гостей ресторана на одного сотрудника ресторана| ->
# -> |Количество проданных новых позиций из меню ресторана на одного сотрудника	| Рейтинг ресторана в социальных сетях
from courses.data_storage_and_processing.final_exercise.task3.Restaurant import Restaurant


class RestaurantDataFile:

    def __init__(self, path_to_file) -> None:
        self.__path_to_file = path_to_file
        super().__init__()

    def restaurants(self) -> []:
        restaurants = []
        with open(self.__path_to_file, 'r') as file:
            for row in file:
                split_row = row.split()
                restaurants.append(
                    Restaurant(
                        str(split_row[0]),
                        float(int(split_row[1])),
                        float(split_row[2]),
                        float(split_row[3]),
                    )
                )
        return restaurants
