# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 13.2.0 for Linux x86 (64-bit) (December 7, 2022)
# Date: Thu 13 Apr 2023 07:48:10



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 91.188,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])

# User-defined parameters.
KHHH = Parameter(name = 'KHHH',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{KHHH}',
                 lhablock = 'H3',
                 lhacode = [ 1 ])

KHTT = Parameter(name = 'KHTT',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{KHTT}',
                 lhablock = 'HQQ',
                 lhacode = [ 1 ])

KHBB = Parameter(name = 'KHBB',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{KHBB}',
                 lhablock = 'HQQ',
                 lhacode = [ 2 ])

KS01BB = Parameter(name = 'KS01BB',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KS01BB}',
                   lhablock = 'KBBS0',
                   lhacode = [ 1 ])

KS02BB = Parameter(name = 'KS02BB',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KS02BB}',
                   lhablock = 'KBBS0',
                   lhacode = [ 2 ])

KHB1B1 = Parameter(name = 'KHB1B1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHB1B1}',
                   lhablock = 'KHBBD',
                   lhacode = [ 1 ])

KHB2B2 = Parameter(name = 'KHB2B2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHB2B2}',
                   lhablock = 'KHBBD',
                   lhacode = [ 2 ])

KHB3B3 = Parameter(name = 'KHB3B3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHB3B3}',
                   lhablock = 'KHBBD',
                   lhacode = [ 3 ])

KHB1B2L = Parameter(name = 'KHB1B2L',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHB1B2L}',
                    lhablock = 'KHBBOL',
                    lhacode = [ 1 ])

KHB1B3L = Parameter(name = 'KHB1B3L',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHB1B3L}',
                    lhablock = 'KHBBOL',
                    lhacode = [ 2 ])

KHB2B3L = Parameter(name = 'KHB2B3L',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHB2B3L}',
                    lhablock = 'KHBBOL',
                    lhacode = [ 3 ])

KHB1B2R = Parameter(name = 'KHB1B2R',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHB1B2R}',
                    lhablock = 'KHBBOR',
                    lhacode = [ 1 ])

KHB1B3R = Parameter(name = 'KHB1B3R',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHB1B3R}',
                    lhablock = 'KHBBOR',
                    lhacode = [ 2 ])

KHB2B3R = Parameter(name = 'KHB2B3R',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHB2B3R}',
                    lhablock = 'KHBBOR',
                    lhacode = [ 3 ])

KHB1BL = Parameter(name = 'KHB1BL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHB1BL}',
                   lhablock = 'KHBBSML',
                   lhacode = [ 1 ])

KHB2BL = Parameter(name = 'KHB2BL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHB2BL}',
                   lhablock = 'KHBBSML',
                   lhacode = [ 2 ])

KHB3BL = Parameter(name = 'KHB3BL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHB3BL}',
                   lhablock = 'KHBBSML',
                   lhacode = [ 3 ])

KHB1BR = Parameter(name = 'KHB1BR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHB1BR}',
                   lhablock = 'KHBBSMR',
                   lhacode = [ 1 ])

KHB2BR = Parameter(name = 'KHB2BR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHB2BR}',
                   lhablock = 'KHBBSMR',
                   lhacode = [ 2 ])

KHB3BR = Parameter(name = 'KHB3BR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHB3BR}',
                   lhablock = 'KHBBSMR',
                   lhacode = [ 3 ])

KHHS01 = Parameter(name = 'KHHS01',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHHS01}',
                   lhablock = 'KHHS0',
                   lhacode = [ 1 ])

KHHS02 = Parameter(name = 'KHHS02',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHHS02}',
                   lhablock = 'KHHS0',
                   lhacode = [ 2 ])

KHHSQ1SQ1 = Parameter(name = 'KHHSQ1SQ1',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{KHHSQ1SQ1}',
                      lhablock = 'KHHSQSQD',
                      lhacode = [ 1 ])

KHHSQ2SQ2 = Parameter(name = 'KHHSQ2SQ2',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{KHHSQ2SQ2}',
                      lhablock = 'KHHSQSQD',
                      lhacode = [ 2 ])

