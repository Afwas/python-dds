import unittest
from board import PBN
from board import Hand

class PBNTest(unittest.TestCase):
	def setUp(self):
		# print(dir(PBN))
		self.testPBN = PBN.PBN("[N:.63.AKQ987.A9732 A8654.KQ5.T.QJT6 J973.J98742.3.K4 KQT2.AT.J6542.85]")

	def test_clean_pbn(self):
		self.assertEqual(len(self.testPBN.get_cards()), 67)

	def test_dealer(self):
		self.assertEqual(self.testPBN.get_dealer(), 'N')

	def test_hand_enum(self):
		self.assertEqual(Hand.Hand.north, 0)
		self.assertEqual(Hand.Hand.west, 3)

	def test_hands(self):
		self.assertEqual(self.testPBN.get_hand(Hand.Hand.north), ".63.AKQ987.A9732")
		self.assertEqual(self.testPBN.get_hand(Hand.Hand.east), "A8654.KQ5.T.QJT6")
		self.assertEqual(self.testPBN.get_hand(Hand.Hand.south), "J973.J98742.3.K4")
		self.assertEqual(self.testPBN.get_hand(Hand.Hand.west), "KQT2.AT.J6542.85")

if __name__== "__main__":
	unittest.main()
