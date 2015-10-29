#! /usr/bin/python

import dds
import ctypes
import hands
import functions

DDdealsPBN = dds.ddTableDealsPBN()
tableRes = dds.ddTablesRes()
pres = dds.allParResults()

mode = 0
tFilter = ctypes.c_int * dds.DDS_STRAINS
trumpFilter = tFilter(0, 0, 0, 0, 0)
line = ctypes.create_string_buffer(80)

dds.SetMaxThreads(0)

DDdealsPBN.noOfTables = 3

for handno in range(3):
    DDdealsPBN.deals[handno].cards = hands.PBN[handno]

res = dds.CalcAllTablesPBN(ctypes.pointer(DDdealsPBN), mode, trumpFilter, ctypes.pointer(tableRes), ctypes.pointer(pres))

if res != dds.RETURN_NO_FAULT:
    dds.ErrorMessage(res, line)
    print("DDS error: {}".format(line.value.decode("utf-8")))

for handno in range(3):
    match = functions.CompareTable(ctypes.pointer(tableRes.results[handno]), handno)

    line = "CalcDDtable, hand {}: {}".format(
        handno + 1,
        "OK" if match else "ERROR")

    functions.PrintPBNHand(line, DDdealsPBN.deals[handno].cards)

    functions.PrintTable(ctypes.pointer(tableRes.results[handno]))
