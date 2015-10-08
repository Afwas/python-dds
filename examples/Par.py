import dds
import hands
import functions
import ctypes

for handno in range(0, 3):
    DDTable = dds.ddTableResults()
    pres = dds.parResults()
    myDDTable = ctypes.pointer(DDTable)
    myPres = ctypes.pointer(pres)

    functions.SetTable(myDDTable, handno)
    res = dds.Par(myDDTable, myPres, hands.vul[handno])
    if res != dds.RETURN_NO_FAULT:
        dds.ErrorMessage(res, line)
        print("DDS error: {}".format(line))

    match = functions.ComparePar(myPres, handno)
    print("Par, hand {}: {}".format(handno + 1, "OK" if match else "ERROR"))
    print("")

    functions.PrintTable(myDDTable)
    functions.PrintPar(myPres)
