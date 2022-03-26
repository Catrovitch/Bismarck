import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_saldo_alussa(self):

        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_rahan_lataaminen(self):

        self.maksukortti.lataa_rahaa(5)


        self.assertEqual(str(self.maksukortti), "saldo: 0.15")

    def test_rahan_ottaminen_vahenee_oikein(self):

        self.maksukortti.ota_rahaa(5)

        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_rahan_ottaminen_ei_vahenee__rahaa_ei_ole_tarpeeksi(self):

        self.maksukortti.ota_rahaa(15)

        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_ottaminen_true(self):

        self.assertEqual(self.maksukortti.ota_rahaa(5), True)

    def test_rahan_ottaminen_false(self):

        self.assertEqual(self.maksukortti.ota_rahaa(15), False)
        
        