
import os
os.system("cls")

class product:
    pass


class product:
    def  __init__(self,n,p,s,w,t):

        self.name = n
        self.price = p
        self.shelf_life = s
        self.weight =  w
        self.type_fruit = t

    def info(self):
        print(f"MAxsulot: {self.name}, Narxi: {self.price}")

p1 = product("Yogurt", 12000, '1-oy', 500, 'banan')
p1.info()

p2 = product("Lavash", 36000, '1-kun', 300, 'sir')
p2.info()
