#! /usr/bin/python

import dds
import ctypes
import hands
import functions

dlPBN = dds.dealPBN()
fut2 = dds.futureTricks()
fut3 = dds.futureTricks()

threadIndex = 0
line = ctypes.create_string_buffer(80)

dds.SetMaxThreads(0)

for handno in range(3):
    dlPBN.trump = hands.trump[handno]
    dlPBN.first = hands.first[handno]

    dlPBN.currentTrickSuit[0] = 0
    dlPBN.currentTrickSuit[1] = 0
    dlPBN.currentTrickSuit[2] = 0

    dlPBN.currentTrickRank[0] = 0
    dlPBN.currentTrickRank[1] = 0
    dlPBN.currentTrickRank[2] = 0

    dlPBN.remainCards = hands.PBN[handno]

    target = -1
    solutions = 3
    mode = 0
    res = dds.SolveBoardPBN(
        dlPBN,
        target,
        solutions,
        mode,
        ctypes.pointer(fut3),
        0)

    if res != dds.RETURN_NO_FAULT:
        dds.ErrorMessage(res, line)
        print("DDS error {}".format(line.value.decode("utf-8")))

    match3 = functions.CompareFut(
        ctypes.pointer(fut3),
        handno,
        solutions)

    solutions = 2
    res = dds.SolveBoardPBN(
        dlPBN,
        target,
        solutions,
        mode,
        ctypes.pointer(fut2),
        0)
    if res != dds.RETURN_NO_FAULT:
        dds.ErrorMessage(res, line)
        print("DDS error {}".foramt(line.value.decode("utf-8")))

    match2= functions.CompareFut(
        ctypes.pointer(fut2),
        handno,
        solutions)

    line = "SolveBoardPBN, hand {}: solutions 3 {}, solutions 2{}".format(
        handno + 1,
        "OK" if match3 else "ERROR",
        "OK" if match2 else "ERROR")

    functions.PrintPBNHand(line, dlPBN.remainCards)

    line = "solutions == 3"
    functions.PrintFut(line, ctypes.pointer(fut3))
    line = "solutions == 2"
    functions.PrintFut(line, ctypes.pointer(fut2))


