class Market:
    def __init__(self, xaridor_ismi):
        self.xaridor_ismi = xaridor_ismi
        self.savat = {}   

    def maxsulot_qoshish(self, nom, narx):
        if nom not in self.savat:
            self.savat[nom] = narx
            print(f"{nom} savatga qo‘shildi.")
        else:
            print("Bu maxsulot savatda bor")

    def maxsulot_ayirish(self, nom):
        if nom in self.savat:
            del self.savat[nom]
            print(f"{nom} savatdan o‘chirildi.")
        else:
            print("Bunday maxsulot savatda yo‘q")

    def buyurtma_qilish(self):
        if not self.savat:
            print("Savat bo‘sh")
            return

        print(f"\nXaridor: {self.xaridor_ismi}")
        print("Savatdagi maxsulotlar:")
        jami = 0
        for nom, narx in self.savat.items():
            print(f"- {nom}: {narx} so'm")
            jami += narx

        print(f"Umumiy summa: {jami} so'm\n")



market1 = Market("Ali")
market1.maxsulot_qoshish("Olma", 5000)
market1.maxsulot_qoshish("Banan", 8000)
market1.maxsulot_qoshish("Olma", 5000)
market1.maxsulot_ayirish("Non")
market1.buyurtma_qilish()

market2 = Market("Vali")
market2.maxsulot_qoshish("Sut", 6000)
market2.maxsulot_qoshish("Non", 3000)
market2.maxsulot_ayirish("Sut")
market2.buyurtma_qilish()
