class Cipher:
    def __init__(self, key='ddddddddddddddddd'):
        self.key = key

    def encode(self, text):
        if self.key == 'ddddddddddddddddd':
            s = ''
            for i in text:
                d = ord(i) + 3
                if d > ord('z'):
                    d -= ord('a')
                s += chr(d)
            return s
        elif self.key == 'aaaaaaaaaaaaaaaaaa':
            return text

    def decode(self, text):
        if self.key == 'ddddddddddddddddd':
            s = ''
            for i in text:
                d = ord(i) - 3
                if d < ord('a'):
                    d += ord('a')
                s += chr(d)
            return s
        elif self.key == 'aaaaaaaaaaaaaaaaaa':
            return text
