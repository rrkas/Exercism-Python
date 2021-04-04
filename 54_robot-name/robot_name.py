import random


def random_letters(param) -> str:
    return ''.join([chr(ord('A') + random.randint(0, 25)) for i in range(param)])


class Robot:
    __names = []

    def __init__(self):
        self.__generate_name()

    def __generate_name(self):
        name = random_letters(2) + str(random.randint(0, 1000)).ljust(3, '0')
        while name in Robot.__names:
            name = random_letters(2) + str(random.randint(0, 1000)).ljust(3, '0')
        self.name = name
        Robot.__names.append(name)

    def reset(self):
        self.__generate_name()
