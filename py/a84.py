# !/usr/bin/env python3

# Aufgabe 8.4 (Dateien, Datenstrukturen)

def auskunft(linie, start, ziel):

    file = open("fahrzeiten.txt", "r")
    fileLines = file.read().splitlines() 
    
    #print(fileLines)
    fahrplan = []
    zeit = 0
    weg = []

    for line in fileLines:
        data = line.split(";")
        data[3].rstrip('\n')
        # data[0] Linie, data[1] Start, data[2] Stop, data[3] stop
        fahrplan.append(data)
    
    # alle Daten zur linie
    linienData = []
    for d in fahrplan:
        if d[0] == linie:
            linienData.append(d)
    
    if start == ziel:
        return (zeit, start)
    else:
        while True:
            for d in linienData:
                if d[1] == start:
                    weg.append(start)
                    zeit += int(d[3])
                    start = d[2]
                if start == ziel:
                    weg.append(start)
                    file.close()
                    return (zeit, weg)
    
    # print(linienData)

minuten, weg = auskunft("Bus6", "Nordfriedhof", "Wiesbaden Hauptbahnhof")
print(minuten, "Minuten so:", weg)
