#! /usr/bin/python

import dds
import ctypes
import hands
import functions

bo = dds.boardsPBN()
solved = dds.solvedBoards()

line = ctypes.create_string_buffer(80)

dds.SetMaxThreads(0)

bo.noOfBoards = 3

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

    bo.target[handno] = -1
    bo.solutions[handno] = 3
    bo.mode[handno] = 0

res = dds.SolveAllBoards(
    ctypes.pointer(bo),
    ctypes.pointer(solved))

if res != dds.RETURN_NO_FAULT:
    dds.ErrorMessage(res, line)
    print("DDS error {}".format(line.value.decode("utf-8")))

for handno in range(3):
    match = functions.CompareFut(
        ctypes.pointer(solved.solvedBoards[handno]),
        handno,
        3)

    line = "SolveAllBoards, hand {}: solutions 3 {}".format(
        handno + 1,
        "OK" if match else "ERROR")
    
    functions.PrintPBNHand(line, bo.deals[handno].remainCards)

    functions.PrintFut(line, ctypes.pointer(solved.solvedBoards[handno]))
