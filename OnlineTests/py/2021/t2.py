import unittest
from a2 import Obstsalat

#
# Ausfuehrbare Tests fuer Ihr Modul a2.py
# (bitte in selbem Verzeichnis wie a2.py ablegen
# und dort ausfuehren)
#
# Diese Testdatei NICHT mit abgeben
# Loesung *nur* in a2.py coden.
#

class Test_1(unittest.TestCase):
    def test_1_instanziierung_ohne_parameter(self):
        o = Obstsalat()
        self.assertEqual(o.name, "")
        self.assertEqual(o.zutaten, {})

    def test_1_instanziierung_mit_parametern(self):
        o = Obstsalat("Apfel",10)
        self.assertEqual(o.name, "Apfel")
        self.assertEqual(o.zutaten, {'Apfel':10})

    def test_1_instanziierung_mit_parametern_schreibung_anpassen(self):
        o = Obstsalat("BaNaNe",8)
        self.assertEqual(o.name, "Banane")
        self.assertEqual(o.zutaten, {'Banane':8})

    def test_1_instanziierung_mit_parametern_kleinschreibung_anpassen(self):
        o = Obstsalat("pfirsich",3)
        self.assertEqual(o.name, "Pfirsich")
        self.assertEqual(o.zutaten, {'Pfirsich':3})

    def test_1_repr_bei_leerem_obstsalat(self):
        o = Obstsalat()
        self.assertEqual(repr(o), "Obstsalat()")

    def test_1_repr_bei_unleerem_obstsalat(self):
        o = Obstsalat("JohannisBeere",2)
        self.assertEqual(repr(o), "Obstsalat('Johannisbeere')")

    def test_1_obstsalate_sind_unabhaengig(self):
        o = Obstsalat("JohannisBeere",2)
        self.assertEqual(repr(o), "Obstsalat('Johannisbeere')")
        self.assertEqual(o.zutaten, {'Johannisbeere':2})
        p = Obstsalat("Brombeere",8)
        self.assertEqual(repr(p), "Obstsalat('Brombeere')")
        self.assertEqual(p.zutaten, {'Brombeere':8})

class Test_2(unittest.TestCase):
    def test_2_verschiedennamige_salate_addieren(self):
        pflaume = Obstsalat("Pflaume", 4)
        birne = Obstsalat("Birne", 5)
        erg = pflaume + birne
        self.assertEqual(erg.name, "Birne-Pflaume")
        self.assertEqual(erg.zutaten, {'Pflaume':4, 'Birne':5})
        self.assertIsNot(erg, birne)
        self.assertIsNot(erg, pflaume)

    def test_2_gleichnamige_salate_addieren(self):
        birne1 = Obstsalat("Birne", 5)
        birne2 = Obstsalat("Birne", 4)
        erg = birne1 + birne2
        self.assertEqual(erg.name, "Birne")
        self.assertEqual(erg.zutaten, {'Birne':9})
        self.assertIsNot(erg, birne1)
        self.assertIsNot(erg, birne2)
        self.assertIsNot(erg.zutaten, birne1.zutaten)
        self.assertIsNot(erg.zutaten, birne2.zutaten)

    def test_2_gleichnamige_salate_addieren_schreibung_unterschiedlich(self):
        birne1 = Obstsalat("BirNE", 5)
        birne2 = Obstsalat("BIRne", 4)
        erg = birne1 + birne2
        self.assertEqual(erg.name, "Birne")
        self.assertEqual(erg.zutaten, {'Birne':9})
        self.assertIsNot(erg, birne1)
        self.assertIsNot(erg, birne2)

    def test_2_verschiedennamige_salate_addieren_mit_dopplungen(self):
        birne1 = Obstsalat("BIRNE", 1)
        apfel = Obstsalat("ApFel",10)
        birne2 = Obstsalat("birne", 2)
        erg = birne1 + apfel + birne2
        self.assertEqual(erg.name, "Apfel-Birne")
        self.assertEqual(erg.zutaten, {'Birne':3, 'Apfel': 10})
        self.assertIsNot(erg, birne1)
        self.assertIsNot(erg, apfel)
        self.assertIsNot(erg, birne2)

    def test_2_additionsergebnis_klaut_nicht_zutaten_der_anderen(self):
        birne1 = Obstsalat("BIRNE", 1)
        apfel = Obstsalat("ApFel",10)
        birne2 = Obstsalat("birne", 2)
        erg = birne1 + apfel + birne2
        self.assertIsNot(erg.zutaten, birne1.zutaten)
        self.assertIsNot(erg.zutaten, apfel.zutaten)
        self.assertIsNot(erg.zutaten, birne2.zutaten)
 

