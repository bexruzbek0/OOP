class Student:
    def __init__(self, ism, familya, yonalish, bosqich):
        self.ism = ism
        self.familya = familya
        self.yonalish = yonalish
        self.bosqich = bosqich

    def check_exam(self, ball):
        if ball >= 70:
            self.bosqich += 1
            print(f"Tabriklaymiz! Siz keyingi bosqichga o'tdingiz. Yangi bosqich: {self.bosqich}")
        else:
            print("Siz imtihondan o'tolmadingiz, bu bosqichni qayta o‘qiysiz")


            
student1 = Student("Ali", "Valiyev", "Dasturlash", 2)
student1.check_exam(75)
