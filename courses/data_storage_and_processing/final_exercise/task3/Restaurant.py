class Restaurant:

    def __init__(self, letter, guests_to_emp, new_sold_to_emp, social_nets_rating) -> None:
        self.letter = letter
        self.guests_to_emp = guests_to_emp
        self.new_sold_to_emp = new_sold_to_emp
        self.social_nets_rating = social_nets_rating
        super().__init__()

    def __str__(self) -> str:
        return str(self.letter) + " " + \
               str(self.guests_to_emp) + " " + \
               str(self.new_sold_to_emp) + " " + \
               str(self.social_nets_rating)