KHHSQ3SQ3 = Parameter(name = 'KHHSQ3SQ3',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{KHHSQ3SQ3}',
                      lhablock = 'KHHSQSQD',
                      lhacode = [ 3 ])

KHHSQ4SQ4 = Parameter(name = 'KHHSQ4SQ4',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{KHHSQ4SQ4}',
                      lhablock = 'KHHSQSQD',
                      lhacode = [ 4 ])

KHHSQ1SQ2 = Parameter(name = 'KHHSQ1SQ2',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{KHHSQ1SQ2}',
                      lhablock = 'KHHSQSQO',
                      lhacode = [ 1 ])

KHHSQ1SQ3 = Parameter(name = 'KHHSQ1SQ3',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{KHHSQ1SQ3}',
                      lhablock = 'KHHSQSQO',
                      lhacode = [ 2 ])

KHHSQ1SQ4 = Parameter(name = 'KHHSQ1SQ4',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{KHHSQ1SQ4}',
                      lhablock = 'KHHSQSQO',
                      lhacode = [ 3 ])

KHHSQ2SQ3 = Parameter(name = 'KHHSQ2SQ3',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{KHHSQ2SQ3}',
                      lhablock = 'KHHSQSQO',
                      lhacode = [ 4 ])

KHHSQ2SQ4 = Parameter(name = 'KHHSQ2SQ4',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{KHHSQ2SQ4}',
                      lhablock = 'KHHSQSQO',
                      lhacode = [ 5 ])

KHHSQ3SQ4 = Parameter(name = 'KHHSQ3SQ4',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{KHHSQ3SQ4}',
                      lhablock = 'KHHSQSQO',
                      lhacode = [ 6 ])

KHSQ1SQ1 = Parameter(name = 'KHSQ1SQ1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KHSQ1SQ1}',
                     lhablock = 'KHSQSQD',
                     lhacode = [ 1 ])

KHSQ2SQ2 = Parameter(name = 'KHSQ2SQ2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KHSQ2SQ2}',
                     lhablock = 'KHSQSQD',
                     lhacode = [ 2 ])

KHSQ3SQ3 = Parameter(name = 'KHSQ3SQ3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KHSQ3SQ3}',
                     lhablock = 'KHSQSQD',
                     lhacode = [ 3 ])

KHSQ4SQ4 = Parameter(name = 'KHSQ4SQ4',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KHSQ4SQ4}',
                     lhablock = 'KHSQSQD',
                     lhacode = [ 4 ])

KHSQ1SQ2 = Parameter(name = 'KHSQ1SQ2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KHSQ1SQ2}',
                     lhablock = 'KHSQSQO',
                     lhacode = [ 1 ])

KHSQ1SQ3 = Parameter(name = 'KHSQ1SQ3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KHSQ1SQ3}',
                     lhablock = 'KHSQSQO',
                     lhacode = [ 2 ])

KHSQ1SQ4 = Parameter(name = 'KHSQ1SQ4',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KHSQ1SQ4}',
                     lhablock = 'KHSQSQO',
                     lhacode = [ 3 ])

KHSQ2SQ3 = Parameter(name = 'KHSQ2SQ3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KHSQ2SQ3}',
                     lhablock = 'KHSQSQO',
                     lhacode = [ 4 ])

KHSQ2SQ4 = Parameter(name = 'KHSQ2SQ4',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KHSQ2SQ4}',
                     lhablock = 'KHSQSQO',
                     lhacode = [ 5 ])

KHSQ3SQ4 = Parameter(name = 'KHSQ3SQ4',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KHSQ3SQ4}',
                     lhablock = 'KHSQSQO',
                     lhacode = [ 6 ])

KHT1T1 = Parameter(name = 'KHT1T1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHT1T1}',
                   lhablock = 'KHTTD',
                   lhacode = [ 1 ])

KHT2T2 = Parameter(name = 'KHT2T2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHT2T2}',
                   lhablock = 'KHTTD',
                   lhacode = [ 2 ])

KHT3T3 = Parameter(name = 'KHT3T3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHT3T3}',
                   lhablock = 'KHTTD',
                   lhacode = [ 3 ])

