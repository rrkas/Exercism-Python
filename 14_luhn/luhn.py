class Luhn:
    def __init__(self, card_num):
        self.card = card_num
        self.card=self.card.replace(" ","")
        self.card.strip()


    def valid(self):
        val = 0
        if len(self.card) < 2:
            return False
        for i in range(len(self.card)):
            c = self.card[i]
            try:
                d = int(c)
                if len(self.card) % 2 ==0:
                    if i%2==0:
                        d = d * 2
                        if d > 9: d = d - 9
                else:
                    if i%2==1:
                        d = d * 2
                        if d > 9: d = d - 9
                val = val + d
            except:
                if self.card[i] !=" ":
                    return False
        if val%10 == 0:
            return True
        return False
