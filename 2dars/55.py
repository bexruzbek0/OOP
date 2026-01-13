
class Device:
    def __init__(self, brand):
        self.brand = brand

class Phone(Device):
    def __init__(self, brand, ram):
        super().__init__(brand)  
        self.ram = ram


phone1 = Phone("Samsung", "8 GB")


print("Telefon brendi:", phone1.brand)
print("RAM hajmi:", phone1.ram)
