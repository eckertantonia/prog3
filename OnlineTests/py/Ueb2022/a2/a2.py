#!/usr/bin/env python3


def statistik(filename):
    """
    Bitte ergänzen Sie die Funktion gemäß Aufgabenstellung
    """    




################################################################

if __name__ == "__main__":
    import doctest

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
