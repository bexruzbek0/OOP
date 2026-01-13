
class Transport:
    def __init__(self, model, year):
        self.model = model
        self.year = year


class Car(Transport):
    def __init__(self, model, year, color):
        super().__init__(model, year) 
        self.color = color


car1 = Car("Toyota Camry", 2022, "Oq")


print("Modeli:", car1.model)
print("Yili:", car1.year)
print("Rangi:", car1.color)
