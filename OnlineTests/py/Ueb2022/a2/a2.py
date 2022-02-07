#!/usr/bin/env python3



from numpy import place


def statistik(filename):
    """
    Bitte ergänzen Sie die Funktion gemäß Aufgabenstellung
    """    
    f = open(filename, "r")
    content = f.read()
    lines = content.split('\n')
    f.close()
    pL = [] #PLZ und Name

    c = []
    for l in lines:
        helper = l.split(';')
        c.append(helper)

    plzList = []
    for i in c:
        if plzList == []:
            plzList.append([i[0]])
        elif i[0] in plzList:
            continue
        else:
            plzList.append([i[0]])
    
    kList = []
    for i in plzList:
        for j in c:
            if i == [j[0]]:
                kList.append([j[1]])

        
            
                
    




    
        
        
                




################################################################

if __name__ == "__main__":
    import doctest

    statistik("/home/mi/Documents/Sem_5/Prog3/prog3_python/OnlineTests/py/Ueb2022/a2/bestellungen-1.txt")

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
