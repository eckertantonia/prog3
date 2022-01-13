# !/usr/bin/env python3

#Aufgabe 1.2 Slicing
liste = list(range(101))
print(liste)

#die ersten 10 Zahlen
print(liste[:10]) 

#die letzten 10 Zahlen
print(liste[-10:])

#jede 10.te Zahl ab 0
print(liste[0::10])

#die mittlere Zahl
mitte = int((len(liste)-1)/2)
print(liste[mitte])

#jede dritte Zahl, aber nicht die ersten vier und die letzten 5
print(liste[5:-5:3])

#Aufgabe3 Kontrollstrukturen
#for-Schleife in while-Schleife umschreiben
lst = [1,2,3]
for e in lst:
    print(e)

i = 0
while i < len(lst):
    print(lst[i])
    i = i+1    

#while-Schleife als for-Schleife
m = [5,3,6,8,1]
i = 0
while i<len(m):
    z = m[i]
    print(z, "hoch zwei ist", z**2)
    i = i+1

for l in m:
    print(l, "hoch zwei ist", l**2)
