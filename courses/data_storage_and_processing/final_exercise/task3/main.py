from courses.data_storage_and_processing.final_exercise.task3.RestaurantDataFile import RestaurantDataFile
from courses.data_storage_and_processing.final_exercise.task3.RestaurantsAnalytics import RestaurantsAnalytics


class App:

    def __init__(self, path_to_data_file) -> None:
        self.__path_to_data_file = path_to_data_file
        super().__init__()

    def start(self) -> None:
        restaurants_data_file = RestaurantDataFile(self.__path_to_data_file)
        restaurants = restaurants_data_file.restaurants()

        # Определите три лучших ресторана месяца.
        # Для определения лучшего ресторана используйте линейную нормировку показателей,
        # а в качестве целевой функции используйте сумму нормированных показателей.
        restaurants_analytics = RestaurantsAnalytics(restaurants)
        restaurants_analytics.normalize()


if __name__ == '__main__':
    app = App(input("Enter path to restaurants data file:"))
    app.start()
