#!/usr/bin/python3

import re

def isHawaiian(w):
    """
    Bitte ergänzen
    """
    vokale = "AEIOUaeiou"
    kons = "HKLMNPWhklmnpw\'"

    # Check 1: nur hawaiianisches Alphabet
    for b in w:
        if b not in vokale and b not in kons:
            return False

    # Check 2: endet mit Vokal
    if w[-1] in kons:
        return False

    # Check 3: auf Kons folgt Vok
    for i in range(len(w)):
        if w[i] in kons:
            if w[i+1] in kons:
                return False
        
        # Check 4: Silbenende kein Kons: wird mit Check 3 schon getestet

    return True
    


def extractHi(iterable):
    """
    Bitte auch ergänzen
    """
    ye = []
    for i in iterable:
        newI = re.split(r'[^\w+\'\w+]', i)
        
        for y in newI:
            if y != "" and isHawaiian(y):
                #ye.append(y)
                yield y
    #yield ye






#######################################################################

if __name__ == "__main__":
    import doctest

    w = "Wahine"
    lst = ["Eine Wahine sagt", "Maika'i no au!"]
    print(isHawaiian(w))
    newL = extractHi(lst)
    for l in newL:
        print(l)

    def test1():
        """
        Wort darf keine unhawaiianischen Zeichen enthalten

        >>> isHawaiian("a") is True and isHawaiian("b") is False
        True
        >>> isHawaiian("Wiesbaden")
        False
        >>> isHawaiian("Wahine") 
        True
        >>> isHawaiian("hake'imowu")
        True
        """
        pass

    def test2():
        """
        Wort muss mit Vokal enden

        >>> isHawaiian("Hanau")
        True
        >>> isHawaiian("Kamehameha")
        True
        >>> isHawaiian("Enihaw")
        False
        >>> isHawaiian("amoka'")
        False
        """
        pass


    def test3():
        """
        Auf Konsonanten folgt stets ein Vokal

        >>> isHawaiian("Hawai'i")
        True
        >>> isHawaiian("Pu'uhonua")
        True
        >>> isHawaiian("lekkeke")
        False
        >>> isHawaiian("mu'kau")
        False
        >>> isHawaiian("Muhkuh")
        False
        """
        pass


    def test4():
        """
        Silben enden nicht mit Konsonanten

        >>> isHawaiian("Hau'oli")
        True
        >>> isHawaiian("Ham'ulu")
        False
        >>> isHawaiian("mau'olum'uha")
        False
        """
        pass


    def test5():
        """
        Hawaiianische Wörter aus String-Liste extrahieren

        >>> from inspect import isgenerator, isgeneratorfunction
        >>>
        >>> isgeneratorfunction(extractHi)
        True
        >>> g = extractHi( ["Eine Wahine sagt", "Maika'i no au!"] )
        >>> isgenerator(g)
        True
        >>>
        >>> list(g)
        ['Eine', 'Wahine', "Maika'i", 'no', 'au']
        """
        pass


    def test6():
        """
        Hawaiianische Wörter aus Tupel

        >>> from inspect import isgenerator, isgeneratorfunction
        >>>
        >>> g = extractHi( ("Der Pu'uhonua o Honaunau befindet",
        ...                 "sich an der Kueste der Honaunau Bay",
        ...                 "in South Kona.") )
        >>> assert isgenerator(g) and isgeneratorfunction(extractHi)
        >>>
        >>> for w in g: print(w)
        Pu'uhonua
        o
        Honaunau
        Honaunau
        Kona
        """
        pass


    def test7():
        """
        Generatoren sind slicebar - mal sehen.

        >>> from inspect import isgenerator, isgeneratorfunction
        >>> from itertools import islice
        >>>
        >>> g = extractHi( ("Ein "+"moko"*n for n in range(1,10)) )
        >>> assert isgenerator(g) and isgeneratorfunction(extractHi)
        >>>
        >>> "-".join(islice(g,0,8,2))
        'moko-mokomokomoko-mokomokomokomokomoko-mokomokomokomokomokomokomoko'
        """
        pass


    def test8():
        """
        Hawaiianische Woerter aus dateiartigem Objekt

        >>> from inspect import isgenerator, isgeneratorfunction
        >>> from io import StringIO
        >>> datei = StringIO('''
        ...   Der Name des Staatsfischs von Hawai'i
        ...   lautet wirklich Humuhumunukunukuapua'a.
        ...   Er schwimmt im Meer vor O'ahu herum.
        ...   A hui hou! (auf Wiedersehen)
        ...   ''')
        >>> g = extractHi(datei)
        >>> assert isgenerator(g) and isgeneratorfunction(extractHi)
        >>>
        >>> tuple(sorted(g))
        ('A', "Hawai'i", "Humuhumunukunukuapua'a", 'Name', "O'ahu", 'hou', 'hui')
        """
        pass

    doctest.testmod(verbose=True,optionflags=doctest.IGNORE_EXCEPTION_DETAIL|doctest.NORMALIZE_WHITESPACE)



