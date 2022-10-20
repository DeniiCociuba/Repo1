class Bird:  # clasa parinte
    def __init__(self):
        self.name = 'Birdy'
        print("Bird created")

    def who_am_i(self):
        print("I am a bird")

    def fly(self):
        print("I am flying")


class Penguin(Bird):  # clasa copil
    def __init__(self):
        super().__init__()  # initializam clasa parinte
        print("Penguin created")
        self.name = "Penguin"

    def who_am_i(self):
        print("I am a penguin")

    def swim(self):
        print("I am swimming")


# clasa copil mosteneste toate metodele si atributele

pengu = Penguin()
pengu.who_am_i()


