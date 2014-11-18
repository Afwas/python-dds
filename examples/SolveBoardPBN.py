#! /usr/bin/python

import dds
import ctypes

"""In this first example I will solve a PBN hand with SolveBoardPBN"""

# Trump = 4 -> No trump
# Hand = 3 -> West to lead which means South is declarer
# We can specify up to three cards already played in the current trick
# Suit of played cards this trick -> No cards have been played so far
# Rank of played cards this trick -> No cards have been played so far
# PBN: The deal to be examined
sarr = [0, 0, 0]
suitArr = (ctypes.c_int * 3)(*sarr)
rarr = [0, 0, 0]
rankArr = (ctypes.c_int * 3)(*rarr)
myPBN = b"W:T5.K4.652.A98542 K6.QJT976.QT7.Q6 432.A.AKJ93.JT73 AQJ987.8532.84.K"
"""trump (0 = S, 1 = H, 2 = D, 3 = C, NT = 4)
hand to lead (N = 0, E = 1, S = 2, W = 3),
played cards (suit) in this trick
played cards (rank) in this trick
PBN"""
deal = dds.dealPBN(4, 3, suitArr, rankArr, myPBN)

# Placeholder for the results
future = dds.futureTricks()
print(future)
myfut = ctypes.pointer(dds.futureTricks())
print(myfut)
res = dds.SolveBoardPBN(deal, -1, 1, 1, myfut, 0)
print(myfut)
print(res)
#'cards', 'equals', 'nodes', 'rank', 'score', 'suit'
print("nodes  ", myfut.contents.nodes)
print("cards  ", myfut.contents.cards)
print("suit   ", list(myfut.contents.suit))
print("rank   ", list(myfut.contents.rank))
print("equals ", list(myfut.contents.equals))
print("score  ", list(myfut.contents.score))
