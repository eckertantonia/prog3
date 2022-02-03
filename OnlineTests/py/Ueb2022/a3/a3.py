#!/usr/bin/python3


def isHawaiian(w):
    """
    Bitte ergänzen
    """




def extractHi(iterable):
    """
    Bitte auch ergänzen
    """





#######################################################################

if __name__ == "__main__":
    import doctest

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



