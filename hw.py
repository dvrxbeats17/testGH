# class City:
#     def __init__(self):
#         self.name = ""
#         self.region = ""
#         self.country = ""
#         self.population = 0
#         self.postal_code = ""
#         self.phone_code = ""

#     def input_data(self):
#         self.name = input("Введите название города: ")
#         self.region = input("Введите название региона: ")
#         self.country = input("Введите название страны: ")
#         self.population = int(input("Введите количество жителей в городе: "))
#         self.postal_code = input("Введите почтовый индекс города: ")
#         self.phone_code = input("Введите телефонный код города: ")

#     def display_data(self):
#         print("Название города:", self.name)
#         print("Название региона:", self.region)
#         print("Название страны:", self.country)
#         print("Количество жителей в городе:", self.population)
#         print("Почтовый индекс города:", self.postal_code)
#         print("Телефонный код города:", self.phone_code)

#     def get_name(self):
#         return self.name

#     def get_region(self):
#         return self.region

#     def get_country(self):
#         return self.country

#     def get_population(self):
#         return self.population

#     def get_postal_code(self):
#         return self.postal_code

#     def get_phone_code(self):
#         return self.phone_code


# city1 = City()
# city1.input_data()
# print("\nДанные о городе:")
# city1.display_data()

# print("\nНазвание города через метод класса:", city1.get_name())
# print("Название региона через метод класса:", city1.get_region())
# print("Название страны через метод класса:", city1.get_country())
# print("Количество жителей в городе через метод класса:", city1.get_population())
# print("Почтовый индекс города через метод класса:", city1.get_postal_code())
# print("Телефонный код города через метод класса:", city1.get_phone_code())


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def simplify(self):
        gcd = self.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def display(self):
        print(f"{self.numerator}/{self.denominator}")


fraction1 = Fraction(3, 4)
fraction2 = Fraction(1, 2)

print("Сложение:")
result = fraction1 + fraction2
result.simplify()
result.display()

print("Вычитание:")
result = fraction1 - fraction2
result.simplify()
result.display()

print("Умножение:")
result = fraction1 * fraction2
result.simplify()
result.display()

print("Деление:")
result = fraction1 / fraction2
result.simplify()
result.display()
