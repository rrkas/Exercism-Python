class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = list(diagram.split("\n"))
        self.students = list(sorted(students))
    
    def plants(self, name):
        idx = self.students.index(name)
        f = ""
        for row in self.diagram:
            f = f + row[idx*2] + row[idx*2+1]
        codes = {
            "G":"Grass",
            "C":"Clover",
            "R":"Radishes",
            "V":"Violets",
        }
        return [codes[code] for code in f]
