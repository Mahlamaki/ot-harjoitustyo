import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alkusaldon_tarkistus(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)
        
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")

    def test_ottaminen_vähentää_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(100)
        
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 9.00 euroa")
        
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1200)
        
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_True_jos_rahat_riittää(self):
        
        riittaa=self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(riittaa), "True")

    def test_Falsee_jos_rahat_ei_riitä(self):
        
        self.assertEqual(str(self.maksukortti.ota_rahaa(1200)), "False")
