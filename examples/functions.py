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
    print("EW list : {}".format(par.contents.parContractsString[1].value.decode('utf-8')))
    print("")
