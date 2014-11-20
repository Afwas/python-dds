#! /usr/bin/python

import dds
import ctypes

def showBoard(PBN):
    PBN = PBN.decode('utf-8')
    dealer = PBN[0]
    first = PBN[2:18]
    second = PBN[19:35]
    third = PBN[36:52]
    fourth = PBN[53:69]
    print(dealer)
    print(first)
    print(second)
    print(third)
    print(fourth)
    if dealer == 'N':
        first = first.split('.')
        second = second.split('.')
        third = third.split('.')
        fourth = fourth.split('.')
    if dealer == 'E':
        temp = first.split('.')
        first = fourth.split('.')
        fourth = third.split('.')
        third = second.split('.')
        second = temp
    if dealer == 'S':
        temp = first.split('.')
        first = third.split('.')
        third = temp
        temp = second.split('.')
        second = fourth.split('.')
        fourth = temp
    if dealer == 'W':
        temp = first.split('.')
        first = second.split('.')
        second = third.split('.')
        third = fourth.split('.')
        fourth = temp
    print(first)
    print("\t\t" + first[0])
    print("\t\t" + first[1])
    print("\t\t" + first[2])
    print("\t\t" + first[3])
    print("\t" + fourth[0] + "\t\t" + second[0])
    print("\t" + fourth[1] + "\t\t" + second[1])
    print("\t" + fourth[2] + "\t\t" + second[2])
    print("\t" + fourth[3] + "\t\t" + second[3])
    print("\t\t" + third[0])
    print("\t\t" + third[1])
    print("\t\t" + third[2])
    print("\t\t" + third[3])    

"""In this first example I will solve a PBN hand with SolveBoardPBN"""

# PBN: The deal to be examined
PBN = b"N:Q4.J8.K852.87654 K986.T2.Q976.JT9 J53.A7643.A3.AK3 AT72.KQ95.JT4.Q2"
print(PBN)
showBoard(PBN)
#myPBN = ctypes.c_char_p(ctypes.pointer(PBN))
#myPBN.value = PBN
deal = dds.ddTableDealPBN(PBN)

tableRes = dds.ddTableResults()
"""for i in range(5):
    for j in range(4):
        print(i, ", ", j, ".")
        tableRes.resTable[i][j] = 0"""
# Alternatively create one with 
# myPythonList - [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
# ((c_int * 4) * 5)(*myPythonList)
myTableRes = ctypes.pointer(tableRes)

"""print("*** Before")
for i in range(len(list(myTableRes.contents.resTable))):
    for j in range(len(list(myTableRes.contents.resTable)[i])):
        print("["+str(i)+"]["+str(j)+"] = "+str(list(myTableRes.contents.resTable)[i][j]))
"""
res = dds.CalcDDtablePBN(deal, myTableRes)

print("res ", res)

print("*** After")
for i in range(len(list(myTableRes.contents.resTable))):
    for j in range(len(list(myTableRes.contents.resTable)[i])):
        print("["+str(i)+"]["+str(j)+"] = "+str(list(myTableRes.contents.resTable)[i][j]))

print("Calculating Par")
"""vulnerable:
    0: None
    1: Both
    2: NS only
    3: EW only"""
parResults = dds.parResults()
myParResults = ctypes.pointer(parResults)
res = dds.Par(myTableRes, myParResults, 1)
print("Res", res)
t1 = myParResults.contents.parContractsString[0].value
print("NS Par:" + t1.decode('utf-8'))
print("EW Par:" + myParResults.contents.parContractsString[1].value.decode('utf-8'))