KHT4T4 = Parameter(name = 'KHT4T4',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHT4T4}',
                   lhablock = 'KHTTD',
                   lhacode = [ 4 ])

KHT1T2L = Parameter(name = 'KHT1T2L',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHT1T2L}',
                    lhablock = 'KHTTOL',
                    lhacode = [ 1 ])

KHT1T3L = Parameter(name = 'KHT1T3L',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHT1T3L}',
                    lhablock = 'KHTTOL',
                    lhacode = [ 2 ])

KHT1T4L = Parameter(name = 'KHT1T4L',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHT1T4L}',
                    lhablock = 'KHTTOL',
                    lhacode = [ 3 ])

KHT2T3L = Parameter(name = 'KHT2T3L',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHT2T3L}',
                    lhablock = 'KHTTOL',
                    lhacode = [ 4 ])

KHT2T4L = Parameter(name = 'KHT2T4L',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHT2T4L}',
                    lhablock = 'KHTTOL',
                    lhacode = [ 5 ])

KHT3T4L = Parameter(name = 'KHT3T4L',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHT3T4L}',
                    lhablock = 'KHTTOL',
                    lhacode = [ 6 ])

KHT1T2R = Parameter(name = 'KHT1T2R',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHT1T2R}',
                    lhablock = 'KHTTOR',
                    lhacode = [ 1 ])

KHT1T3R = Parameter(name = 'KHT1T3R',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHT1T3R}',
                    lhablock = 'KHTTOR',
                    lhacode = [ 2 ])

KHT1T4R = Parameter(name = 'KHT1T4R',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHT1T4R}',
                    lhablock = 'KHTTOR',
                    lhacode = [ 3 ])

KHT2T3R = Parameter(name = 'KHT2T3R',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHT2T3R}',
                    lhablock = 'KHTTOR',
                    lhacode = [ 4 ])

KHT2T4R = Parameter(name = 'KHT2T4R',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHT2T4R}',
                    lhablock = 'KHTTOR',
                    lhacode = [ 5 ])

KHT3T4R = Parameter(name = 'KHT3T4R',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{KHT3T4R}',
                    lhablock = 'KHTTOR',
                    lhacode = [ 6 ])

KHT1TL = Parameter(name = 'KHT1TL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHT1TL}',
                   lhablock = 'KHTTSML',
                   lhacode = [ 1 ])

KHT2TL = Parameter(name = 'KHT2TL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHT2TL}',
                   lhablock = 'KHTTSML',
                   lhacode = [ 2 ])

KHT3TL = Parameter(name = 'KHT3TL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHT3TL}',
                   lhablock = 'KHTTSML',
                   lhacode = [ 3 ])

KHT4TL = Parameter(name = 'KHT4TL',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHT4TL}',
                   lhablock = 'KHTTSML',
                   lhacode = [ 4 ])

KHT1TR = Parameter(name = 'KHT1TR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHT1TR}',
                   lhablock = 'KHTTSMR',
                   lhacode = [ 1 ])

KHT2TR = Parameter(name = 'KHT2TR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHT2TR}',
                   lhablock = 'KHTTSMR',
                   lhacode = [ 2 ])

KHT3TR = Parameter(name = 'KHT3TR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHT3TR}',
                   lhablock = 'KHTTSMR',
                   lhacode = [ 3 ])

KHT4TR = Parameter(name = 'KHT4TR',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KHT4TR}',
                   lhablock = 'KHTTSMR',
                   lhacode = [ 4 ])

KS01B1B1 = Parameter(name = 'KS01B1B1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KS01B1B1}',
                     lhablock = 'KS01BPBP',
                     lhacode = [ 1 ])

KS01B2B2 = Parameter(name = 'KS01B2B2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KS01B2B2}',
                     lhablock = 'KS01BPBP',
                     lhacode = [ 2 ])

KS01SQ1SQ1 = Parameter(name = 'KS01SQ1SQ1',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{KS01SQ1SQ1}',
                       lhablock = 'KS01SQSQ',
                       lhacode = [ 1 ])

