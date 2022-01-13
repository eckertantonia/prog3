#Aufgabe 1.4 (Funktionen, Strings)
#PCTest

def devocalize(s):
    "Entferne Vokale aus einem String"
    vokale = "aeiouAEIOU"

    for v in vokale:
        s = s.replace(v, '')

    return s

print(devocalize("Das ist ein Baerenspass"))