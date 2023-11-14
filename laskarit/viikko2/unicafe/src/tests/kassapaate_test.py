import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
       self.kassapaate = Kassapaate()
    
    def test_kassapaate_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_kasvattaa_oikean_verran_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000+2.4)

    def test_kateisosto_kasvattaa_oikean_verran_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000+4.0)

    def test_korttiosto_ei_lisaa_kassaan_rahaa_edullinen_palauttaa_True(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(kortti))
    
    def test_korttiosto_kun_kortilla_ei_tarpeeksi_edullinen_palauttaa_False(self):
        kortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))

    def test_korttiosto_ei_lisaa_kassaan_rahaa_maukas_palauttaa_True(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(kortti))

    def test_korttiosto_kun_kortilla_ei_tarpeeksi_maukas_palauttaa_False(self):
        kortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))

    def test_edullinen_osto_nakyy_lounaita_myyty(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.kassapaate.syo_edullisesti_kateisella(400)

        self.assertEqual(self.kassapaate.edulliset,2)

    def test_maukas_osto_nakyy_lounaita_myyty(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 2)

    def test_vaihtoraha_edulliset(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual(takaisin, 260)

    def test_vaihtoraha_maukkaat(self):
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(takaisin,100)

    def test_myynti_ei_kasva_jos_maksu_ei_riita_edullinen(self):
        kortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.kassapaate.syo_edullisesti_kateisella(10)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myynti_ei_kasva_jos_maksu_ei_riita_maukkaat(self):
        kortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.kassapaate.syo_maukkaasti_kateisella(10)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_vaihtoraha_kun_maksu_ei_riita_edullinen(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(10)

        self.assertEqual(takaisin, 10)

    def test_vaihtoraha_kun_maksu_ei_riita_maukkaat(self):

        takaisin = self.kassapaate.syo_maukkaasti_kateisella(10)

        self.assertEqual(takaisin, 10)

    def test_lataa_rahaa_kortille(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti,100)

        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001.0)

    def test_lataa_rahaa_kortille_ei_onnistu_jos_negatiivinen_maara(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti,-100)

        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        