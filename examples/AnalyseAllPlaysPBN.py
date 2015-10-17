#! /usr/bin/python

import hands
import functions
import dds
import ctypes

bo = dds.boardsPBN()
DDplays = dds.playTracesPBN()
solved = dds.solvedPlays()

chunkSize = 1

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

	bo.deals[handno].remainCards = hands.PBN[handno]

	DDplays.plays[handno].number = hands.playNo[handno]
	DDplays.plays[handno].cards = hands.play[handno]

res = dds.AnalyseAllPlaysPBN(ctypes.pointer(bo), ctypes.pointer(DDplays), ctypes.pointer(solved), chunkSize)

line = ctypes.create_string_buffer(80)
if res != dds.RETURN_NO_FAULT:
	dds.ErrorMessage(res, line)
	print("DDS error: {}".format(line.value.decode("utf-8")))

for handno in range(3):
	match = functions.ComparePlay(ctypes.pointer(solved.solved[handno]), handno)

	line = "AnalyseAllPlaysPBN, hand {}, {}".format(
		handno + 1,
		"OK" if match else "ERROR")

	functions.PrintPBNHand(line, bo.deals[handno].remainCards)

	functions.PrintPBNPlay(ctypes.pointer(DDplays.plays[handno]), ctypes.pointer(solved.solved[handno]))
