import dds
import hands
import functions
import ctypes

DDtable = dds.ddTableResults()
pres = dds.parResults()

line = ctypes.create_string_buffer(80)

dds.SetMaxThreads(0)

for handno in range(0, 3):
    functions.SetTable(ctypes.pointer(DDtable), handno)
    res = dds.Par(
        ctypes.pointer(DDtable),
        pres,
        hands.vul[handno])

    if res != dds.RETURN_NO_FAULT:
        dds.ErrorMessage(res, line)
        print("DDS error: {}".format(line.value.decode("utf-8")))

    match = functions.ComparePar(ctypes.pointer(pres), handno)

    print("Par, hand {}: {}\n".format(handno + 1, "OK" if match else "ERROR"))

    functions.PrintTable(ctypes.pointer(DDtable))
    functions.PrintPar(ctypes.pointer(pres))
