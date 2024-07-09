from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio: str, age: int, passport: str, weight: float):
        self.verify_fio(fio)
        self.verify_age(age)
        self.verify_passport(passport)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__age = age
        self.__passport = passport
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if not isinstance(fio, str):
            raise TypeError('ФИО должно быть строкой')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('В ФИО должно быть больше одного символа')
            if len(s.strip(letters)) != 0:
                raise TypeError('В ФИО можно использовать только буквы и дефис')

    @classmethod
    def verify_age(cls, age):
        if not isinstance(age, int) or age <= 14 or age >= 120:
            raise TypeError('Возраст должен быть целым числом в диапазоне [14;120]')

    @classmethod
    def verify_weight(cls, weight):
        if not isinstance(weight, float) or weight <= 20:
            raise TypeError('Вec должен быть вещественным числом от 20 и выше')

    @classmethod
    def verify_passport(cls, passport):
        if not isinstance(passport, str):
            raise TypeError('Паспорт должен быть строкой')

        s = passport.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат паспорта')

        for p in s:
            if not p.isdigit():
                raise TypeError('Серия и номер должны быть числами')

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_passport(passport)
        self.__passport = passport

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight


person = Person('Васильев Семен Дмитриевич', 20, '1234 567890', 80.1)
person.age = 15
person.passport = '3456 898212'
person.weight = 300.0
