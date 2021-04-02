class Team:
    def __init__(self, name):
        self.name = name
        self.mp=0
        self.w=0
        self.d=0
        self.l=0
        self.p=0

    def win(self):
        self.mp= self.mp + 1
        self.w = self.w + 1
        self.p = self.p + 3
    
    def lose(self):
        self.mp= self.mp + 1
        self.l = self.l + 1
    
    def draw(self):
        self.mp= self.mp + 1
        self.d = self.d + 1
        self.p = self.p + 1

def tally(rows):
    teams = {}
    first = "Team                           | MP |  W |  D |  L |  P"
    for match in rows:
        parts = match.split(";")
        if parts[0] not in teams.keys():
            t1 = Team(parts[0])
            teams[parts[0]]=t1
        else:
            t1 = teams[parts[0]]

        if parts[1] not in teams.keys():
            t2 = Team(parts[1])
            teams[parts[1]]=t2
        else:
            t2 = teams[parts[1]]

        if parts[2] == "win":
            t1.win()
            t2.lose()
        elif parts[2] == 'loss':
            t1.lose()
            t2.win()
        else:
            t1.draw()
            t2.draw()
    r = [first]
    for p in list(sorted(set([t.p for t in teams.values()])))[::-1]:
        for name in list(sorted([t.name for t in teams.values() if t.p==p])):
            t = teams[name]
            r.append(f"{t.name:30s} | {t.mp:2d} | {t.w:2d} | {t.d:2d} | {t.l:2d} | {t.p:2d}")
    return r