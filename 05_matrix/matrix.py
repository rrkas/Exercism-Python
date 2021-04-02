class Matrix:
    def __init__(self, matrix_string):
        self.__r = []
        self.__c = []
        rows = matrix_string.split("\n")
        for r in range(len(rows)):
            t = list(map(int, rows[r].split(" ")))
            self.__r.append(t)
        
        for c in range(len(self.__r[0])):
            t = [ self.__r[i][c] for i in range(len(self.__r))]
            self.__c.append(t)


    def row(self, index):
        return self.__r[index-1]

    def column(self, index):
        return self.__c[index-1]
