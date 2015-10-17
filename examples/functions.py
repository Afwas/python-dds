import hands
import dds
import ctypes

def PrintFut(title, fut):
    print("{}\n".format(title))

    print("{:6s} {:<6s} {:<6s} {:<6s} {:<6s}".format( \
        "card", "suit", "rank", "equals", "score"))

    for i in range(fut.contents.cards):
        res = ctypes.create_string_buffer(15)
        equals_to_string(fut.contents.equals[i], res)
        print("{:6} {:<6s} {:<6s} {:<6s} {:<6}".format( \
            i, \
            hands.dcardSuit[fut.contents.suit[i]], \
            hands.dcardRank[fut.contents.rank[i]], \
            res.value.decode("utf-8"), \
            fut.contents.score[i]))
    print()

def equals_to_string(equals, res):
    p = 0
    m = equals >> 2
    for i in range(15, 1, -1):
        if m & int(hands.dbitMapRank[i]):
            res[p] = bytes(hands.dcardRank[i], "ascii")
            p = p + 1
    res[p] = 0

def CompareFut(fut, handno, solutions):
    if solutions == 2:
        if fut.contents.cards != hands.cardsSoln2[handno]:
            return False
    elif fut.contents.cards != hands.cardsSoln3[handno]:
        return False

    for i in range(fut.contents.cards):
        if fut.contents.suit[i] != hands.cardsSuits[handno][i]:
            return False
        if fut.contents.rank[i] != hands.cardsRanks[handno][i]:
            return False
        if fut.contents.equals[i] != hands.cardsEquals[handno][i]:
            return False
        if fut.contents.score[i] != hands.cardsScores[handno][i]:
            return False
    return True

def SetTable(table, handno):
    for suit in range(0, dds.DDS_STRAINS):
        for pl in range(0, 4):
           table.contents.resTable[suit][pl] = hands.DDtable[handno][4 * suit + pl]

def CompareTable(table, handno):
    for suit in range(dds.DDS_STRAINS):
        for pl in range(4):
            if table.contents.resTable[suit][pl] != hands.DDtable[handno][4 * suit + pl]:
                return False
    return True

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
    print("{:5} {:<5} {:<5} {:<5} {:<5}".format("", "North", "South", "East", "West"))
    print("{:>5} {:5} {:5} {:5} {:5}".format(
        "NT",
        table.contents.resTable[4][0],
        table.contents.resTable[4][2],
        table.contents.resTable[4][1],
        table.contents.resTable[4][3]))
    for suit in range(0, dds.DDS_SUITS):
        print("{:>5} {:5} {:5} {:5} {:5}".format(
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
        if solved.contents.tricks[i] != hands.trace[handno][i]:
            print("error  {} {} {}\n".format(i, solved.contents.tricks[i], \
                hands.trace[handno][i]))
            return False
    return True

def PrintBinPlay(playp, solved):
    print("Number : {}".format(solved.contents.number))

    print("Play {:2}: {} {}".format(
        0, "--", solved.contents.tricks[0]))

    for i in range(solved.contents.number):
        print("Play {:2}: {}{} {}".format(
            i,
            hands.dcardSuit[playp.contents.suit[i - 1]],
            hands.dcardRank[playp.contents.rank[i - 1]],
            solved.contents.tricks[i]))

def PrintPBNPlay(playp, solved):
    print("Number : {}".format(solved.contents.number))

    print("Play {:2d}: {} {}".format(0, "--", solved.contents.tricks[0]))

    for i in range(1, solved.contents.number):
        print("Play {:2d}: {}{} {:2d}".format(i, chr(playp.contents.cards[2 * (i - 1)]), \
            chr(playp.contents.cards[2 * i - 1]), solved.contents.tricks[i]))
    print()

DDS_FULL_LINE = 80
DDS_HAND_OFFSET = 12
DDS_HAND_LINES = 12

def PrintHand(title, remainCards):
    text = []
    blankLine =  b''
    blankLine = blankLine.ljust(80)
    for l in range(DDS_HAND_LINES):
        text.append(bytearray(blankLine))

    for h in range(dds.DDS_HANDS):
        if h == 0:
            offset = DDS_HAND_OFFSET
            line = 0
        elif h == 1:
            offset = DDS_HAND_OFFSET * 2
            line = 4
        elif h == 2:
            offset = DDS_HAND_OFFSET
            line = 8
        else:
            offset = 0
            line = 4

        for s in range(dds.DDS_SUITS):
            c = offset
            for r in range(14, 1, -1):
                if (int(remainCards[h][s]) >> 2) & hands.dbitMapRank[r]:
                    text[line + s][c] = ord(hands.dcardRank[r])
                    c = c + 1

        if c == offset:
            text[line + s][c] = ord('-')
            c = c + 1

        if h != 3:
            text[line + s][c] = ord('\0')
            c = c + 1

    # Print it
    print("{}".format(title))
    dashes = bytearray('', "utf-8")
    dashes = dashes.ljust(80)
    l = len(title)
    for i in range(l):
        dashes[i] = ord('-')
    print("{}".format(dashes.decode("utf-8")))
    for i in range(DDS_HAND_LINES):
        print("{}".format(text[i].decode("utf-8")))
    print("\n")



def PrintPBNHand(title, remainCardsPBN):
    remainCards = [[[] for j in range(dds.DDS_SUITS)] for i in range(dds.DDS_HANDS)]
    ConvertPBN(remainCardsPBN, remainCards)
    PrintHand(title, remainCards)

def ConvertPBN(dealBuff, remainCards):
    for h in range(dds.DDS_HANDS):
        for s in range(dds.DDS_SUITS):
            remainCards[h][s] = b'0'

    bp = 0
    while dealBuff[bp] not in b'NESWnesw' and bp < 3:
        bp = bp + 1

    if bp >= 3:
        # NESW not fount in first characters of PBN string
        return 0

    # dealBuff[bp] now in "NESWnesw" 
    if chr(dealBuff[bp]) == 'N' or chr(dealBuff[bp]) == 'n':
        first1 = 0
    elif chr(dealBuff[bp]) == 'E' or chr(dealBuff[bp]) == 'e':
        first1 = 1
    elif chr(dealBuff[bp]) == 'S' or chr(dealBuff[bp]) == 's':
        first1 = 2
    else:
        first1 = 3

    # Skip ":" in PBN string
    bp = bp + 2

    # bp pointer now at start of first card
    handRelFirst= 0
    suitInHand = 0
    # @TODO Move to calling function
    # as a way of initializing this thing
    dealBuff = dealBuff.ljust(80)

    while bp < 80 and dealBuff[bp] != b'\0':
        card = IsACard(chr(dealBuff[bp]))
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
                    hand = 3
                else:
                    hand = handRelFirst - 2
            else:
                if handRelFirst == 0:
                    hand = 3
                else:
                    hand = handRelFirst - 1
            remainCards[hand][suitInHand] = int(remainCards[hand][suitInHand]) | (hands.dbitMapRank[card] << 2)
        elif chr(dealBuff[bp]) == '.':
            suitInHand = suitInHand + 1
        elif chr(dealBuff[bp]) == ' ':
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
