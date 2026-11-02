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

    # Aloitetaan omat testit, tavoitteena 100% coverage kattavuus
    # Muistio aivoille: assertAlmostEqual koska float-luvut

    def test_mita_jos_uusi_varasto_negatiivinen_tilavuus(self):
        self.uusi_varasto = Varasto(-10)
        self.assertAlmostEqual(self.uusi_varasto.tilavuus, 0)
        # Tässä näyttää saldoksi asettuvan -10 vaikka sen pitäisi olla 0.....

    def test_mita_jos_lisataan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_mita_jos_ota_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(-3)
        self.assertAlmostEqual(saatu_maara, 0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_mita_jos_negatiivinen_alkusaldo(self):
        self.uusi_varasto = Varasto(10, -5)
        self.assertAlmostEqual(self.uusi_varasto.saldo, 0)

    def test_lisays_yli_tilavuuden_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_yli_saldon_palauttaa_koko_saldon(self):
        self.varasto.lisaa_varastoon(6)
        saatu_maara = self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(saatu_maara, 6)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varaston_merkkijonoesitys(self):
        self.varasto.lisaa_varastoon(4)
        self.assertEqual(str(self.varasto), "saldo = 4, vielä tilaa 6")
