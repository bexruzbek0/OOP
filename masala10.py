class Weather:
    def __init__(self, temp, shamol, namlik):
        self.temp = temp
        self.shamol = shamol
        self.namlik = namlik



    def describe(self):
        return (
            f"Havo harorati: {self.temp}°C, "
            f"Shamol tezligi: {self.shamol} m/s, "
            f"Namlik: {self.namlik}%."
        )
w = Weather(12.5, 4.0, 60)
print(w.describe())
