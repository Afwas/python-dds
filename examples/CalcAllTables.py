#! /ur/bin/python

import dds
import ctypes
import hands
import functions

DDdeals = dds.ddTableDeals()
tableRes = dds.ddTablesRes()
pres = dds.allParResults()

mode = 0
# Probably the definition of trumpFilter should go to dds.py
tFilter = ctypes.c_int * dds.DDS_STRAINS
trumpFilter = tFilter(0, 0, 0, 0, 0)
line = ctypes.create_string_buffer(80)

dds.SetMaxThreads(0)

DDdeals.noOfTables = 3

for handno in range(3):
    for h in range(dds.DDS_HANDS):
        for s in range(dds.DDS_SUITS):
            DDdeals.deals[handno].cards[h][s] = hands.holdings[handno][s][h]

res = dds.CalcAllTables(ctypes.pointer(DDdeals), mode, trumpFilter, ctypes.pointer(tableRes), ctypes.pointer(pres))

if res != dds.RETURN_NO_FAULT:
    dds.ErrorMessage(res, line)
    print("DDS error: {}".format(line.value.decode("utf-8")))

for handno in range(3):
    match = functions.CompareTable(ctypes.pointer(tableRes.results[handno]),
        handno)

    line = "CalcDDtable, hand {}: {}".format(
        handno + 1,
        "OK" if match else "ERROR")

    functions.PrintHand(line, DDdeals.deals[handno].cards)

    functions.PrintTable(ctypes.pointer(tableRes.results[handno]))
