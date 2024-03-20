from __future__ import annotations


class RomanianNumber:
    romanian_map = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f'RomanianNumber({self.value})'

    def __str__(self) -> str:
        return self.to_roman()

    def to_roman(self) -> str:
        result = ''
        for num in sorted(self.romanian_map.keys(), reverse=True):
            while self.value >= num:
                result += self.romanian_map[num]
                self.value -= num
        return result

    def __add__(self, other: RomanianNumber) -> RomanianNumber:
        return RomanianNumber(self.value + other.value)

    def __sub__(self, other: RomanianNumber) -> RomanianNumber:
        return RomanianNumber(self.value - other.value)

    def __mul__(self, other: RomanianNumber) -> RomanianNumber:
        return RomanianNumber(self.value * other.value)

    def __truediv__(self, other: RomanianNumber) -> RomanianNumber:
        return RomanianNumber(self.value // other.value)

    def __eq__(self, other: RomanianNumber) -> bool:
        return self.value == other.value

    def __lt__(self, other: RomanianNumber) -> bool:
        return self.value < other.value

    def __gt__(self, other: RomanianNumber) -> bool:
        return self.value > other.value

    def __le__(self, other: RomanianNumber) -> bool:
        return self.value <= other.value

    def __ge__(self, other: RomanianNumber) -> bool:
        return self.value >= other.value

    @staticmethod
    def from_arabic(arabic_number: int) -> RomanianNumber:
        result = 0
        for num, roman_numeral in sorted(RomanianNumber.romanian_map.items(), reverse=True):
            while arabic_number >= num:
                result += num
                arabic_number -= num
        return RomanianNumber(result)

num1 = RomanianNumber(9)
num2 = RomanianNumber.from_arabic(7)
sum_num = num1 + num2
print(sum_num)
