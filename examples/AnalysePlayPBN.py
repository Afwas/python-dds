import dds
import ctypes
import hands
import functions

dlPBN = dds.dealPBN()
DDplayPBN = dds.playTracePBN()
solved = dds.solvedPlay()

line = ctypes.create_string_buffer(80);

threadIndex = 0

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

#    print(myDlPBN.remainCards)

    DDplayPBN.number = hands.playNo[handno]
    DDplayPBN.cards = hands.play[handno]

    res = dds.AnalysePlayPBN(
        dlPBN,
        DDplayPBN,
        ctypes.pointer(solved),
        threadIndex)

    if res != dds.RETURN_NO_FAULT:
        dds.ErrorMessage(res, line)
        print("DDS error: {}\n".format(line.value.decode("utf-8")))

    match = functions.ComparePlay(ctypes.pointer(solved), handno)

    line = "AnalysePlayPBNBin, hand {}: {}".format(
        handno + 1,
        "OK" if match else "ERROR")

    functions.PrintPBNHand(line, dlPBN.remainCards)

    functions.PrintPBNPlay(ctypes.pointer(DDplayPBN), ctypes.pointer(solved))
