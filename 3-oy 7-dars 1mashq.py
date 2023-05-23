class RationalRaqam:
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def __add__(self, boshqa):
        if isinstance(boshqa, RationalRaqam):
            yangi_son1 = (self.son1 * boshqa.son2) + (boshqa.son1 * self.son2)
            yangi_son2 = self.son2 * boshqa.son2
            return RationalRaqam(yangi_son1, yangi_son2)
        else:
            raise TypeError("Qollanilmaydigan operant turi: +")

    def __sub__(self, boshqa):
        if isinstance(boshqa, RationalRaqam):
            yangi_son1 = (self.son1 * boshqa.son2) - (boshqa.son1 * self.son2)
            yangi_son2 = self.son2 * boshqa.son2
            return RationalRaqam(yangi_son1, yangi_son2)
        else:
            raise TypeError("Qollanilmaydigan operant turi: -")

    def __mul__(self, boshqa):
        if isinstance(boshqa, RationalRaqam):
            yangi_son1 = self.son1 * boshqa.son1
            yangi_son2 = self.son2 * boshqa.son2
            return RationalRaqam(yangi_son1, yangi_son2)
        else:
            raise TypeError("Qollanilmaydigan operant turi: *")

    def __truediv__(self, boshqa):
        if isinstance(boshqa, RationalRaqam):
            if boshqa.son1 == 0:
                raise ZeroDivisionError("Nolga bo'lish")
            yangi_son1 = self.son1 * boshqa.son2
            yangi_son2 = self.son2 * boshqa.son1
            return RationalRaqam(yangi_son1, yangi_son2)
        else:
            raise TypeError("Qollanilmaydigan operant turi: /")

    def __str__(self):
        return f"{self.son1}/{self.son2}"


son1 = RationalRaqam(1, 2)
son2 = RationalRaqam(3, 4)

yigindi_natija = son1 + son2
ayirish_natija = son1 - son2
kopaytirish_natija = son1 * son2
bolish_natija = son1 / son2

print("Yigindi:", yigindi_natija)
print("Ayirish:", ayirish_natija)
print("Kopaytirish:", kopaytirish_natija)
print("Bolish:", bolish_natija)