KS01SQ2SQ2 = Parameter(name = 'KS01SQ2SQ2',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{KS01SQ2SQ2}',
                       lhablock = 'KS01SQSQ',
                       lhacode = [ 2 ])

KS01SQ3SQ3 = Parameter(name = 'KS01SQ3SQ3',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{KS01SQ3SQ3}',
                       lhablock = 'KS01SQSQ',
                       lhacode = [ 3 ])

KS01T1T1 = Parameter(name = 'KS01T1T1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KS01T1T1}',
                     lhablock = 'KS01TPTP',
                     lhacode = [ 1 ])

KS01T2T2 = Parameter(name = 'KS01T2T2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KS01T2T2}',
                     lhablock = 'KS01TPTP',
                     lhacode = [ 2 ])

KS02B1B1 = Parameter(name = 'KS02B1B1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KS02B1B1}',
                     lhablock = 'KS02BPBP',
                     lhacode = [ 1 ])

KS02B2B2 = Parameter(name = 'KS02B2B2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KS02B2B2}',
                     lhablock = 'KS02BPBP',
                     lhacode = [ 2 ])

KS02SQ1SQ1 = Parameter(name = 'KS02SQ1SQ1',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{KS02SQ1SQ1}',
                       lhablock = 'KS02SQSQ',
                       lhacode = [ 1 ])

KS02SQ2SQ2 = Parameter(name = 'KS02SQ2SQ2',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{KS02SQ2SQ2}',
                       lhablock = 'KS02SQSQ',
                       lhacode = [ 2 ])

KS02T1T1 = Parameter(name = 'KS02T1T1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KS02T1T1}',
                     lhablock = 'KS02TPTP',
                     lhacode = [ 1 ])

KS02T2T2 = Parameter(name = 'KS02T2T2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{KS02T2T2}',
                     lhablock = 'KS02TPTP',
                     lhacode = [ 2 ])

KS01TT = Parameter(name = 'KS01TT',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KS01TT}',
                   lhablock = 'KTTS0',
                   lhacode = [ 1 ])

