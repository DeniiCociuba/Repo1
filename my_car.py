class Car:
    brand = "Dacia"
    model = "1310"
    year = 1970

    # metode
    def accelerate(self):
        print("VRRUUUUMM")

    def show_year(self):
        print(self.year)

my_car = Car()
my_car.accelerate()


class Car:
    # constructor
    def __init__(self, input_brand, input_model, input_year, input_has_leather=True):
        self.brand = input_brand
        self.model = input_model
        self.year = input_year
        self.has_leather = True

    # metode
    def accelerate(self):
        print("VRRUUUUMM")

    def show_year(self):
        print(self.year)  # cu self suntem in interiorul clasei si lucram cu tot ce tine de clasa
    def add_seats(self, nr_of_seats):
        self.seats = nr_of_seats

audi = Car('Audi', 'A7', 2021)



