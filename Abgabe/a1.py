#!/usr/bin/env python3

#
# Name: Antonia Eckert
# Matrikelnummer: 1175268
#

import re

def html2java(s):
    "Ihre Loesung"
    newS = ""
    prev = False

    for b in s:
        if b == "-":
            prev = True
            continue
        elif prev:
            prev = False
            newS += b.upper()
        else:
            newS += b

    return newS

    
    
def java2html(s):
    "Ihre Loesung"
    newS = ""

    for b in s:
        if b.isupper():
            newS += "-"+b.lower()
        else:
            newS += b

    return newS



##################################################################

if __name__=="__main__":
    import unittest, sys
    assert sys.version > '3.6', 'Bitte mindestens Python 3.6 verwenden'

    class TestStringMethods(unittest.TestCase):
        """
        Automatischer Vergleich der tatsächlichen Ergebnisse
        der zu implementierenden Funktionen mit einer Referenzlösung.
        """
        def test_1(self):
            htmlname = 'admin-user-eingabe-formular'
            javaname = html2java(htmlname)
            self.assertEqual(javaname, 'adminUserEingabeFormular')

        def test_2(self):
            htmlname = 'titelseite'
            javaname = html2java(htmlname)
            self.assertEqual(javaname, 'titelseite')

        def test_3(self):
            htmlname = 'hilfe-seite'
            javaname = html2java(htmlname)
            self.assertEqual(javaname, 'hilfeSeite')

        def test_4(self):
            javaname = "navigationBar"
            htmlname = java2html(javaname)
            self.assertEqual(htmlname, "navigation-bar")

        def test_5(self):
            javaname = "titel"
            htmlname = java2html(javaname)
            self.assertEqual(htmlname, "titel")

        def test_6(self):
            javaname = "intersectionDetectionActionPanelFrameThing"
            htmlname = java2html(javaname)
            self.assertEqual(htmlname, "intersection-detection-action-panel-frame-thing")


    unittest.main()
    
