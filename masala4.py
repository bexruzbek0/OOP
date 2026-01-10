class Car:
    def __init__(self, model, yil, yolovchilar_soni):
        self.model = model
        self.yil = yil
        self.yolovchilar_soni = yolovchilar_soni

    def yolovchi_qoshish(self):
        self.yolovchilar_soni += 1
        print(f"Yo‘lovchi qo‘shildi. Hozirgi soni: {self.yolovchilar_soni}")

    def yolovchi_tushirish(self):
        if self.yolovchilar_soni > 0:
            self.yolovchilar_soni -= 1
            print(f"Yo‘lovchi tushirildi. Hozirgi soni: {self.yolovchilar_soni}")
        else:
            print("Yo‘lovchi yo‘q, tushirib bo‘lmaydi!")


car = Car("Gentra", 2022, 1)

car.yolovchi_qoshish()   
car.yolovchi_qoshish()   
car.yolovchi_tushirish() 
