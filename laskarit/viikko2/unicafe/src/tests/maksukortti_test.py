import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_saldo_alussa(self):

        self.assertNotEqual(str(self.maksukortti), "saldo: 10")

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)