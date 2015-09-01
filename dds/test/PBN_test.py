import unittest
from board import PBN

class PBNTest(unittest.TestCase):
	def setUp(self):
		# print(dir(PBN))
		self.testPBN = PBN.PBN("[N:.63.AKQ987.A9732 A8654.KQ5.T.QJT6 J973.J98742.3.K4 KQT2.AT.J6542.85]")

	def test_dealer(self):
		self.assertEqual(self.testPBN.getDealer(), 'N')

if __name__== "__main__":
	unittest.main()
