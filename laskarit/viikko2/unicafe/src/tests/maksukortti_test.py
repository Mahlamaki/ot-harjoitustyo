import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_alkusaldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_saldo_vahenee_oikein_kun_tarpeeksi_saldoa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_saldo_ei_muutu_jos_ei_tarpeeksi_saldoa(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_palauttaa_True_jos_rahat_riittavat(self):
        tulos = self.maksukortti.ota_rahaa(1000)

        self.assertTrue(tulos)

    def test_palauttaa_False_jos_rahat_ei_riita(self):
        tulos = self.maksukortti.ota_rahaa(2000)

        self.assertFalse(tulos)

    def test_str_tulostus_toimii_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
