class Fractie():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        print(str(self.numerator) + "/" + str(self.denominator))

    def __add__(self, other):
        common_multiple = 1
        while True:
            if common_multiple % self.denominator == 0 and common_multiple % other.denominator == 0:
                break
            common_multiple += 1
        new_denominator = common_multiple
        new_numerator = common_multiple / self.denominator * self.numerator + common_multiple / other.denominator * other.numerator

        return Fractie(round(new_numerator), new_denominator)

    def __sub__(self, other):
        common_multiple = 1
        while True:
            if common_multiple % self.denominator == 0 and common_multiple % other.denominator == 0:
                break
            common_multiple += 1
        new_denominator = common_multiple
        new_numerator = common_multiple / self.denominator * self.numerator - common_multiple / other.denominator * other.numerator

        return Fractie(round(new_numerator), new_denominator)

    def inverse(self):
        return Fractie(self.denominator, self.numerator)


def main():
    f1 = Fractie(1, 5)
    f2 = Fractie(2, 3)

    f1.__str__()
    (f1.inverse()).__str__()
    (f1.__add__(f2)).__str__()
    (f1.__sub__(f2)).__str__()


if __name__ == "__main__":
    main()
