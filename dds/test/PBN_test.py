import unittest
from board import PBN

class PBNTest(unittest.TestCase):
	def setUp(self):
		# print(dir(PBN))
		self.testPBN = PBN.PBN("[N:.63.AKQ987.A9732 A8654.KQ5.T.QJT6 J973.J98742.3.K4 KQT2.AT.J6542.85]")

	def test_clean_pbn(self):
		self.assertEqual(len(self.testPBN.get_cards()), 67)

	def test_dealer(self):
		self.assertEqual(self.testPBN.get_dealer(), 'N')

	def test_hands(self):
		self.assertEqual(self.testPBN.get_hand(0), ".63.AKQ987.A9732")
		self.assertEqual(self.testPBN.get_hand(1), "A8654.KQ5.T.QJT6")
		self.assertEqual(self.testPBN.get_hand(2), "J973.J98742.3.K4")
		self.assertEqual(self.testPBN.get_hand(3), "KQT2.AT.J6542.85")

if __name__== "__main__":
	unittest.main()
