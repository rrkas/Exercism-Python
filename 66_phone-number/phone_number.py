class PhoneNumber:
    def __init__(self, number):
        s = ''
        for i in number:
            if i in '1234567890':
                s += i
        if len(s) < 10:
            raise ValueError(' ')
        if len(s) >= 11:
            if len(s) == 11 and s[0] == '1':
                s = s[1:]
            else:
                raise ValueError(' ')
        if s[0] in ('0', '1') or s[3] in ('0', '1'):
            raise ValueError(' ')
        self.number = s
        self.area_code = s[0:3]

    def pretty(self):
        return '(' + self.number[:3] + ')-' + self.number[3:6] + '-' + self.number[6:]
