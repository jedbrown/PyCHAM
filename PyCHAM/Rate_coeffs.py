'''module for calculating gas-phase reaction rate coefficients, automatically generated by eqn_parser'''

##################################################################################################### 
# Python function to hold expressions for calculating rate coefficients for a given equation number # 
#    Copyright (C) 2017  David Topping : david.topping@manchester.ac.uk                             # 
#                                      : davetopp80@gmail.com                                       # 
#    Personal website: davetoppingsci.com                                                           # 
#                                                                                                   # 
#                                                                                                   # 
#                                                                                                   # 
##################################################################################################### 
# Minor modified by XSX
# File Created as 2019-11-20 11:44:32.510435

import numpy

def evaluate_rates(RO2, H2O, TEMP, lightm):
    # mcm_constants_dict: given by mcm_constants.py
    # RO2: specified by the chemical scheme. eg: subset of MCM
    # H2O, TEMP: given by the user
    # lightm: given by the user and is 0 for lights off and 1 for on
    # Creating reference to constant values used in rate expressions
    # mcm_constants_dict: given by MCM_constants.py
    KRO2NO = 9.180825715586685e-12 
    KRO2HO2 = 2.416926637791736e-11 
    KAPHO2 = 1.4551688760645419e-11 
    KAPNO = 2.0101502680038634e-11 
    KRO2NO3 = 2.3e-12 
    KNO3AL = 2.5116077328102446e-15 
    KDEC = 1000000.0 
    KROPRIM = 9.015884918617853e-15 
    KROSEC = 9.015884918617853e-15 
    KCH3O2 = 3.5623566538021364e-13 
    K298CH3O2 = 3.5e-13 
    KD0 = 0.1613839467444603 
    KDI = 0.00020570494794194444 
    KRD = 784.5409085152743 
    FCD = 0.3 
    NCD = 1.4140560065060288 
    FD = 0.7929743154543676 
    KBPAN = 0.00016291108878962242 
    KC0 = 7.493072176355027e-09 
    KCI = 1.2214576331165244e-11 
    KRC = 613.4533014654471 
    FCC = 0.3 
    NC = 1.4140560065060288 
    FC = 0.7816282619662761 
    KFPAN = 9.531720259332986e-12 
    K10 = 2.4903359658729046e-12 
    K1I = 2.982328880018226e-11 
    KR1 = 0.08350306307792872 
    FC1 = 0.85 
    NC1 = 0.8396379643428482 
    F1 = 0.9404990169661523 
    KMT01 = 2.1616538131101394e-12 
    K20 = 3.2310676634020842e-12 
    K2I = 2.2891553138312854e-11 
    KR2 = 0.14114672097081743 
    FC2 = 0.6 
    NC2 = 1.0317479120127726 
    F2 = 0.7377137327588735 
    KMT02 = 2.0887787196522987e-12 
    K30 = 9.417626154573176e-11 
    K3I = 1.892531516393803e-12 
    KR3 = 49.76205718633607 
    FC3 = 0.35 
    NC3 = 1.32903358367515 
    F3 = 0.670895282120826 
    KMT03 = 1.2446778767629536e-12 
    K40 = 1.9302951731277502 
    K4I = 0.0423617853658737 
    KR4 = 45.5668984783342 
    FC4 = 0.35 
    NC4 = 1.32903358367515 
    F4 = 0.6633302468802736 
    KMT04 = 0.027496423759859445 
    KMT05 = 2.2673462433579967e-13 
    KMT06 = 1.9870680674965064 
    K70 = 1.872110944120546e-11 
    K7I = 3.319553408857945e-11 
    KR7 = 0.5639647005301911 
    FC7 = 0.8128994235774208 
    NC7 = 0.8642532441914358 
    F7 = 0.8258842575092662 
    KMT07 = 9.886073237687639e-12 
    K80 = 8.447831511565145e-11 
    K8I = 4.1e-11 
    KR8 = 2.0604467101378403 
    FC8 = 0.4 
    NC8 = 1.2553838110134876 
    F8 = 0.42216714922102955 
    KMT08 = 1.1653190805522671e-11 
    K90 = 4.626092252030531e-12 
    K9I = 4.7e-12 
    KR9 = 0.9842749472405385 
    FC9 = 0.6 
    NC9 = 1.0317479120127726 
    F9 = 0.6000136423646976 
    KMT09 = 1.398857787281969e-12 
    K100 = 0.18676023540899958 
    K10I = 0.15467477895509874 
    KR10 = 1.2074381917378727 
    FC10 = 0.6 
    NC10 = 1.0317479120127726 
    F10 = 0.6019206172059376 
    KMT10 = 0.05092547396691059 
    K1 = 1.1464974776641956e-13 
    K3 = 6.080778653751884e-32 
    K4 = 4.7648886021725876e-14 
    K2 = 4.61502588569476e-14 
    KMT11 = 1.6080000662336717e-13 
    K120 = 1.1725759412594944e-11 
    K12I = 1.3180443800862464e-12 
    KR12 = 8.89633125390487 
    FC12 = 0.525 
    NC12 = 1.1053976846744347 
    F12 = 0.6901269906526685 
    KMT12 = 8.177033335801411e-13 
    K130 = 6.722832907719589e-11 
    K13I = 1.8e-11 
    KR13 = 3.7349071709553274 
    FC13 = 0.36 
    NC13 = 1.3134958240255452 
    F13 = 0.4237316925581669 
    KMT13 = 6.01633202916417e-12 
    K140 = 10.718261347174394 
    K14I = 2.819672302240446 
    KR14 = 3.8012436192169963 
    FC14 = 0.4 
    NC14 = 1.2553838110134876 
    F14 = 0.46994292989482467 
    KMT14 = 1.0490971798867044 
    K150 = 2.2058958062002046e-09 
    K15I = 9.151916543682877e-12 
    KR15 = 241.03102291976506 
    FC15 = 0.48 
    NC15 = 1.1548236285330042 
    F15 = 0.8696399161036162 
    KMT15 = 7.925988250164137e-12 
    K160 = 2.0682236100901387e-07 
    K16I = 3.0596634370219274e-11 
    KR16 = 6759.644165644604 
    FC16 = 0.5 
    NC16 = 1.1323080944932562 
    F16 = 0.94580744790786 
    KMT16 = 2.8934244229308933e-11 
    K170 = 1.2427183320777249e-10 
    K17I = 1e-12 
    KR17 = 124.27183320777249 
    FC17 = 0.37941417594157845 
    NC17 = 1.284525787341662 
    F17 = 0.7672798373785644 
    KMT17 = 7.611549183306731e-13 
    KMT18 = 2.7040956117978905e-12 
    KPPN0 = 0.9094797093339249 
    KPPNI = 0.00021753082121893914 
    KRPPN = 4180.923439895247 
    FCPPN = 0.36 
    NCPPN = 1.3134958240255452 
    FPPN = 0.8879993731372627 
    KBPPN = 7.829236954381317e-05 
    J = [0.0, 2.3706768705670786e-05, 0.0, 0.0, 0.0011216654096221574, 0.0024080663555999995, 0.02122656504799999, 0.0002830012299999995, 0.0, 0.0, 0.0, 0.0, 6.155370761783531e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] 
    
    if lightm == 0:
    	J = [0]*len(J)
    # Environmental Variables: M, O2, N2
    M = 2.4130932097941574e+19 # 3rd body; number of molecules in per unit volume
    N2 = 1.9063436357373846e+19 # Nitrogen mass mixing ratio : 79%
    O2 = 5.057843367728554e+18 # Oxygen mass mixing ratio : 20.96%
    rate_values = numpy.zeros(946)
    # reac_coef has been formatted so that python can recognize it
    rate_values[0] = 5.6e-34*N2*(TEMP/300)**-2.6*O2
    rate_values[1] = 6.0e-34*O2*(TEMP/300)**-2.6*O2
    rate_values[2] = 8.0e-12*numpy.exp(-2060/TEMP)
    rate_values[3] = KMT01
    rate_values[4] = 5.5e-12*numpy.exp(188/TEMP)
    rate_values[5] = KMT02
    rate_values[6] = 3.2e-11*numpy.exp(67/TEMP)*O2
    rate_values[7] = 2.0e-11*numpy.exp(130/TEMP)*N2
    rate_values[8] = 1.4e-12*numpy.exp(-1310/TEMP)
    rate_values[9] = 1.4e-13*numpy.exp(-2470/TEMP)
    rate_values[10] = 3.3e-39*numpy.exp(530/TEMP)*O2
    rate_values[11] = 1.8e-11*numpy.exp(110/TEMP)
    rate_values[12] = 4.50e-14*numpy.exp(-1260/TEMP)
    rate_values[13] = KMT03
    rate_values[14] = 2.14e-10*H2O
    rate_values[15] = 1.70e-12*numpy.exp(-940/TEMP)
    rate_values[16] = 7.7e-12*numpy.exp(-2100/TEMP)
    rate_values[17] = KMT05
    rate_values[18] = 2.9e-12*numpy.exp(-160/TEMP)
    rate_values[19] = 2.03e-16*(TEMP/300)**4.57*numpy.exp(693/TEMP)
    rate_values[20] = 4.8e-11*numpy.exp(250/TEMP)
    rate_values[21] = 2.20e-13*KMT06*numpy.exp(600/TEMP)
    rate_values[22] = 1.90e-33*M*KMT06*numpy.exp(980/TEMP)
    rate_values[23] = KMT07
    rate_values[24] = KMT08
    rate_values[25] = 2.0e-11
    rate_values[26] = 3.45e-12*numpy.exp(270/TEMP)
    rate_values[27] = KMT09
    rate_values[28] = 3.2e-13*numpy.exp(690/TEMP)*1.0
    rate_values[29] = 4.0e-12
    rate_values[30] = 2.5e-12*numpy.exp(260/TEMP)
    rate_values[31] = KMT11
    rate_values[32] = 4.0e-32*numpy.exp(-1000/TEMP)*M
    rate_values[33] = KMT12
    rate_values[34] = 1.3e-12*numpy.exp(-330/TEMP)*O2
    rate_values[35] = 6.00e-06
    rate_values[36] = 4.00e-04
    rate_values[37] = 1.20e-15*H2O
    rate_values[38] = J[1]
    rate_values[39] = J[2]
    rate_values[40] = J[3]
    rate_values[41] = J[4]
    rate_values[42] = J[5]
    rate_values[43] = J[6]
    rate_values[44] = J[7]
    rate_values[45] = J[8]
    rate_values[46] = KMT04
    rate_values[47] = KMT10
    rate_values[48] = KRO2HO2*0.914
    rate_values[49] = KRO2NO
    rate_values[50] = KRO2NO3
    rate_values[51] = 6.70e-15*0.1*RO2
    rate_values[52] = 6.70e-15*0.9*RO2
    rate_values[53] = KRO2HO2*0.914
    rate_values[54] = KRO2NO
    rate_values[55] = KRO2NO3
    rate_values[56] = 2.50e-13*0.1*RO2
    rate_values[57] = 2.50e-13*0.8*RO2
    rate_values[58] = 2.50e-13*0.1*RO2
    rate_values[59] = KDEC*0.55
    rate_values[60] = KDEC*0.45
    rate_values[61] = KDEC*0.50
    rate_values[62] = KDEC*0.50
    rate_values[63] = KRO2HO2*0.914
    rate_values[64] = KRO2NO*0.230
    rate_values[65] = KRO2NO*0.770
    rate_values[66] = KRO2NO3
    rate_values[67] = 9.20e-14*RO2*0.7
    rate_values[68] = 9.20e-14*RO2*0.3
    rate_values[69] = KRO2HO2*0.914
    rate_values[70] = KRO2NO*0.230
    rate_values[71] = KRO2NO*0.770
    rate_values[72] = KRO2NO3
    rate_values[73] = 8.80e-13*RO2*0.2
    rate_values[74] = 8.80e-13*RO2*0.6
    rate_values[75] = 8.80e-13*RO2*0.2
    rate_values[76] = KRO2HO2*0.914
    rate_values[77] = KRO2NO*0.125
    rate_values[78] = KRO2NO*0.875
    rate_values[79] = KRO2NO3
    rate_values[80] = 6.70e-15*RO2*0.7
    rate_values[81] = 6.70e-15*RO2*0.3
    rate_values[82] = 6.87e-12
    rate_values[83] = J[41]
    rate_values[84] = KDEC
    rate_values[85] = 3.64e-12
    rate_values[86] = 1.90e-12*numpy.exp(190/TEMP)
    rate_values[87] = 1.23e-11
    rate_values[88] = J[41]
    rate_values[89] = KROSEC*O2
    rate_values[90] = 4.00e+05
    rate_values[91] = 5.50e-12
    rate_values[92] = 5.55e-12
    rate_values[93] = J[55]
    rate_values[94] = KRO2HO2*0.914
    rate_values[95] = KRO2NO
    rate_values[96] = KRO2NO3
    rate_values[97] = 9.20e-14*0.7*RO2
    rate_values[98] = 9.20e-14*0.3*RO2
    rate_values[99] = KRO2HO2*0.914
    rate_values[100] = KRO2NO
    rate_values[101] = KRO2NO3
    rate_values[102] = 2.00e-12*RO2*0.05
    rate_values[103] = 2.00e-12*RO2*0.90
    rate_values[104] = 2.00e-12*RO2*0.05
    rate_values[105] = 1.20e-15
    rate_values[106] = 1.00e-14
    rate_values[107] = 1.00e-15
    rate_values[108] = 7.00e-14
    rate_values[109] = 1.40e-17*H2O
    rate_values[110] = 2.00e-18*H2O
    rate_values[111] = KRO2HO2*0.890
    rate_values[112] = KRO2NO*0.157
    rate_values[113] = KRO2NO*0.843
    rate_values[114] = KRO2NO3
    rate_values[115] = 1.30e-12*0.6*RO2
    rate_values[116] = 1.30e-12*0.2*RO2
    rate_values[117] = 1.30e-12*0.2*RO2
    rate_values[118] = 1.83e-11
    rate_values[119] = J[41]
    rate_values[120] = KDEC
    rate_values[121] = 1.49e-11
    rate_values[122] = 3.28e-11
    rate_values[123] = J[41]
    rate_values[124] = KDEC
    rate_values[125] = 8.18e-12
    rate_values[126] = 1.03e-10
    rate_values[127] = J[41]
    rate_values[128] = 9.87e-11
    rate_values[129] = J[55]
    rate_values[130] = KDEC
    rate_values[131] = 9.91e-11
    rate_values[132] = 2.0e-14
    rate_values[133] = 5.2e-12*numpy.exp(600/TEMP)*0.772
    rate_values[134] = 5.2e-12*numpy.exp(600/TEMP)*0.228
    rate_values[135] = J[15]
    rate_values[136] = KRO2HO2*0.914
    rate_values[137] = KRO2NO
    rate_values[138] = KRO2NO3
    rate_values[139] = 6.70e-15*RO2
    rate_values[140] = KAPHO2*0.44
    rate_values[141] = KAPHO2*0.41
    rate_values[142] = KAPHO2*0.15
    rate_values[143] = KAPNO
    rate_values[144] = KFPAN
    rate_values[145] = KRO2NO3*1.74
    rate_values[146] = 1.00e-11*0.7*RO2
    rate_values[147] = 1.00e-11*0.3*RO2
    rate_values[148] = 3.01e-11
    rate_values[149] = J[41]
    rate_values[150] = J[15]
    rate_values[151] = KDEC
    rate_values[152] = 2.66e-11
    rate_values[153] = J[15]
    rate_values[154] = 5.47e-11
    rate_values[155] = J[41]
    rate_values[156] = J[15]
    rate_values[157] = J[22]
    rate_values[158] = KDEC*0.80
    rate_values[159] = KDEC*0.20
    rate_values[160] = 5.47e-11
    rate_values[161] = J[34]
    rate_values[162] = J[15]
    rate_values[163] = 4.45e-11
    rate_values[164] = J[22]
    rate_values[165] = J[15]
    rate_values[166] = 6.65e-12
    rate_values[167] = J[22]
    rate_values[168] = 1.90e-12*numpy.exp(190/TEMP)
    rate_values[169] = 1.30e-11
    rate_values[170] = J[41]
    rate_values[171] = J[22]
    rate_values[172] = 2.88e-12
    rate_values[173] = J[53]
    rate_values[174] = J[22]
    rate_values[175] = 4.20e+10*numpy.exp(-3523/TEMP)
    rate_values[176] = 7.67e-12
    rate_values[177] = J[22]
    rate_values[178] = KNO3AL*8.5
    rate_values[179] = 2.64e-11
    rate_values[180] = J[15]
    rate_values[181] = 8.8e-12*numpy.exp(-1320/TEMP) + 1.7e-14*numpy.exp(423/TEMP)
    rate_values[182] = J[21]
    rate_values[183] = 1.19e-10
    rate_values[184] = KRO2HO2*0.820
    rate_values[185] = KRO2NO*0.278
    rate_values[186] = KRO2NO*0.722
    rate_values[187] = KRO2NO3
    rate_values[188] = 2.50e-13*RO2*0.6
    rate_values[189] = 2.50e-13*RO2*0.2
    rate_values[190] = 2.50e-13*RO2*0.2
    rate_values[191] = KRO2HO2*0.914
    rate_values[192] = KRO2NO*0.050
    rate_values[193] = KRO2NO*0.950
    rate_values[194] = KRO2NO3
    rate_values[195] = 6.70e-15*0.7*RO2
    rate_values[196] = 6.70e-15*0.3*RO2
    rate_values[197] = 5.94e-12
    rate_values[198] = J[41]
    rate_values[199] = KDEC
    rate_values[200] = 9.73e-12
    rate_values[201] = J[41]
    rate_values[202] = J[22]
    rate_values[203] = 3.66e-12
    rate_values[204] = KBPAN
    rate_values[205] = KRO2HO2*0.914
    rate_values[206] = KRO2NO*0.125
    rate_values[207] = KRO2NO*0.875
    rate_values[208] = KRO2NO3
    rate_values[209] = 6.70e-15*0.7*RO2
    rate_values[210] = 6.70e-15*0.3*RO2
    rate_values[211] = KAPHO2*0.44
    rate_values[212] = KAPHO2*0.15
    rate_values[213] = KAPHO2*0.41
    rate_values[214] = KAPNO
    rate_values[215] = KFPAN
    rate_values[216] = KRO2NO3*1.74
    rate_values[217] = 1.00e-11*RO2*0.7
    rate_values[218] = 1.00e-11*RO2*0.3
    rate_values[219] = J[11]
    rate_values[220] = J[12]
    rate_values[221] = 5.5e-16
    rate_values[222] = 5.4e-12*numpy.exp(135/TEMP)
    rate_values[223] = KAPHO2*0.41
    rate_values[224] = KAPHO2*0.44
    rate_values[225] = KAPHO2*0.15
    rate_values[226] = KAPNO
    rate_values[227] = KFPAN
    rate_values[228] = KRO2NO3*1.74
    rate_values[229] = 1.00e-11*RO2*0.7
    rate_values[230] = 1.00e-11*RO2*0.3
    rate_values[231] = KRO2HO2*0.890
    rate_values[232] = KRO2NO
    rate_values[233] = KRO2NO3
    rate_values[234] = 1.30e-12*RO2
    rate_values[235] = KRO2HO2*0.890
    rate_values[236] = KRO2NO
    rate_values[237] = KRO2NO3
    rate_values[238] = 6.70e-15*0.7*RO2
    rate_values[239] = 6.70e-15*0.3*RO2
    rate_values[240] = KAPHO2*0.56
    rate_values[241] = KAPHO2*0.44
    rate_values[242] = KAPNO
    rate_values[243] = KFPAN
    rate_values[244] = KRO2NO3*1.74
    rate_values[245] = 1.00e-11*RO2
    rate_values[246] = KRO2HO2*0.859
    rate_values[247] = KRO2NO
    rate_values[248] = KRO2NO3
    rate_values[249] = 6.70e-15*RO2
    rate_values[250] = 1.36e-13*numpy.exp(1250/TEMP)*0.15
    rate_values[251] = 1.36e-13*numpy.exp(1250/TEMP)*0.85
    rate_values[252] = KRO2NO
    rate_values[253] = KRO2NO3
    rate_values[254] = 2*(K298CH3O2*8.0e-12)**0.5*RO2*0.2
    rate_values[255] = 2*(K298CH3O2*8.0e-12)**0.5*RO2*0.6
    rate_values[256] = 2*(K298CH3O2*8.0e-12)**0.5*RO2*0.2
    rate_values[257] = KAPHO2*0.15
    rate_values[258] = KAPHO2*0.41
    rate_values[259] = KAPHO2*0.44
    rate_values[260] = 7.5e-12*numpy.exp(290/TEMP)
    rate_values[261] = KFPAN
    rate_values[262] = 4.0e-12
    rate_values[263] = 2*(K298CH3O2*2.9e-12*numpy.exp(500/TEMP))**0.5*RO2*0.3
    rate_values[264] = 2*(K298CH3O2*2.9e-12*numpy.exp(500/TEMP))**0.5*RO2*0.7
    rate_values[265] = 3.8e-13*numpy.exp(780/TEMP)*(1-1/(1+498*numpy.exp(-1160/TEMP)))
    rate_values[266] = 3.8e-13*numpy.exp(780/TEMP)*(1/(1+498*numpy.exp(-1160/TEMP)))
    rate_values[267] = 2.3e-12*numpy.exp(360/TEMP)*0.001
    rate_values[268] = 2.3e-12*numpy.exp(360/TEMP)*0.999
    rate_values[269] = KMT13
    rate_values[270] = 1.2e-12
    rate_values[271] = 2*KCH3O2*RO2*7.18*numpy.exp(-885/TEMP)
    rate_values[272] = 2*KCH3O2*RO2*0.5*(1-7.18*numpy.exp(-885/TEMP))
    rate_values[273] = 2*KCH3O2*RO2*0.5*(1-7.18*numpy.exp(-885/TEMP))
    rate_values[274] = KRO2HO2*0.820
    rate_values[275] = KRO2NO*0.042
    rate_values[276] = KRO2NO*0.958
    rate_values[277] = KRO2NO3
    rate_values[278] = 9.20e-14*RO2*0.7
    rate_values[279] = 9.20e-14*RO2*0.3
    rate_values[280] = 1.27e-10
    rate_values[281] = J[41]
    rate_values[282] = 9.60e-11
    rate_values[283] = J[54]
    rate_values[284] = KROSEC*O2
    rate_values[285] = 1.09e-10
    rate_values[286] = 2.75e-11
    rate_values[287] = J[41]
    rate_values[288] = J[15]
    rate_values[289] = 2.25e-11
    rate_values[290] = J[55]
    rate_values[291] = J[15]
    rate_values[292] = KDEC
    rate_values[293] = 2.41e-11
    rate_values[294] = J[22]
    rate_values[295] = KRO2HO2*0.914
    rate_values[296] = KRO2NO
    rate_values[297] = KRO2NO3
    rate_values[298] = 6.70e-15*RO2
    rate_values[299] = 6.28e-11
    rate_values[300] = J[41]
    rate_values[301] = J[35]
    rate_values[302] = 2.85e-11
    rate_values[303] = J[55]
    rate_values[304] = J[35]
    rate_values[305] = KDEC
    rate_values[306] = 5.93e-11
    rate_values[307] = J[35]
    rate_values[308] = KDEC*0.80
    rate_values[309] = KDEC*0.20
    rate_values[310] = 2.69e-11
    rate_values[311] = J[15]
    rate_values[312] = 3.00e-11
    rate_values[313] = J[41]
    rate_values[314] = J[15]
    rate_values[315] = 2.52e-11
    rate_values[316] = KBPAN
    rate_values[317] = 9.16e-12
    rate_values[318] = J[41]
    rate_values[319] = J[22]
    rate_values[320] = 5.70e-12
    rate_values[321] = J[22]
    rate_values[322] = 5.56e-12
    rate_values[323] = KBPAN
    rate_values[324] = 2.36e-11
    rate_values[325] = J[41]
    rate_values[326] = J[22]
    rate_values[327] = 4.20e+10*numpy.exp(-3523/TEMP)
    rate_values[328] = 1.05e-11
    rate_values[329] = J[41]
    rate_values[330] = J[22]
    rate_values[331] = KDEC
    rate_values[332] = 7.20e-12
    rate_values[333] = J[22]
    rate_values[334] = 1.02e-11
    rate_values[335] = J[41]
    rate_values[336] = J[22]
    rate_values[337] = 6.60e-12
    rate_values[338] = KBPAN
    rate_values[339] = 1.29e-11
    rate_values[340] = J[41]
    rate_values[341] = J[22]
    rate_values[342] = KDEC
    rate_values[343] = KDEC
    rate_values[344] = 1.90e-12*numpy.exp(190/TEMP)
    rate_values[345] = 8.39e-12
    rate_values[346] = J[22]
    rate_values[347] = J[41]
    rate_values[348] = 1.6e-12*numpy.exp(305/TEMP)
    rate_values[349] = J[22]
    rate_values[350] = J[34]
    rate_values[351] = KNO3AL*2.4
    rate_values[352] = 1.9e-12*numpy.exp(575/TEMP)
    rate_values[353] = 8.00e-13
    rate_values[354] = 3.70e-12
    rate_values[355] = J[41]
    rate_values[356] = 3e-14
    rate_values[357] = KBPAN
    rate_values[358] = J[41]
    rate_values[359] = 5.3e-12*numpy.exp(190/TEMP)*0.6
    rate_values[360] = 5.3e-12*numpy.exp(190/TEMP)*0.4
    rate_values[361] = J[51]
    rate_values[362] = 4.0e-13*numpy.exp(-845/TEMP)
    rate_values[363] = 7.2e-14*numpy.exp(-1080/TEMP)*O2
    rate_values[364] = KMT14
    rate_values[365] = 2.85e-12*numpy.exp(-345/TEMP)
    rate_values[366] = 7.06e-11
    rate_values[367] = J[41]
    rate_values[368] = 1.26e-11
    rate_values[369] = KDEC
    rate_values[370] = 6.72e-11
    rate_values[371] = KNO3AL*5.5
    rate_values[372] = 6.70e-11
    rate_values[373] = J[35]
    rate_values[374] = KRO2HO2*0.914
    rate_values[375] = KRO2NO*0.125
    rate_values[376] = KRO2NO*0.875
    rate_values[377] = KRO2NO3
    rate_values[378] = 6.70e-15*0.7*RO2
    rate_values[379] = 6.70e-15*0.3*RO2
    rate_values[380] = 8.03e-12
    rate_values[381] = J[41]
    rate_values[382] = KDEC
    rate_values[383] = KRO2HO2*0.820
    rate_values[384] = KRO2NO*0.278
    rate_values[385] = KRO2NO*0.722
    rate_values[386] = KRO2NO3
    rate_values[387] = 2.50e-13*0.6*RO2
    rate_values[388] = 2.50e-13*0.2*RO2
    rate_values[389] = 2.50e-13*0.2*RO2
    rate_values[390] = KAPHO2*0.41
    rate_values[391] = KAPHO2*0.44
    rate_values[392] = KAPHO2*0.15
    rate_values[393] = KAPNO
    rate_values[394] = KFPAN
    rate_values[395] = KRO2NO3*1.74
    rate_values[396] = 1.00e-11*RO2*0.7
    rate_values[397] = 1.00e-11*RO2*0.3
    rate_values[398] = KRO2HO2*0.859
    rate_values[399] = KRO2NO*0.104
    rate_values[400] = KRO2NO*0.896
    rate_values[401] = KRO2NO3
    rate_values[402] = 6.70e-15*RO2*0.7
    rate_values[403] = 6.70e-15*RO2*0.3
    rate_values[404] = 2*KNO3AL*5.5
    rate_values[405] = 1.33e-10
    rate_values[406] = J[15]*2
    rate_values[407] = KRO2HO2*0.890
    rate_values[408] = KRO2NO
    rate_values[409] = KRO2NO3
    rate_values[410] = 6.70e-15*RO2
    rate_values[411] = KRO2HO2*0.890
    rate_values[412] = KRO2NO*0.118
    rate_values[413] = KRO2NO*0.882
    rate_values[414] = KRO2NO3
    rate_values[415] = 6.70e-15*0.7*RO2
    rate_values[416] = 6.70e-15*0.3*RO2
    rate_values[417] = KRO2HO2*0.859
    rate_values[418] = KRO2NO
    rate_values[419] = KRO2NO3
    rate_values[420] = 6.70e-15*RO2
    rate_values[421] = KNO3AL*5.5
    rate_values[422] = 8.92e-11*0.232
    rate_values[423] = 8.92e-11*0.768
    rate_values[424] = J[15]
    rate_values[425] = KAPHO2*0.56
    rate_values[426] = KAPHO2*0.44
    rate_values[427] = KAPNO
    rate_values[428] = KFPAN
    rate_values[429] = KRO2NO3*1.74
    rate_values[430] = 1.00e-11*RO2
    rate_values[431] = KAPHO2*0.44
    rate_values[432] = KAPHO2*0.56
    rate_values[433] = KAPNO
    rate_values[434] = KFPAN
    rate_values[435] = KRO2NO3*1.74
    rate_values[436] = 1.00e-11*RO2
    rate_values[437] = 8.01e-11
    rate_values[438] = J[41]
    rate_values[439] = J[15]
    rate_values[440] = 7.03e-11
    rate_values[441] = J[55]
    rate_values[442] = J[15]
    rate_values[443] = KDEC
    rate_values[444] = 7.66e-11
    rate_values[445] = J[15]
    rate_values[446] = KRO2HO2*0.820
    rate_values[447] = KRO2NO
    rate_values[448] = KRO2NO3
    rate_values[449] = 2.50e-13*RO2
    rate_values[450] = 2.00e-10
    rate_values[451] = J[41]
    rate_values[452] = J[35]
    rate_values[453] = 2.23e-11
    rate_values[454] = J[54]
    rate_values[455] = J[35]
    rate_values[456] = KROSEC*O2
    rate_values[457] = 1.26e-10
    rate_values[458] = J[35]
    rate_values[459] = 1.04e-11
    rate_values[460] = J[41]
    rate_values[461] = KRO2HO2*0.859
    rate_values[462] = KRO2NO*0.138
    rate_values[463] = KRO2NO*0.862
    rate_values[464] = KRO2NO3
    rate_values[465] = 1.30e-12*RO2*0.2
    rate_values[466] = 1.30e-12*RO2*0.6
    rate_values[467] = 1.30e-12*RO2*0.2
    rate_values[468] = 7.29e-12
    rate_values[469] = 6.77e-12
    rate_values[470] = KBPAN
    rate_values[471] = 3.61e-11
    rate_values[472] = J[41]
    rate_values[473] = J[15]
    rate_values[474] = 2.56e-11
    rate_values[475] = J[55]
    rate_values[476] = J[15]
    rate_values[477] = 2.70e+14*numpy.exp(-6643/TEMP)
    rate_values[478] = 2.86e-11
    rate_values[479] = J[15]
    rate_values[480] = KRO2HO2*0.625
    rate_values[481] = KRO2NO
    rate_values[482] = KRO2NO3
    rate_values[483] = 2.00e-12*RO2
    rate_values[484] = 1.29e-11
    rate_values[485] = J[41]
    rate_values[486] = J[22]
    rate_values[487] = KDEC
    rate_values[488] = 2.05e-11
    rate_values[489] = J[41]
    rate_values[490] = J[35]
    rate_values[491] = 5.37e-12
    rate_values[492] = J[55]
    rate_values[493] = J[35]
    rate_values[494] = KDEC
    rate_values[495] = 1.69e-11
    rate_values[496] = J[35]
    rate_values[497] = 3.45e-11
    rate_values[498] = J[41]
    rate_values[499] = J[15]
    rate_values[500] = KDEC
    rate_values[501] = KAPHO2*0.44
    rate_values[502] = KAPHO2*0.15
    rate_values[503] = KAPHO2*0.41
    rate_values[504] = KAPNO
    rate_values[505] = KFPAN
    rate_values[506] = KRO2NO3*1.74
    rate_values[507] = 1.00e-11*RO2*0.7
    rate_values[508] = 1.00e-11*RO2*0.3
    rate_values[509] = KRO2HO2*0.770
    rate_values[510] = KRO2NO
    rate_values[511] = KRO2NO3
    rate_values[512] = 2.00e-12*RO2*0.2
    rate_values[513] = 2.00e-12*RO2*0.6
    rate_values[514] = 2.00e-12*RO2*0.2
    rate_values[515] = 4.75e-12
    rate_values[516] = J[41]
    rate_values[517] = J[35]
    rate_values[518] = KRO2HO2*0.770
    rate_values[519] = KRO2NO
    rate_values[520] = KRO2NO3
    rate_values[521] = 2.00e-12*RO2
    rate_values[522] = 8.83e-13
    rate_values[523] = KBPAN
    rate_values[524] = 7.55e-11
    rate_values[525] = J[41]
    rate_values[526] = J[22]
    rate_values[527] = J[15]
    rate_values[528] = 7.19e-11
    rate_values[529] = KBPAN
    rate_values[530] = KRO2HO2*0.820
    rate_values[531] = KRO2NO
    rate_values[532] = KRO2NO3
    rate_values[533] = 8.80e-13*0.6*RO2
    rate_values[534] = 8.80e-13*0.2*RO2
    rate_values[535] = 8.80e-13*0.2*RO2
    rate_values[536] = 3.25e-11
    rate_values[537] = J[41]
    rate_values[538] = 4.00e+04
    rate_values[539] = KROSEC*O2
    rate_values[540] = 1.70e-11
    rate_values[541] = J[41]
    rate_values[542] = 3.29e-12
    rate_values[543] = J[53]
    rate_values[544] = KDEC
    rate_values[545] = KNO3AL*8.5
    rate_values[546] = 2.63e-11
    rate_values[547] = J[15]
    rate_values[548] = 7.89e-12
    rate_values[549] = KRO2HO2*0.914
    rate_values[550] = KRO2NO*0.104
    rate_values[551] = KRO2NO*0.896
    rate_values[552] = KRO2NO3
    rate_values[553] = 6.70e-15*RO2*0.7
    rate_values[554] = 6.70e-15*RO2*0.3
    rate_values[555] = 8.33e-11
    rate_values[556] = J[41]
    rate_values[557] = J[22]
    rate_values[558] = J[15]
    rate_values[559] = KDEC
    rate_values[560] = KRO2HO2*0.890
    rate_values[561] = KRO2NO
    rate_values[562] = KRO2NO3
    rate_values[563] = 6.70e-15*RO2
    rate_values[564] = 3.22e-12
    rate_values[565] = J[22]
    rate_values[566] = KRO2HO2*0.770
    rate_values[567] = KRO2NO*0.098
    rate_values[568] = KRO2NO*0.902
    rate_values[569] = KRO2NO3
    rate_values[570] = 8.80e-13*0.2*RO2
    rate_values[571] = 8.80e-13*0.6*RO2
    rate_values[572] = 8.80e-13*0.2*RO2
    rate_values[573] = KRO2HO2*0.706
    rate_values[574] = KRO2NO
    rate_values[575] = KRO2NO3
    rate_values[576] = 8.80e-13*RO2
    rate_values[577] = 2.39e-11
    rate_values[578] = J[22]*2
    rate_values[579] = 2.70e-11
    rate_values[580] = J[41]
    rate_values[581] = J[22]*2
    rate_values[582] = 2.29e-11
    rate_values[583] = KBPAN
    rate_values[584] = 3.23e-11
    rate_values[585] = J[41]
    rate_values[586] = J[22]*2
    rate_values[587] = KDEC
    rate_values[588] = 3.55e-11
    rate_values[589] = J[34]
    rate_values[590] = 2.54e-11*0.890
    rate_values[591] = 2.54e-11*0.110
    rate_values[592] = J[22]*2
    rate_values[593] = 1.01e-11
    rate_values[594] = J[41]
    rate_values[595] = J[35]
    rate_values[596] = KDEC
    rate_values[597] = KNO3AL*5.5
    rate_values[598] = 1.33e-11
    rate_values[599] = J[34]
    rate_values[600] = 2*KNO3AL*4.0
    rate_values[601] = 3.39e-11
    rate_values[602] = J[15]
    rate_values[603] = J[34]
    rate_values[604] = 1.20e-10
    rate_values[605] = J[41]
    rate_values[606] = J[15]
    rate_values[607] = KDEC
    rate_values[608] = 1.25e-12
    rate_values[609] = J[55]
    rate_values[610] = KRO2HO2*0.859
    rate_values[611] = KRO2NO
    rate_values[612] = KRO2NO3
    rate_values[613] = 9.20e-14*RO2*0.7
    rate_values[614] = 9.20e-14*RO2*0.3
    rate_values[615] = KAPHO2*0.41
    rate_values[616] = KAPHO2*0.44
    rate_values[617] = KAPHO2*0.15
    rate_values[618] = KAPNO
    rate_values[619] = KFPAN
    rate_values[620] = KRO2NO3*1.74
    rate_values[621] = 1.00e-11*RO2*0.7
    rate_values[622] = 1.00e-11*RO2*0.3
    rate_values[623] = KRO2HO2*0.820
    rate_values[624] = KRO2NO
    rate_values[625] = KRO2NO3
    rate_values[626] = 1.30e-12*RO2
    rate_values[627] = 8.35e-11
    rate_values[628] = J[41]
    rate_values[629] = J[15]
    rate_values[630] = 4.96e-11
    rate_values[631] = J[55]
    rate_values[632] = J[15]
    rate_values[633] = 2.70e+14*numpy.exp(-6643/TEMP)
    rate_values[634] = 8.00e-11
    rate_values[635] = J[15]
    rate_values[636] = KAPHO2*0.15
    rate_values[637] = KAPHO2*0.41
    rate_values[638] = KAPHO2*0.44
    rate_values[639] = KAPNO
    rate_values[640] = KFPAN
    rate_values[641] = KRO2NO3*1.74
    rate_values[642] = 1.00e-11*0.3*RO2
    rate_values[643] = 1.00e-11*0.7*RO2
    rate_values[644] = 1.51e-11
    rate_values[645] = J[41]
    rate_values[646] = J[22]
    rate_values[647] = KDEC
    rate_values[648] = KRO2HO2*0.625
    rate_values[649] = KRO2NO
    rate_values[650] = KRO2NO3
    rate_values[651] = 2.00e-12*0.6*RO2
    rate_values[652] = 2.00e-12*0.2*RO2
    rate_values[653] = 2.00e-12*0.2*RO2
    rate_values[654] = KAPHO2*0.44
    rate_values[655] = KAPHO2*0.15
    rate_values[656] = KAPHO2*0.41
    rate_values[657] = KAPNO
    rate_values[658] = KFPAN
    rate_values[659] = KRO2NO3*1.74
    rate_values[660] = 1.00e-11*0.7*RO2
    rate_values[661] = 1.00e-11*0.3*RO2
    rate_values[662] = 8.69e-11
    rate_values[663] = J[41]
    rate_values[664] = J[35]
    rate_values[665] = 71.11e-12
    rate_values[666] = J[35]
    rate_values[667] = KDEC
    rate_values[668] = 3.78e-11
    rate_values[669] = J[35]
    rate_values[670] = 7.49e-11
    rate_values[671] = J[41]
    rate_values[672] = J[15]
    rate_values[673] = KDEC
    rate_values[674] = KAPHO2*0.15
    rate_values[675] = KAPHO2*0.41
    rate_values[676] = KAPHO2*0.44
    rate_values[677] = KAPNO
    rate_values[678] = KFPAN
    rate_values[679] = KRO2NO3*1.74
    rate_values[680] = 1.00e-11*RO2*0.3
    rate_values[681] = 1.00e-11*RO2*0.7
    rate_values[682] = KRO2HO2*0.625
    rate_values[683] = KRO2NO*0.017
    rate_values[684] = KRO2NO*0.983
    rate_values[685] = KRO2NO3
    rate_values[686] = 2.00e-12*0.2*RO2
    rate_values[687] = 2.00e-12*0.6*RO2
    rate_values[688] = 2.00e-12*0.2*RO2
    rate_values[689] = KAPHO2*0.44
    rate_values[690] = KAPHO2*0.56
    rate_values[691] = KAPNO
    rate_values[692] = KFPAN
    rate_values[693] = KRO2NO3*1.74
    rate_values[694] = 1.00e-11*RO2
    rate_values[695] = KAPHO2*0.56
    rate_values[696] = KAPHO2*0.44
    rate_values[697] = KAPNO
    rate_values[698] = KFPAN
    rate_values[699] = KRO2NO3*1.74
    rate_values[700] = 1.00e-11*RO2
    rate_values[701] = KRO2HO2*0.520
    rate_values[702] = KRO2NO
    rate_values[703] = KRO2NO3
    rate_values[704] = 2.00e-12*RO2
    rate_values[705] = KRO2HO2*0.820
    rate_values[706] = KRO2NO
    rate_values[707] = KRO2NO3
    rate_values[708] = 8.80e-13*RO2
    rate_values[709] = 1.09e-11
    rate_values[710] = J[41]
    rate_values[711] = KDEC
    rate_values[712] = 7.42e-12
    rate_values[713] = 9.65e-12
    rate_values[714] = J[41]
    rate_values[715] = 6.57e-12
    rate_values[716] = 2.96e-12
    rate_values[717] = KBPAN
    rate_values[718] = 1.27e-11
    rate_values[719] = J[41]
    rate_values[720] = KDEC
    rate_values[721] = KRO2HO2*0.706
    rate_values[722] = KRO2NO*0.129
    rate_values[723] = KRO2NO*0.871
    rate_values[724] = KRO2NO3
    rate_values[725] = 2.50e-13*RO2*0.6
    rate_values[726] = 2.50e-13*RO2*0.2
    rate_values[727] = 2.50e-13*RO2*0.2
    rate_values[728] = J[15]
    rate_values[729] = 2.14e-11
    rate_values[730] = J[41]
    rate_values[731] = J[15]
    rate_values[732] = 2.49e-11
    rate_values[733] = KRO2HO2*0.387
    rate_values[734] = KRO2NO
    rate_values[735] = KRO2NO3
    rate_values[736] = 2.00e-12*0.2*RO2
    rate_values[737] = 2.00e-12*0.6*RO2
    rate_values[738] = 2.00e-12*0.2*RO2
    rate_values[739] = KBPAN
    rate_values[740] = 2.10e-11
    rate_values[741] = KRO2HO2*0.770
    rate_values[742] = KRO2NO
    rate_values[743] = KRO2NO3
    rate_values[744] = 8.80e-13*RO2
    rate_values[745] = J[41]
    rate_values[746] = J[35]
    rate_values[747] = 1.90e-12*numpy.exp(190/TEMP)
    rate_values[748] = 5.99e-12
    rate_values[749] = KDEC
    rate_values[750] = J[35]
    rate_values[751] = 2.69e-12
    rate_values[752] = J[34]
    rate_values[753] = J[35]
    rate_values[754] = KNO3AL*4.0
    rate_values[755] = 1.23e-11
    rate_values[756] = 2.73e-12
    rate_values[757] = 6.19e-12
    rate_values[758] = J[41]
    rate_values[759] = 1.12e-12
    rate_values[760] = KBPAN
    rate_values[761] = J[15]
    rate_values[762] = J[35]
    rate_values[763] = KNO3AL*5.5
    rate_values[764] = 6.65e-11
    rate_values[765] = J[15]*2
    rate_values[766] = 2*KNO3AL*2.4
    rate_values[767] = 4.29e-11
    rate_values[768] = 2.34e-11
    rate_values[769] = J[22]
    rate_values[770] = 2.65e-11
    rate_values[771] = J[41]
    rate_values[772] = J[22]
    rate_values[773] = 7.60e-12
    rate_values[774] = KBPAN
    rate_values[775] = J[41]
    rate_values[776] = 5.77e-11
    rate_values[777] = 2.23e-12
    rate_values[778] = KDEC
    rate_values[779] = J[15]
    rate_values[780] = KNO3AL*4.0
    rate_values[781] = 2.45e-11
    rate_values[782] = J[22]
    rate_values[783] = 1.88e-11
    rate_values[784] = J[41]
    rate_values[785] = J[15]
    rate_values[786] = 4.23e-12
    rate_values[787] = KBPAN
    rate_values[788] = 3.12e-13
    rate_values[789] = 1.63e-11
    rate_values[790] = J[41]
    rate_values[791] = J[34]
    rate_values[792] = 1.27e-11
    rate_values[793] = KBPAN
    rate_values[794] = 2.41e-11
    rate_values[795] = J[41]
    rate_values[796] = J[34]
    rate_values[797] = KDEC*0.6
    rate_values[798] = KDEC*0.4
    rate_values[799] = 1.85e-11
    rate_values[800] = J[41]
    rate_values[801] = KDEC
    rate_values[802] = KRO2HO2*0.859
    rate_values[803] = KRO2NO*0.104
    rate_values[804] = KRO2NO*0.896
    rate_values[805] = KRO2NO3
    rate_values[806] = 6.70e-15*RO2*0.7
    rate_values[807] = 6.70e-15*RO2*0.3
    rate_values[808] = KRO2HO2*0.820
    rate_values[809] = KRO2NO
    rate_values[810] = KRO2NO3
    rate_values[811] = 6.70e-15*RO2
    rate_values[812] = 1.10e-10
    rate_values[813] = J[41]
    rate_values[814] = J[15]*2
    rate_values[815] = 4.33e-11
    rate_values[816] = J[54]
    rate_values[817] = J[15]*2
    rate_values[818] = 1.80e-14*numpy.exp(-260/TEMP)*O2
    rate_values[819] = 6.99e-11
    rate_values[820] = J[15]*2
    rate_values[821] = 2.91e-11
    rate_values[822] = 1.90e-12*numpy.exp(190/TEMP)
    rate_values[823] = J[41]
    rate_values[824] = J[15]
    rate_values[825] = KDEC
    rate_values[826] = J[31]
    rate_values[827] = J[33]
    rate_values[828] = J[32]
    rate_values[829] = KNO3AL*0.6
    rate_values[830] = KNO3AL*0.4
    rate_values[831] = 3.1e-12*numpy.exp(340/TEMP)*0.6
    rate_values[832] = 3.1e-12*numpy.exp(340/TEMP)*0.4
    rate_values[833] = KNO3AL
    rate_values[834] = 1.00e-11*0.200
    rate_values[835] = 1.00e-11*0.800
    rate_values[836] = J[15]
    rate_values[837] = 1.00e-10
    rate_values[838] = J[41]
    rate_values[839] = J[22]
    rate_values[840] = KDEC
    rate_values[841] = KAPHO2*0.15
    rate_values[842] = KAPHO2*0.41
    rate_values[843] = KAPHO2*0.44
    rate_values[844] = KAPNO
    rate_values[845] = KFPAN
    rate_values[846] = KRO2NO3*1.74
    rate_values[847] = 1.00e-11*0.7*RO2
    rate_values[848] = 1.00e-11*0.3*RO2
    rate_values[849] = KAPHO2*0.56
    rate_values[850] = KAPHO2*0.44
    rate_values[851] = KAPNO
    rate_values[852] = KFPAN
    rate_values[853] = KRO2NO3*1.74
    rate_values[854] = 1.00e-11*RO2
    rate_values[855] = 5.77e-11
    rate_values[856] = J[15]*2
    rate_values[857] = KAPHO2*0.44
    rate_values[858] = KAPHO2*0.56
    rate_values[859] = KAPNO
    rate_values[860] = KFPAN
    rate_values[861] = KRO2NO3*1.74
    rate_values[862] = 1.00e-11*RO2
    rate_values[863] = 1.86e-11
    rate_values[864] = J[41]
    rate_values[865] = J[34]
    rate_values[866] = 7.82e-12
    rate_values[867] = J[55]
    rate_values[868] = J[34]
    rate_values[869] = KDEC
    rate_values[870] = 1.75e-11
    rate_values[871] = J[34]
    rate_values[872] = 3.31e-11
    rate_values[873] = J[41]
    rate_values[874] = KDEC
    rate_values[875] = KNO3AL*5.5
    rate_values[876] = 2.37e-11
    rate_values[877] = J[15]
    rate_values[878] = J[35]
    rate_values[879] = J[34]
    rate_values[880] = 1.23e-11
    rate_values[881] = J[41]
    rate_values[882] = J[15]
    rate_values[883] = 1.58e-11
    rate_values[884] = KBPAN
    rate_values[885] = 1.22e-11
    rate_values[886] = J[22]
    rate_values[887] = J[41]
    rate_values[888] = 7.34e-12
    rate_values[889] = KBPAN
    rate_values[890] = 3.74e-12
    rate_values[891] = 1.68e-11
    rate_values[892] = J[41]
    rate_values[893] = 1.32e-11
    rate_values[894] = KBPAN
    rate_values[895] = 6.69e-11
    rate_values[896] = J[34]
    rate_values[897] = J[15]
    rate_values[898] = KRO2HO2*0.706
    rate_values[899] = KRO2NO
    rate_values[900] = KRO2NO3
    rate_values[901] = 8.8e-13*RO2
    rate_values[902] = KRO2HO2*0.625
    rate_values[903] = KRO2NO
    rate_values[904] = KRO2NO3
    rate_values[905] = 8.80e-13*RO2
    rate_values[906] = KAPHO2*0.44
    rate_values[907] = KAPHO2*0.56
    rate_values[908] = KAPNO
    rate_values[909] = KFPAN
    rate_values[910] = KRO2NO3*1.74
    rate_values[911] = 1.00e-11*RO2
    rate_values[912] = KRO2HO2*0.625
    rate_values[913] = KRO2NO
    rate_values[914] = KRO2NO3
    rate_values[915] = 2.00e-12*RO2
    rate_values[916] = J[41]
    rate_values[917] = J[22]
    rate_values[918] = 3.38e-11
    rate_values[919] = KDEC
    rate_values[920] = 7.46e-11
    rate_values[921] = J[41]
    rate_values[922] = KDEC
    rate_values[923] = 6.55e-12
    rate_values[924] = J[41]
    rate_values[925] = J[35]
    rate_values[926] = 2.92e-12
    rate_values[927] = KBPAN
    rate_values[928] = 9.61e-12
    rate_values[929] = J[41]
    rate_values[930] = J[35]
    rate_values[931] = KDEC
    rate_values[932] = 1.44e-11
    rate_values[933] = J[34]
    rate_values[934] = J[35]
    rate_values[935] = 1.2e-12*numpy.exp(490/TEMP)*0.65
    rate_values[936] = 1.2e-12*numpy.exp(490/TEMP)*0.35
    rate_values[937] = 1.2e-11*numpy.exp(440/TEMP)*0.522
    rate_values[938] = 1.2e-11*numpy.exp(440/TEMP)*0.333
    rate_values[939] = 1.2e-11*numpy.exp(440/TEMP)*0.065
    rate_values[940] = 6.3e-16*numpy.exp(-580/TEMP)*0.59
    rate_values[941] = 6.3e-16*numpy.exp(-580/TEMP)*0.38
    rate_values[942] = 6.3e-16*numpy.exp(-580/TEMP)*0.03
    rate_values[943] = 6.3e-16*numpy.exp(-580/TEMP)*0.00
    rate_values[944] = 1.2e-11*numpy.exp(440/TEMP)*0.08
    rate_values[945] = 1.2e-11*numpy.exp(440/TEMP)*0.00

    return rate_values
