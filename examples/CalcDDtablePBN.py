#! /usr/bin/python

import hands
import functions
import dds
import ctypes

tableDealPBN = dds.ddTableDealPBN()
table = dds.ddTableResults()
myTable = ctypes.pointer(table)

line = ctypes.create_string_buffer(80)

dds.SetMaxThreads(0)

for handno in range(3):
	tableDealPBN.cards = hands.PBN[handno]

	res = dds.CalcDDtablePBN(tableDealPBN, myTable)

	if res != dds.RETURN_NO_FAULT:
		dds.ErrorMessage(res, line)
		print("DDS error: {}".format(line.encode("utf-8")))

	match = functions.CompareTable(myTable, handno)

	line = "CalcDDtable, hand {}: {}".format(
		handno + 1,
		"OK" if match else "ERROR")

	functions.PrintPBNHand(line, tableDealPBN.cards)

	functions.PrintTable(myTable)