# !/usr/bin/env python3

# Aufgabe 8.2 (Funktionen, variable Argumentlisten, Textdatei lesen)

def ggTr(x, y):
    if (x==0):
        return y
    if (y == 0):
        return x
    if (x > y):
        return ggTr(x-y, y)
    else:
        return ggTr(x, y-x)
    

def ggT(x,y):
    while  y != 0:
        x, y = y, x%y
    return x

def ggTl(x, y, *z):
    ergebnis = ggT(x, y)
    for zahl in z:
        ergebnis = ggT(ergebnis, zahl)
    return ergebnis

ggtListe = list(open("ggtbeispiele.txt"))

for ggt in ggtListe:
    inhalt = ggt.split()
    #print("zeile ", inhalt)
    newggt = ggT(int(inhalt[0]), int(inhalt[1]))
    #print(newggt)
    if(newggt != int(inhalt[2])):
        print(ggt, newggt)

print(ggTl(10, 80, 20, 75))
print(ggTl(17,4))
print(ggTl(7,2,2,1,20,11))