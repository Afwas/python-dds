import dds
import ctypes
import hands
import functions

dl = dds.deal()
DDplay = dds.playTraceBin()
solved = dds.solvedPlay()

line = ctypes.create_string_buffer(80)

threadIndex = 0

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

    DDplay.number = hands.playNo[handno]

    for i in range(hands.playNo[handno]):
        DDplay.suit[i] = hands.playSuit[handno][i]
        DDplay.rank[i] = hands.playRank[handno][i]

    res = dds.AnalysePlayBin(dl, DDplay, ctypes.pointer(solved), threadIndex)

    if res != dds.RETURN_NO_FAULT:
        dds.ErrorMessage(res, line)
        print("DDS error: {}\n".format(line.value.decode("utf-8")))

    match = functions.ComparePlay(ctypes.pointer(solved), handno)

    line = "AnalysePlayPBNBin, hand {}: {}".format(handno + 1, \
        "OK" if match else "ERROR")

    functions.PrintHand(line, dl.remainCards)

    functions.PrintBinPlay(ctypes.pointer(DDplay), ctypes.pointer(solved))
