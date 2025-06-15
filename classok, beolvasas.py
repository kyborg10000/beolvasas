lista = []

class Eladas():
    def __init__(self, sor):
        reszek = sor.split(";")
        self.termekID = reszek[0]
        self.bolt_neve = reszek[1]
        self.db = int(reszek[2])
        self.bevetel = int(reszek[3])
    
    def __str__(self):
        return f"{self.termekID}, {self.bolt_neve}, {self.db}, {self.bevetel}"

def beolvasas():
    f = open("bolt 2.txt", encoding="UTF-8")
    f.readline()
    for item in f:
        obj = Eladas(item.strip())
        lista.append(obj)
    f.close()