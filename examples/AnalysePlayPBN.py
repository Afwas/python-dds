import dds
import ctypes
import hands
import functions

dlPBN = dds.dealPBN()
myDlPBN = dlPBN
DDplayPBN = dds.playTracePBN()
myDDplayPBN = DDplayPBN
solved = dds.solvedPlay()
mySolved = ctypes.pointer(solved)

threadIndex = 0

for handno in range(3):
    myDlPBN.trump = hands.trump[handno]
    myDlPBN.first = hands.first[handno]

    myDlPBN.currentTrickSuit[0] = 0
    myDlPBN.currentTrickSuit[1] = 0
    myDlPBN.currentTrickSuit[2] = 0

    myDlPBN.currentTrickRank[0] = 0
    myDlPBN.currentTrickRank[1] = 0
    myDlPBN.currentTrickRank[2] = 0

    myDlPBN.remainCards = hands.PBN[handno]

    print(myDlPBN.remainCards)

    myDDplayPBN.number = hands.playNo[handno]
    myDDplayPBN.cards = hands.play[handno]

    res = dds.AnalysePlayPBN(myDlPBN, myDDplayPBN, mySolved, threadIndex)

    if res != dds.RETURN_NO_FAULT:
        dds.ErrorMessage(res, line)
        print("DDS error: {}\n".format(line))

    match = functions.ComparePlay(mySolved, handno)

    print("AnalysePlayPBNBin, hand {}: {}\n".format(handno + 1, \
        "OK" if match else "ERROR"))


    functions.PrintPBNHand(b'' * 80, myDlPBN.remainCards + b'' * 20)

    functions.PrintPBNPlay(ctypes.pointer(myDDplayPBN), solved)
