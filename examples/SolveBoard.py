#! /usr/bin/python

import dds
import hands
import functions
import ctypes

dl = dds.deal()
fut2 = dds.futureTricks()
fut3 = dds.futureTricks()

threadIndex = 0
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

        ###
        # target: Either a number <= 13 or 0 or -1: The 'target' number of tricks to make
        # solutions: 1 - 3: 1 means return 1 solution, 
        #   2 means return all maximum solutions, 3 means all solutions
        # mode: 0 or 1. Just for internal use. 0 is fine here.
        ###
	target = -1 # No target; find all results
	solutions = 3 # Return all solutions
	mode = 0 # The way dds internally handles the last trick
	res = dds.SolveBoard(dl, target, solutions, mode, ctypes.pointer(fut3), threadIndex)

	if res != dds.RETURN_NO_FAULT:
		dds.ErrorMessage(res, line)
		print("DDS error: {}".format(line.value.decode("utf-8")))

	match3 = functions.CompareFut(ctypes.pointer(fut3), handno, solutions)

	solutions = 2 # Return only the optmial solutions
	res = dds.SolveBoard(dl, target, solutions, mode, ctypes.pointer(fut2), threadIndex)
	if res != dds.RETURN_NO_FAULT:
		dds.ErrorMessage(res, line)
		print("DDS error: {}".format(line.value.decode("utf-8")))

	match2 = functions.CompareFut(ctypes.pointer(fut2), handno, solutions)

	line = "SolveBoard, hand {}: solutions 3 {}, solutions 2 {}".format( \
		handno + 1, "OK" if match3 else "ERROR", "OK" if match2 else "ERROR")

	functions.PrintHand(line, dl.remainCards)

	line = "solutions == 3"
	functions.PrintFut(line, ctypes.pointer(fut3))
	line = "solutions == 2"
	functions.PrintFut(line, ctypes.pointer(fut2))
