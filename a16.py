# !/usr/bin/env python3

# Aufgabe 1.6 (Funktionen, Listen)

def dreh(lst):
    #Abbruch:
    if len(lst) == 0: 
        return []
    return [lst[-1]] + dreh(lst[:-1])

liste = [1,2,3,4]
print(dreh(liste))