KS02TT = Parameter(name = 'KS02TT',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{KS02TT}',
                   lhablock = 'KTTS0',
                   lhacode = [ 2 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MS01 = Parameter(name = 'MS01',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{MS01}',
                 lhablock = 'MASS',
                 lhacode = [ 6100001 ])

MS02 = Parameter(name = 'MS02',
                 nature = 'external',
                 type = 'real',
                 value = 150,
                 texname = '\\text{MS02}',
                 lhablock = 'MASS',
                 lhacode = [ 6100002 ])

MTP1 = Parameter(name = 'MTP1',
                 nature = 'external',
                 type = 'real',
                 value = 1100,
                 texname = '\\text{MTP1}',
                 lhablock = 'MASS',
                 lhacode = [ 6000101 ])

MTP2 = Parameter(name = 'MTP2',
                 nature = 'external',
                 type = 'real',
                 value = 1200,
                 texname = '\\text{MTP2}',
                 lhablock = 'MASS',
                 lhacode = [ 6000102 ])

MTP3 = Parameter(name = 'MTP3',
                 nature = 'external',
                 type = 'real',
                 value = 1300,
                 texname = '\\text{MTP3}',
                 lhablock = 'MASS',
                 lhacode = [ 6000103 ])

MTP4 = Parameter(name = 'MTP4',
                 nature = 'external',
                 type = 'real',
                 value = 1400,
                 texname = '\\text{MTP4}',
                 lhablock = 'MASS',
                 lhacode = [ 6000104 ])

MBP1 = Parameter(name = 'MBP1',
                 nature = 'external',
                 type = 'real',
                 value = 1500,
                 texname = '\\text{MBP1}',
                 lhablock = 'MASS',
                 lhacode = [ 6000201 ])

MBP2 = Parameter(name = 'MBP2',
                 nature = 'external',
                 type = 'real',
                 value = 1600,
                 texname = '\\text{MBP2}',
                 lhablock = 'MASS',
                 lhacode = [ 6000202 ])

MBP3 = Parameter(name = 'MBP3',
                 nature = 'external',
                 type = 'real',
                 value = 1700,
                 texname = '\\text{MBP3}',
                 lhablock = 'MASS',
                 lhacode = [ 6000203 ])

MSQ1 = Parameter(name = 'MSQ1',
                 nature = 'external',
                 type = 'real',
                 value = 1100,
                 texname = '\\text{MSQ1}',
                 lhablock = 'MASS',
                 lhacode = [ 6000001 ])

MSQ2 = Parameter(name = 'MSQ2',
                 nature = 'external',
                 type = 'real',
                 value = 1200,
                 texname = '\\text{MSQ2}',
                 lhablock = 'MASS',
                 lhacode = [ 6000002 ])

MSQ3 = Parameter(name = 'MSQ3',
                 nature = 'external',
                 type = 'real',
                 value = 1300,
                 texname = '\\text{MSQ3}',
                 lhablock = 'MASS',
                 lhacode = [ 6000003 ])

MSQ4 = Parameter(name = 'MSQ4',
                 nature = 'external',
                 type = 'real',
                 value = 1400,
                 texname = '\\text{MSQ4}',
                 lhablock = 'MASS',
                 lhacode = [ 6000004 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WS01 = Parameter(name = 'WS01',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WS01}',
                 lhablock = 'DECAY',
                 lhacode = [ 6100001 ])

WS02 = Parameter(name = 'WS02',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WS02}',
                 lhablock = 'DECAY',
                 lhacode = [ 6100002 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

KHBPBP1x1 = Parameter(name = 'KHBPBP1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHB1B1/2.',
                      texname = '\\text{KHBPBP1x1}')

KHBPBP1x2 = Parameter(name = 'KHBPBP1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHB1B2L/2.',
                      texname = '\\text{KHBPBP1x2}')

KHBPBP1x3 = Parameter(name = 'KHBPBP1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHB1B3L/2.',
                      texname = '\\text{KHBPBP1x3}')

KHBPBP2x1 = Parameter(name = 'KHBPBP2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHB1B2R/2.',
                      texname = '\\text{KHBPBP2x1}')

KHBPBP2x2 = Parameter(name = 'KHBPBP2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHB2B2/2.',
                      texname = '\\text{KHBPBP2x2}')

KHBPBP2x3 = Parameter(name = 'KHBPBP2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHB2B3L/2.',
                      texname = '\\text{KHBPBP2x3}')

KHBPBP3x1 = Parameter(name = 'KHBPBP3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHB1B3R/2.',
                      texname = '\\text{KHBPBP3x1}')

KHBPBP3x2 = Parameter(name = 'KHBPBP3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHB2B3R/2.',
                      texname = '\\text{KHBPBP3x2}')

KHBPBP3x3 = Parameter(name = 'KHBPBP3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHB3B3/2.',
                      texname = '\\text{KHBPBP3x3}')

KHBSML1 = Parameter(name = 'KHBSML1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHB1BL',
                    texname = '\\text{KHBSML1}')

KHBSML2 = Parameter(name = 'KHBSML2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHB2BL',
                    texname = '\\text{KHBSML2}')

KHBSML3 = Parameter(name = 'KHBSML3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHB3BL',
                    texname = '\\text{KHBSML3}')

KHBSMR1 = Parameter(name = 'KHBSMR1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHB1BR',
                    texname = '\\text{KHBSMR1}')

KHBSMR2 = Parameter(name = 'KHBSMR2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHB2BR',
                    texname = '\\text{KHBSMR2}')

KHBSMR3 = Parameter(name = 'KHBSMR3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHB3BR',
                    texname = '\\text{KHBSMR3}')

KHHSQSQ1x1 = Parameter(name = 'KHHSQSQ1x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ1SQ1',
                       texname = '\\text{KHHSQSQ1x1}')

KHHSQSQ1x2 = Parameter(name = 'KHHSQSQ1x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ1SQ2',
                       texname = '\\text{KHHSQSQ1x2}')

KHHSQSQ1x3 = Parameter(name = 'KHHSQSQ1x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ1SQ3',
                       texname = '\\text{KHHSQSQ1x3}')

KHHSQSQ1x4 = Parameter(name = 'KHHSQSQ1x4',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ1SQ4',
                       texname = '\\text{KHHSQSQ1x4}')

KHHSQSQ2x1 = Parameter(name = 'KHHSQSQ2x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ1SQ2',
                       texname = '\\text{KHHSQSQ2x1}')

KHHSQSQ2x2 = Parameter(name = 'KHHSQSQ2x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ2SQ2',
                       texname = '\\text{KHHSQSQ2x2}')

KHHSQSQ2x3 = Parameter(name = 'KHHSQSQ2x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ2SQ3',
                       texname = '\\text{KHHSQSQ2x3}')

KHHSQSQ2x4 = Parameter(name = 'KHHSQSQ2x4',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ2SQ4',
                       texname = '\\text{KHHSQSQ2x4}')

KHHSQSQ3x1 = Parameter(name = 'KHHSQSQ3x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ1SQ3',
                       texname = '\\text{KHHSQSQ3x1}')

KHHSQSQ3x2 = Parameter(name = 'KHHSQSQ3x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ2SQ3',
                       texname = '\\text{KHHSQSQ3x2}')

KHHSQSQ3x3 = Parameter(name = 'KHHSQSQ3x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ3SQ3',
                       texname = '\\text{KHHSQSQ3x3}')

KHHSQSQ3x4 = Parameter(name = 'KHHSQSQ3x4',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ3SQ4',
                       texname = '\\text{KHHSQSQ3x4}')

KHHSQSQ4x1 = Parameter(name = 'KHHSQSQ4x1',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ1SQ4',
                       texname = '\\text{KHHSQSQ4x1}')

KHHSQSQ4x2 = Parameter(name = 'KHHSQSQ4x2',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ2SQ4',
                       texname = '\\text{KHHSQSQ4x2}')

KHHSQSQ4x3 = Parameter(name = 'KHHSQSQ4x3',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ3SQ4',
                       texname = '\\text{KHHSQSQ4x3}')

KHHSQSQ4x4 = Parameter(name = 'KHHSQSQ4x4',
                       nature = 'internal',
                       type = 'real',
                       value = 'KHHSQ4SQ4',
                       texname = '\\text{KHHSQSQ4x4}')

KHTPTP1x1 = Parameter(name = 'KHTPTP1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT1T1/2.',
                      texname = '\\text{KHTPTP1x1}')

KHTPTP1x2 = Parameter(name = 'KHTPTP1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT1T2L/2.',
                      texname = '\\text{KHTPTP1x2}')

KHTPTP1x3 = Parameter(name = 'KHTPTP1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT1T3L/2.',
                      texname = '\\text{KHTPTP1x3}')

KHTPTP1x4 = Parameter(name = 'KHTPTP1x4',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT1T4L/2.',
                      texname = '\\text{KHTPTP1x4}')

KHTPTP2x1 = Parameter(name = 'KHTPTP2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT1T2R/2.',
                      texname = '\\text{KHTPTP2x1}')

KHTPTP2x2 = Parameter(name = 'KHTPTP2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT2T2/2.',
                      texname = '\\text{KHTPTP2x2}')

KHTPTP2x3 = Parameter(name = 'KHTPTP2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT2T3L/2.',
                      texname = '\\text{KHTPTP2x3}')

KHTPTP2x4 = Parameter(name = 'KHTPTP2x4',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT2T4L/2.',
                      texname = '\\text{KHTPTP2x4}')

KHTPTP3x1 = Parameter(name = 'KHTPTP3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT1T3R/2.',
                      texname = '\\text{KHTPTP3x1}')

KHTPTP3x2 = Parameter(name = 'KHTPTP3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT2T3R/2.',
                      texname = '\\text{KHTPTP3x2}')

KHTPTP3x3 = Parameter(name = 'KHTPTP3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT3T3/2.',
                      texname = '\\text{KHTPTP3x3}')

KHTPTP3x4 = Parameter(name = 'KHTPTP3x4',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT3T4L/2.',
                      texname = '\\text{KHTPTP3x4}')

KHTPTP4x1 = Parameter(name = 'KHTPTP4x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT1T4R/2.',
                      texname = '\\text{KHTPTP4x1}')

KHTPTP4x2 = Parameter(name = 'KHTPTP4x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT2T4R/2.',
                      texname = '\\text{KHTPTP4x2}')

KHTPTP4x3 = Parameter(name = 'KHTPTP4x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT3T4R/2.',
                      texname = '\\text{KHTPTP4x3}')

KHTPTP4x4 = Parameter(name = 'KHTPTP4x4',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHT4T4/2.',
                      texname = '\\text{KHTPTP4x4}')

KHTSML1 = Parameter(name = 'KHTSML1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHT1TL',
                    texname = '\\text{KHTSML1}')

KHTSML2 = Parameter(name = 'KHTSML2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHT2TL',
                    texname = '\\text{KHTSML2}')

KHTSML3 = Parameter(name = 'KHTSML3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHT3TL',
                    texname = '\\text{KHTSML3}')

KHTSML4 = Parameter(name = 'KHTSML4',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHT4TL',
                    texname = '\\text{KHTSML4}')

KHTSMR1 = Parameter(name = 'KHTSMR1',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHT1TR',
                    texname = '\\text{KHTSMR1}')

KHTSMR2 = Parameter(name = 'KHTSMR2',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHT2TR',
                    texname = '\\text{KHTSMR2}')

KHTSMR3 = Parameter(name = 'KHTSMR3',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHT3TR',
                    texname = '\\text{KHTSMR3}')

KHTSMR4 = Parameter(name = 'KHTSMR4',
                    nature = 'internal',
                    type = 'real',
                    value = 'KHT4TR',
                    texname = '\\text{KHTSMR4}')

KHSQSQ1x1 = Parameter(name = 'KHSQSQ1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ1SQ1',
                      texname = '\\text{KHSQSQ1x1}')

KHSQSQ1x2 = Parameter(name = 'KHSQSQ1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ1SQ2',
                      texname = '\\text{KHSQSQ1x2}')

KHSQSQ1x3 = Parameter(name = 'KHSQSQ1x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ1SQ3',
                      texname = '\\text{KHSQSQ1x3}')

KHSQSQ1x4 = Parameter(name = 'KHSQSQ1x4',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ1SQ4',
                      texname = '\\text{KHSQSQ1x4}')

KHSQSQ2x1 = Parameter(name = 'KHSQSQ2x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ1SQ2',
                      texname = '\\text{KHSQSQ2x1}')

KHSQSQ2x2 = Parameter(name = 'KHSQSQ2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ2SQ2',
                      texname = '\\text{KHSQSQ2x2}')

KHSQSQ2x3 = Parameter(name = 'KHSQSQ2x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ2SQ3',
                      texname = '\\text{KHSQSQ2x3}')

KHSQSQ2x4 = Parameter(name = 'KHSQSQ2x4',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ2SQ4',
                      texname = '\\text{KHSQSQ2x4}')

KHSQSQ3x1 = Parameter(name = 'KHSQSQ3x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ1SQ3',
                      texname = '\\text{KHSQSQ3x1}')

KHSQSQ3x2 = Parameter(name = 'KHSQSQ3x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ2SQ3',
                      texname = '\\text{KHSQSQ3x2}')

KHSQSQ3x3 = Parameter(name = 'KHSQSQ3x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ3SQ3',
                      texname = '\\text{KHSQSQ3x3}')

KHSQSQ3x4 = Parameter(name = 'KHSQSQ3x4',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ3SQ4',
                      texname = '\\text{KHSQSQ3x4}')

KHSQSQ4x1 = Parameter(name = 'KHSQSQ4x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ1SQ4',
                      texname = '\\text{KHSQSQ4x1}')

KHSQSQ4x2 = Parameter(name = 'KHSQSQ4x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ2SQ4',
                      texname = '\\text{KHSQSQ4x2}')

KHSQSQ4x3 = Parameter(name = 'KHSQSQ4x3',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ3SQ4',
                      texname = '\\text{KHSQSQ4x3}')

KHSQSQ4x4 = Parameter(name = 'KHSQSQ4x4',
                      nature = 'internal',
                      type = 'real',
                      value = 'KHSQ4SQ4',
                      texname = '\\text{KHSQSQ4x4}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

