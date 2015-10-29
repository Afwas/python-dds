#! /usr/bin/python

import dds
import ctypes
import hands
import functions

DDtable = dds.ddTableResults()
pres = dds.parResultsDealer()

line = ctypes.create_string_buffer(80)

dds.SetMaxThreads(0)

for handno in range(3):
    functions.SetTable(ctypes.pointer(DDtable), handno)
    res = dds.DealerPar(ctypes.pointer(DDtable), ctypes.pointer(pres), hands.dealer[handno], hands.vul[handno])

    if res != dds.RETURN_NO_FAULT:
        dds.ErrorMessage(res, line)
        print("DDS error: {}".format(line.value.decode("utf8")))

    match = functions.CompareDealerPar(ctypes.pointer(pres), handno)

    print("match: {}".format(match))
    print("DealerPar, hand {}: {}".format(
        handno + 1,
        "OK" if match else "ERROR"))

    functions.PrintTable(ctypes.pointer(DDtable))

    functions.PrintDealerPar(ctypes.pointer(pres))