class Test_3(unittest.TestCase):
    def test_3_gewicht_summe_einzeln(self):
        erg = Obstsalat("PampelMuse", 12)
        self.assertEqual(erg.gewicht, 12)

    def test_3_gewicht_summe_mehrere(self):
        papaya = Obstsalat("Papaya",5)
        kiwi = Obstsalat("Kiwi",8)
        traube = Obstsalat("TrAUbe",4)
        erg = papaya + kiwi + traube
        self.assertEqual(erg.gewicht, 17)
        self.assertIsNot(erg, papaya)
        self.assertIsNot(erg, kiwi)
        self.assertIsNot(erg.zutaten, papaya.zutaten)
        self.assertIsNot(erg.zutaten, kiwi.zutaten)
        self.assertIsNot(erg.zutaten, traube.zutaten)


class Test_4(unittest.TestCase):
    def test_4_gewicht_ueberschritten_zwei(self):
        with self.assertRaises(ValueError):
            erg = Obstsalat("Litschi",17) + Obstsalat("Litschi", 1)

    def test_4_gewicht_ueberschritten_drei(self):
        with self.assertRaises(ValueError):
            erg = Obstsalat("Himbeere", 6) + Obstsalat("Pflaume",6) + Obstsalat("Quitte",6)

    def test_4_gewicht_ueberschritten_noch_drei(self):
        with self.assertRaises(ValueError):
            erg = Obstsalat("Himbeere", 6) + Obstsalat("Pflaume",6) + Obstsalat("HimBeere",6)

    def test_4_gewicht_ok(self):
        h1 = Obstsalat("Himbeere", 6)
        p  = Obstsalat("Pflaume",6)
        h2 = Obstsalat("HimBeere",5)
        erg = h1 + p + h2
        self.assertIsNot(erg.zutaten, h1.zutaten)
        self.assertIsNot(erg.zutaten, p.zutaten)
        self.assertIsNot(erg.zutaten, h2.zutaten)


class Test_5(unittest.TestCase):
    def test_5_sortieren_zwei_sehr_unterschiedlich(self):
        b1 = Obstsalat("B",5)
        a = Obstsalat("A",8)
        b2 = Obstsalat("B",7)
        b = b1 + b2
        lst = sorted([b, a])
        self.assertEqual(lst, [a, b])
        self.assertIsNot(b.zutaten, b1.zutaten)
        self.assertIsNot(b.zutaten, b2.zutaten)

    def test_5_sortieren_zwei_gleichnamig_verschiedengewichtig(self):
        o1 = Obstsalat("A", 2) + Obstsalat("A",5)
        o2 = Obstsalat("A",6)
        lst = sorted([o1, o2])
        self.assertEqual(lst, [o2, o1])

    def test_5_sortieren_zwei_verschiedennamig_gleichgewichtig(self):
        o1 = Obstsalat("X",1)
        o2 = Obstsalat("M",1)
        lst = sorted([o1, o2])
        self.assertEqual(lst, [o2, o1])

    def test_5_sortieren_beispiel_aufgabenblatt(self):
        o1 = Obstsalat("M",5)
        o2 = Obstsalat("T",1)
        o3 = Obstsalat("C",2)
        o4 = Obstsalat("T",4)
        lst = sorted([o1, o2, o3, o4])
        self.assertEqual(lst, [o3, o1, o2, o4])

    def test_5_sortieren_zwei_geleich_mehrkomponentig(self):
        a1 = Obstsalat("A",3)
        a2 = Obstsalat("B",4)
        b1 = Obstsalat("A",2)
        b2 = Obstsalat("B",7)
        a = a1 + a2
        b = b1 + b2
        lst = sorted([b, a])
        self.assertEqual(lst, [a, b])
        self.assertIsNot(b.zutaten, b1.zutaten)
        self.assertIsNot(b.zutaten, b2.zutaten)


if __name__ == "__main__":
    unittest.main(verbosity=255)

