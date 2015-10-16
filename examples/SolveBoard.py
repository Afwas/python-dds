#! /usr/bin/python

import dds
import hands
import functions
import ctypes

dl = dds.deal()
fut2 = dds.futureTricks()
myFut2 = ctypes.pointer(fut2)
fut3 = dds.futureTricks()
myFut3 = ctypes.pointer(fut3)

threadIndex = 0
#line = " " * 80
#myLine = ctypes.pointer(line)
line = ctypes.create_string_buffer(80)

dds.SetMaxThreads(0)

for handno in range(3):
	dl.trump = hands.trump[handno]
	dl.first = hands.first[handno]

	dl.currentTrickSuit[0] = 0
	dl.currentTrickSuit[1] = 0
	dl.currentTrickSuit[2] = 0

	dl.currentTrickRank[0] = 0
	dl.currentTrickRank[1] = 0
	dl.currentTrickRank[2] = 0

	for h in range(dds.DDS_HANDS):
		for s in range(dds.DDS_SUITS):
			dl.remainCards[h][s] = hands.holdings[handno][s][h]

	target = -1 # No target; find maximum results
	solutions = 3 # Return 3 solutions
	mode = 0
	res = dds.SolveBoard(dl, target, solutions, mode, myFut3, threadIndex)

	if res != dds.RETURN_NO_FAULT:
		dds.ErrorMessage(res, line)
		print("DDS error: {}".format(line.value.decode("utf-8")))

	match3 = functions.CompareFut(myFut3, handno, solutions)

	solutions = 2
	res = dds.SolveBoard(dl, target, solutions, mode, myFut2, threadIndex)
	if res != dds.RETURN_NO_FAULT:
		dds.ErrorMessage(res, line)
		print("DDS error: {}".format(line.value.decode("utf-8")))

	match2 = functions.CompareFut(myFut2, handno, solutions)

	line = "SolveBoard, hand {}: solutions 3 {}, solutions 2 {}".format( \
		handno + 1, "OK" if match3 else "ERROR", "OK" if match2 else "ERROR")

	functions.PrintHand(line, dl.remainCards)

	line = "solutions == 3"
	functions.PrintFut(line, myFut3)
	line = "solutions == 2"
	functions.PrintFut(line, myFut2)