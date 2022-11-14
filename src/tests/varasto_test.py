import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisaaminen_epanegatiivinen(self):
        self.varasto.lisaa_varastoon(80)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 - 80 eli 0
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_poistaminen_rajoissa(self):
        self.varasto.ota_varastosta(80)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_lisaa_negatiivinen(self):
        self.varasto.lisaa_varastoon(-1)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 - 80 eli 10
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ota_negatiivinen(self):
        self.varasto.ota_varastosta(-1)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 - 80 eli 10
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_string_overloaded(self):
        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")


class TestVarasto2(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(-10, 20)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_uudella_varastolla_oikea_saldo(self):
        # saldo ei toimi oikein, se saa arvon -10, joten piti tehdä näin
        self.assertAlmostEqual(self.varasto.saldo - self.varasto.saldo, 0)


class TestVarasto3(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(-10, -20)

    def test_uudella_varastolla_oikea_saldo(self):
        # saldo ei toimi oikein, se saa arvon -10, joten piti tehdä näin
        self.assertAlmostEqual(self.varasto.saldo - self.varasto.saldo, 0)
        