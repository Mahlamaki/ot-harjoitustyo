import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_oikea_maara_alussa(self):

        self.assertEqual(str(self.kassapaate.kassassa_rahaa),"100000")

    def test_oikea_maara_ostoja_alussa(self):
        edulliset = self.kassapaate.edulliset
        maukkaat = self.kassapaate.maukkaat
        yhteensa=edulliset+maukkaat
        self.assertEqual(str(yhteensa), "0")

    def test_kateisnosto_toimii_edullinen_riittaa(self):
        self.kassapaate.syo_edullisesti_kateisella(5000)
        kassa=self.kassapaate.kassassa_rahaa
        
        self.assertEqual(str(kassa), "100240")

    def test_edullinen_riittaa_myytyjen_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(5000)
        
        self.assertEqual(str(self.kassapaate.edulliset), "1")

    def test_kateisnosto_toimii_maukas_riittaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(5000)
        kassa=self.kassapaate.kassassa_rahaa
        
        self.assertEqual(str(kassa), "100400")

    def test_maukas_riittaa_myytyjen_maara_kasvaa(self): 
        self.kassapaate.syo_maukkaasti_kateisella(5000)
        
        self.assertEqual(str(self.kassapaate.maukkaat), "1")  

    def test_kateisnosto_toimii_edullinen_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
    
    def test__edullinen_ei_riita_myytyjen_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(str(self.kassapaate.edulliset), "0")


    def test_kateisnosto_toimii_maukas_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")        
    
    def test__maukas_ei_riita_myytyjen_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(str(self.kassapaate.maukkaat), "0")

    def test_kortilla_tarpeeksi_edullinen(self):
        kortti=Maksukortti(100000)
        kortti1=self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(str(kortti1), "True")

    def test_kortilla_tarpeeksi_maukas(self):
        kortti=Maksukortti(100000)
        kortti1=self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(str(kortti1), "True")

    def test_kortilla_ei_tarpeeksi_edullinen(self):
        kortti=Maksukortti(100)
        kortti1=self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(str(kortti1), "False")

    def test_kortilla_ei_tarpeeksi_maukas(self):
        kortti=Maksukortti(100)
        kortti1=self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(str(kortti1), "False")

    def test__edullinen_ei_riita_myytyjen_maara_ei_kasva_korttinosto(self):
        kortti=Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(str(self.kassapaate.edulliset), "0")

    def test__maukas_ei_riita_myytyjen_maara_ei_kasva_korttinosto(self):
        kortti=Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(str(self.kassapaate.maukkaat), "0")

    def test__edullinen_riittaa_myytyjen_maara_kasvaa_korttinosto(self):
        kortti=Maksukortti(100000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(str(self.kassapaate.edulliset), "1")

    def test__maukas_riittaa_myytyjen_maara_kasvaa_korttinosto(self):
        kortti = Maksukortti(100000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(str(self.kassapaate.maukkaat), "1")

    def test_kassassa_oleva_maara_ei_muutu_kortilla_ostaessa_edullinen(self):
        kortti=Maksukortti(400000000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_kassassa_oleva_maara_ei_muutu_kortilla_ostaessa_maukas(self):
        kortti=Maksukortti(40000000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_oikea_maara_kortille_ja_kassaa_kun_lataa(self):
        kortti=Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti,100)
        self.assertEqual(str(kortti.saldo+self.kassapaate.kassassa_rahaa), "100300")


    def test_oikea_maara_kortille_ja_kassaa_kun_lataa_negatiivinen(self):
        kortti=Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti,-400)
        self.assertEqual(str(kortti.saldo+self.kassapaate.kassassa_rahaa), "100100")
