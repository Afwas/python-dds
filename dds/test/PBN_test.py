import unittest
from board import PBN
from board import Hand

class PBNTest(unittest.TestCase):
	def setUp(self):
		# print(dir(PBN))
		self.testPBN = PBN.PBN("[N:.63.AKQ987.A9732 A8654.KQ5.T.QJT6 J973.J98742.3.K4 KQT2.AT.J6542.85]")
		self.testPBN_east = PBN.PBN("[E:A8654.KQ5.T.QJT6 J973.J98742.3.K4 KQT2.AT.J6542.85 .63.AKQ987.A9732]")
		self.testPBN_south = PBN.PBN("[S:J973.J98742.3.K4 KQT2.AT.J6542.85 .63.AKQ987.A9732 A8654.KQ5.T.QJT6]")
		self.testPBN_west = PBN.PBN("[W:KQT2.AT.J6542.85 .63.AKQ987.A9732 A8654.KQ5.T.QJT6 J973.J98742.3.K4]")

	def test_clean_pbn(self):
		self.assertEqual(len(self.testPBN.get_cards()), 67)

	def test_dealer(self):
		self.assertEqual(self.testPBN.get_dealer(), 'N')

	def test_hand_enum(self):
		self.assertEqual(Hand.Hand.north, 0)
		self.assertEqual(Hand.Hand.west, 3)

	def test_hand(self):
		self.assertEqual(Hand.Hand.north, 0)
		self.assertEqual(Hand.Hand.east, 1)
		self.assertEqual(Hand.Hand.south, 2)
		self.assertEqual(Hand.Hand.west, 3)

	def test_hands(self):
		self.assertEqual(self.testPBN.get_hand(Hand.Hand.north), ".63.AKQ987.A9732")
		self.assertEqual(self.testPBN.get_hand(Hand.Hand.east), "A8654.KQ5.T.QJT6")
		self.assertEqual(self.testPBN.get_hand(Hand.Hand.south), "J973.J98742.3.K4")
		self.assertEqual(self.testPBN.get_hand(Hand.Hand.west), "KQT2.AT.J6542.85")

	def test_not_north_as_dealer(self):
		self.assertEqual(self.testPBN.get_hand(Hand.Hand.east), self.testPBN_east.get_hand(Hand.Hand.east))
		self.assertEqual(self.testPBN.get_hand(Hand.Hand.south), self.testPBN_south.get_hand(Hand.Hand.south))
		self.assertEqual(self.testPBN.get_hand(Hand.Hand.west), self.testPBN_west.get_hand(Hand.Hand.west))

if __name__== "__main__":
	unittest.main()
