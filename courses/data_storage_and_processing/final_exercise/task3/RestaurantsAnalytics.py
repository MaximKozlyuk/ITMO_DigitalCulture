class RestaurantsAnalytics:

    def __init__(self, restaurants) -> None:
        self.__restaurants = restaurants
        self.__normalized = []
        super().__init__()

    def normalize(self):
        guests_to_emp_arr = self.__guests_to_emp_arr()
        new_sold_to_emp_arr = self.__new_sold_to_emp_arr()
        social_nets_rating_arr = self.__social_nets_rating_arr()

        guests_to_emp_max = max(guests_to_emp_arr)
        guests_to_emp_min = min(guests_to_emp_arr)

        new_sold_to_emp_max = max(new_sold_to_emp_arr)
        new_sold_to_emp_min = min(new_sold_to_emp_arr)

        social_nets_rating_max = max(social_nets_rating_arr)
        social_nets_rating_min = min(social_nets_rating_arr)

        guests_to_emp_norm = self.__normalize_array(guests_to_emp_arr, guests_to_emp_max - guests_to_emp_min)
        new_sold_to_emp_norm = self.__normalize_array(new_sold_to_emp_arr, new_sold_to_emp_max - new_sold_to_emp_min)
        social_nets_rating_norm = self.__normalize_array(
            social_nets_rating_arr, social_nets_rating_max - social_nets_rating_min)

        norm_restaurants = []
        for i in range(len(guests_to_emp_norm)):
            norm_restaurants.append(
                NormRestaurant(
                    self.__restaurants[i].letter,
                    guests_to_emp_norm[i] + new_sold_to_emp_norm[i] + social_nets_rating_norm[i]
                )
            )
        sorted_restaurants = sorted(norm_restaurants, key=lambda x: x.norma, reverse=True)
        print("Top 3 restaurants:")
        for i in (0, 1, 2):
            print(sorted_restaurants[i])

    def __normalize_array(self, array, min_max_delta) -> []:
        norm_arr = []
        for i in range(len(array)):
            norm_arr.append(array[i] / min_max_delta)
        return norm_arr

    def __guests_to_emp_arr(self):
        arr = []
        for i in range(len(self.__restaurants)):
            arr.append(self.__restaurants[i].guests_to_emp)
        return arr

    def __new_sold_to_emp_arr(self):
        arr = []
        for i in range(len(self.__restaurants)):
            arr.append(self.__restaurants[i].new_sold_to_emp)
        return arr

    def __social_nets_rating_arr(self):
        arr = []
        for i in range(len(self.__restaurants)):
            arr.append(self.__restaurants[i].social_nets_rating)
        return arr

    def __str__(self) -> str:
        string = ""
        for i in range(len(self.__restaurants)):
            string += str(i) + " " + str(self.__restaurants[i]) + "\n"
        return string


class NormRestaurant:

    def __init__(self, letter, norma) -> None:
        self.letter = letter
        self.norma = norma
        super().__init__()

    def __str__(self) -> str:
        return self.letter + " " + str(self.norma)
