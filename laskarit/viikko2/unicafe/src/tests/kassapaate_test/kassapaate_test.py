import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_oikea_maara_rahaa(self):

        rahat_e = round(self.kassapaate.kassassa_rahaa / 100, 2)

        self.assertEqual(rahat_e, 1000)

    def test_oikea_maara_lounaita(self):

        lounaita = self.kassapaate.edulliset + self.kassapaate.maukkaat

        self.assertEqual(lounaita, 0)

    def test_kateis_riittaa_edullinen(self):

        vaihto = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(vaihto, 60)

    def test_kateis_riittaa_maukas(self):

        vaihto = self.kassapaate.syo_maukkaasti_kateisella(600)

        self.assertEqual(vaihto, 200)

    def test_kateis_riittaa_kassa_kasvaa_edullinen(self):

        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateis_riittaa_kassa_kasvaa_maukas(self):

        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateis_riittaa_lounas_kasvaa_edullinen(self):

        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateis_riittaa_lounas_kasvaa_maukas(self):

        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateis_ei_riita_kassa_ei_muutu_edullinen(self):

        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateis_ei_riita_kassa_ei_muutu_maukas(self):

        self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateis_ei_riita_vaihto_edullinen(self):

        vaihto = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(vaihto, 200)

    def test_kateis_ei_riita_vaihto_maukas(self):

        vaihto = self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(vaihto, 200)

    def test_kateis_ei_riita_lounaita_edullinen(self):

        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateis_ei_riita_lounaita_maukas(self):

        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilla_tarpeeksi_rahaa_edullinen(self):

        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo, 760)

      
    def test_kortilla_tarpeeksi_rahaa_maukas(self):

        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo, 600)

    def test_kortilla_tarpeeksi_rahaa_true_edullinen(self):

        vastaus = self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(vastaus, True)

      
    def test_kortilla_tarpeeksi_rahaa_true_maukas(self):

        vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(vastaus, True)

    def test_kortilla_tarpeeksi_rahaa_lounas_edullinen(self):

        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

      
    def test_kortilla_tarpeeksi_rahaa_lounas_maukas(self):

        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_ei_tarpeeksi_rahaa_edullinen(self):

        for i in range(5):
            self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo, 40)

      
    def test_kortilla_ei_tarpeeksi_rahaa_maukas(self):

        for i in range(3):
            self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo, 200)

    def test_kortilla_ei_tarpeeksi_rahaa_lounas_edullinen(self):

        for i in range(5):
            self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.edulliset, 4)

      
    def test_kortilla_ei_tarpeeksi_rahaa_lounas_maukas(self):

        for i in range(3):
            self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.maukkaat, 2)

    def test_kortilla_ei_tarpeeksi_rahaa_false_edullinen(self):

        for i in range(5):
            vastaus = self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(vastaus, False)

      
    def test_kortilla_ei_tarpeeksi_rahaa_false_maukas(self):

        for i in range(3):
            vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(vastaus, False)


    def test_kassan_raha_ei_muutu_kortilla_ostaessa(self):

        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_kortti_ladaus_kortin_saldo_muttuu(self):

        self.kassapaate.lataa_rahaa_kortille(self.kortti, 2000)

        self.assertEqual(self.kortti.saldo, 3000)

    def test_kortti_ladaus_kassan_raha_muttuu(self):

        self.kassapaate.lataa_rahaa_kortille(self.kortti, 2000)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 102000)


    def test_kortti_ladaus_negatiivinen_summa_saldo_ei_muutu(self):

        vastaus = self.kassapaate.lataa_rahaa_kortille(self.kortti, -500)

        self.assertEqual(vastaus, None)

    def test_kortti_ladaus_negatiivinen_summa_kassa_ei_muutu(self):

        vastaus = self.kassapaate.lataa_rahaa_kortille(self.kortti, -500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)