class Student:
    def __init__(self, ism, familiya, yosh, kurs):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.kurs = kurs

    def info(self):
        print("Talaba ma'lumotlari:")
        print(f"Ismi: {self.ism}")
        print(f"Familiyasi: {self.familiya}")
        print(f"Yoshi: {self.yosh}")
        print(f"Kursi: {self.kurs}")
