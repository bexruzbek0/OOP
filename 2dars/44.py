
class Building:
    def __init__(self, address):
        self.address = address


class School(Building):
    def __init__(self, address, student_count):
        super().__init__(address)  
        self.student_count = student_count


school1 = School("Toshkent sh., Yunusobod tumani", 850)

print("Maktab manzili:", school1.address)
print("Oquvchilar soni:", school1.student_count)
