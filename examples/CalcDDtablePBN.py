#! /usr/bin/python

import dds
import ctypes

"""In this first example I will solve a PBN hand with SolveBoardPBN"""

# PBN: The deal to be examined
PBN = b"W:T5.K4.652.A98542 K6.QJT976.QT7.Q6 432.A.AKJ93.JT73 AQJ987.8532.84.K"
print(PBN)
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

print("*** Before")
for i in range(len(list(myTableRes.contents.resTable))):
    for j in range(len(list(myTableRes.contents.resTable)[i])):
        print("["+str(i)+"]["+str(j)+"] = "+str(list(myTableRes.contents.resTable)[i][j]))

res = dds.CalcDDtablePBN(deal, myTableRes)

print("res ", res)

print("*** After")
for i in range(len(list(myTableRes.contents.resTable))):
    for j in range(len(list(myTableRes.contents.resTable)[i])):
        print("["+str(i)+"]["+str(j)+"] = "+str(list(myTableRes.contents.resTable)[i][j]))
