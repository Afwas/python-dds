SP = 0
HE = 1
DI = 2
CL = 3

SPADES = 0
HEARTS = 1
DIAMONDS = 2
CLUBS = 3
NOTRUMP = 4

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

VUL_NONE = 0
VUL_BOTH = 1
VUL_NS = 2
VUL_EW = 3

R2 = 0x0004
R3 = 0x0008
R4 = 0x0010
R5 = 0x0020
R6 = 0x0040
R7 = 0x0080
R8 = 0x0100
R9 = 0x0200
RT = 0x0400
RJ = 0x0800
RQ = 0x1000
RK = 0x2000
RA = 0x4000

K2 = 2
K3 = 3
K4 = 4
K5 = 5
K6 = 6
K7 = 7
K8 = 8
K9 = 9
KT = 10
KJ = 11
KQ = 12
KK = 13
KA = 14

trump = [SPADES, NOTRUMP, SPADES]
first = [NORTH, EAST, SOUTH]
dealer = [NORTH, EAST, SOUTH]
vul = [VUL_NONE, VUL_NS, VUL_NONE]

PBN = [b"N:QJ6.K652.J85.T98 873.J97.AT764.Q4 K5.T83.KQ9.A7652 AT942.AQ4.32.KJ3",
       b"E:QJT5432.T.6.QJ82 .J97543.K7532.94 87.A62.QJT4.AT75 AK96.KQ8.A98.K63",
       b"N:73.QJT.AQ54.T752 QT6.876.KJ9.AQ84 5.A95432.7632.K6 AKJ9842.K.T8.J93"]


holdings = [
    [
         [RQ|RJ|R6, R8|R7|R3, RK|R5, RA|RT|R9|R4|R2],
         [RK|R6|R5|R2, RJ|R9|R7, RT|R8|R3, RA|RQ|R4],
         [RJ|R8|R5, RA|RT|R7|R6|R4, RK|RQ|R9, R3|R2],
         [RT|R9|R8, RQ|R4, RA|R7|R6|R5|R2, RK|RJ|R3]
    ],
    [
         [RA|RK|R9|R6, RQ|RJ|RT|R5|R4|R3|R2, 0, R8|R7],
         [RK|RQ|R8, RT, RJ|R9|R7|R5|R4|R3, RA|R6|R2],
         [RA|R9|R8, R6, RK|R7|R5|R3|R2, RQ|RJ|RT|R4],
         [RK|R6|R3, RQ|RJ|R8|R2, R9|R4, RA|RT|R7|R5]
    ],
    [
         [R7|R3, RQ|RT|R6, R5, RA|RK|RJ|R9|R8|R4|R2],
         [RQ|RJ|RT, R8|R7|R6, RA|R9|R5|R4|R3|R2, RK],
         [RA|RQ|R5|R4, RK|RJ|R9, R7|R6|R3|R2, RT|R8],
         [RT|R7|R5|R2, RA|RQ|R8|R4, RK|R6, RJ|R9|R3]
    ]
]

playNo = [45, 52, 12]

# Actual cards played before claim
play = [
        b"CTC4CACJH8H4HKH9D5DAD9D2S7S5S2SQD8D4DQD3H3HAH6H7C3C8CQC2S3SKSAS6HQH5HJHTCKC9D6C5S4SJS8C6DJ",
        b"SQD2S8SAHKHTH3H2HQS2H4H6H8D6HJHAS7SKS4C4D8C2DKD4H9C5S6S3H7C7C3S5H5CTD9STD3DQDAC8S9SJC9DTCQD5CAC6DJCKCJD7",
        b"HAHKHQH7D7D8DAD9C5CAC6C3" 
]

