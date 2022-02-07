#!/usr/bin/env python3



from numpy import place


def statistik1(filename):
    """
    Bitte ergänzen Sie die Funktion gemäß Aufgabenstellung
    """    
    f = open(filename, "r")
    content = f.read()
    lines = content.split('\n')
    f.close()

    h1 = []
    for z in lines:
        h2 = z.split(';')
        h1.append(h2)
    
    h3 = []
    ausgabe = []

    for z in h1:
        for h in h3:
            if z[0] == h[0] and z[1] == h[1]:
                break
        else:
            zwischenspeicher = [l for l in h1 if l[0] == z[0]]
            """ for l in h1:
                if l[0] == z[0]:
                    zwischenspeicher.append(l) """
            helper = []
            for k in zwischenspeicher:
                if k[1] in helper:
                    continue
                else:
                    sameName = [l for l in zwischenspeicher if l[1]==k[1]]
                    num = 0
                    for i in sameName:
                        num += int(i[2])
                    helper.append(k[1])
                    helper.append(num)
            h3.append([z[0],*helper])
        
    for h in h3:
        samePLZ = [s for s in h3 if s[0]==h[0]]
        str = f"{h[0]}:"
        for s in samePLZ:
            str += f" {s[1]}({s[2]})"

        print(str)

def statistik(filename):
    f = open(filename, "r")
    content = f.read()
    lines = content.split('\n')
    f.close()

    h1 = []
    for z in lines:
        h2 = z.split(';')
        if h2 != ['']:
            h1.append(h2)
    
    # liste mit plz
    plz = []
    for h in h1:
        if h[0] not in plz:
            plz.append(h[0])
    #plz aufsteigend sortieren
    plz.sort()
    
    #helper = []
    #ausgabe = []
    for p in plz:
        ausgabe = []
        str = f"{p}:"
        # alle eintraege fuer eine plz
        l = [h for h in h1 if h[0]==p]
        # alle namen aus l
        names = []
        for li in l:
            if li[1] not in names:
                names.append(li[1])
        # names aufsteigend sortieren
        names.sort()
        # alles fuer einen namen zsm rechen
        for nam in names:
            n = [ele for ele in l if ele[1]==nam]
            anzahl = 0
            for ns in n:
                anzahl += int(ns[2])
            ausgabe.append(ns[1])
            ausgabe.append(anzahl)
            str += f" {ns[1]}({anzahl})"
        print(str)
        
        


        
        





################################################################

if __name__ == "__main__":
    import doctest

    statistik("/home/mi/Documents/Sem_5/Prog3/prog3_python/OnlineTests/py/Ueb2022/a2/bestellungen-2.txt")
    print("STOP")

    def test1():
        """
        Test: Nur eine Bestellung je Ort

        >>> from a2 import statistik
        >>> statistik("bestellungen-1.txt")
        30813: Mayer(80)
        59824: Zorkel(80)
        80444: Mayer(41)
        >>>
        """
        pass

    def test2():
        """
        Test: Mehrere Bestellungen je Ort

        >>> from a2 import statistik
        >>> statistik("bestellungen-2.txt")
        30813: Mayer(80) Schnorchel(4)
        80444: Mayer(41) Powaltschik(6) Zorkel(80)
        >>>
        """
        pass

    def test3():
        """
        Test: Mehrere Orte, mehrere Bestellungen je Person

        >>> from a2 import statistik
        >>> statistik("bestellungen-3.txt")
        30813: Mayer(169) Powaltschik(696)
        59824: Meier(84) Zorkel(159)
        64357: Glosema(9)
        80444: Hempel(36) Mayer(42)
        90909: Bembel(8)
        >>>
        """
        pass

    def test4():
        """
        Test: Grosser Abschlusstest

        >>> from a2 import statistik
        >>> statistik("bestellungen-4.txt")
        10883: Arlykkendorf(107)
        30813: Glogomir(4) Kattenhuis(8) Mayer(161) Powaltschik(696) Schnorchel(4)
        59824: Huber(79) Meier(174) Zorkel(87)
        64357: Glosema(9)
        80444: Hempel(36) Mayer(41) von Brabeck(1)
        90909: Bembel(8)
        >>>
        """
        pass

    doctest.testmod(verbose=True, optionflags=doctest.IGNORE_EXCEPTION_DETAIL|doctest.NORMALIZE_WHITESPACE)
