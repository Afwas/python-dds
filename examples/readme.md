## Examples
This folder contains Python files implementing the original dds examples. These examples show the use of the internal dds functions.
I implemented the functions in Python in a way that is consistent with the original C implementations. This means that the code is not so much Pythonic but might help a developer creating a package implementing these functions.

I suggest you stay away from the bin files and use the PBN alternatives instead. The bin files use the dds specific implementation of a deal. The PBN alternatives are a facade that convert a deal in PBN to that dds implementation. This is done inside dds and hence (thanks to the C / C++ implementation) faster than you probably could implement.

### AnalyseAllPlaysBin.py
This function takes a deal and a description of the cards played. At each play of a card it will evaluate the total number of tricks leader can make. If either a defender or the leader makes a mistake you see a shift in the verwachting. This is deal number 2 (of three) where you see this shift after the lead and later in the game. Note that four cards make a trick.

```
AnalyseAllPlaysBin, hand 2: OK
------------------------------                                                  
            AK96                                                                
            KQ8                                                                 
            A98                                                                 
            K63                                                                
87                      QJT5432                                                 
A62                     T                                                       
QJT4                    6                                                       
AT75                    QJ82                                                   
                                                                                
            J97543                                                              
            K7532                                                               
            94                                                                 


Number : 49
Play  0: -- 9
Play  0: D7 9
Play  1: SQ 10
Play  2: D2 10
Play  3: S8 10
Play  4: SA 10
Play  5: HK 10
Play  6: HT 10
Play  7: H3 10
Play  8: H2 10
Play  9: HQ 10
Play 10: S2 10
Play 11: H4 10
Play 12: H6 10
Play 13: H8 10
Play 14: D6 10
Play 15: HJ 10
Play 16: HA 10
Play 17: S7 10
Play 18: SK 10
Play 19: S4 10
Play 20: C4 10
Play 21: D8 10
Play 22: C2 10
Play 23: DK 10
Play 24: D4 10
Play 25: H9 10
Play 26: C5 10
Play 27: S6 10
Play 28: S3 10
Play 29: H7 10
Play 30: C7 10
Play 31: C3 10
Play 32: S5 10
Play 33: H5 10
Play 34: CT 10
Play 35: D9 10
Play 36: ST 10
Play 37: D3 9
Play 38: DQ 9
Play 39: DA 9
Play 40: C8 9
Play 41: S9 9
Play 42: SJ 9
Play 43: C9 9
Play 44: DT 9
Play 45: CQ 9
Play 46: D5 9
Play 47: CA 9
Play 48: C6 9
```