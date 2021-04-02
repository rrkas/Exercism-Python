class School:
    def __init__(self):
        self.studs = {}

    def add_student(self, name, grade):
        if grade in self.studs.keys():
            self.studs[grade].append(name)
        else:
            self.studs[grade] = [name]

    def roster(self):
        l=[]
        for grade in sorted(self.studs.keys()):
            l.extend(list(sorted(self.studs[grade])))
        return l

    def grade(self, grade_number):
        if grade_number in self.studs.keys():
            return list(sorted(self.studs[grade_number]))
        return []
 