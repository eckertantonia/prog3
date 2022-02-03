#!/usr/bin/env python3

#
# Name: 
# Matrikelnummer:
#

from tokenize import String

from numpy import empty


class Obstsalat:
    """
    Bitte implementieren Sie nachfolgend Ihre Loesung
    """
    def __init__(self, name="", gewicht = None):
       
        self.name = name.capitalize()
        self.gewicht = gewicht        
        if gewicht != None:
            self.zutaten = {self.name:self.gewicht}
        else:
            self.zutaten = {}
    
    def __repr__(self):
        if self.name != "":
            ausgabeName = repr(self.name)
        else:
            ausgabeName = ""
        return "Obstsalat({})".format(ausgabeName)

    def __add__(self, obstVar):
        print(repr(self))
        names = []
        oldNames = self.name.split('-')
        for n in oldNames:
            names.append(n)
        
        newObst = Obstsalat()
        newObst.zutaten.update(self.zutaten)
        newObst.gewicht = self.gewicht
        
        if obstVar.name in newObst.zutaten:
            newObst.zutaten[obstVar.name]+= obstVar.zutaten.get(obstVar.name) 
        else:
            names.append(obstVar.name)
            newObst.zutaten.update(obstVar.zutaten)
        newObst.gewicht += obstVar.gewicht
        # ValueException Error, wenn gewicht goesser 17
        if(newObst.gewicht>17):
            raise ValueError
        names.sort()
        newObst.name = "-".join(names)

        return newObst

    def __lt__(self, other):

        if self.name < other.name:
            return (self.name, self.gewicht) < (other.name, other.gewicht)
        elif self.gewicht < other.gewicht:
            return (self.name, self.gewicht) < (other.name, other.gewicht)
        """ if self.name > other.name:
            return (other.name, other.gewicht) < (self.name, self.gewicht)
        elif self.name < other.name:
            return (self.name, self.gewicht) < (other.name, other.gewicht)
        else:
            if self.gewicht > other.gewicht:
                return (other.name, other.gewicht) < (self.name, self.gewicht)
            else:
                return (self.name, self.gewicht) < (other.name, other.gewicht)
         """


def main():
    """
    Hier koennen Sie eigenen Testcode unterbringen

    Hinweis: Ausfuehrbare Tests zu allen Teilaufgaben in t2.py bekoemmlich.
    Einfach im gleichen Verzeichnis wie a2.py speichern und t2.py starten.
    """
    obst = Obstsalat("Apfel", 5)
    print(obst.name)
    print(obst.zutaten)
    print(repr(obst))
    c = Obstsalat("hl", 1) + Obstsalat("bl", 2) + Obstsalat("Banane", 10)
    #print(repr(c))
    #print(c.zutaten)
    x = Obstsalat("Banane", 3) + Obstsalat("Apfel", 5) + Obstsalat("Banane", 2)
    print(x.zutaten)
    lst = sorted([obst, c, x])
    print(lst)
    


if __name__=="__main__":
    main()


