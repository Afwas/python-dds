#! /usr/bin/python

import hands
import functions
import dds
import ctypes

bo = dds.boards()
DDplays = dds.playTracesBin()
solved = dds.solvedPlays()

chunkSize = 1
line = ctypes.create_string_buffer(80)

dds.SetMaxThreads(0)

bo.noOfBoards = 3
DDplays.noOfBoards = 3

for handno in range(3):
	bo.deals[handno].trump = hands.trump[handno]
	bo.deals[handno].first = hands.first[handno]

	bo.deals[handno].currentTrickSuit[0] = 0
	bo.deals[handno].currentTrickSuit[1] = 0
	bo.deals[handno].currentTrickSuit[2] = 0

	bo.deals[handno].currentTrickRank[0] = 0
	bo.deals[handno].currentTrickRank[1] = 0
	bo.deals[handno].currentTrickRank[2] = 0

	for h in range(dds.DDS_HANDS):
		for s in range(dds.DDS_SUITS):
			bo.deals[handno].remainCards[h][s] = hands.holdings[handno][s][h]

	DDplays.plays[handno].number = hands.playNo[handno]

	for i in range(hands.playNo[handno]):
		DDplays.plays[handno].suit[i] = hands.playSuit[handno][i]
		DDplays.plays[handno].rank[i] = hands.playRank[handno][i]

res = dds.AnalyseAllPlaysBin(ctypes.pointer(bo), ctypes.pointer(DDplays), ctypes.pointer(solved), chunkSize)

if res != dds.RETURN_NO_FAULT:
	dds.ErrorMessage(res, line)
	print("DDS error: {}".format(line.decode("utf-8")))

for handno in range(3):
	match = functions.ComparePlay(ctypes.pointer(solved.solved[handno]), handno)

	line = "AnalyseAllPlaysBin, hand {}: {}".format(
		handno + 1,
		"OK" if match else "ERROR")

	functions.PrintHand(line, bo.deals[handno].remainCards)

	functions.PrintBinPlay(ctypes.pointer(DDplays.plays[handno]), ctypes.pointer(solved.solved[handno]))