playSuit = [
    [
        CL, CL, CL, CL,    HE, HE, HE, HE,    DI, DI, DI, DI,
        SP, SP, SP, SP,    DI, DI, DI, DI,    HE, HE, HE, HE,
        CL, CL, CL, CL,    SP, SP, SP, SP,    HE, HE, HE, HE,
        CL, CL, DI, CL,    SP, SP, SP, CL,    DI, -1, -1, -1,
        -1, -1, -1, -1
    ],
    [
        SP, DI, SP, SP,    HE, HE, HE, HE,    HE, SP, HE, HE,
        HE, DI, HE, HE,    SP, SP, SP, CL,    DI, CL, DI, DI,
        HE, CL, SP, SP,    HE, CL, CL, SP,    HE, CL, DI, SP,
        DI, DI, DI, CL,    SP, SP, CL, DI,    CL, DI, CL, CL,
        DI, CL, CL, DI
    ],
    [
       HE, HE, HE, HE,    DI, DI, DI, DI,    CL, CL, CL, CL,
       -1, -1, -1, -1,    -1, -1, -1, -1,    -1, -1, -1, -1,
       -1, -1, -1, -1,    -1, -1, -1, -1,    -1, -1, -1, -1,
       -1, -1, -1, -1
    ]
]

playRank = [
    [
        KT, K4, KA, KJ,    K8, K4, KK, K9,    K5, KA, K9, K2,
        K7, K5, K2, KQ,    K8, K4, KQ, K3,    K3, KA, K6, K7,
        K3, K8, KQ, K2,    K3, KK, KA, K6,    KQ, K5, KJ, KT,
        KK, K9, K6, K5,    K4, KJ, K8, K6,    KJ, -1, -1, -1,
        -1, -1, -1, -1
    ],
    [
        KQ, K2, K8, KA,    KK, KT, K3, K2,    KQ, K2, K4, K6,
        K8, K6, KJ, KA,    K7, KK, K4, K4,    K8, K2, KK, K4,
        K9, K5, K6, K3,    K7, K7, K3, K5,    K5, KT, K9, KT,
        K3, KQ, KA, K8,    K9, KJ, K9, KT,    KQ, K5, KA, K6,
        KJ, KK, KJ, K7
    ],
    [
        KA, KK, KQ, K7,    K7, K8, KA, K9,    K5, KA, K6, K3,
        -1, -1, -1, -1,    -1, -1, -1, -1,    -1, -1, -1, -1,
        -1, -1, -1, -1,    -1, -1, -1, -1,    -1, -1, -1, -1,
        -1, -1, -1, -1
    ]
]

#// Actual cards played before claim
play = [
    b"CTC4CACJH8H4HKH9D5DAD9D2S7S5S2SQD8D4DQD3H3HAH6H7C3C8CQC2S3SKSAS6HQH5HJHTCKC9D6C5S4SJS8C6DJ",
    b"SQD2S8SAHKHTH3H2HQS2H4H6H8D6HJHAS7SKS4C4D8C2DKD4H9C5S6S3H7C7C3S5H5CTD9STD3DQDAC8S9SJC9DTCQD5CAC6DJCKCJD7",
    b"HAHKHQH7D7D8DAD9C5CAC6C3" 
    ]

#//////////////////////////////////////////////////////////
#//                 Expected outputs                     //
#//////////////////////////////////////////////////////////

#// Number of cards returned for solutions == 2, i.e. for
#// all cards leading to the optimal score (taking into
#// account equivalences.

cardsSoln2 = [6, 3, 4]
        
#// Number of cards returned for solutions == 3, i.e. for
#// all legally playable cards (taking into account equivalences).
cardsSoln3 = [9, 7, 8]
        
#// Suits of cards returned. Padded with zeroes.
cardsSuits = [
    [
        2, 2, 2, 3, 0, 0, 1, 1, 1,    0, 0, 0, 0
    ],
    [
        3, 3, 3, 1, 2, 0, 0,    0, 0, 0, 0, 0, 0
    ],
    [
        1, 2, 2, 0, 1, 1, 3, 3,    0, 0, 0, 0, 0
    ]
]
        
#// Ranks for cards returned (2 .. 14).  Padded with zeroes.
cardsRanks = [
    [
        5, 8,11,10, 6,12, 2, 6,13,    0, 0, 0, 0
    ],
    [
        2, 8,12,10, 6,12, 5,    0, 0, 0, 0, 0, 0
    ],
    [
        14, 3, 7, 5, 5, 9, 6,13,    0, 0, 0, 0, 0
    ]
]
        
