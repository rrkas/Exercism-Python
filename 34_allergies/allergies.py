allergy_map = {
    1: 'eggs',
    2: 'peanuts',
    4: 'shellfish',
    8: 'strawberries',
    16: 'tomatoes',
    32: 'chocolate',
    64: 'pollen',
    128: 'cats'
}


class Allergies:
    def __init__(self, score):
        self.score = score
        self.items = [v for k, v in allergy_map.items() if k == (score & k)]

    def allergic_to(self, item):
        return item in self.items

    @property
    def lst(self):
        return self.items[:]
