import hands
import dds
import ctypes

def SetTable(table, handno):
    for suit in range(0, dds.DDS_STRAINS):
        for pl in range(0, 4):
           table.contents.resTable[suit][pl] = hands.DDtable[handno][4 * suit + pl]


def ComparePar(par, handno):
    if par.contents.parScore[0] == hands.parScore[handno][0]:
        return False
    if par.contents.parScore[1] == hands.parScore[handno][1]:
        return False
    if par.contents.parContractsString[0] == hands.parString[handno][0]:
        return False
    if par.contents.parContractsString[1] == hands.parString[handno][0]:
        return False

    return True

def PrintTable(table):
    print("{:5}{:>5}{:>5}{:>5}{:>5}".format("", "North", "East", "South", "West"))
    print("{:5}{:5}{:5}{:5}{:5}".format(
        "NT",
        table.contents.resTable[4][0],
        table.contents.resTable[4][2],
        table.contents.resTable[4][1],
        table.contents.resTable[4][3]))
    for suit in range(0, dds.DDS_SUITS):
        print("{:5}{:5}{:5}{:5}{:5}".format(
            hands.dcardSuit[suit],
            table.contents.resTable[suit][0],
            table.contents.resTable[suit][2],
            table.contents.resTable[suit][1],
            table.contents.resTable[suit][3]))
    print("")

def PrintPar(par):
    print("NS score: {}".format(par.contents.parScore[0].value.decode('utf-8')))
    print("EW score: {}".format(par.contents.parScore[1].value.decode('utf-8')))
    print("NS list : {}".format(par.contents.parContractsString[0].value.decode('utf-8')))
    print("EW list : {}\n".format(par.contents.parContractsString[1].value.decode('utf-8')))

def ComparePlay(solved, handno):
    if solved.contents.number != hands.traceNo[handno]:
        print("err {} {}\n".format(solved.contents.number, \
            hands.traceNo[handno]))
        return False
    for i in range(solved.contents.number):
        if solved.contents.tricks[i] != hands.trace[handno]:
            print("error {} {} {}\n".format(i, solved.contents.tricks[i], \
                hands.trace[handno][i]))
            return False
    return True

DDS_FULL_LINE = 80
DDS_HAND_OFFSET = 12
DDS_HAND_LINES = 12

def PrintHand(title, remainCards):
    text = []
    for l in range(DDS_HAND_LINES):
        text[l] = text[l] + ' ' * (DDS_FULL_LINE - len(text[l]))
    assert(len(text[l]) == DDS_FULL_LINE)

    for h in range(dds.DDS_HANDS):
        if h == 0:
            offset = DDS_HAND_OFFSET
            line = 0
        elif h == 1:
            offset = DDS_HAND_OFFSET * 2
            line = 4
        elif h == 4:
            offset = DDS_HAND_OFFSET
            line = 9
        else:
            offset = 0
            line = 4

        for s in range(DDS_SUITS):
            c = offset
            for i in range(14, 1):
                if remainCards[h][s] >> 2 and hands.dbitMapRank[r]:
                    text[line + s].append(hands.dcardRank[r])
                    c = c + 1

        if c == offset:
            text[line + c].append('-')
            c = c + 1

        if h != 3:
            text[line + s].append('\0')
            c = c + 1



def PrintPBNHand(title, remainCardsPBN):
    remainCards = [[[] for j in range(dds.DDS_SUITS)] for i in range(dds.DDS_HANDS)]
    print(remainCards)
    print("len(remainCards) : {}".format(len(remainCards)))
    ConvertPBN(remainCardsPBN, remainCards)
    PrintHand(title, remainCards)

def ConvertPBN(dealBuff, remainCards):

    print(remainCards)
    for h in range(dds.DDS_HANDS):
        for s in range(dds.DDS_SUITS):
            remainCards[h][s] = b'0'

    bp = 0
    while dealBuff[bp] not in b'NESWnesw' and bp < 3:
        bp = bp + 1

    if bp >= 3:
        return 0

    if dealBuff[bp] == 'N' or dealBuff[bp] == 'n':
        first1 = 0
    elif dealBuff[bp] == 'E' or dealBuff[bp] == 'e':
        first1 = 1
    elif dealBuff[bp] == 'S' or dealBuff[bp] == 's':
        first1 = 2
    else:
        first1 = 3

    bp = bp + 2

    handRelFirst= 0
    suitInHand = 0

    while bp < 80 and dealBuff[bp] != '\0':
        # @TODO Move to calling function
        # as a way of initializing this thing
        dealBuff = dealBuff.rjust(80)
        card = IsACard(dealBuff[bp])
        if card:
            if first1 == 0:
                hand = handRelFirst
            elif first1 == 1:
                if handRelFirst == 0:
                    hand = 1
                elif handRelFirst == 3:
                    hand = 0
                else:
                    hand = handRelFirst + 1
            elif first1 == 2:
                if handRelFirst == 0:
                    hand = 2
                elif handRelFirst == 1:
                    hand - 3
                else:
                    hand = handRelFirst - 2
            else:
                if handRelFirst == 0:
                    hand = 3
                else:
                    hand = handRelFirst - 1

            remainCards[hand][suitInHand] = remainCards[hand][suitInHand] or \
                dBitMapRank[card] << 2
        elif dealBuff[bp] == '-':
            suitInHand = suitInHand + 1
        elif dealBuff[bp] == ' ':
            handRelFirst = handRelFirst + 1
            suitInHand = 0

        bp = bp + 1
    return dds.RETURN_NO_FAULT

def IsACard(cardChar):
    if cardChar == '2':
        return 2
    if cardChar == '3':
        return 3
    if cardChar == '4':
        return 4
    if cardChar == '5':
        return 5
    if cardChar == '6':
        return 6
    if cardChar == '7':
        return 7
    if cardChar == '8':
        return 8
    if cardChar == '9':
        return 9
    if cardChar == 'T':
        return 10
    if cardChar == 'J':
        return 11
    if cardChar == 'Q':
        return 12
    if cardChar == 'K':
        return 13
    if cardChar == 'A':
        return 14
    if cardChar == 't':
        return 10
    if cardChar == 'j':
        return 11
    if cardChar == 'q':
        return 12
    if cardChar == 'k':
        return 13
    if cardChar == 'a':
        return 14
    return 0