#// Scores for cards returned.
cardsScores = [
    [
        5, 5, 5, 5, 5, 5, 4, 4, 4,    0, 0, 0, 0
    ],
    [
        4, 4, 4, 3, 3, 3, 2,    0, 0, 0, 0, 0, 0
    ],
    [
        3, 3, 3, 3, 2, 2, 1, 1,    0, 0, 0, 0, 0
    ]
]
        
#// Equals for cards returned, i.e. equivalent cards (rank vectors).
cardsEquals = [
    [
        0,   0,   0, 768,   0,2048,   0,  32,   0,    0,0,0,0
    ],
    [
        0,   0,2048,   0,   0,3072,  28,          0,0,0,0,0,0
    ],
    [
        0,   4,  64,   0,  28,   0,   0,   0,       0,0,0,0,0
    ]
]
        
#// Double dummy table.  The order here is:
#// Spades: North, East, South, West
#// Hearts: same
#// etc.
DDtable = [
    [
 
        5, 8, 5, 8,  6, 6, 6, 6,  5, 7, 5, 7,  7, 5, 7, 5,  6, 6, 6, 6
    ],
    [
        4, 9, 4, 9, 10, 2,10, 2,  8, 3, 8, 3,  6, 7, 6, 7,  9, 3, 9, 3 
    ],
    [
        3,10, 3,10,  9, 4, 9, 4,  8, 4, 8, 4,  3, 9, 3, 9,  4, 8, 4, 8
    ]
]
        
#// Number of results expected for the play analysis.
#// Generally the number of cards + 1.  For example, if only one
#// card is played, then there is a result before the opening lead
#// and after the opening lead.  Limited to 49 as the last trick 
#//holds no excitement.
traceNo = [46, 49, 13]

#// Results expected from the play analysis.  Padded with zeroes here.
trace = [
    [
        8,   8, 8, 8, 8,   8, 8, 8, 8,   8, 8, 8, 8,   8, 8, 8, 8, 
        8, 8, 8, 8,   8, 8, 8, 8,   8, 8, 8, 8,   8, 8, 8, 8, 
        8, 8, 8, 8,   8, 8, 8, 8,   8, 8, 8, 8,   8, 0, 0, 0,
        0, 0, 0, 0
    ],
    [
        9,  10,10,10,10,  10,10,10,10,  10,10,10,10,  10,10,10,10,
        10,10,10,10,  10,10,10,10,  10,10,10,10,  10,10,10,10,
        10,10,10,10,   9, 9, 9, 9,   9, 9, 9, 9,   9, 9, 9, 9,
        0, 0, 0, 0
    ],
    [
        10, 10,10,10,10,  10,10,10,10,  10,10,10,10,   0, 0, 0, 0,
        0, 0, 0, 0,   0, 0, 0, 0,   0, 0, 0, 0,   0, 0, 0, 0,
        0, 0, 0, 0,   0, 0, 0, 0,   0, 0, 0, 0,   0, 0, 0, 0,
        0, 0, 0, 0
    ]
]
       
parScore = [
    [
        "NS -110", "EW 110"
    ],
    [
        "NS 100" , "EW -100"
    ],
    [
        "NS -300", "EW 300"
    ]
]

parString = [
    [
        "NS:EW 2S" , "EW:EW 2S"
    ],
    [
        "NS:EW 4Sx", "EW:EW 4Sx"
    ],
    [
        "NS:NS 5Hx", "EW:NS 5Hx"
    ]
]

#// Number of dealer par contracts expected.
dealerParNo = [1, 1, 1];

#// Dealer par scores expected.
dealerScore = [-110, 100, -300]

#// Dealer par contracts expected, here only one per deal.
#// That is not always the case.
dealerContract = [ 
    [
        "2S-EW"   , "", "", ""
    ],
    [
        "4S*-EW-1", "", "", ""
    ],
    [
        "5H*-NS-2", "", "", ""
    ]
]

#// Useful constants
dcardSuit = ["S", "H", "D", "C", "N"]
