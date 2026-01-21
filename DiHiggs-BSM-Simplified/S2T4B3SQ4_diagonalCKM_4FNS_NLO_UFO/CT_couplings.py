# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 13.2.0 for Linux x86 (64-bit) (December 7, 2022)
# Date: Thu 13 Apr 2023 07:48:10


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



R2GC_112_1 = Coupling(name = 'R2GC_112_1',
                      value = '-0.0625*(complex(0,1)*G**2)/cmath.pi**2',
                      order = {'QCD':2})

R2GC_113_2 = Coupling(name = 'R2GC_113_2',
                      value = '(complex(0,1)*G**2)/(12.*cmath.pi**2)',
                      order = {'QCD':2})

R2GC_114_3 = Coupling(name = 'R2GC_114_3',
                      value = '-0.1111111111111111*(ee*complex(0,1)*G**2)/cmath.pi**2',
                      order = {'QCD':2,'QED':1})

R2GC_115_4 = Coupling(name = 'R2GC_115_4',
                      value = '(ee*complex(0,1)*G**2*sw)/(9.*cw*cmath.pi**2)',
                      order = {'QCD':2,'QED':1})

R2GC_117_5 = Coupling(name = 'R2GC_117_5',
                      value = '-0.05555555555555555*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2)',
                      order = {'QCD':2,'QED':1})

#R2GC_122_6 = Coupling(name = 'R2GC_122_6',
                      #value = '(complex(0,1)*G**2*KHBB*KS01BB)/(8.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*KS01BB*yb)/(8.*cmath.pi**2*cmath.sqrt(2))',
                      #order = {'HBBMOD':1,'QCD':2,'S01BB':1})

R2GC_122_7 = Coupling(name = 'R2GC_122_7',
                      value = '-0.125*(complex(0,1)*G**2*KHBPBP1x1*KS01B1B1)/cmath.pi**2',
                      order = {'HB1B1':1,'QCD':2,'S01B1B1':1})

R2GC_122_8 = Coupling(name = 'R2GC_122_8',
                      value = '-0.125*(complex(0,1)*G**2*KHBPBP2x2*KS01B2B2)/cmath.pi**2',
                      order = {'HB2B2':1,'QCD':2,'S01B2B2':1})

#R2GC_122_9 = Coupling(name = 'R2GC_122_9',
                      #value = '(complex(0,1)*G**2*KHTT*KS01TT)/(8.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*KS01TT*yt)/(8.*cmath.pi**2*cmath.sqrt(2))',
                      #order = {'HTTMOD':1,'QCD':2,'S01TT':1})

R2GC_122_10 = Coupling(name = 'R2GC_122_10',
                       value = '-0.125*(complex(0,1)*G**2*KHTPTP1x1*KS01T1T1)/cmath.pi**2',
                       order = {'HT1T1':1,'QCD':2,'S01T1T1':1})

R2GC_122_11 = Coupling(name = 'R2GC_122_11',
                       value = '-0.125*(complex(0,1)*G**2*KHTPTP2x2*KS01T2T2)/cmath.pi**2',
                       order = {'HT2T2':1,'QCD':2,'S01T2T2':1})

R2GC_123_12 = Coupling(name = 'R2GC_123_12',
                       value = '-0.125*(complex(0,1)*G**2*KS01BB**2)/cmath.pi**2',
                       order = {'QCD':2,'S01BB':2})

R2GC_123_13 = Coupling(name = 'R2GC_123_13',
                       value = '-0.125*(complex(0,1)*G**2*KS01B1B1**2)/cmath.pi**2',
                       order = {'QCD':2,'S01B1B1':2})

R2GC_123_14 = Coupling(name = 'R2GC_123_14',
                       value = '-0.125*(complex(0,1)*G**2*KS01B2B2**2)/cmath.pi**2',
                       order = {'QCD':2,'S01B2B2':2})

R2GC_123_15 = Coupling(name = 'R2GC_123_15',
                       value = '-0.125*(complex(0,1)*G**2*KS01TT**2)/cmath.pi**2',
                       order = {'QCD':2,'S01TT':2})

R2GC_123_16 = Coupling(name = 'R2GC_123_16',
                       value = '-0.125*(complex(0,1)*G**2*KS01T1T1**2)/cmath.pi**2',
                       order = {'QCD':2,'S01T1T1':2})

R2GC_123_17 = Coupling(name = 'R2GC_123_17',
                       value = '-0.125*(complex(0,1)*G**2*KS01T2T2**2)/cmath.pi**2',
                       order = {'QCD':2,'S01T2T2':2})

#R2GC_124_18 = Coupling(name = 'R2GC_124_18',
                       #value = '(complex(0,1)*G**2*KHBB*KS02BB)/(8.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*KS02BB*yb)/(8.*cmath.pi**2*cmath.sqrt(2))',
                       #order = {'HBBMOD':1,'QCD':2,'S02BB':1})

R2GC_124_19 = Coupling(name = 'R2GC_124_19',
                       value = '-0.125*(complex(0,1)*G**2*KHBPBP1x1*KS02B1B1)/cmath.pi**2',
                       order = {'HB1B1':1,'QCD':2,'S02B1B1':1})

R2GC_124_20 = Coupling(name = 'R2GC_124_20',
                       value = '-0.125*(complex(0,1)*G**2*KHBPBP2x2*KS02B2B2)/cmath.pi**2',
                       order = {'HB2B2':1,'QCD':2,'S02B2B2':1})

#R2GC_124_21 = Coupling(name = 'R2GC_124_21',
                       #value = '(complex(0,1)*G**2*KHTT*KS02TT)/(8.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*KS02TT*yt)/(8.*cmath.pi**2*cmath.sqrt(2))',
                       #order = {'HTTMOD':1,'QCD':2,'S02TT':1})

R2GC_124_22 = Coupling(name = 'R2GC_124_22',
                       value = '-0.125*(complex(0,1)*G**2*KHTPTP1x1*KS02T1T1)/cmath.pi**2',
                       order = {'HT1T1':1,'QCD':2,'S02T1T1':1})

R2GC_124_23 = Coupling(name = 'R2GC_124_23',
                       value = '-0.125*(complex(0,1)*G**2*KHTPTP2x2*KS02T2T2)/cmath.pi**2',
                       order = {'HT2T2':1,'QCD':2,'S02T2T2':1})

R2GC_125_24 = Coupling(name = 'R2GC_125_24',
                       value = '-0.125*(complex(0,1)*G**2*KS01BB*KS02BB)/cmath.pi**2',
                       order = {'QCD':2,'S01BB':1,'S02BB':1})

R2GC_125_25 = Coupling(name = 'R2GC_125_25',
                       value = '-0.125*(complex(0,1)*G**2*KS01B1B1*KS02B1B1)/cmath.pi**2',
                       order = {'QCD':2,'S01B1B1':1,'S02B1B1':1})

R2GC_125_26 = Coupling(name = 'R2GC_125_26',
                       value = '-0.125*(complex(0,1)*G**2*KS01B2B2*KS02B2B2)/cmath.pi**2',
                       order = {'QCD':2,'S01B2B2':1,'S02B2B2':1})

R2GC_125_27 = Coupling(name = 'R2GC_125_27',
                       value = '-0.125*(complex(0,1)*G**2*KS01TT*KS02TT)/cmath.pi**2',
                       order = {'QCD':2,'S01TT':1,'S02TT':1})

R2GC_125_28 = Coupling(name = 'R2GC_125_28',
                       value = '-0.125*(complex(0,1)*G**2*KS01T1T1*KS02T1T1)/cmath.pi**2',
                       order = {'QCD':2,'S01T1T1':1,'S02T1T1':1})

R2GC_125_29 = Coupling(name = 'R2GC_125_29',
                       value = '-0.125*(complex(0,1)*G**2*KS01T2T2*KS02T2T2)/cmath.pi**2',
                       order = {'QCD':2,'S01T2T2':1,'S02T2T2':1})

R2GC_126_30 = Coupling(name = 'R2GC_126_30',
                       value = '-0.125*(complex(0,1)*G**2*KS02BB**2)/cmath.pi**2',
                       order = {'QCD':2,'S02BB':2})

R2GC_126_31 = Coupling(name = 'R2GC_126_31',
                       value = '-0.125*(complex(0,1)*G**2*KS02B1B1**2)/cmath.pi**2',
                       order = {'QCD':2,'S02B1B1':2})

R2GC_126_32 = Coupling(name = 'R2GC_126_32',
                       value = '-0.125*(complex(0,1)*G**2*KS02B2B2**2)/cmath.pi**2',
                       order = {'QCD':2,'S02B2B2':2})

R2GC_126_33 = Coupling(name = 'R2GC_126_33',
                       value = '-0.125*(complex(0,1)*G**2*KS02TT**2)/cmath.pi**2',
                       order = {'QCD':2,'S02TT':2})

R2GC_126_34 = Coupling(name = 'R2GC_126_34',
                       value = '-0.125*(complex(0,1)*G**2*KS02T1T1**2)/cmath.pi**2',
                       order = {'QCD':2,'S02T1T1':2})

R2GC_126_35 = Coupling(name = 'R2GC_126_35',
                       value = '-0.125*(complex(0,1)*G**2*KS02T2T2**2)/cmath.pi**2',
                       order = {'QCD':2,'S02T2T2':2})

R2GC_127_36 = Coupling(name = 'R2GC_127_36',
                       value = '(complex(0,1)*G**2*KS01BB*MB)/(8.*cmath.pi**2)',
                       order = {'QCD':2,'S01BB':1})

R2GC_127_37 = Coupling(name = 'R2GC_127_37',
                       value = '(complex(0,1)*G**2*KS01B1B1*MBP1)/(8.*cmath.pi**2)',
                       order = {'QCD':2,'S01B1B1':1})

R2GC_127_38 = Coupling(name = 'R2GC_127_38',
                       value = '(complex(0,1)*G**2*KS01B2B2*MBP2)/(8.*cmath.pi**2)',
                       order = {'QCD':2,'S01B2B2':1})

R2GC_127_39 = Coupling(name = 'R2GC_127_39',
                       value = '(complex(0,1)*G**2*KS01TT*MT)/(8.*cmath.pi**2)',
                       order = {'QCD':2,'S01TT':1})

R2GC_127_40 = Coupling(name = 'R2GC_127_40',
                       value = '(complex(0,1)*G**2*KS01T1T1*MTP1)/(8.*cmath.pi**2)',
                       order = {'QCD':2,'S01T1T1':1})

R2GC_127_41 = Coupling(name = 'R2GC_127_41',
                       value = '(complex(0,1)*G**2*KS01T2T2*MTP2)/(8.*cmath.pi**2)',
                       order = {'QCD':2,'S01T2T2':1})

R2GC_128_42 = Coupling(name = 'R2GC_128_42',
                       value = '(complex(0,1)*G**2*KS02BB*MB)/(8.*cmath.pi**2)',
                       order = {'QCD':2,'S02BB':1})

R2GC_128_43 = Coupling(name = 'R2GC_128_43',
                       value = '(complex(0,1)*G**2*KS02B1B1*MBP1)/(8.*cmath.pi**2)',
                       order = {'QCD':2,'S02B1B1':1})

R2GC_128_44 = Coupling(name = 'R2GC_128_44',
                       value = '(complex(0,1)*G**2*KS02B2B2*MBP2)/(8.*cmath.pi**2)',
                       order = {'QCD':2,'S02B2B2':1})

R2GC_128_45 = Coupling(name = 'R2GC_128_45',
                       value = '(complex(0,1)*G**2*KS02TT*MT)/(8.*cmath.pi**2)',
                       order = {'QCD':2,'S02TT':1})

R2GC_128_46 = Coupling(name = 'R2GC_128_46',
                       value = '(complex(0,1)*G**2*KS02T1T1*MTP1)/(8.*cmath.pi**2)',
                       order = {'QCD':2,'S02T1T1':1})

R2GC_128_47 = Coupling(name = 'R2GC_128_47',
                       value = '(complex(0,1)*G**2*KS02T2T2*MTP2)/(8.*cmath.pi**2)',
                       order = {'QCD':2,'S02T2T2':1})

#R2GC_129_48 = Coupling(name = 'R2GC_129_48',
                       #value = '-0.125*(complex(0,1)*G**2*KHBB*MB)/(cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*MB*yb)/(8.*cmath.pi**2*cmath.sqrt(2))',
                       #order = {'HBBMOD':1,'QCD':2})

R2GC_129_49 = Coupling(name = 'R2GC_129_49',
                       value = '(complex(0,1)*G**2*KHBPBP1x1*MBP1)/(8.*cmath.pi**2)',
                       order = {'HB1B1':1,'QCD':2})

R2GC_129_50 = Coupling(name = 'R2GC_129_50',
                       value = '(complex(0,1)*G**2*KHBPBP2x2*MBP2)/(8.*cmath.pi**2)',
                       order = {'HB2B2':1,'QCD':2})

R2GC_129_51 = Coupling(name = 'R2GC_129_51',
                       value = '(complex(0,1)*G**2*KHBPBP3x3*MBP3)/(8.*cmath.pi**2)',
                       order = {'HB3B3':1,'QCD':2})

#R2GC_129_52 = Coupling(name = 'R2GC_129_52',
                       #value = '-0.125*(complex(0,1)*G**2*KHTT*MT)/(cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*MT*yt)/(8.*cmath.pi**2*cmath.sqrt(2))',
                       #order = {'HTTMOD':1,'QCD':2})

R2GC_129_53 = Coupling(name = 'R2GC_129_53',
                       value = '(complex(0,1)*G**2*KHTPTP1x1*MTP1)/(8.*cmath.pi**2)',
                       order = {'HT1T1':1,'QCD':2})

R2GC_129_54 = Coupling(name = 'R2GC_129_54',
                       value = '(complex(0,1)*G**2*KHTPTP2x2*MTP2)/(8.*cmath.pi**2)',
                       order = {'HT2T2':1,'QCD':2})

R2GC_129_55 = Coupling(name = 'R2GC_129_55',
                       value = '(complex(0,1)*G**2*KHTPTP3x3*MTP3)/(8.*cmath.pi**2)',
                       order = {'HT3T3':1,'QCD':2})

R2GC_129_56 = Coupling(name = 'R2GC_129_56',
                       value = '(complex(0,1)*G**2*KHTPTP4x4*MTP4)/(8.*cmath.pi**2)',
                       order = {'HT4T4':1,'QCD':2})

R2GC_130_57 = Coupling(name = 'R2GC_130_57',
                       value = '-0.125*(complex(0,1)*G**2*MB**2)/cmath.pi**2',
                       order = {'QCD':2})

R2GC_130_58 = Coupling(name = 'R2GC_130_58',
                       value = '-0.125*(complex(0,1)*G**2*MBP1**2)/cmath.pi**2',
                       order = {'QCD':2})

R2GC_130_59 = Coupling(name = 'R2GC_130_59',
                       value = '-0.125*(complex(0,1)*G**2*MBP2**2)/cmath.pi**2',
                       order = {'QCD':2})

R2GC_130_60 = Coupling(name = 'R2GC_130_60',
                       value = '-0.125*(complex(0,1)*G**2*MBP3**2)/cmath.pi**2',
                       order = {'QCD':2})

R2GC_130_61 = Coupling(name = 'R2GC_130_61',
                       value = '-0.125*(complex(0,1)*G**2*MT**2)/cmath.pi**2',
                       order = {'QCD':2})

R2GC_130_62 = Coupling(name = 'R2GC_130_62',
                       value = '-0.125*(complex(0,1)*G**2*MTP1**2)/cmath.pi**2',
                       order = {'QCD':2})

R2GC_130_63 = Coupling(name = 'R2GC_130_63',
                       value = '-0.125*(complex(0,1)*G**2*MTP2**2)/cmath.pi**2',
                       order = {'QCD':2})

R2GC_130_64 = Coupling(name = 'R2GC_130_64',
                       value = '-0.125*(complex(0,1)*G**2*MTP3**2)/cmath.pi**2',
                       order = {'QCD':2})

R2GC_130_65 = Coupling(name = 'R2GC_130_65',
                       value = '-0.125*(complex(0,1)*G**2*MTP4**2)/cmath.pi**2',
                       order = {'QCD':2})

R2GC_131_66 = Coupling(name = 'R2GC_131_66',
                       value = '(complex(0,1)*G**2)/(48.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_132_67 = Coupling(name = 'R2GC_132_67',
                       value = '(ee**2*complex(0,1)*G**2)/(216.*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_132_68 = Coupling(name = 'R2GC_132_68',
                       value = '(ee**2*complex(0,1)*G**2)/(54.*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_133_69 = Coupling(name = 'R2GC_133_69',
                       value = '-0.006944444444444444*(ee*complex(0,1)*G**3)/cmath.pi**2',
                       order = {'QCD':3,'QED':1})

R2GC_133_70 = Coupling(name = 'R2GC_133_70',
                       value = '(ee*complex(0,1)*G**3)/(72.*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_134_71 = Coupling(name = 'R2GC_134_71',
                       value = '(cw*ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2*sw) - (ee**2*complex(0,1)*G**2*sw)/(864.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_134_72 = Coupling(name = 'R2GC_134_72',
                       value = '(cw*ee**2*complex(0,1)*G**2)/(144.*cmath.pi**2*sw) - (5*ee**2*complex(0,1)*G**2*sw)/(432.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_135_73 = Coupling(name = 'R2GC_135_73',
                       value = '-0.005208333333333333*(cw*ee*complex(0,1)*G**3)/(cmath.pi**2*sw) + (ee*complex(0,1)*G**3*sw)/(576.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_135_74 = Coupling(name = 'R2GC_135_74',
                       value = '(cw*ee*complex(0,1)*G**3)/(192.*cmath.pi**2*sw) - (5*ee*complex(0,1)*G**3*sw)/(576.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_136_75 = Coupling(name = 'R2GC_136_75',
                       value = '(-3*cw*ee*complex(0,1)*G**3)/(64.*cmath.pi**2*sw) - (3*ee*complex(0,1)*G**3*sw)/(64.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_136_76 = Coupling(name = 'R2GC_136_76',
                       value = '(3*cw*ee*complex(0,1)*G**3)/(64.*cmath.pi**2*sw) + (3*ee*complex(0,1)*G**3*sw)/(64.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_137_77 = Coupling(name = 'R2GC_137_77',
                       value = '(ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2) + (cw**2*ee**2*complex(0,1)*G**2)/(192.*cmath.pi**2*sw**2) + (5*ee**2*complex(0,1)*G**2*sw**2)/(1728.*cw**2*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_137_78 = Coupling(name = 'R2GC_137_78',
                       value = '-0.003472222222222222*(ee**2*complex(0,1)*G**2)/cmath.pi**2 + (cw**2*ee**2*complex(0,1)*G**2)/(192.*cmath.pi**2*sw**2) + (17*ee**2*complex(0,1)*G**2*sw**2)/(1728.*cw**2*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_138_79 = Coupling(name = 'R2GC_138_79',
                       value = '-0.08333333333333333*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_139_80 = Coupling(name = 'R2GC_139_80',
                       value = '(cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

#R2GC_141_81 = Coupling(name = 'R2GC_141_81',
                       #value = '-0.0625*(complex(0,1)*G**2*KHBB**2)/cmath.pi**2 - (complex(0,1)*G**2*KHBB*yb)/(8.*cmath.pi**2) - (complex(0,1)*G**2*yb**2)/(16.*cmath.pi**2)',
                       #order = {'HBBMOD':2,'QCD':2})

R2GC_141_82 = Coupling(name = 'R2GC_141_82',
                       value = '-0.125*(complex(0,1)*G**2*KHBPBP1x1**2)/cmath.pi**2',
                       order = {'HB1B1':2,'QCD':2})

R2GC_141_83 = Coupling(name = 'R2GC_141_83',
                       value = '-0.125*(complex(0,1)*G**2*KHBPBP2x2**2)/cmath.pi**2',
                       order = {'HB2B2':2,'QCD':2})

R2GC_141_84 = Coupling(name = 'R2GC_141_84',
                       value = '-0.125*(complex(0,1)*G**2*KHBPBP3x3**2)/cmath.pi**2',
                       order = {'HB3B3':2,'QCD':2})

#R2GC_141_85 = Coupling(name = 'R2GC_141_85',
                       #value = '-0.0625*(complex(0,1)*G**2*KHTT**2)/cmath.pi**2 - (complex(0,1)*G**2*KHTT*yt)/(8.*cmath.pi**2) - (complex(0,1)*G**2*yt**2)/(16.*cmath.pi**2)',
                       #order = {'HTTMOD':2,'QCD':2})

R2GC_141_86 = Coupling(name = 'R2GC_141_86',
                       value = '-0.125*(complex(0,1)*G**2*KHTPTP1x1**2)/cmath.pi**2',
                       order = {'HT1T1':2,'QCD':2})

R2GC_141_87 = Coupling(name = 'R2GC_141_87',
                       value = '-0.125*(complex(0,1)*G**2*KHTPTP2x2**2)/cmath.pi**2',
                       order = {'HT2T2':2,'QCD':2})

R2GC_141_88 = Coupling(name = 'R2GC_141_88',
                       value = '-0.125*(complex(0,1)*G**2*KHTPTP3x3**2)/cmath.pi**2',
                       order = {'HT3T3':2,'QCD':2})

R2GC_141_89 = Coupling(name = 'R2GC_141_89',
                       value = '-0.125*(complex(0,1)*G**2*KHTPTP4x4**2)/cmath.pi**2',
                       order = {'HT4T4':2,'QCD':2})

R2GC_141_90 = Coupling(name = 'R2GC_141_90',
                       value = '-0.125*(complex(0,1)*G**2*KHBSML1**2)/cmath.pi**2 - (complex(0,1)*G**2*KHBSMR1**2)/(8.*cmath.pi**2)',
                       order = {'HB1B':2,'QCD':2})

R2GC_141_91 = Coupling(name = 'R2GC_141_91',
                       value = '-0.125*(complex(0,1)*G**2*KHBSML2**2)/cmath.pi**2 - (complex(0,1)*G**2*KHBSMR2**2)/(8.*cmath.pi**2)',
                       order = {'HB2B':2,'QCD':2})

R2GC_141_92 = Coupling(name = 'R2GC_141_92',
                       value = '-0.125*(complex(0,1)*G**2*KHBSML3**2)/cmath.pi**2 - (complex(0,1)*G**2*KHBSMR3**2)/(8.*cmath.pi**2)',
                       order = {'HB3B':2,'QCD':2})

R2GC_141_93 = Coupling(name = 'R2GC_141_93',
                       value = '-0.125*(complex(0,1)*G**2*KHBPBP1x2**2)/cmath.pi**2 - (complex(0,1)*G**2*KHBPBP2x1**2)/(8.*cmath.pi**2)',
                       order = {'HB1B2':2,'QCD':2})

R2GC_141_94 = Coupling(name = 'R2GC_141_94',
                       value = '-0.125*(complex(0,1)*G**2*KHBPBP1x3**2)/cmath.pi**2 - (complex(0,1)*G**2*KHBPBP3x1**2)/(8.*cmath.pi**2)',
                       order = {'HB1B3':2,'QCD':2})

R2GC_141_95 = Coupling(name = 'R2GC_141_95',
                       value = '-0.125*(complex(0,1)*G**2*KHBPBP2x3**2)/cmath.pi**2 - (complex(0,1)*G**2*KHBPBP3x2**2)/(8.*cmath.pi**2)',
                       order = {'HB2B3':2,'QCD':2})

R2GC_141_96 = Coupling(name = 'R2GC_141_96',
                       value = '-0.125*(complex(0,1)*G**2*KHTSML1**2)/cmath.pi**2 - (complex(0,1)*G**2*KHTSMR1**2)/(8.*cmath.pi**2)',
                       order = {'HT1T':2,'QCD':2})

R2GC_141_97 = Coupling(name = 'R2GC_141_97',
                       value = '-0.125*(complex(0,1)*G**2*KHTSML2**2)/cmath.pi**2 - (complex(0,1)*G**2*KHTSMR2**2)/(8.*cmath.pi**2)',
                       order = {'HT2T':2,'QCD':2})

R2GC_141_98 = Coupling(name = 'R2GC_141_98',
                       value = '-0.125*(complex(0,1)*G**2*KHTSML3**2)/cmath.pi**2 - (complex(0,1)*G**2*KHTSMR3**2)/(8.*cmath.pi**2)',
                       order = {'HT3T':2,'QCD':2})

R2GC_141_99 = Coupling(name = 'R2GC_141_99',
                       value = '-0.125*(complex(0,1)*G**2*KHTSML4**2)/cmath.pi**2 - (complex(0,1)*G**2*KHTSMR4**2)/(8.*cmath.pi**2)',
                       order = {'HT4T':2,'QCD':2})

R2GC_141_100 = Coupling(name = 'R2GC_141_100',
                        value = '-0.125*(complex(0,1)*G**2*KHTPTP1x2**2)/cmath.pi**2 - (complex(0,1)*G**2*KHTPTP2x1**2)/(8.*cmath.pi**2)',
                        order = {'HT1T2':2,'QCD':2})

R2GC_141_101 = Coupling(name = 'R2GC_141_101',
                        value = '-0.125*(complex(0,1)*G**2*KHTPTP1x3**2)/cmath.pi**2 - (complex(0,1)*G**2*KHTPTP3x1**2)/(8.*cmath.pi**2)',
                        order = {'HT1T3':2,'QCD':2})

R2GC_141_102 = Coupling(name = 'R2GC_141_102',
                        value = '-0.125*(complex(0,1)*G**2*KHTPTP1x4**2)/cmath.pi**2 - (complex(0,1)*G**2*KHTPTP4x1**2)/(8.*cmath.pi**2)',
                        order = {'HT1T4':2,'QCD':2})

R2GC_141_103 = Coupling(name = 'R2GC_141_103',
                        value = '-0.125*(complex(0,1)*G**2*KHTPTP2x3**2)/cmath.pi**2 - (complex(0,1)*G**2*KHTPTP3x2**2)/(8.*cmath.pi**2)',
                        order = {'HT2T3':2,'QCD':2})

R2GC_141_104 = Coupling(name = 'R2GC_141_104',
                        value = '-0.125*(complex(0,1)*G**2*KHTPTP2x4**2)/cmath.pi**2 - (complex(0,1)*G**2*KHTPTP4x2**2)/(8.*cmath.pi**2)',
                        order = {'HT2T4':2,'QCD':2})

R2GC_141_105 = Coupling(name = 'R2GC_141_105',
                        value = '-0.125*(complex(0,1)*G**2*KHTPTP3x4**2)/cmath.pi**2 - (complex(0,1)*G**2*KHTPTP4x3**2)/(8.*cmath.pi**2)',
                        order = {'HT3T4':2,'QCD':2})

R2GC_142_106 = Coupling(name = 'R2GC_142_106',
                        value = '(ee**2*complex(0,1)*G**2)/(96.*cmath.pi**2*sw**2)',
                        order = {'QCD':2,'QED':2})

R2GC_155_107 = Coupling(name = 'R2GC_155_107',
                        value = '-0.005208333333333333*G**4/cmath.pi**2',
                        order = {'QCD':4})

R2GC_155_108 = Coupling(name = 'R2GC_155_108',
                        value = 'G**4/(64.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_156_109 = Coupling(name = 'R2GC_156_109',
                        value = '-0.005208333333333333*(complex(0,1)*G**4)/cmath.pi**2',
                        order = {'QCD':4})

R2GC_156_110 = Coupling(name = 'R2GC_156_110',
                        value = '(complex(0,1)*G**4)/(64.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_157_111 = Coupling(name = 'R2GC_157_111',
                        value = '(complex(0,1)*G**4)/(192.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_157_112 = Coupling(name = 'R2GC_157_112',
                        value = '-0.015625*(complex(0,1)*G**4)/cmath.pi**2',
                        order = {'QCD':4})

R2GC_158_113 = Coupling(name = 'R2GC_158_113',
                        value = '-0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2',
                        order = {'QCD':4})

R2GC_159_114 = Coupling(name = 'R2GC_159_114',
                        value = '(complex(0,1)*G**4)/(288.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_159_115 = Coupling(name = 'R2GC_159_115',
                        value = '-0.03125*(complex(0,1)*G**4)/cmath.pi**2',
                        order = {'QCD':4})

R2GC_161_116 = Coupling(name = 'R2GC_161_116',
                        value = '-0.0625*(complex(0,1)*G**4)/cmath.pi**2',
                        order = {'QCD':4})

R2GC_161_117 = Coupling(name = 'R2GC_161_117',
                        value = '(complex(0,1)*G**4)/(4.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_162_118 = Coupling(name = 'R2GC_162_118',
                        value = '(-3*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_162_119 = Coupling(name = 'R2GC_162_119',
                        value = '(-23*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_163_120 = Coupling(name = 'R2GC_163_120',
                        value = '(ee*complex(0,1)*G**2)/(18.*cmath.pi**2)',
                        order = {'QCD':2,'QED':1})

R2GC_164_121 = Coupling(name = 'R2GC_164_121',
                        value = '-0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2',
                        order = {'QCD':3})

R2GC_176_122 = Coupling(name = 'R2GC_176_122',
                        value = '(13*complex(0,1)*G**4)/(384.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_177_123 = Coupling(name = 'R2GC_177_123',
                        value = '-0.013888888888888888*(complex(0,1)*G**2)/cmath.pi**2',
                        order = {'QCD':2})

R2GC_178_124 = Coupling(name = 'R2GC_178_124',
                        value = '(53*complex(0,1)*G**3)/(576.*cmath.pi**2)',
                        order = {'QCD':3})

R2GC_179_125 = Coupling(name = 'R2GC_179_125',
                        value = '(-3*complex(0,1)*G**4)/(32.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_179_126 = Coupling(name = 'R2GC_179_126',
                        value = '(-79*complex(0,1)*G**4)/(1152.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_180_127 = Coupling(name = 'R2GC_180_127',
                        value = '-0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x1*vev)/cmath.pi**2',
                        order = {'HSQ1SQ1':1,'QCD':2})

R2GC_181_128 = Coupling(name = 'R2GC_181_128',
                        value = '-0.041666666666666664*(complex(0,1)*G**2*KS01SQ1SQ1*vev)/cmath.pi**2',
                        order = {'QCD':2,'S01SQ1SQ1':1})

R2GC_182_129 = Coupling(name = 'R2GC_182_129',
                        value = '-0.041666666666666664*(complex(0,1)*G**2*KS02SQ1SQ1*vev)/cmath.pi**2',
                        order = {'QCD':2,'S02SQ1SQ1':1})

R2GC_187_130 = Coupling(name = 'R2GC_187_130',
                        value = '-0.041666666666666664*(complex(0,1)*G**2*KHSQSQ2x2*vev)/cmath.pi**2',
                        order = {'HSQ2SQ2':1,'QCD':2})

R2GC_188_131 = Coupling(name = 'R2GC_188_131',
                        value = '-0.041666666666666664*(complex(0,1)*G**2*KS01SQ2SQ2*vev)/cmath.pi**2',
                        order = {'QCD':2,'S01SQ2SQ2':1})

R2GC_189_132 = Coupling(name = 'R2GC_189_132',
                        value = '-0.041666666666666664*(complex(0,1)*G**2*KS02SQ2SQ2*vev)/cmath.pi**2',
                        order = {'QCD':2,'S02SQ2SQ2':1})

R2GC_194_133 = Coupling(name = 'R2GC_194_133',
                        value = '-0.041666666666666664*(complex(0,1)*G**2*KHSQSQ3x3*vev)/cmath.pi**2',
                        order = {'HSQ3SQ3':1,'QCD':2})

R2GC_195_134 = Coupling(name = 'R2GC_195_134',
                        value = '-0.041666666666666664*(complex(0,1)*G**2*KS01SQ3SQ3*vev)/cmath.pi**2',
                        order = {'QCD':2,'S01SQ3SQ3':1})

R2GC_200_135 = Coupling(name = 'R2GC_200_135',
                        value = '-0.041666666666666664*(complex(0,1)*G**2*KHSQSQ4x4*vev)/cmath.pi**2',
                        order = {'HSQ4SQ4':1,'QCD':2})

R2GC_217_136 = Coupling(name = 'R2GC_217_136',
                        value = '-0.16666666666666666*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2))',
                        order = {'QCD':2,'QED':1})

R2GC_218_137 = Coupling(name = 'R2GC_218_137',
                        value = '-0.020833333333333332*(complex(0,1)*G**2*KHSQSQ1x2*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ2x1*vev)/(48.*cmath.pi**2)',
                        order = {'HSQ1SQ2':1,'QCD':2})

R2GC_219_138 = Coupling(name = 'R2GC_219_138',
                        value = '-0.020833333333333332*(complex(0,1)*G**2*KHSQSQ1x3*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ3x1*vev)/(48.*cmath.pi**2)',
                        order = {'HSQ1SQ3':1,'QCD':2})

R2GC_220_139 = Coupling(name = 'R2GC_220_139',
                        value = '-0.020833333333333332*(complex(0,1)*G**2*KHSQSQ1x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x1*vev)/(48.*cmath.pi**2)',
                        order = {'HSQ1SQ4':1,'QCD':2})

R2GC_221_140 = Coupling(name = 'R2GC_221_140',
                        value = '-0.020833333333333332*(complex(0,1)*G**2*KHSQSQ2x3*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ3x2*vev)/(48.*cmath.pi**2)',
                        order = {'HSQ2SQ3':1,'QCD':2})

R2GC_222_141 = Coupling(name = 'R2GC_222_141',
                        value = '-0.020833333333333332*(complex(0,1)*G**2*KHSQSQ2x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x2*vev)/(48.*cmath.pi**2)',
                        order = {'HSQ2SQ4':1,'QCD':2})

R2GC_223_142 = Coupling(name = 'R2GC_223_142',
                        value = '-0.020833333333333332*(complex(0,1)*G**2*KHSQSQ3x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x3*vev)/(48.*cmath.pi**2)',
                        order = {'HSQ3SQ4':1,'QCD':2})

R2GC_228_143 = Coupling(name = 'R2GC_228_143',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KS01BB)/cmath.pi**2',
                        order = {'QCD':2,'S01BB':1})

R2GC_229_144 = Coupling(name = 'R2GC_229_144',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KS02BB)/cmath.pi**2',
                        order = {'QCD':2,'S02BB':1})

R2GC_230_145 = Coupling(name = 'R2GC_230_145',
                        value = '(complex(0,1)*G**2*MB)/(6.*cmath.pi**2)',
                        order = {'QCD':2})

#R2GC_233_146 = Coupling(name = 'R2GC_233_146',
                        #value = '(complex(0,1)*G**2*KHBB)/(3.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',
                        #order = {'HBBMOD':1,'QCD':2})

R2GC_237_147 = Coupling(name = 'R2GC_237_147',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBPBP1x1)/cmath.pi**2',
                        order = {'HB1B1':1,'QCD':2})

R2GC_238_148 = Coupling(name = 'R2GC_238_148',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBSML1)/cmath.pi**2',
                        order = {'HB1B':1,'QCD':2})

R2GC_239_149 = Coupling(name = 'R2GC_239_149',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBSMR1)/cmath.pi**2',
                        order = {'HB1B':1,'QCD':2})

R2GC_240_150 = Coupling(name = 'R2GC_240_150',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KS01B1B1)/cmath.pi**2',
                        order = {'QCD':2,'S01B1B1':1})

R2GC_241_151 = Coupling(name = 'R2GC_241_151',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KS02B1B1)/cmath.pi**2',
                        order = {'QCD':2,'S02B1B1':1})

R2GC_242_152 = Coupling(name = 'R2GC_242_152',
                        value = '(complex(0,1)*G**2*MBP1)/(6.*cmath.pi**2)',
                        order = {'QCD':2})

R2GC_246_153 = Coupling(name = 'R2GC_246_153',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBPBP1x2)/cmath.pi**2',
                        order = {'HB1B2':1,'QCD':2})

R2GC_247_154 = Coupling(name = 'R2GC_247_154',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBPBP2x1)/cmath.pi**2',
                        order = {'HB1B2':1,'QCD':2})

R2GC_248_155 = Coupling(name = 'R2GC_248_155',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBPBP2x2)/cmath.pi**2',
                        order = {'HB2B2':1,'QCD':2})

R2GC_249_156 = Coupling(name = 'R2GC_249_156',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBSML2)/cmath.pi**2',
                        order = {'HB2B':1,'QCD':2})

R2GC_250_157 = Coupling(name = 'R2GC_250_157',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBSMR2)/cmath.pi**2',
                        order = {'HB2B':1,'QCD':2})

R2GC_251_158 = Coupling(name = 'R2GC_251_158',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KS01B2B2)/cmath.pi**2',
                        order = {'QCD':2,'S01B2B2':1})

R2GC_252_159 = Coupling(name = 'R2GC_252_159',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KS02B2B2)/cmath.pi**2',
                        order = {'QCD':2,'S02B2B2':1})

R2GC_253_160 = Coupling(name = 'R2GC_253_160',
                        value = '(complex(0,1)*G**2*MBP2)/(6.*cmath.pi**2)',
                        order = {'QCD':2})

R2GC_257_161 = Coupling(name = 'R2GC_257_161',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBPBP1x3)/cmath.pi**2',
                        order = {'HB1B3':1,'QCD':2})

R2GC_258_162 = Coupling(name = 'R2GC_258_162',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBPBP2x3)/cmath.pi**2',
                        order = {'HB2B3':1,'QCD':2})

R2GC_259_163 = Coupling(name = 'R2GC_259_163',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBPBP3x1)/cmath.pi**2',
                        order = {'HB1B3':1,'QCD':2})

R2GC_260_164 = Coupling(name = 'R2GC_260_164',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBPBP3x2)/cmath.pi**2',
                        order = {'HB2B3':1,'QCD':2})

R2GC_261_165 = Coupling(name = 'R2GC_261_165',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBPBP3x3)/cmath.pi**2',
                        order = {'HB3B3':1,'QCD':2})

R2GC_262_166 = Coupling(name = 'R2GC_262_166',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBSML3)/cmath.pi**2',
                        order = {'HB3B':1,'QCD':2})

R2GC_263_167 = Coupling(name = 'R2GC_263_167',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHBSMR3)/cmath.pi**2',
                        order = {'HB3B':1,'QCD':2})

R2GC_264_168 = Coupling(name = 'R2GC_264_168',
                        value = '(complex(0,1)*G**2*MBP3)/(6.*cmath.pi**2)',
                        order = {'QCD':2})

R2GC_265_169 = Coupling(name = 'R2GC_265_169',
                        value = '(complex(0,1)*G**2*MSQ1**2)/(24.*cmath.pi**2)',
                        order = {'QCD':2})

R2GC_266_170 = Coupling(name = 'R2GC_266_170',
                        value = '(complex(0,1)*G**2*MSQ2**2)/(24.*cmath.pi**2)',
                        order = {'QCD':2})

R2GC_267_171 = Coupling(name = 'R2GC_267_171',
                        value = '(complex(0,1)*G**2*MSQ3**2)/(24.*cmath.pi**2)',
                        order = {'QCD':2})

R2GC_268_172 = Coupling(name = 'R2GC_268_172',
                        value = '(complex(0,1)*G**2*MSQ4**2)/(24.*cmath.pi**2)',
                        order = {'QCD':2})

R2GC_272_173 = Coupling(name = 'R2GC_272_173',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KS01TT)/cmath.pi**2',
                        order = {'QCD':2,'S01TT':1})

R2GC_273_174 = Coupling(name = 'R2GC_273_174',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KS02TT)/cmath.pi**2',
                        order = {'QCD':2,'S02TT':1})

R2GC_274_175 = Coupling(name = 'R2GC_274_175',
                        value = '(complex(0,1)*G**2*MT)/(6.*cmath.pi**2)',
                        order = {'QCD':2})

#R2GC_278_176 = Coupling(name = 'R2GC_278_176',
                        #value = '(complex(0,1)*G**2*KHTT)/(3.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
                        #order = {'HTTMOD':1,'QCD':2})

R2GC_282_177 = Coupling(name = 'R2GC_282_177',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP1x1)/cmath.pi**2',
                        order = {'HT1T1':1,'QCD':2})

R2GC_283_178 = Coupling(name = 'R2GC_283_178',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTSML1)/cmath.pi**2',
                        order = {'HT1T':1,'QCD':2})

R2GC_284_179 = Coupling(name = 'R2GC_284_179',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTSMR1)/cmath.pi**2',
                        order = {'HT1T':1,'QCD':2})

R2GC_285_180 = Coupling(name = 'R2GC_285_180',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KS01T1T1)/cmath.pi**2',
                        order = {'QCD':2,'S01T1T1':1})

R2GC_286_181 = Coupling(name = 'R2GC_286_181',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KS02T1T1)/cmath.pi**2',
                        order = {'QCD':2,'S02T1T1':1})

R2GC_287_182 = Coupling(name = 'R2GC_287_182',
                        value = '(complex(0,1)*G**2*MTP1)/(6.*cmath.pi**2)',
                        order = {'QCD':2})

R2GC_291_183 = Coupling(name = 'R2GC_291_183',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP1x2)/cmath.pi**2',
                        order = {'HT1T2':1,'QCD':2})

R2GC_292_184 = Coupling(name = 'R2GC_292_184',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP2x1)/cmath.pi**2',
                        order = {'HT1T2':1,'QCD':2})

R2GC_293_185 = Coupling(name = 'R2GC_293_185',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP2x2)/cmath.pi**2',
                        order = {'HT2T2':1,'QCD':2})

R2GC_294_186 = Coupling(name = 'R2GC_294_186',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTSML2)/cmath.pi**2',
                        order = {'HT2T':1,'QCD':2})

R2GC_295_187 = Coupling(name = 'R2GC_295_187',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTSMR2)/cmath.pi**2',
                        order = {'HT2T':1,'QCD':2})

R2GC_296_188 = Coupling(name = 'R2GC_296_188',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KS01T2T2)/cmath.pi**2',
                        order = {'QCD':2,'S01T2T2':1})

R2GC_297_189 = Coupling(name = 'R2GC_297_189',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KS02T2T2)/cmath.pi**2',
                        order = {'QCD':2,'S02T2T2':1})

R2GC_298_190 = Coupling(name = 'R2GC_298_190',
                        value = '(complex(0,1)*G**2*MTP2)/(6.*cmath.pi**2)',
                        order = {'QCD':2})

R2GC_302_191 = Coupling(name = 'R2GC_302_191',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP1x3)/cmath.pi**2',
                        order = {'HT1T3':1,'QCD':2})

R2GC_303_192 = Coupling(name = 'R2GC_303_192',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP2x3)/cmath.pi**2',
                        order = {'HT2T3':1,'QCD':2})

R2GC_304_193 = Coupling(name = 'R2GC_304_193',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP3x1)/cmath.pi**2',
                        order = {'HT1T3':1,'QCD':2})

R2GC_305_194 = Coupling(name = 'R2GC_305_194',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP3x2)/cmath.pi**2',
                        order = {'HT2T3':1,'QCD':2})

R2GC_306_195 = Coupling(name = 'R2GC_306_195',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP3x3)/cmath.pi**2',
                        order = {'HT3T3':1,'QCD':2})

R2GC_307_196 = Coupling(name = 'R2GC_307_196',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTSML3)/cmath.pi**2',
                        order = {'HT3T':1,'QCD':2})

R2GC_308_197 = Coupling(name = 'R2GC_308_197',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTSMR3)/cmath.pi**2',
                        order = {'HT3T':1,'QCD':2})

R2GC_309_198 = Coupling(name = 'R2GC_309_198',
                        value = '(complex(0,1)*G**2*MTP3)/(6.*cmath.pi**2)',
                        order = {'QCD':2})

R2GC_311_199 = Coupling(name = 'R2GC_311_199',
                        value = 'G**3/(24.*cmath.pi**2)',
                        order = {'QCD':3})

R2GC_311_200 = Coupling(name = 'R2GC_311_200',
                        value = '(11*G**3)/(64.*cmath.pi**2)',
                        order = {'QCD':3})

R2GC_312_201 = Coupling(name = 'R2GC_312_201',
                        value = '(23*complex(0,1)*G**4)/(192.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_313_202 = Coupling(name = 'R2GC_313_202',
                        value = '(5*complex(0,1)*G**4)/(48.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_313_203 = Coupling(name = 'R2GC_313_203',
                        value = '(19*complex(0,1)*G**4)/(32.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_314_204 = Coupling(name = 'R2GC_314_204',
                        value = '(31*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_315_205 = Coupling(name = 'R2GC_315_205',
                        value = '(-17*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_316_206 = Coupling(name = 'R2GC_316_206',
                        value = '(-7*complex(0,1)*G**4)/(32.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_317_207 = Coupling(name = 'R2GC_317_207',
                        value = '(7*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_321_208 = Coupling(name = 'R2GC_321_208',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP1x4)/cmath.pi**2',
                        order = {'HT1T4':1,'QCD':2})

R2GC_322_209 = Coupling(name = 'R2GC_322_209',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP2x4)/cmath.pi**2',
                        order = {'HT2T4':1,'QCD':2})

R2GC_323_210 = Coupling(name = 'R2GC_323_210',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP3x4)/cmath.pi**2',
                        order = {'HT3T4':1,'QCD':2})

R2GC_324_211 = Coupling(name = 'R2GC_324_211',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP4x1)/cmath.pi**2',
                        order = {'HT1T4':1,'QCD':2})

R2GC_325_212 = Coupling(name = 'R2GC_325_212',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP4x2)/cmath.pi**2',
                        order = {'HT2T4':1,'QCD':2})

R2GC_326_213 = Coupling(name = 'R2GC_326_213',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP4x3)/cmath.pi**2',
                        order = {'HT3T4':1,'QCD':2})

R2GC_327_214 = Coupling(name = 'R2GC_327_214',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTPTP4x4)/cmath.pi**2',
                        order = {'HT4T4':1,'QCD':2})

R2GC_328_215 = Coupling(name = 'R2GC_328_215',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTSML4)/cmath.pi**2',
                        order = {'HT4T':1,'QCD':2})

R2GC_329_216 = Coupling(name = 'R2GC_329_216',
                        value = '-0.3333333333333333*(complex(0,1)*G**2*KHTSMR4)/cmath.pi**2',
                        order = {'HT4T':1,'QCD':2})

R2GC_330_217 = Coupling(name = 'R2GC_330_217',
                        value = '(complex(0,1)*G**2*MTP4)/(6.*cmath.pi**2)',
                        order = {'QCD':2})












# LP debug: couplings modified to correctly separate contributions, NLOct does not do it automatically

R2GC_1000_1001 = Coupling(name = 'R2GC_1000_1001',
                       value = '(complex(0,1)*G**2*KHTT*KS01TT)/(8.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'HTTMOD':1,'QCD':2,'S01TT':1})

R2GC_1000_1002 = Coupling(name = 'R2GC_1000_1002',
                       value = '(complex(0,1)*G**2*KS01TT*yt)/(8.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QED':1,'QCD':2,'S01TT':1})

R2GC_1000_1003 = Coupling(name = 'R2GC_1000_1003',
                       value = '(complex(0,1)*G**2*KHTT*KS02TT)/(8.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'HTTMOD':1,'QCD':2,'S02TT':1})

R2GC_1000_1004 = Coupling(name = 'R2GC_1000_1004',
                       value = '(complex(0,1)*G**2*KS02TT*yt)/(8.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QED':1,'QCD':2,'S02TT':1})

R2GC_1000_1005 = Coupling(name = 'R2GC_1000_1005',
                       value = '-0.125*(complex(0,1)*G**2*KHTT*MT)/(cmath.pi**2*cmath.sqrt(2))',
                       order = {'HTTMOD':1,'QCD':2})

R2GC_1000_1006 = Coupling(name = 'R2GC_1000_1006',
                       value = '- (complex(0,1)*G**2*MT*yt)/(8.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QED':1,'QCD':2})

R2GC_1000_1007 = Coupling(name = 'R2GC_1000_1007',
                       value = '-0.0625*(complex(0,1)*G**2*KHTT**2)/cmath.pi**2',
                       order = {'HTTMOD':2,'QCD':2})

R2GC_1000_1008 = Coupling(name = 'R2GC_1000_1008',
                       value = '- (complex(0,1)*G**2*KHTT*yt)/(8.*cmath.pi**2)',
                       order = {'QED':1,'HTTMOD':1,'QCD':2})

R2GC_1000_1009 = Coupling(name = 'R2GC_1000_1009',
                       value = '- (complex(0,1)*G**2*yt**2)/(16.*cmath.pi**2)',
                       order = {'QED':2,'QCD':2})

R2GC_1000_1010 = Coupling(name = 'R2GC_1000_1010',
                        value = '(complex(0,1)*G**2*KHTT)/(3.*cmath.pi**2*cmath.sqrt(2))',
                        order = {'HTTMOD':1,'QCD':2})

R2GC_1000_1011 = Coupling(name = 'R2GC_1000_1011',
                        value = '(complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
                        order = {'QED':1,'QCD':2})




R2GC_1000_1012 = Coupling(name = 'R2GC_1000_1012',
                      value = '(complex(0,1)*G**2*KHBB*KS01BB)/(8.*cmath.pi**2*cmath.sqrt(2))',
                      order = {'HBBMOD':1,'QCD':2,'S01BB':1})

R2GC_1000_1013 = Coupling(name = 'R2GC_1000_1013',
                      value = '(complex(0,1)*G**2*KS01BB*yb)/(8.*cmath.pi**2*cmath.sqrt(2))',
                      order = {'QED':1,'QCD':2,'S01BB':1})

R2GC_1000_1014 = Coupling(name = 'R2GC_1000_1014',
                       value = '(complex(0,1)*G**2*KHBB*KS02BB)/(8.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'HBBMOD':1,'QCD':2,'S02BB':1})

R2GC_1000_1015 = Coupling(name = 'R2GC_1000_1015',
                       value = '(complex(0,1)*G**2*KS02BB*yb)/(8.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QED':1,'QCD':2,'S02BB':1})

R2GC_1000_1016 = Coupling(name = 'R2GC_1000_1016',
                       value = '-0.125*(complex(0,1)*G**2*KHBB*MB)/(cmath.pi**2*cmath.sqrt(2))',
                       order = {'HBBMOD':1,'QCD':2})

R2GC_1000_1017 = Coupling(name = 'R2GC_1000_1017',
                       value = '- (complex(0,1)*G**2*MB*yb)/(8.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QED':1,'QCD':2})

R2GC_1000_1018 = Coupling(name = 'R2GC_1000_1018',
                       value = '-0.0625*(complex(0,1)*G**2*KHBB**2)/cmath.pi**2',
                       order = {'HBBMOD':2,'QCD':2})

R2GC_1000_1019 = Coupling(name = 'R2GC_1000_1019',
                       value = '- (complex(0,1)*G**2*KHBB*yb)/(8.*cmath.pi**2)',
                       order = {'QED':1,'HBBMOD':1,'QCD':2})

R2GC_1000_1020 = Coupling(name = 'R2GC_1000_1020',
                       value = '- (complex(0,1)*G**2*yb**2)/(16.*cmath.pi**2)',
                       order = {'QED':2,'QCD':2})

R2GC_1000_1021 = Coupling(name = 'R2GC_1000_1021',
                        value = '(complex(0,1)*G**2*KHBB)/(3.*cmath.pi**2*cmath.sqrt(2))',
                        order = {'HBBMOD':1,'QCD':2})

R2GC_1000_1022 = Coupling(name = 'R2GC_1000_1022',
                        value = '(complex(0,1)*G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',
                        order = {'QED':1,'QCD':2})









UVGC_144_1 = Coupling(name = 'UVGC_144_1',
                      value = {-1:'(51*G**3)/(128.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_145_2 = Coupling(name = 'UVGC_145_2',
                      value = {-1:'G**3/(128.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_146_3 = Coupling(name = 'UVGC_146_3',
                      value = {-1:'-0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2'},
                      order = {'QCD':2})

UVGC_147_4 = Coupling(name = 'UVGC_147_4',
                      value = {-1:'-0.05555555555555555*(ee*complex(0,1)*G**2)/cmath.pi**2'},
                      order = {'QCD':2,'QED':1})

UVGC_149_5 = Coupling(name = 'UVGC_149_5',
                      value = {-1:'-0.027777777777777776*(ee*complex(0,1)*G**2)/cmath.pi**2'},
                      order = {'QCD':2,'QED':1})

UVGC_154_6 = Coupling(name = 'UVGC_154_6',
                      value = {-1:'(3*complex(0,1)*G**2)/(64.*cmath.pi**2)'},
                      order = {'QCD':2})

UVGC_154_7 = Coupling(name = 'UVGC_154_7',
                      value = {-1:'(-3*complex(0,1)*G**2)/(64.*cmath.pi**2)'},
                      order = {'QCD':2})

UVGC_155_8 = Coupling(name = 'UVGC_155_8',
                      value = {-1:'(3*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_155_9 = Coupling(name = 'UVGC_155_9',
                      value = {-1:'(-3*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_156_10 = Coupling(name = 'UVGC_156_10',
                       value = {-1:'(3*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_156_11 = Coupling(name = 'UVGC_156_11',
                       value = {-1:'(-3*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_158_12 = Coupling(name = 'UVGC_158_12',
                       value = {-1:'-0.0078125*(complex(0,1)*G**4)/cmath.pi**2'},
                       order = {'QCD':4})

UVGC_158_13 = Coupling(name = 'UVGC_158_13',
                       value = {-1:'(complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_159_14 = Coupling(name = 'UVGC_159_14',
                       value = {-1:'(-3*complex(0,1)*G**4)/(256.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_159_15 = Coupling(name = 'UVGC_159_15',
                       value = {-1:'(3*complex(0,1)*G**4)/(256.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_160_16 = Coupling(name = 'UVGC_160_16',
                       value = {-1:'G**3/(96.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_161_17 = Coupling(name = 'UVGC_161_17',
                       value = {-1:'-0.041666666666666664*(complex(0,1)*G**4)/cmath.pi**2'},
                       order = {'QCD':4})

UVGC_161_18 = Coupling(name = 'UVGC_161_18',
                       value = {-1:'(47*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_161_19 = Coupling(name = 'UVGC_161_19',
                       value = {-1:'(complex(0,1)*G**4)/(48.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_162_20 = Coupling(name = 'UVGC_162_20',
                       value = {-1:'(-253*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_162_21 = Coupling(name = 'UVGC_162_21',
                       value = {-1:'(5*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_163_22 = Coupling(name = 'UVGC_163_22',
                       value = {-1:'(ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_164_23 = Coupling(name = 'UVGC_164_23',
                       value = {-1:'(-13*complex(0,1)*G**3)/(48.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_171_24 = Coupling(name = 'UVGC_171_24',
                       value = {-1:'( 0 if MB else (complex(0,1)*G**3)/(48.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_171_25 = Coupling(name = 'UVGC_171_25',
                       value = {-1:'( 0 if MBP1 else (complex(0,1)*G**3)/(48.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_171_26 = Coupling(name = 'UVGC_171_26',
                       value = {-1:'( 0 if MBP2 else (complex(0,1)*G**3)/(48.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_171_27 = Coupling(name = 'UVGC_171_27',
                       value = {-1:'( 0 if MBP3 else (complex(0,1)*G**3)/(48.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_171_28 = Coupling(name = 'UVGC_171_28',
                       value = {-1:'(complex(0,1)*G**3)/(48.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_171_29 = Coupling(name = 'UVGC_171_29',
                       value = {-1:'(-19*complex(0,1)*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_171_30 = Coupling(name = 'UVGC_171_30',
                       value = {-1:'-0.0078125*(complex(0,1)*G**3)/cmath.pi**2'},
                       order = {'QCD':3})

UVGC_171_31 = Coupling(name = 'UVGC_171_31',
                       value = {-1:'( 0 if MSQ1 else (complex(0,1)*G**3)/(192.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_171_32 = Coupling(name = 'UVGC_171_32',
                       value = {-1:'( 0 if MSQ2 else (complex(0,1)*G**3)/(192.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_171_33 = Coupling(name = 'UVGC_171_33',
                       value = {-1:'( 0 if MSQ3 else (complex(0,1)*G**3)/(192.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_171_34 = Coupling(name = 'UVGC_171_34',
                       value = {-1:'( 0 if MSQ4 else (complex(0,1)*G**3)/(192.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_171_35 = Coupling(name = 'UVGC_171_35',
                       value = {-1:'( 0 if MT else (complex(0,1)*G**3)/(48.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_171_36 = Coupling(name = 'UVGC_171_36',
                       value = {-1:'( 0 if MTP1 else (complex(0,1)*G**3)/(48.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_171_37 = Coupling(name = 'UVGC_171_37',
                       value = {-1:'( 0 if MTP2 else (complex(0,1)*G**3)/(48.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_171_38 = Coupling(name = 'UVGC_171_38',
                       value = {-1:'( 0 if MTP3 else (complex(0,1)*G**3)/(48.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_171_39 = Coupling(name = 'UVGC_171_39',
                       value = {-1:'( 0 if MTP4 else (complex(0,1)*G**3)/(48.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_171_40 = Coupling(name = 'UVGC_171_40',
                       value = {-1:'(complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_176_41 = Coupling(name = 'UVGC_176_41',
                       value = {-1:'(-3*complex(0,1)*G**4)/(64.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_176_42 = Coupling(name = 'UVGC_176_42',
                       value = {-1:'(3*complex(0,1)*G**4)/(64.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_177_43 = Coupling(name = 'UVGC_177_43',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2)/cmath.pi**2 if MSQ1 else -0.16666666666666666*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(6.*cmath.pi**2)',0:'( (complex(0,1)*G**2)/(72.*cmath.pi**2) if MSQ1 else (complex(0,1)*G**2)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2)/(72.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_178_44 = Coupling(name = 'UVGC_178_44',
                       value = {-1:'( 0 if MB else -0.020833333333333332*(complex(0,1)*G**3)/cmath.pi**2 )'},
                       order = {'QCD':3})

UVGC_178_45 = Coupling(name = 'UVGC_178_45',
                       value = {-1:'( 0 if MBP1 else -0.020833333333333332*(complex(0,1)*G**3)/cmath.pi**2 )'},
                       order = {'QCD':3})

UVGC_178_46 = Coupling(name = 'UVGC_178_46',
                       value = {-1:'( 0 if MBP2 else -0.020833333333333332*(complex(0,1)*G**3)/cmath.pi**2 )'},
                       order = {'QCD':3})

UVGC_178_47 = Coupling(name = 'UVGC_178_47',
                       value = {-1:'( 0 if MBP3 else -0.020833333333333332*(complex(0,1)*G**3)/cmath.pi**2 )'},
                       order = {'QCD':3})

UVGC_178_48 = Coupling(name = 'UVGC_178_48',
                       value = {-1:'-0.020833333333333332*(complex(0,1)*G**3)/cmath.pi**2'},
                       order = {'QCD':3})

UVGC_178_49 = Coupling(name = 'UVGC_178_49',
                       value = {-1:'(19*complex(0,1)*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_178_50 = Coupling(name = 'UVGC_178_50',
                       value = {-1:'(complex(0,1)*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_178_51 = Coupling(name = 'UVGC_178_51',
                       value = {-1:'( 0 if MSQ1 else -0.005208333333333333*(complex(0,1)*G**3)/cmath.pi**2 )'},
                       order = {'QCD':3})

UVGC_178_52 = Coupling(name = 'UVGC_178_52',
                       value = {-1:'( 0 if MSQ2 else -0.005208333333333333*(complex(0,1)*G**3)/cmath.pi**2 )'},
                       order = {'QCD':3})

UVGC_178_53 = Coupling(name = 'UVGC_178_53',
                       value = {-1:'( 0 if MSQ3 else -0.005208333333333333*(complex(0,1)*G**3)/cmath.pi**2 )'},
                       order = {'QCD':3})

UVGC_178_54 = Coupling(name = 'UVGC_178_54',
                       value = {-1:'( 0 if MSQ4 else -0.005208333333333333*(complex(0,1)*G**3)/cmath.pi**2 )'},
                       order = {'QCD':3})

UVGC_178_55 = Coupling(name = 'UVGC_178_55',
                       value = {-1:'( 0 if MT else -0.020833333333333332*(complex(0,1)*G**3)/cmath.pi**2 )'},
                       order = {'QCD':3})

UVGC_178_56 = Coupling(name = 'UVGC_178_56',
                       value = {-1:'( 0 if MTP1 else -0.020833333333333332*(complex(0,1)*G**3)/cmath.pi**2 )'},
                       order = {'QCD':3})

UVGC_178_57 = Coupling(name = 'UVGC_178_57',
                       value = {-1:'( 0 if MTP2 else -0.020833333333333332*(complex(0,1)*G**3)/cmath.pi**2 )'},
                       order = {'QCD':3})

UVGC_178_58 = Coupling(name = 'UVGC_178_58',
                       value = {-1:'( 0 if MTP3 else -0.020833333333333332*(complex(0,1)*G**3)/cmath.pi**2 )'},
                       order = {'QCD':3})

UVGC_178_59 = Coupling(name = 'UVGC_178_59',
                       value = {-1:'( 0 if MTP4 else -0.020833333333333332*(complex(0,1)*G**3)/cmath.pi**2 )'},
                       order = {'QCD':3})

UVGC_178_60 = Coupling(name = 'UVGC_178_60',
                       value = {-1:'( (complex(0,1)*G**3)/(6.*cmath.pi**2) if MSQ1 else (complex(0,1)*G**3)/(6.*cmath.pi**2) ) + (complex(0,1)*G**3)/(48.*cmath.pi**2)',0:'( -0.013888888888888888*(complex(0,1)*G**3)/cmath.pi**2 if MSQ1 else -0.013888888888888888*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(72.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_179_61 = Coupling(name = 'UVGC_179_61',
                       value = {-1:'( 0 if MB else (complex(0,1)*G**4)/(24.*cmath.pi**2) )'},
                       order = {'QCD':4})

UVGC_179_62 = Coupling(name = 'UVGC_179_62',
                       value = {-1:'( 0 if MBP1 else (complex(0,1)*G**4)/(24.*cmath.pi**2) )'},
                       order = {'QCD':4})

UVGC_179_63 = Coupling(name = 'UVGC_179_63',
                       value = {-1:'( 0 if MBP2 else (complex(0,1)*G**4)/(24.*cmath.pi**2) )'},
                       order = {'QCD':4})

UVGC_179_64 = Coupling(name = 'UVGC_179_64',
                       value = {-1:'( 0 if MBP3 else (complex(0,1)*G**4)/(24.*cmath.pi**2) )'},
                       order = {'QCD':4})

UVGC_179_65 = Coupling(name = 'UVGC_179_65',
                       value = {-1:'(complex(0,1)*G**4)/(24.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_179_66 = Coupling(name = 'UVGC_179_66',
                       value = {-1:'(-7*complex(0,1)*G**4)/(16.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_179_67 = Coupling(name = 'UVGC_179_67',
                       value = {-1:'-0.015625*(complex(0,1)*G**4)/cmath.pi**2'},
                       order = {'QCD':4})

UVGC_179_68 = Coupling(name = 'UVGC_179_68',
                       value = {-1:'( 0 if MSQ1 else (complex(0,1)*G**4)/(96.*cmath.pi**2) )'},
                       order = {'QCD':4})

UVGC_179_69 = Coupling(name = 'UVGC_179_69',
                       value = {-1:'( 0 if MSQ2 else (complex(0,1)*G**4)/(96.*cmath.pi**2) )'},
                       order = {'QCD':4})

UVGC_179_70 = Coupling(name = 'UVGC_179_70',
                       value = {-1:'( 0 if MSQ3 else (complex(0,1)*G**4)/(96.*cmath.pi**2) )'},
                       order = {'QCD':4})

UVGC_179_71 = Coupling(name = 'UVGC_179_71',
                       value = {-1:'( 0 if MSQ4 else (complex(0,1)*G**4)/(96.*cmath.pi**2) )'},
                       order = {'QCD':4})

UVGC_179_72 = Coupling(name = 'UVGC_179_72',
                       value = {-1:'( 0 if MT else (complex(0,1)*G**4)/(24.*cmath.pi**2) )'},
                       order = {'QCD':4})

UVGC_179_73 = Coupling(name = 'UVGC_179_73',
                       value = {-1:'( 0 if MTP1 else (complex(0,1)*G**4)/(24.*cmath.pi**2) )'},
                       order = {'QCD':4})

UVGC_179_74 = Coupling(name = 'UVGC_179_74',
                       value = {-1:'( 0 if MTP2 else (complex(0,1)*G**4)/(24.*cmath.pi**2) )'},
                       order = {'QCD':4})

UVGC_179_75 = Coupling(name = 'UVGC_179_75',
                       value = {-1:'( 0 if MTP3 else (complex(0,1)*G**4)/(24.*cmath.pi**2) )'},
                       order = {'QCD':4})

UVGC_179_76 = Coupling(name = 'UVGC_179_76',
                       value = {-1:'( 0 if MTP4 else (complex(0,1)*G**4)/(24.*cmath.pi**2) )'},
                       order = {'QCD':4})

UVGC_179_77 = Coupling(name = 'UVGC_179_77',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**4)/cmath.pi**2 if MSQ1 else -0.16666666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) - (13*complex(0,1)*G**4)/(192.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(72.*cmath.pi**2) if MSQ1 else (complex(0,1)*G**4)/(72.*cmath.pi**2) ) - (complex(0,1)*G**4)/(72.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_180_78 = Coupling(name = 'UVGC_180_78',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KHSQSQ1x1*vev)/cmath.pi**2 if MSQ1 else -0.16666666666666666*(complex(0,1)*G**2*KHSQSQ1x1*vev)/cmath.pi**2 ) - (complex(0,1)*G**2*KHSQSQ1x1*vev)/(12.*cmath.pi**2)',0:'( (complex(0,1)*G**2*KHSQSQ1x1*vev)/(72.*cmath.pi**2) if MSQ1 else (complex(0,1)*G**2*KHSQSQ1x1*vev)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ1x1*vev)/(72.*cmath.pi**2)'},
                       order = {'HSQ1SQ1':1,'QCD':2})

UVGC_181_79 = Coupling(name = 'UVGC_181_79',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS01SQ1SQ1*vev)/cmath.pi**2 if MSQ1 else -0.16666666666666666*(complex(0,1)*G**2*KS01SQ1SQ1*vev)/cmath.pi**2 ) - (complex(0,1)*G**2*KS01SQ1SQ1*vev)/(12.*cmath.pi**2)',0:'( (complex(0,1)*G**2*KS01SQ1SQ1*vev)/(72.*cmath.pi**2) if MSQ1 else (complex(0,1)*G**2*KS01SQ1SQ1*vev)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2*KS01SQ1SQ1*vev)/(72.*cmath.pi**2)'},
                       order = {'QCD':2,'S01SQ1SQ1':1})

UVGC_182_80 = Coupling(name = 'UVGC_182_80',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS02SQ1SQ1*vev)/cmath.pi**2 if MSQ1 else -0.16666666666666666*(complex(0,1)*G**2*KS02SQ1SQ1*vev)/cmath.pi**2 ) - (complex(0,1)*G**2*KS02SQ1SQ1*vev)/(12.*cmath.pi**2)',0:'( (complex(0,1)*G**2*KS02SQ1SQ1*vev)/(72.*cmath.pi**2) if MSQ1 else (complex(0,1)*G**2*KS02SQ1SQ1*vev)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2*KS02SQ1SQ1*vev)/(72.*cmath.pi**2)'},
                       order = {'QCD':2,'S02SQ1SQ1':1})

UVGC_184_81 = Coupling(name = 'UVGC_184_81',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2)/cmath.pi**2 if MSQ2 else -0.16666666666666666*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(6.*cmath.pi**2)',0:'( (complex(0,1)*G**2)/(72.*cmath.pi**2) if MSQ2 else (complex(0,1)*G**2)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2)/(72.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_185_82 = Coupling(name = 'UVGC_185_82',
                       value = {-1:'( (complex(0,1)*G**3)/(6.*cmath.pi**2) if MSQ2 else (complex(0,1)*G**3)/(6.*cmath.pi**2) ) + (complex(0,1)*G**3)/(48.*cmath.pi**2)',0:'( -0.013888888888888888*(complex(0,1)*G**3)/cmath.pi**2 if MSQ2 else -0.013888888888888888*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(72.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_186_83 = Coupling(name = 'UVGC_186_83',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**4)/cmath.pi**2 if MSQ2 else -0.16666666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) - (13*complex(0,1)*G**4)/(192.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(72.*cmath.pi**2) if MSQ2 else (complex(0,1)*G**4)/(72.*cmath.pi**2) ) - (complex(0,1)*G**4)/(72.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_187_84 = Coupling(name = 'UVGC_187_84',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KHSQSQ2x2*vev)/cmath.pi**2 if MSQ2 else -0.16666666666666666*(complex(0,1)*G**2*KHSQSQ2x2*vev)/cmath.pi**2 ) - (complex(0,1)*G**2*KHSQSQ2x2*vev)/(12.*cmath.pi**2)',0:'( (complex(0,1)*G**2*KHSQSQ2x2*vev)/(72.*cmath.pi**2) if MSQ2 else (complex(0,1)*G**2*KHSQSQ2x2*vev)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ2x2*vev)/(72.*cmath.pi**2)'},
                       order = {'HSQ2SQ2':1,'QCD':2})

UVGC_188_85 = Coupling(name = 'UVGC_188_85',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS01SQ2SQ2*vev)/cmath.pi**2 if MSQ2 else -0.16666666666666666*(complex(0,1)*G**2*KS01SQ2SQ2*vev)/cmath.pi**2 ) - (complex(0,1)*G**2*KS01SQ2SQ2*vev)/(12.*cmath.pi**2)',0:'( (complex(0,1)*G**2*KS01SQ2SQ2*vev)/(72.*cmath.pi**2) if MSQ2 else (complex(0,1)*G**2*KS01SQ2SQ2*vev)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2*KS01SQ2SQ2*vev)/(72.*cmath.pi**2)'},
                       order = {'QCD':2,'S01SQ2SQ2':1})

UVGC_189_86 = Coupling(name = 'UVGC_189_86',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS02SQ2SQ2*vev)/cmath.pi**2 if MSQ2 else -0.16666666666666666*(complex(0,1)*G**2*KS02SQ2SQ2*vev)/cmath.pi**2 ) - (complex(0,1)*G**2*KS02SQ2SQ2*vev)/(12.*cmath.pi**2)',0:'( (complex(0,1)*G**2*KS02SQ2SQ2*vev)/(72.*cmath.pi**2) if MSQ2 else (complex(0,1)*G**2*KS02SQ2SQ2*vev)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2*KS02SQ2SQ2*vev)/(72.*cmath.pi**2)'},
                       order = {'QCD':2,'S02SQ2SQ2':1})

UVGC_191_87 = Coupling(name = 'UVGC_191_87',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2)/cmath.pi**2 if MSQ3 else -0.16666666666666666*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(6.*cmath.pi**2)',0:'( (complex(0,1)*G**2)/(72.*cmath.pi**2) if MSQ3 else (complex(0,1)*G**2)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2)/(72.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_192_88 = Coupling(name = 'UVGC_192_88',
                       value = {-1:'( (complex(0,1)*G**3)/(6.*cmath.pi**2) if MSQ3 else (complex(0,1)*G**3)/(6.*cmath.pi**2) ) + (complex(0,1)*G**3)/(48.*cmath.pi**2)',0:'( -0.013888888888888888*(complex(0,1)*G**3)/cmath.pi**2 if MSQ3 else -0.013888888888888888*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(72.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_193_89 = Coupling(name = 'UVGC_193_89',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**4)/cmath.pi**2 if MSQ3 else -0.16666666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) - (13*complex(0,1)*G**4)/(192.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(72.*cmath.pi**2) if MSQ3 else (complex(0,1)*G**4)/(72.*cmath.pi**2) ) - (complex(0,1)*G**4)/(72.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_194_90 = Coupling(name = 'UVGC_194_90',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KHSQSQ3x3*vev)/cmath.pi**2 if MSQ3 else -0.16666666666666666*(complex(0,1)*G**2*KHSQSQ3x3*vev)/cmath.pi**2 ) - (complex(0,1)*G**2*KHSQSQ3x3*vev)/(12.*cmath.pi**2)',0:'( (complex(0,1)*G**2*KHSQSQ3x3*vev)/(72.*cmath.pi**2) if MSQ3 else (complex(0,1)*G**2*KHSQSQ3x3*vev)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ3x3*vev)/(72.*cmath.pi**2)'},
                       order = {'HSQ3SQ3':1,'QCD':2})

UVGC_195_91 = Coupling(name = 'UVGC_195_91',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS01SQ3SQ3*vev)/cmath.pi**2 if MSQ3 else -0.16666666666666666*(complex(0,1)*G**2*KS01SQ3SQ3*vev)/cmath.pi**2 ) - (complex(0,1)*G**2*KS01SQ3SQ3*vev)/(12.*cmath.pi**2)',0:'( (complex(0,1)*G**2*KS01SQ3SQ3*vev)/(72.*cmath.pi**2) if MSQ3 else (complex(0,1)*G**2*KS01SQ3SQ3*vev)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2*KS01SQ3SQ3*vev)/(72.*cmath.pi**2)'},
                       order = {'QCD':2,'S01SQ3SQ3':1})

UVGC_197_92 = Coupling(name = 'UVGC_197_92',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2)/cmath.pi**2 if MSQ4 else -0.16666666666666666*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(6.*cmath.pi**2)',0:'( (complex(0,1)*G**2)/(72.*cmath.pi**2) if MSQ4 else (complex(0,1)*G**2)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2)/(72.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_198_93 = Coupling(name = 'UVGC_198_93',
                       value = {-1:'( (complex(0,1)*G**3)/(6.*cmath.pi**2) if MSQ4 else (complex(0,1)*G**3)/(6.*cmath.pi**2) ) + (complex(0,1)*G**3)/(48.*cmath.pi**2)',0:'( -0.013888888888888888*(complex(0,1)*G**3)/cmath.pi**2 if MSQ4 else -0.013888888888888888*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(72.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_199_94 = Coupling(name = 'UVGC_199_94',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**4)/cmath.pi**2 if MSQ4 else -0.16666666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) - (13*complex(0,1)*G**4)/(192.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(72.*cmath.pi**2) if MSQ4 else (complex(0,1)*G**4)/(72.*cmath.pi**2) ) - (complex(0,1)*G**4)/(72.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_200_95 = Coupling(name = 'UVGC_200_95',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KHSQSQ4x4*vev)/cmath.pi**2 if MSQ4 else -0.16666666666666666*(complex(0,1)*G**2*KHSQSQ4x4*vev)/cmath.pi**2 ) - (complex(0,1)*G**2*KHSQSQ4x4*vev)/(12.*cmath.pi**2)',0:'( (complex(0,1)*G**2*KHSQSQ4x4*vev)/(72.*cmath.pi**2) if MSQ4 else (complex(0,1)*G**2*KHSQSQ4x4*vev)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ4x4*vev)/(72.*cmath.pi**2)'},
                       order = {'HSQ4SQ4':1,'QCD':2})

UVGC_214_96 = Coupling(name = 'UVGC_214_96',
                       value = {-1:'(complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_217_97 = Coupling(name = 'UVGC_217_97',
                       value = {-1:'(ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_217_98 = Coupling(name = 'UVGC_217_98',
                       value = {-1:'-0.08333333333333333*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_218_99 = Coupling(name = 'UVGC_218_99',
                       value = {-1:'( -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x2*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ2x1*vev)/(24.*cmath.pi**2) if MSQ1 else -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x2*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ2x1*vev)/(24.*cmath.pi**2) )',0:'( (complex(0,1)*G**2*KHSQSQ1x2*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ2x1*vev)/(288.*cmath.pi**2) if MSQ1 else (complex(0,1)*G**2*KHSQSQ1x2*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ2x1*vev)/(288.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ1x2*vev)/(288.*cmath.pi**2) - (complex(0,1)*G**2*KHSQSQ2x1*vev)/(288.*cmath.pi**2)'},
                       order = {'HSQ1SQ2':1,'QCD':2})

UVGC_218_100 = Coupling(name = 'UVGC_218_100',
                        value = {-1:'( -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x2*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ2x1*vev)/(24.*cmath.pi**2) if MSQ2 else -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x2*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ2x1*vev)/(24.*cmath.pi**2) )',0:'( (complex(0,1)*G**2*KHSQSQ1x2*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ2x1*vev)/(288.*cmath.pi**2) if MSQ2 else (complex(0,1)*G**2*KHSQSQ1x2*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ2x1*vev)/(288.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ1x2*vev)/(288.*cmath.pi**2) - (complex(0,1)*G**2*KHSQSQ2x1*vev)/(288.*cmath.pi**2)'},
                        order = {'HSQ1SQ2':1,'QCD':2})

UVGC_218_101 = Coupling(name = 'UVGC_218_101',
                        value = {-1:'-0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x2*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ2x1*vev)/(24.*cmath.pi**2)'},
                        order = {'HSQ1SQ2':1,'QCD':2})

UVGC_219_102 = Coupling(name = 'UVGC_219_102',
                        value = {-1:'( -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x3*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ3x1*vev)/(24.*cmath.pi**2) if MSQ1 else -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x3*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ3x1*vev)/(24.*cmath.pi**2) )',0:'( (complex(0,1)*G**2*KHSQSQ1x3*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ3x1*vev)/(288.*cmath.pi**2) if MSQ1 else (complex(0,1)*G**2*KHSQSQ1x3*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ3x1*vev)/(288.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ1x3*vev)/(288.*cmath.pi**2) - (complex(0,1)*G**2*KHSQSQ3x1*vev)/(288.*cmath.pi**2)'},
                        order = {'HSQ1SQ3':1,'QCD':2})

UVGC_219_103 = Coupling(name = 'UVGC_219_103',
                        value = {-1:'( -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x3*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ3x1*vev)/(24.*cmath.pi**2) if MSQ3 else -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x3*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ3x1*vev)/(24.*cmath.pi**2) )',0:'( (complex(0,1)*G**2*KHSQSQ1x3*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ3x1*vev)/(288.*cmath.pi**2) if MSQ3 else (complex(0,1)*G**2*KHSQSQ1x3*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ3x1*vev)/(288.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ1x3*vev)/(288.*cmath.pi**2) - (complex(0,1)*G**2*KHSQSQ3x1*vev)/(288.*cmath.pi**2)'},
                        order = {'HSQ1SQ3':1,'QCD':2})

UVGC_219_104 = Coupling(name = 'UVGC_219_104',
                        value = {-1:'-0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x3*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ3x1*vev)/(24.*cmath.pi**2)'},
                        order = {'HSQ1SQ3':1,'QCD':2})

UVGC_220_105 = Coupling(name = 'UVGC_220_105',
                        value = {-1:'( -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x1*vev)/(24.*cmath.pi**2) if MSQ1 else -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x1*vev)/(24.*cmath.pi**2) )',0:'( (complex(0,1)*G**2*KHSQSQ1x4*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ4x1*vev)/(288.*cmath.pi**2) if MSQ1 else (complex(0,1)*G**2*KHSQSQ1x4*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ4x1*vev)/(288.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ1x4*vev)/(288.*cmath.pi**2) - (complex(0,1)*G**2*KHSQSQ4x1*vev)/(288.*cmath.pi**2)'},
                        order = {'HSQ1SQ4':1,'QCD':2})

UVGC_220_106 = Coupling(name = 'UVGC_220_106',
                        value = {-1:'( -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x1*vev)/(24.*cmath.pi**2) if MSQ4 else -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x1*vev)/(24.*cmath.pi**2) )',0:'( (complex(0,1)*G**2*KHSQSQ1x4*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ4x1*vev)/(288.*cmath.pi**2) if MSQ4 else (complex(0,1)*G**2*KHSQSQ1x4*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ4x1*vev)/(288.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ1x4*vev)/(288.*cmath.pi**2) - (complex(0,1)*G**2*KHSQSQ4x1*vev)/(288.*cmath.pi**2)'},
                        order = {'HSQ1SQ4':1,'QCD':2})

UVGC_220_107 = Coupling(name = 'UVGC_220_107',
                        value = {-1:'-0.041666666666666664*(complex(0,1)*G**2*KHSQSQ1x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x1*vev)/(24.*cmath.pi**2)'},
                        order = {'HSQ1SQ4':1,'QCD':2})

UVGC_221_108 = Coupling(name = 'UVGC_221_108',
                        value = {-1:'( -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ2x3*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ3x2*vev)/(24.*cmath.pi**2) if MSQ2 else -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ2x3*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ3x2*vev)/(24.*cmath.pi**2) )',0:'( (complex(0,1)*G**2*KHSQSQ2x3*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ3x2*vev)/(288.*cmath.pi**2) if MSQ2 else (complex(0,1)*G**2*KHSQSQ2x3*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ3x2*vev)/(288.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ2x3*vev)/(288.*cmath.pi**2) - (complex(0,1)*G**2*KHSQSQ3x2*vev)/(288.*cmath.pi**2)'},
                        order = {'HSQ2SQ3':1,'QCD':2})

UVGC_221_109 = Coupling(name = 'UVGC_221_109',
                        value = {-1:'( -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ2x3*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ3x2*vev)/(24.*cmath.pi**2) if MSQ3 else -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ2x3*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ3x2*vev)/(24.*cmath.pi**2) )',0:'( (complex(0,1)*G**2*KHSQSQ2x3*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ3x2*vev)/(288.*cmath.pi**2) if MSQ3 else (complex(0,1)*G**2*KHSQSQ2x3*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ3x2*vev)/(288.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ2x3*vev)/(288.*cmath.pi**2) - (complex(0,1)*G**2*KHSQSQ3x2*vev)/(288.*cmath.pi**2)'},
                        order = {'HSQ2SQ3':1,'QCD':2})

UVGC_221_110 = Coupling(name = 'UVGC_221_110',
                        value = {-1:'-0.041666666666666664*(complex(0,1)*G**2*KHSQSQ2x3*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ3x2*vev)/(24.*cmath.pi**2)'},
                        order = {'HSQ2SQ3':1,'QCD':2})

UVGC_222_111 = Coupling(name = 'UVGC_222_111',
                        value = {-1:'( -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ2x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x2*vev)/(24.*cmath.pi**2) if MSQ2 else -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ2x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x2*vev)/(24.*cmath.pi**2) )',0:'( (complex(0,1)*G**2*KHSQSQ2x4*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ4x2*vev)/(288.*cmath.pi**2) if MSQ2 else (complex(0,1)*G**2*KHSQSQ2x4*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ4x2*vev)/(288.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ2x4*vev)/(288.*cmath.pi**2) - (complex(0,1)*G**2*KHSQSQ4x2*vev)/(288.*cmath.pi**2)'},
                        order = {'HSQ2SQ4':1,'QCD':2})

UVGC_222_112 = Coupling(name = 'UVGC_222_112',
                        value = {-1:'( -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ2x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x2*vev)/(24.*cmath.pi**2) if MSQ4 else -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ2x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x2*vev)/(24.*cmath.pi**2) )',0:'( (complex(0,1)*G**2*KHSQSQ2x4*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ4x2*vev)/(288.*cmath.pi**2) if MSQ4 else (complex(0,1)*G**2*KHSQSQ2x4*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ4x2*vev)/(288.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ2x4*vev)/(288.*cmath.pi**2) - (complex(0,1)*G**2*KHSQSQ4x2*vev)/(288.*cmath.pi**2)'},
                        order = {'HSQ2SQ4':1,'QCD':2})

UVGC_222_113 = Coupling(name = 'UVGC_222_113',
                        value = {-1:'-0.041666666666666664*(complex(0,1)*G**2*KHSQSQ2x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x2*vev)/(24.*cmath.pi**2)'},
                        order = {'HSQ2SQ4':1,'QCD':2})

UVGC_223_114 = Coupling(name = 'UVGC_223_114',
                        value = {-1:'( -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ3x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x3*vev)/(24.*cmath.pi**2) if MSQ3 else -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ3x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x3*vev)/(24.*cmath.pi**2) )',0:'( (complex(0,1)*G**2*KHSQSQ3x4*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ4x3*vev)/(288.*cmath.pi**2) if MSQ3 else (complex(0,1)*G**2*KHSQSQ3x4*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ4x3*vev)/(288.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ3x4*vev)/(288.*cmath.pi**2) - (complex(0,1)*G**2*KHSQSQ4x3*vev)/(288.*cmath.pi**2)'},
                        order = {'HSQ3SQ4':1,'QCD':2})

UVGC_223_115 = Coupling(name = 'UVGC_223_115',
                        value = {-1:'( -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ3x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x3*vev)/(24.*cmath.pi**2) if MSQ4 else -0.041666666666666664*(complex(0,1)*G**2*KHSQSQ3x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x3*vev)/(24.*cmath.pi**2) )',0:'( (complex(0,1)*G**2*KHSQSQ3x4*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ4x3*vev)/(288.*cmath.pi**2) if MSQ4 else (complex(0,1)*G**2*KHSQSQ3x4*vev)/(288.*cmath.pi**2) + (complex(0,1)*G**2*KHSQSQ4x3*vev)/(288.*cmath.pi**2) ) - (complex(0,1)*G**2*KHSQSQ3x4*vev)/(288.*cmath.pi**2) - (complex(0,1)*G**2*KHSQSQ4x3*vev)/(288.*cmath.pi**2)'},
                        order = {'HSQ3SQ4':1,'QCD':2})

UVGC_223_116 = Coupling(name = 'UVGC_223_116',
                        value = {-1:'-0.041666666666666664*(complex(0,1)*G**2*KHSQSQ3x4*vev)/cmath.pi**2 - (complex(0,1)*G**2*KHSQSQ4x3*vev)/(24.*cmath.pi**2)'},
                        order = {'HSQ3SQ4':1,'QCD':2})

UVGC_225_117 = Coupling(name = 'UVGC_225_117',
                        value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MB else -0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MB/MU_R))/(2.*cmath.pi**2) if MB else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_226_118 = Coupling(name = 'UVGC_226_118',
                        value = {-1:'( (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) if MB else -0.027777777777777776*(ee*complex(0,1)*G**2)/cmath.pi**2 )',0:'( (5*ee*complex(0,1)*G**2)/(36.*cmath.pi**2) - (ee*complex(0,1)*G**2*reglog(MB/MU_R))/(6.*cmath.pi**2) if MB else (ee*complex(0,1)*G**2)/(36.*cmath.pi**2) ) - (ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

UVGC_227_119 = Coupling(name = 'UVGC_227_119',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2 if MB else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MB/MU_R))/(2.*cmath.pi**2) if MB else -0.08333333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_228_120 = Coupling(name = 'UVGC_228_120',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS01BB)/cmath.pi**2 if MB else (complex(0,1)*G**2*KS01BB)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KS01BB)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KS01BB)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KS01BB*reglog(MB/MU_R))/(2.*cmath.pi**2) if MB else -0.08333333333333333*(complex(0,1)*G**2*KS01BB)/cmath.pi**2 ) + (complex(0,1)*G**2*KS01BB)/(12.*cmath.pi**2)'},
                        order = {'QCD':2,'S01BB':1})

UVGC_229_121 = Coupling(name = 'UVGC_229_121',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS02BB)/cmath.pi**2 if MB else (complex(0,1)*G**2*KS02BB)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KS02BB)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KS02BB)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KS02BB*reglog(MB/MU_R))/(2.*cmath.pi**2) if MB else -0.08333333333333333*(complex(0,1)*G**2*KS02BB)/cmath.pi**2 ) + (complex(0,1)*G**2*KS02BB)/(12.*cmath.pi**2)'},
                        order = {'QCD':2,'S02BB':1})

UVGC_230_122 = Coupling(name = 'UVGC_230_122',
                        value = {-1:'( (complex(0,1)*G**2*MB)/(6.*cmath.pi**2) if MB else -0.08333333333333333*(complex(0,1)*G**2*MB)/cmath.pi**2 ) + (complex(0,1)*G**2*MB)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MB)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MB*reglog(MB/MU_R))/cmath.pi**2 if MB else (complex(0,1)*G**2*MB)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MB)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_231_123 = Coupling(name = 'UVGC_231_123',
                        value = {-1:'( (cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2) if MB else -0.041666666666666664*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) + (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)',0:'( (5*cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (5*ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) - (cw*ee*complex(0,1)*G**2*reglog(MB/MU_R))/(4.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw*reglog(MB/MU_R))/(12.*cw*cmath.pi**2) if MB else (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) - (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

UVGC_232_124 = Coupling(name = 'UVGC_232_124',
                        value = {-1:'( -0.05555555555555555*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) if MB else (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)',0:'( (-5*ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2) + (ee*complex(0,1)*G**2*sw*reglog(MB/MU_R))/(6.*cw*cmath.pi**2) if MB else -0.027777777777777776*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) ) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

#UVGC_233_125 = Coupling(name = 'UVGC_233_125',
                        #value = {-1:'( (complex(0,1)*G**2*KHBB)/(6.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yb)/(6.*cmath.pi**2*cmath.sqrt(2)) if MB else -0.08333333333333333*(complex(0,1)*G**2*KHBB)/(cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*KHBB)/(3.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (5*complex(0,1)*G**2*KHBB)/(12.*cmath.pi**2*cmath.sqrt(2)) + (3*complex(0,1)*G**2*yb)/(4.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*KHBB*reglog(MB/MU_R))/(2.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yb*reglog(MB/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MB else (complex(0,1)*G**2*KHBB)/(12.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*KHBB)/(12.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                        #order = {'HBBMOD':1,'QCD':2})

UVGC_234_126 = Coupling(name = 'UVGC_234_126',
                        value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MBP1 else -0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MBP1/MU_R))/(2.*cmath.pi**2) if MBP1 else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_235_127 = Coupling(name = 'UVGC_235_127',
                        value = {-1:'( (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) if MBP1 else -0.027777777777777776*(ee*complex(0,1)*G**2)/cmath.pi**2 )',0:'( (5*ee*complex(0,1)*G**2)/(36.*cmath.pi**2) - (ee*complex(0,1)*G**2*reglog(MBP1/MU_R))/(6.*cmath.pi**2) if MBP1 else (ee*complex(0,1)*G**2)/(36.*cmath.pi**2) ) - (ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

UVGC_236_128 = Coupling(name = 'UVGC_236_128',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2 if MBP1 else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MBP1/MU_R))/(2.*cmath.pi**2) if MBP1 else -0.08333333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_237_129 = Coupling(name = 'UVGC_237_129',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KHBPBP1x1)/cmath.pi**2 if MBP1 else (complex(0,1)*G**2*KHBPBP1x1)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KHBPBP1x1)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KHBPBP1x1)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP1x1*reglog(MBP1/MU_R))/(2.*cmath.pi**2) if MBP1 else -0.08333333333333333*(complex(0,1)*G**2*KHBPBP1x1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP1x1)/(12.*cmath.pi**2)'},
                        order = {'HB1B1':1,'QCD':2})

UVGC_238_130 = Coupling(name = 'UVGC_238_130',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBSML1)/cmath.pi**2 if MB else (complex(0,1)*G**2*KHBSML1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBSML1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBSML1*reglog(MB/MU_R))/(4.*cmath.pi**2) if MB else -0.041666666666666664*(complex(0,1)*G**2*KHBSML1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBSML1)/(24.*cmath.pi**2)'},
                        order = {'HB1B':1,'QCD':2})

UVGC_238_131 = Coupling(name = 'UVGC_238_131',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBSML1)/cmath.pi**2 if MBP1 else (complex(0,1)*G**2*KHBSML1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBSML1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBSML1*reglog(MBP1/MU_R))/(4.*cmath.pi**2) if MBP1 else -0.041666666666666664*(complex(0,1)*G**2*KHBSML1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBSML1)/(24.*cmath.pi**2)'},
                        order = {'HB1B':1,'QCD':2})

UVGC_238_132 = Coupling(name = 'UVGC_238_132',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHBSML1)/cmath.pi**2'},
                        order = {'HB1B':1,'QCD':2})

UVGC_239_133 = Coupling(name = 'UVGC_239_133',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBSMR1)/cmath.pi**2 if MB else (complex(0,1)*G**2*KHBSMR1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBSMR1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBSMR1*reglog(MB/MU_R))/(4.*cmath.pi**2) if MB else -0.041666666666666664*(complex(0,1)*G**2*KHBSMR1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBSMR1)/(24.*cmath.pi**2)'},
                        order = {'HB1B':1,'QCD':2})

UVGC_239_134 = Coupling(name = 'UVGC_239_134',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBSMR1)/cmath.pi**2 if MBP1 else (complex(0,1)*G**2*KHBSMR1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBSMR1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBSMR1*reglog(MBP1/MU_R))/(4.*cmath.pi**2) if MBP1 else -0.041666666666666664*(complex(0,1)*G**2*KHBSMR1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBSMR1)/(24.*cmath.pi**2)'},
                        order = {'HB1B':1,'QCD':2})

UVGC_239_135 = Coupling(name = 'UVGC_239_135',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHBSMR1)/cmath.pi**2'},
                        order = {'HB1B':1,'QCD':2})

UVGC_240_136 = Coupling(name = 'UVGC_240_136',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS01B1B1)/cmath.pi**2 if MBP1 else (complex(0,1)*G**2*KS01B1B1)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KS01B1B1)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KS01B1B1)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KS01B1B1*reglog(MBP1/MU_R))/(2.*cmath.pi**2) if MBP1 else -0.08333333333333333*(complex(0,1)*G**2*KS01B1B1)/cmath.pi**2 ) + (complex(0,1)*G**2*KS01B1B1)/(12.*cmath.pi**2)'},
                        order = {'QCD':2,'S01B1B1':1})

UVGC_241_137 = Coupling(name = 'UVGC_241_137',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS02B1B1)/cmath.pi**2 if MBP1 else (complex(0,1)*G**2*KS02B1B1)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KS02B1B1)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KS02B1B1)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KS02B1B1*reglog(MBP1/MU_R))/(2.*cmath.pi**2) if MBP1 else -0.08333333333333333*(complex(0,1)*G**2*KS02B1B1)/cmath.pi**2 ) + (complex(0,1)*G**2*KS02B1B1)/(12.*cmath.pi**2)'},
                        order = {'QCD':2,'S02B1B1':1})

UVGC_242_138 = Coupling(name = 'UVGC_242_138',
                        value = {-1:'( (complex(0,1)*G**2*MBP1)/(6.*cmath.pi**2) if MBP1 else -0.08333333333333333*(complex(0,1)*G**2*MBP1)/cmath.pi**2 ) + (complex(0,1)*G**2*MBP1)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MBP1)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MBP1*reglog(MBP1/MU_R))/cmath.pi**2 if MBP1 else (complex(0,1)*G**2*MBP1)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MBP1)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_243_139 = Coupling(name = 'UVGC_243_139',
                        value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MBP2 else -0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MBP2/MU_R))/(2.*cmath.pi**2) if MBP2 else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_244_140 = Coupling(name = 'UVGC_244_140',
                        value = {-1:'( (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) if MBP2 else -0.027777777777777776*(ee*complex(0,1)*G**2)/cmath.pi**2 )',0:'( (5*ee*complex(0,1)*G**2)/(36.*cmath.pi**2) - (ee*complex(0,1)*G**2*reglog(MBP2/MU_R))/(6.*cmath.pi**2) if MBP2 else (ee*complex(0,1)*G**2)/(36.*cmath.pi**2) ) - (ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

UVGC_245_141 = Coupling(name = 'UVGC_245_141',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2 if MBP2 else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MBP2/MU_R))/(2.*cmath.pi**2) if MBP2 else -0.08333333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_246_142 = Coupling(name = 'UVGC_246_142',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBPBP1x2)/cmath.pi**2 if MBP1 else (complex(0,1)*G**2*KHBPBP1x2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBPBP1x2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP1x2*reglog(MBP1/MU_R))/(4.*cmath.pi**2) if MBP1 else -0.041666666666666664*(complex(0,1)*G**2*KHBPBP1x2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP1x2)/(24.*cmath.pi**2)'},
                        order = {'HB1B2':1,'QCD':2})

UVGC_246_143 = Coupling(name = 'UVGC_246_143',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBPBP1x2)/cmath.pi**2 if MBP2 else (complex(0,1)*G**2*KHBPBP1x2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBPBP1x2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP1x2*reglog(MBP2/MU_R))/(4.*cmath.pi**2) if MBP2 else -0.041666666666666664*(complex(0,1)*G**2*KHBPBP1x2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP1x2)/(24.*cmath.pi**2)'},
                        order = {'HB1B2':1,'QCD':2})

UVGC_246_144 = Coupling(name = 'UVGC_246_144',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHBPBP1x2)/cmath.pi**2'},
                        order = {'HB1B2':1,'QCD':2})

UVGC_247_145 = Coupling(name = 'UVGC_247_145',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBPBP2x1)/cmath.pi**2 if MBP1 else (complex(0,1)*G**2*KHBPBP2x1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBPBP2x1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP2x1*reglog(MBP1/MU_R))/(4.*cmath.pi**2) if MBP1 else -0.041666666666666664*(complex(0,1)*G**2*KHBPBP2x1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP2x1)/(24.*cmath.pi**2)'},
                        order = {'HB1B2':1,'QCD':2})

UVGC_247_146 = Coupling(name = 'UVGC_247_146',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBPBP2x1)/cmath.pi**2 if MBP2 else (complex(0,1)*G**2*KHBPBP2x1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBPBP2x1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP2x1*reglog(MBP2/MU_R))/(4.*cmath.pi**2) if MBP2 else -0.041666666666666664*(complex(0,1)*G**2*KHBPBP2x1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP2x1)/(24.*cmath.pi**2)'},
                        order = {'HB1B2':1,'QCD':2})

UVGC_247_147 = Coupling(name = 'UVGC_247_147',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHBPBP2x1)/cmath.pi**2'},
                        order = {'HB1B2':1,'QCD':2})

UVGC_248_148 = Coupling(name = 'UVGC_248_148',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KHBPBP2x2)/cmath.pi**2 if MBP2 else (complex(0,1)*G**2*KHBPBP2x2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KHBPBP2x2)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KHBPBP2x2)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP2x2*reglog(MBP2/MU_R))/(2.*cmath.pi**2) if MBP2 else -0.08333333333333333*(complex(0,1)*G**2*KHBPBP2x2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP2x2)/(12.*cmath.pi**2)'},
                        order = {'HB2B2':1,'QCD':2})

UVGC_249_149 = Coupling(name = 'UVGC_249_149',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBSML2)/cmath.pi**2 if MB else (complex(0,1)*G**2*KHBSML2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBSML2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBSML2*reglog(MB/MU_R))/(4.*cmath.pi**2) if MB else -0.041666666666666664*(complex(0,1)*G**2*KHBSML2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBSML2)/(24.*cmath.pi**2)'},
                        order = {'HB2B':1,'QCD':2})

UVGC_249_150 = Coupling(name = 'UVGC_249_150',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBSML2)/cmath.pi**2 if MBP2 else (complex(0,1)*G**2*KHBSML2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBSML2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBSML2*reglog(MBP2/MU_R))/(4.*cmath.pi**2) if MBP2 else -0.041666666666666664*(complex(0,1)*G**2*KHBSML2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBSML2)/(24.*cmath.pi**2)'},
                        order = {'HB2B':1,'QCD':2})

UVGC_249_151 = Coupling(name = 'UVGC_249_151',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHBSML2)/cmath.pi**2'},
                        order = {'HB2B':1,'QCD':2})

UVGC_250_152 = Coupling(name = 'UVGC_250_152',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBSMR2)/cmath.pi**2 if MB else (complex(0,1)*G**2*KHBSMR2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBSMR2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBSMR2*reglog(MB/MU_R))/(4.*cmath.pi**2) if MB else -0.041666666666666664*(complex(0,1)*G**2*KHBSMR2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBSMR2)/(24.*cmath.pi**2)'},
                        order = {'HB2B':1,'QCD':2})

UVGC_250_153 = Coupling(name = 'UVGC_250_153',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBSMR2)/cmath.pi**2 if MBP2 else (complex(0,1)*G**2*KHBSMR2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBSMR2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBSMR2*reglog(MBP2/MU_R))/(4.*cmath.pi**2) if MBP2 else -0.041666666666666664*(complex(0,1)*G**2*KHBSMR2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBSMR2)/(24.*cmath.pi**2)'},
                        order = {'HB2B':1,'QCD':2})

UVGC_250_154 = Coupling(name = 'UVGC_250_154',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHBSMR2)/cmath.pi**2'},
                        order = {'HB2B':1,'QCD':2})

UVGC_251_155 = Coupling(name = 'UVGC_251_155',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS01B2B2)/cmath.pi**2 if MBP2 else (complex(0,1)*G**2*KS01B2B2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KS01B2B2)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KS01B2B2)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KS01B2B2*reglog(MBP2/MU_R))/(2.*cmath.pi**2) if MBP2 else -0.08333333333333333*(complex(0,1)*G**2*KS01B2B2)/cmath.pi**2 ) + (complex(0,1)*G**2*KS01B2B2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2,'S01B2B2':1})

UVGC_252_156 = Coupling(name = 'UVGC_252_156',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS02B2B2)/cmath.pi**2 if MBP2 else (complex(0,1)*G**2*KS02B2B2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KS02B2B2)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KS02B2B2)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KS02B2B2*reglog(MBP2/MU_R))/(2.*cmath.pi**2) if MBP2 else -0.08333333333333333*(complex(0,1)*G**2*KS02B2B2)/cmath.pi**2 ) + (complex(0,1)*G**2*KS02B2B2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2,'S02B2B2':1})

UVGC_253_157 = Coupling(name = 'UVGC_253_157',
                        value = {-1:'( (complex(0,1)*G**2*MBP2)/(6.*cmath.pi**2) if MBP2 else -0.08333333333333333*(complex(0,1)*G**2*MBP2)/cmath.pi**2 ) + (complex(0,1)*G**2*MBP2)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MBP2)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MBP2*reglog(MBP2/MU_R))/cmath.pi**2 if MBP2 else (complex(0,1)*G**2*MBP2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MBP2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_254_158 = Coupling(name = 'UVGC_254_158',
                        value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MBP3 else -0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MBP3/MU_R))/(2.*cmath.pi**2) if MBP3 else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_255_159 = Coupling(name = 'UVGC_255_159',
                        value = {-1:'( (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) if MBP3 else -0.027777777777777776*(ee*complex(0,1)*G**2)/cmath.pi**2 )',0:'( (5*ee*complex(0,1)*G**2)/(36.*cmath.pi**2) - (ee*complex(0,1)*G**2*reglog(MBP3/MU_R))/(6.*cmath.pi**2) if MBP3 else (ee*complex(0,1)*G**2)/(36.*cmath.pi**2) ) - (ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

UVGC_256_160 = Coupling(name = 'UVGC_256_160',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2 if MBP3 else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MBP3/MU_R))/(2.*cmath.pi**2) if MBP3 else -0.08333333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_257_161 = Coupling(name = 'UVGC_257_161',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBPBP1x3)/cmath.pi**2 if MBP1 else (complex(0,1)*G**2*KHBPBP1x3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBPBP1x3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP1x3*reglog(MBP1/MU_R))/(4.*cmath.pi**2) if MBP1 else -0.041666666666666664*(complex(0,1)*G**2*KHBPBP1x3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP1x3)/(24.*cmath.pi**2)'},
                        order = {'HB1B3':1,'QCD':2})

UVGC_257_162 = Coupling(name = 'UVGC_257_162',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBPBP1x3)/cmath.pi**2 if MBP3 else (complex(0,1)*G**2*KHBPBP1x3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBPBP1x3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP1x3*reglog(MBP3/MU_R))/(4.*cmath.pi**2) if MBP3 else -0.041666666666666664*(complex(0,1)*G**2*KHBPBP1x3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP1x3)/(24.*cmath.pi**2)'},
                        order = {'HB1B3':1,'QCD':2})

UVGC_257_163 = Coupling(name = 'UVGC_257_163',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHBPBP1x3)/cmath.pi**2'},
                        order = {'HB1B3':1,'QCD':2})

UVGC_258_164 = Coupling(name = 'UVGC_258_164',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBPBP2x3)/cmath.pi**2 if MBP2 else (complex(0,1)*G**2*KHBPBP2x3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBPBP2x3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP2x3*reglog(MBP2/MU_R))/(4.*cmath.pi**2) if MBP2 else -0.041666666666666664*(complex(0,1)*G**2*KHBPBP2x3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP2x3)/(24.*cmath.pi**2)'},
                        order = {'HB2B3':1,'QCD':2})

UVGC_258_165 = Coupling(name = 'UVGC_258_165',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBPBP2x3)/cmath.pi**2 if MBP3 else (complex(0,1)*G**2*KHBPBP2x3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBPBP2x3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP2x3*reglog(MBP3/MU_R))/(4.*cmath.pi**2) if MBP3 else -0.041666666666666664*(complex(0,1)*G**2*KHBPBP2x3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP2x3)/(24.*cmath.pi**2)'},
                        order = {'HB2B3':1,'QCD':2})

UVGC_258_166 = Coupling(name = 'UVGC_258_166',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHBPBP2x3)/cmath.pi**2'},
                        order = {'HB2B3':1,'QCD':2})

UVGC_259_167 = Coupling(name = 'UVGC_259_167',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBPBP3x1)/cmath.pi**2 if MBP1 else (complex(0,1)*G**2*KHBPBP3x1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBPBP3x1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP3x1*reglog(MBP1/MU_R))/(4.*cmath.pi**2) if MBP1 else -0.041666666666666664*(complex(0,1)*G**2*KHBPBP3x1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP3x1)/(24.*cmath.pi**2)'},
                        order = {'HB1B3':1,'QCD':2})

UVGC_259_168 = Coupling(name = 'UVGC_259_168',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBPBP3x1)/cmath.pi**2 if MBP3 else (complex(0,1)*G**2*KHBPBP3x1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBPBP3x1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP3x1*reglog(MBP3/MU_R))/(4.*cmath.pi**2) if MBP3 else -0.041666666666666664*(complex(0,1)*G**2*KHBPBP3x1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP3x1)/(24.*cmath.pi**2)'},
                        order = {'HB1B3':1,'QCD':2})

UVGC_259_169 = Coupling(name = 'UVGC_259_169',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHBPBP3x1)/cmath.pi**2'},
                        order = {'HB1B3':1,'QCD':2})

UVGC_260_170 = Coupling(name = 'UVGC_260_170',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBPBP3x2)/cmath.pi**2 if MBP2 else (complex(0,1)*G**2*KHBPBP3x2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBPBP3x2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP3x2*reglog(MBP2/MU_R))/(4.*cmath.pi**2) if MBP2 else -0.041666666666666664*(complex(0,1)*G**2*KHBPBP3x2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP3x2)/(24.*cmath.pi**2)'},
                        order = {'HB2B3':1,'QCD':2})

UVGC_260_171 = Coupling(name = 'UVGC_260_171',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBPBP3x2)/cmath.pi**2 if MBP3 else (complex(0,1)*G**2*KHBPBP3x2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBPBP3x2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP3x2*reglog(MBP3/MU_R))/(4.*cmath.pi**2) if MBP3 else -0.041666666666666664*(complex(0,1)*G**2*KHBPBP3x2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP3x2)/(24.*cmath.pi**2)'},
                        order = {'HB2B3':1,'QCD':2})

UVGC_260_172 = Coupling(name = 'UVGC_260_172',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHBPBP3x2)/cmath.pi**2'},
                        order = {'HB2B3':1,'QCD':2})

UVGC_261_173 = Coupling(name = 'UVGC_261_173',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KHBPBP3x3)/cmath.pi**2 if MBP3 else (complex(0,1)*G**2*KHBPBP3x3)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KHBPBP3x3)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KHBPBP3x3)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KHBPBP3x3*reglog(MBP3/MU_R))/(2.*cmath.pi**2) if MBP3 else -0.08333333333333333*(complex(0,1)*G**2*KHBPBP3x3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBPBP3x3)/(12.*cmath.pi**2)'},
                        order = {'HB3B3':1,'QCD':2})

UVGC_262_174 = Coupling(name = 'UVGC_262_174',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBSML3)/cmath.pi**2 if MB else (complex(0,1)*G**2*KHBSML3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBSML3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBSML3*reglog(MB/MU_R))/(4.*cmath.pi**2) if MB else -0.041666666666666664*(complex(0,1)*G**2*KHBSML3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBSML3)/(24.*cmath.pi**2)'},
                        order = {'HB3B':1,'QCD':2})

UVGC_262_175 = Coupling(name = 'UVGC_262_175',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBSML3)/cmath.pi**2 if MBP3 else (complex(0,1)*G**2*KHBSML3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBSML3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBSML3*reglog(MBP3/MU_R))/(4.*cmath.pi**2) if MBP3 else -0.041666666666666664*(complex(0,1)*G**2*KHBSML3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBSML3)/(24.*cmath.pi**2)'},
                        order = {'HB3B':1,'QCD':2})

UVGC_262_176 = Coupling(name = 'UVGC_262_176',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHBSML3)/cmath.pi**2'},
                        order = {'HB3B':1,'QCD':2})

UVGC_263_177 = Coupling(name = 'UVGC_263_177',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBSMR3)/cmath.pi**2 if MB else (complex(0,1)*G**2*KHBSMR3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBSMR3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBSMR3*reglog(MB/MU_R))/(4.*cmath.pi**2) if MB else -0.041666666666666664*(complex(0,1)*G**2*KHBSMR3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBSMR3)/(24.*cmath.pi**2)'},
                        order = {'HB3B':1,'QCD':2})

UVGC_263_178 = Coupling(name = 'UVGC_263_178',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHBSMR3)/cmath.pi**2 if MBP3 else (complex(0,1)*G**2*KHBSMR3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHBSMR3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHBSMR3*reglog(MBP3/MU_R))/(4.*cmath.pi**2) if MBP3 else -0.041666666666666664*(complex(0,1)*G**2*KHBSMR3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHBSMR3)/(24.*cmath.pi**2)'},
                        order = {'HB3B':1,'QCD':2})

UVGC_263_179 = Coupling(name = 'UVGC_263_179',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHBSMR3)/cmath.pi**2'},
                        order = {'HB3B':1,'QCD':2})

UVGC_264_180 = Coupling(name = 'UVGC_264_180',
                        value = {-1:'( (complex(0,1)*G**2*MBP3)/(6.*cmath.pi**2) if MBP3 else -0.08333333333333333*(complex(0,1)*G**2*MBP3)/cmath.pi**2 ) + (complex(0,1)*G**2*MBP3)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MBP3)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MBP3*reglog(MBP3/MU_R))/cmath.pi**2 if MBP3 else (complex(0,1)*G**2*MBP3)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MBP3)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_265_181 = Coupling(name = 'UVGC_265_181',
                        value = {-1:'( (complex(0,1)*G**2*MSQ1**2)/(6.*cmath.pi**2) if MSQ1 else (complex(0,1)*G**2*MSQ1**2)/(6.*cmath.pi**2) ) + (complex(0,1)*G**2*MSQ1**2)/(12.*cmath.pi**2)',0:'( (41*complex(0,1)*G**2*MSQ1**2)/(72.*cmath.pi**2) - (complex(0,1)*G**2*MSQ1**2*reglog(MSQ1/MU_R))/(2.*cmath.pi**2) if MSQ1 else -0.013888888888888888*(complex(0,1)*G**2*MSQ1**2)/cmath.pi**2 ) + (complex(0,1)*G**2*MSQ1**2)/(72.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_266_182 = Coupling(name = 'UVGC_266_182',
                        value = {-1:'( (complex(0,1)*G**2*MSQ2**2)/(6.*cmath.pi**2) if MSQ2 else (complex(0,1)*G**2*MSQ2**2)/(6.*cmath.pi**2) ) + (complex(0,1)*G**2*MSQ2**2)/(12.*cmath.pi**2)',0:'( (41*complex(0,1)*G**2*MSQ2**2)/(72.*cmath.pi**2) - (complex(0,1)*G**2*MSQ2**2*reglog(MSQ2/MU_R))/(2.*cmath.pi**2) if MSQ2 else -0.013888888888888888*(complex(0,1)*G**2*MSQ2**2)/cmath.pi**2 ) + (complex(0,1)*G**2*MSQ2**2)/(72.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_267_183 = Coupling(name = 'UVGC_267_183',
                        value = {-1:'( (complex(0,1)*G**2*MSQ3**2)/(6.*cmath.pi**2) if MSQ3 else (complex(0,1)*G**2*MSQ3**2)/(6.*cmath.pi**2) ) + (complex(0,1)*G**2*MSQ3**2)/(12.*cmath.pi**2)',0:'( (41*complex(0,1)*G**2*MSQ3**2)/(72.*cmath.pi**2) - (complex(0,1)*G**2*MSQ3**2*reglog(MSQ3/MU_R))/(2.*cmath.pi**2) if MSQ3 else -0.013888888888888888*(complex(0,1)*G**2*MSQ3**2)/cmath.pi**2 ) + (complex(0,1)*G**2*MSQ3**2)/(72.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_268_184 = Coupling(name = 'UVGC_268_184',
                        value = {-1:'( (complex(0,1)*G**2*MSQ4**2)/(6.*cmath.pi**2) if MSQ4 else (complex(0,1)*G**2*MSQ4**2)/(6.*cmath.pi**2) ) + (complex(0,1)*G**2*MSQ4**2)/(12.*cmath.pi**2)',0:'( (41*complex(0,1)*G**2*MSQ4**2)/(72.*cmath.pi**2) - (complex(0,1)*G**2*MSQ4**2*reglog(MSQ4/MU_R))/(2.*cmath.pi**2) if MSQ4 else -0.013888888888888888*(complex(0,1)*G**2*MSQ4**2)/cmath.pi**2 ) + (complex(0,1)*G**2*MSQ4**2)/(72.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_269_185 = Coupling(name = 'UVGC_269_185',
                        value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MT/MU_R))/(2.*cmath.pi**2) if MT else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_270_186 = Coupling(name = 'UVGC_270_186',
                        value = {-1:'( -0.1111111111111111*(ee*complex(0,1)*G**2)/cmath.pi**2 if MT else (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) )',0:'( (-5*ee*complex(0,1)*G**2)/(18.*cmath.pi**2) + (ee*complex(0,1)*G**2*reglog(MT/MU_R))/(3.*cmath.pi**2) if MT else -0.05555555555555555*(ee*complex(0,1)*G**2)/cmath.pi**2 ) + (ee*complex(0,1)*G**2)/(18.*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

UVGC_271_187 = Coupling(name = 'UVGC_271_187',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2 if MT else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MT/MU_R))/(2.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_272_188 = Coupling(name = 'UVGC_272_188',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS01TT)/cmath.pi**2 if MT else (complex(0,1)*G**2*KS01TT)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KS01TT)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KS01TT)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KS01TT*reglog(MT/MU_R))/(2.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**2*KS01TT)/cmath.pi**2 ) + (complex(0,1)*G**2*KS01TT)/(12.*cmath.pi**2)'},
                        order = {'QCD':2,'S01TT':1})

UVGC_273_189 = Coupling(name = 'UVGC_273_189',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS02TT)/cmath.pi**2 if MT else (complex(0,1)*G**2*KS02TT)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KS02TT)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KS02TT)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KS02TT*reglog(MT/MU_R))/(2.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**2*KS02TT)/cmath.pi**2 ) + (complex(0,1)*G**2*KS02TT)/(12.*cmath.pi**2)'},
                        order = {'QCD':2,'S02TT':1})

UVGC_274_190 = Coupling(name = 'UVGC_274_190',
                        value = {-1:'( (complex(0,1)*G**2*MT)/(6.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**2*MT)/cmath.pi**2 ) + (complex(0,1)*G**2*MT)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MT)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MT*reglog(MT/MU_R))/cmath.pi**2 if MT else (complex(0,1)*G**2*MT)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MT)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_275_191 = Coupling(name = 'UVGC_275_191',
                        value = {-1:'( -0.08333333333333333*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2)) if MB else (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) )',0:'( (-5*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*G**2*reglog(MB/MU_R))/(4.*cmath.pi**2*sw*cmath.sqrt(2)) if MB else -0.041666666666666664*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2)) ) + (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                        order = {'QCD':2,'QED':1})

UVGC_275_192 = Coupling(name = 'UVGC_275_192',
                        value = {-1:'( -0.08333333333333333*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2)) if MT else (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) )',0:'( (-5*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*G**2*reglog(MT/MU_R))/(4.*cmath.pi**2*sw*cmath.sqrt(2)) if MT else -0.041666666666666664*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2)) ) + (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                        order = {'QCD':2,'QED':1})

UVGC_276_193 = Coupling(name = 'UVGC_276_193',
                        value = {-1:'( -0.08333333333333333*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2) if MT else (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) - (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)',0:'( (-5*cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (5*ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) + (cw*ee*complex(0,1)*G**2*reglog(MT/MU_R))/(4.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw*reglog(MT/MU_R))/(12.*cw*cmath.pi**2) if MT else -0.041666666666666664*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) + (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

UVGC_277_194 = Coupling(name = 'UVGC_277_194',
                        value = {-1:'( (ee*complex(0,1)*G**2*sw)/(9.*cw*cmath.pi**2) if MT else -0.05555555555555555*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) ) + (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2)',0:'( (5*ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2) - (ee*complex(0,1)*G**2*sw*reglog(MT/MU_R))/(3.*cw*cmath.pi**2) if MT else (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

#UVGC_278_195 = Coupling(name = 'UVGC_278_195',
                        #value = {-1:'( (complex(0,1)*G**2*KHTT)/(6.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yt)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else -0.08333333333333333*(complex(0,1)*G**2*KHTT)/(cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*KHTT)/(3.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (5*complex(0,1)*G**2*KHTT)/(12.*cmath.pi**2*cmath.sqrt(2)) + (3*complex(0,1)*G**2*yt)/(4.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*KHTT*reglog(MT/MU_R))/(2.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yt*reglog(MT/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MT else (complex(0,1)*G**2*KHTT)/(12.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*KHTT)/(12.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                        #order = {'HTTMOD':1,'QCD':2})

UVGC_279_196 = Coupling(name = 'UVGC_279_196',
                        value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MTP1 else -0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MTP1/MU_R))/(2.*cmath.pi**2) if MTP1 else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_280_197 = Coupling(name = 'UVGC_280_197',
                        value = {-1:'( -0.1111111111111111*(ee*complex(0,1)*G**2)/cmath.pi**2 if MTP1 else (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) )',0:'( (-5*ee*complex(0,1)*G**2)/(18.*cmath.pi**2) + (ee*complex(0,1)*G**2*reglog(MTP1/MU_R))/(3.*cmath.pi**2) if MTP1 else -0.05555555555555555*(ee*complex(0,1)*G**2)/cmath.pi**2 ) + (ee*complex(0,1)*G**2)/(18.*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

UVGC_281_198 = Coupling(name = 'UVGC_281_198',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2 if MTP1 else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MTP1/MU_R))/(2.*cmath.pi**2) if MTP1 else -0.08333333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_282_199 = Coupling(name = 'UVGC_282_199',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KHTPTP1x1)/cmath.pi**2 if MTP1 else (complex(0,1)*G**2*KHTPTP1x1)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KHTPTP1x1)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KHTPTP1x1)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP1x1*reglog(MTP1/MU_R))/(2.*cmath.pi**2) if MTP1 else -0.08333333333333333*(complex(0,1)*G**2*KHTPTP1x1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP1x1)/(12.*cmath.pi**2)'},
                        order = {'HT1T1':1,'QCD':2})

UVGC_283_200 = Coupling(name = 'UVGC_283_200',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSML1)/cmath.pi**2 if MT else (complex(0,1)*G**2*KHTSML1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSML1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSML1*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else -0.041666666666666664*(complex(0,1)*G**2*KHTSML1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSML1)/(24.*cmath.pi**2)'},
                        order = {'HT1T':1,'QCD':2})

UVGC_283_201 = Coupling(name = 'UVGC_283_201',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSML1)/cmath.pi**2 if MTP1 else (complex(0,1)*G**2*KHTSML1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSML1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSML1*reglog(MTP1/MU_R))/(4.*cmath.pi**2) if MTP1 else -0.041666666666666664*(complex(0,1)*G**2*KHTSML1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSML1)/(24.*cmath.pi**2)'},
                        order = {'HT1T':1,'QCD':2})

UVGC_283_202 = Coupling(name = 'UVGC_283_202',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTSML1)/cmath.pi**2'},
                        order = {'HT1T':1,'QCD':2})

UVGC_284_203 = Coupling(name = 'UVGC_284_203',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSMR1)/cmath.pi**2 if MT else (complex(0,1)*G**2*KHTSMR1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSMR1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSMR1*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else -0.041666666666666664*(complex(0,1)*G**2*KHTSMR1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSMR1)/(24.*cmath.pi**2)'},
                        order = {'HT1T':1,'QCD':2})

UVGC_284_204 = Coupling(name = 'UVGC_284_204',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSMR1)/cmath.pi**2 if MTP1 else (complex(0,1)*G**2*KHTSMR1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSMR1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSMR1*reglog(MTP1/MU_R))/(4.*cmath.pi**2) if MTP1 else -0.041666666666666664*(complex(0,1)*G**2*KHTSMR1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSMR1)/(24.*cmath.pi**2)'},
                        order = {'HT1T':1,'QCD':2})

UVGC_284_205 = Coupling(name = 'UVGC_284_205',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTSMR1)/cmath.pi**2'},
                        order = {'HT1T':1,'QCD':2})

UVGC_285_206 = Coupling(name = 'UVGC_285_206',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS01T1T1)/cmath.pi**2 if MTP1 else (complex(0,1)*G**2*KS01T1T1)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KS01T1T1)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KS01T1T1)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KS01T1T1*reglog(MTP1/MU_R))/(2.*cmath.pi**2) if MTP1 else -0.08333333333333333*(complex(0,1)*G**2*KS01T1T1)/cmath.pi**2 ) + (complex(0,1)*G**2*KS01T1T1)/(12.*cmath.pi**2)'},
                        order = {'QCD':2,'S01T1T1':1})

UVGC_286_207 = Coupling(name = 'UVGC_286_207',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS02T1T1)/cmath.pi**2 if MTP1 else (complex(0,1)*G**2*KS02T1T1)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KS02T1T1)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KS02T1T1)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KS02T1T1*reglog(MTP1/MU_R))/(2.*cmath.pi**2) if MTP1 else -0.08333333333333333*(complex(0,1)*G**2*KS02T1T1)/cmath.pi**2 ) + (complex(0,1)*G**2*KS02T1T1)/(12.*cmath.pi**2)'},
                        order = {'QCD':2,'S02T1T1':1})

UVGC_287_208 = Coupling(name = 'UVGC_287_208',
                        value = {-1:'( (complex(0,1)*G**2*MTP1)/(6.*cmath.pi**2) if MTP1 else -0.08333333333333333*(complex(0,1)*G**2*MTP1)/cmath.pi**2 ) + (complex(0,1)*G**2*MTP1)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MTP1)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MTP1*reglog(MTP1/MU_R))/cmath.pi**2 if MTP1 else (complex(0,1)*G**2*MTP1)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MTP1)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_288_209 = Coupling(name = 'UVGC_288_209',
                        value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MTP2 else -0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MTP2/MU_R))/(2.*cmath.pi**2) if MTP2 else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_289_210 = Coupling(name = 'UVGC_289_210',
                        value = {-1:'( -0.1111111111111111*(ee*complex(0,1)*G**2)/cmath.pi**2 if MTP2 else (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) )',0:'( (-5*ee*complex(0,1)*G**2)/(18.*cmath.pi**2) + (ee*complex(0,1)*G**2*reglog(MTP2/MU_R))/(3.*cmath.pi**2) if MTP2 else -0.05555555555555555*(ee*complex(0,1)*G**2)/cmath.pi**2 ) + (ee*complex(0,1)*G**2)/(18.*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

UVGC_290_211 = Coupling(name = 'UVGC_290_211',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2 if MTP2 else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MTP2/MU_R))/(2.*cmath.pi**2) if MTP2 else -0.08333333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_291_212 = Coupling(name = 'UVGC_291_212',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP1x2)/cmath.pi**2 if MTP1 else (complex(0,1)*G**2*KHTPTP1x2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP1x2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP1x2*reglog(MTP1/MU_R))/(4.*cmath.pi**2) if MTP1 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP1x2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP1x2)/(24.*cmath.pi**2)'},
                        order = {'HT1T2':1,'QCD':2})

UVGC_291_213 = Coupling(name = 'UVGC_291_213',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP1x2)/cmath.pi**2 if MTP2 else (complex(0,1)*G**2*KHTPTP1x2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP1x2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP1x2*reglog(MTP2/MU_R))/(4.*cmath.pi**2) if MTP2 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP1x2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP1x2)/(24.*cmath.pi**2)'},
                        order = {'HT1T2':1,'QCD':2})

UVGC_291_214 = Coupling(name = 'UVGC_291_214',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTPTP1x2)/cmath.pi**2'},
                        order = {'HT1T2':1,'QCD':2})

UVGC_292_215 = Coupling(name = 'UVGC_292_215',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP2x1)/cmath.pi**2 if MTP1 else (complex(0,1)*G**2*KHTPTP2x1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP2x1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP2x1*reglog(MTP1/MU_R))/(4.*cmath.pi**2) if MTP1 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP2x1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP2x1)/(24.*cmath.pi**2)'},
                        order = {'HT1T2':1,'QCD':2})

UVGC_292_216 = Coupling(name = 'UVGC_292_216',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP2x1)/cmath.pi**2 if MTP2 else (complex(0,1)*G**2*KHTPTP2x1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP2x1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP2x1*reglog(MTP2/MU_R))/(4.*cmath.pi**2) if MTP2 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP2x1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP2x1)/(24.*cmath.pi**2)'},
                        order = {'HT1T2':1,'QCD':2})

UVGC_292_217 = Coupling(name = 'UVGC_292_217',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTPTP2x1)/cmath.pi**2'},
                        order = {'HT1T2':1,'QCD':2})

UVGC_293_218 = Coupling(name = 'UVGC_293_218',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KHTPTP2x2)/cmath.pi**2 if MTP2 else (complex(0,1)*G**2*KHTPTP2x2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KHTPTP2x2)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KHTPTP2x2)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP2x2*reglog(MTP2/MU_R))/(2.*cmath.pi**2) if MTP2 else -0.08333333333333333*(complex(0,1)*G**2*KHTPTP2x2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP2x2)/(12.*cmath.pi**2)'},
                        order = {'HT2T2':1,'QCD':2})

UVGC_294_219 = Coupling(name = 'UVGC_294_219',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSML2)/cmath.pi**2 if MT else (complex(0,1)*G**2*KHTSML2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSML2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSML2*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else -0.041666666666666664*(complex(0,1)*G**2*KHTSML2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSML2)/(24.*cmath.pi**2)'},
                        order = {'HT2T':1,'QCD':2})

UVGC_294_220 = Coupling(name = 'UVGC_294_220',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSML2)/cmath.pi**2 if MTP2 else (complex(0,1)*G**2*KHTSML2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSML2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSML2*reglog(MTP2/MU_R))/(4.*cmath.pi**2) if MTP2 else -0.041666666666666664*(complex(0,1)*G**2*KHTSML2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSML2)/(24.*cmath.pi**2)'},
                        order = {'HT2T':1,'QCD':2})

UVGC_294_221 = Coupling(name = 'UVGC_294_221',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTSML2)/cmath.pi**2'},
                        order = {'HT2T':1,'QCD':2})

UVGC_295_222 = Coupling(name = 'UVGC_295_222',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSMR2)/cmath.pi**2 if MT else (complex(0,1)*G**2*KHTSMR2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSMR2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSMR2*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else -0.041666666666666664*(complex(0,1)*G**2*KHTSMR2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSMR2)/(24.*cmath.pi**2)'},
                        order = {'HT2T':1,'QCD':2})

UVGC_295_223 = Coupling(name = 'UVGC_295_223',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSMR2)/cmath.pi**2 if MTP2 else (complex(0,1)*G**2*KHTSMR2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSMR2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSMR2*reglog(MTP2/MU_R))/(4.*cmath.pi**2) if MTP2 else -0.041666666666666664*(complex(0,1)*G**2*KHTSMR2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSMR2)/(24.*cmath.pi**2)'},
                        order = {'HT2T':1,'QCD':2})

UVGC_295_224 = Coupling(name = 'UVGC_295_224',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTSMR2)/cmath.pi**2'},
                        order = {'HT2T':1,'QCD':2})

UVGC_296_225 = Coupling(name = 'UVGC_296_225',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS01T2T2)/cmath.pi**2 if MTP2 else (complex(0,1)*G**2*KS01T2T2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KS01T2T2)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KS01T2T2)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KS01T2T2*reglog(MTP2/MU_R))/(2.*cmath.pi**2) if MTP2 else -0.08333333333333333*(complex(0,1)*G**2*KS01T2T2)/cmath.pi**2 ) + (complex(0,1)*G**2*KS01T2T2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2,'S01T2T2':1})

UVGC_297_226 = Coupling(name = 'UVGC_297_226',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KS02T2T2)/cmath.pi**2 if MTP2 else (complex(0,1)*G**2*KS02T2T2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KS02T2T2)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KS02T2T2)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KS02T2T2*reglog(MTP2/MU_R))/(2.*cmath.pi**2) if MTP2 else -0.08333333333333333*(complex(0,1)*G**2*KS02T2T2)/cmath.pi**2 ) + (complex(0,1)*G**2*KS02T2T2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2,'S02T2T2':1})

UVGC_298_227 = Coupling(name = 'UVGC_298_227',
                        value = {-1:'( (complex(0,1)*G**2*MTP2)/(6.*cmath.pi**2) if MTP2 else -0.08333333333333333*(complex(0,1)*G**2*MTP2)/cmath.pi**2 ) + (complex(0,1)*G**2*MTP2)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MTP2)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MTP2*reglog(MTP2/MU_R))/cmath.pi**2 if MTP2 else (complex(0,1)*G**2*MTP2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MTP2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_299_228 = Coupling(name = 'UVGC_299_228',
                        value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MTP3 else -0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MTP3/MU_R))/(2.*cmath.pi**2) if MTP3 else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_300_229 = Coupling(name = 'UVGC_300_229',
                        value = {-1:'( -0.1111111111111111*(ee*complex(0,1)*G**2)/cmath.pi**2 if MTP3 else (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) )',0:'( (-5*ee*complex(0,1)*G**2)/(18.*cmath.pi**2) + (ee*complex(0,1)*G**2*reglog(MTP3/MU_R))/(3.*cmath.pi**2) if MTP3 else -0.05555555555555555*(ee*complex(0,1)*G**2)/cmath.pi**2 ) + (ee*complex(0,1)*G**2)/(18.*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

UVGC_301_230 = Coupling(name = 'UVGC_301_230',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2 if MTP3 else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MTP3/MU_R))/(2.*cmath.pi**2) if MTP3 else -0.08333333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_302_231 = Coupling(name = 'UVGC_302_231',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP1x3)/cmath.pi**2 if MTP1 else (complex(0,1)*G**2*KHTPTP1x3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP1x3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP1x3*reglog(MTP1/MU_R))/(4.*cmath.pi**2) if MTP1 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP1x3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP1x3)/(24.*cmath.pi**2)'},
                        order = {'HT1T3':1,'QCD':2})

UVGC_302_232 = Coupling(name = 'UVGC_302_232',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP1x3)/cmath.pi**2 if MTP3 else (complex(0,1)*G**2*KHTPTP1x3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP1x3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP1x3*reglog(MTP3/MU_R))/(4.*cmath.pi**2) if MTP3 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP1x3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP1x3)/(24.*cmath.pi**2)'},
                        order = {'HT1T3':1,'QCD':2})

UVGC_302_233 = Coupling(name = 'UVGC_302_233',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTPTP1x3)/cmath.pi**2'},
                        order = {'HT1T3':1,'QCD':2})

UVGC_303_234 = Coupling(name = 'UVGC_303_234',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP2x3)/cmath.pi**2 if MTP2 else (complex(0,1)*G**2*KHTPTP2x3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP2x3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP2x3*reglog(MTP2/MU_R))/(4.*cmath.pi**2) if MTP2 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP2x3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP2x3)/(24.*cmath.pi**2)'},
                        order = {'HT2T3':1,'QCD':2})

UVGC_303_235 = Coupling(name = 'UVGC_303_235',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP2x3)/cmath.pi**2 if MTP3 else (complex(0,1)*G**2*KHTPTP2x3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP2x3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP2x3*reglog(MTP3/MU_R))/(4.*cmath.pi**2) if MTP3 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP2x3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP2x3)/(24.*cmath.pi**2)'},
                        order = {'HT2T3':1,'QCD':2})

UVGC_303_236 = Coupling(name = 'UVGC_303_236',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTPTP2x3)/cmath.pi**2'},
                        order = {'HT2T3':1,'QCD':2})

UVGC_304_237 = Coupling(name = 'UVGC_304_237',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP3x1)/cmath.pi**2 if MTP1 else (complex(0,1)*G**2*KHTPTP3x1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP3x1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP3x1*reglog(MTP1/MU_R))/(4.*cmath.pi**2) if MTP1 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP3x1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP3x1)/(24.*cmath.pi**2)'},
                        order = {'HT1T3':1,'QCD':2})

UVGC_304_238 = Coupling(name = 'UVGC_304_238',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP3x1)/cmath.pi**2 if MTP3 else (complex(0,1)*G**2*KHTPTP3x1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP3x1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP3x1*reglog(MTP3/MU_R))/(4.*cmath.pi**2) if MTP3 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP3x1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP3x1)/(24.*cmath.pi**2)'},
                        order = {'HT1T3':1,'QCD':2})

UVGC_304_239 = Coupling(name = 'UVGC_304_239',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTPTP3x1)/cmath.pi**2'},
                        order = {'HT1T3':1,'QCD':2})

UVGC_305_240 = Coupling(name = 'UVGC_305_240',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP3x2)/cmath.pi**2 if MTP2 else (complex(0,1)*G**2*KHTPTP3x2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP3x2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP3x2*reglog(MTP2/MU_R))/(4.*cmath.pi**2) if MTP2 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP3x2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP3x2)/(24.*cmath.pi**2)'},
                        order = {'HT2T3':1,'QCD':2})

UVGC_305_241 = Coupling(name = 'UVGC_305_241',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP3x2)/cmath.pi**2 if MTP3 else (complex(0,1)*G**2*KHTPTP3x2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP3x2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP3x2*reglog(MTP3/MU_R))/(4.*cmath.pi**2) if MTP3 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP3x2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP3x2)/(24.*cmath.pi**2)'},
                        order = {'HT2T3':1,'QCD':2})

UVGC_305_242 = Coupling(name = 'UVGC_305_242',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTPTP3x2)/cmath.pi**2'},
                        order = {'HT2T3':1,'QCD':2})

UVGC_306_243 = Coupling(name = 'UVGC_306_243',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KHTPTP3x3)/cmath.pi**2 if MTP3 else (complex(0,1)*G**2*KHTPTP3x3)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KHTPTP3x3)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KHTPTP3x3)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP3x3*reglog(MTP3/MU_R))/(2.*cmath.pi**2) if MTP3 else -0.08333333333333333*(complex(0,1)*G**2*KHTPTP3x3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP3x3)/(12.*cmath.pi**2)'},
                        order = {'HT3T3':1,'QCD':2})

UVGC_307_244 = Coupling(name = 'UVGC_307_244',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSML3)/cmath.pi**2 if MT else (complex(0,1)*G**2*KHTSML3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSML3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSML3*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else -0.041666666666666664*(complex(0,1)*G**2*KHTSML3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSML3)/(24.*cmath.pi**2)'},
                        order = {'HT3T':1,'QCD':2})

UVGC_307_245 = Coupling(name = 'UVGC_307_245',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSML3)/cmath.pi**2 if MTP3 else (complex(0,1)*G**2*KHTSML3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSML3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSML3*reglog(MTP3/MU_R))/(4.*cmath.pi**2) if MTP3 else -0.041666666666666664*(complex(0,1)*G**2*KHTSML3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSML3)/(24.*cmath.pi**2)'},
                        order = {'HT3T':1,'QCD':2})

UVGC_307_246 = Coupling(name = 'UVGC_307_246',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTSML3)/cmath.pi**2'},
                        order = {'HT3T':1,'QCD':2})

UVGC_308_247 = Coupling(name = 'UVGC_308_247',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSMR3)/cmath.pi**2 if MT else (complex(0,1)*G**2*KHTSMR3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSMR3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSMR3*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else -0.041666666666666664*(complex(0,1)*G**2*KHTSMR3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSMR3)/(24.*cmath.pi**2)'},
                        order = {'HT3T':1,'QCD':2})

UVGC_308_248 = Coupling(name = 'UVGC_308_248',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSMR3)/cmath.pi**2 if MTP3 else (complex(0,1)*G**2*KHTSMR3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSMR3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSMR3*reglog(MTP3/MU_R))/(4.*cmath.pi**2) if MTP3 else -0.041666666666666664*(complex(0,1)*G**2*KHTSMR3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSMR3)/(24.*cmath.pi**2)'},
                        order = {'HT3T':1,'QCD':2})

UVGC_308_249 = Coupling(name = 'UVGC_308_249',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTSMR3)/cmath.pi**2'},
                        order = {'HT3T':1,'QCD':2})

UVGC_309_250 = Coupling(name = 'UVGC_309_250',
                        value = {-1:'( (complex(0,1)*G**2*MTP3)/(6.*cmath.pi**2) if MTP3 else -0.08333333333333333*(complex(0,1)*G**2*MTP3)/cmath.pi**2 ) + (complex(0,1)*G**2*MTP3)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MTP3)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MTP3*reglog(MTP3/MU_R))/cmath.pi**2 if MTP3 else (complex(0,1)*G**2*MTP3)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MTP3)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_310_251 = Coupling(name = 'UVGC_310_251',
                        value = {-1:'( 0 if MB else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MB/MU_R))/(12.*cmath.pi**2) if MB else 0 )'},
                        order = {'QCD':2})

UVGC_310_252 = Coupling(name = 'UVGC_310_252',
                        value = {-1:'( 0 if MBP1 else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MBP1/MU_R))/(12.*cmath.pi**2) if MBP1 else 0 )'},
                        order = {'QCD':2})

UVGC_310_253 = Coupling(name = 'UVGC_310_253',
                        value = {-1:'( 0 if MBP2 else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MBP2/MU_R))/(12.*cmath.pi**2) if MBP2 else 0 )'},
                        order = {'QCD':2})

UVGC_310_254 = Coupling(name = 'UVGC_310_254',
                        value = {-1:'( 0 if MBP3 else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MBP3/MU_R))/(12.*cmath.pi**2) if MBP3 else 0 )'},
                        order = {'QCD':2})

UVGC_310_255 = Coupling(name = 'UVGC_310_255',
                        value = {-1:'( 0 if MSQ1 else (complex(0,1)*G**2)/(96.*cmath.pi**2) ) - (complex(0,1)*G**2)/(96.*cmath.pi**2)',0:'( (complex(0,1)*G**2)/(96.*cmath.pi**2) + (complex(0,1)*G**2*reglog(MSQ1/MU_R))/(48.*cmath.pi**2) if MSQ1 else (complex(0,1)*G**2)/(96.*cmath.pi**2) ) - (complex(0,1)*G**2)/(96.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_310_256 = Coupling(name = 'UVGC_310_256',
                        value = {-1:'( 0 if MSQ2 else (complex(0,1)*G**2)/(96.*cmath.pi**2) ) - (complex(0,1)*G**2)/(96.*cmath.pi**2)',0:'( (complex(0,1)*G**2)/(96.*cmath.pi**2) + (complex(0,1)*G**2*reglog(MSQ2/MU_R))/(48.*cmath.pi**2) if MSQ2 else (complex(0,1)*G**2)/(96.*cmath.pi**2) ) - (complex(0,1)*G**2)/(96.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_310_257 = Coupling(name = 'UVGC_310_257',
                        value = {-1:'( 0 if MSQ3 else (complex(0,1)*G**2)/(96.*cmath.pi**2) ) - (complex(0,1)*G**2)/(96.*cmath.pi**2)',0:'( (complex(0,1)*G**2)/(96.*cmath.pi**2) + (complex(0,1)*G**2*reglog(MSQ3/MU_R))/(48.*cmath.pi**2) if MSQ3 else (complex(0,1)*G**2)/(96.*cmath.pi**2) ) - (complex(0,1)*G**2)/(96.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_310_258 = Coupling(name = 'UVGC_310_258',
                        value = {-1:'( 0 if MSQ4 else (complex(0,1)*G**2)/(96.*cmath.pi**2) ) - (complex(0,1)*G**2)/(96.*cmath.pi**2)',0:'( (complex(0,1)*G**2)/(96.*cmath.pi**2) + (complex(0,1)*G**2*reglog(MSQ4/MU_R))/(48.*cmath.pi**2) if MSQ4 else (complex(0,1)*G**2)/(96.*cmath.pi**2) ) - (complex(0,1)*G**2)/(96.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_310_259 = Coupling(name = 'UVGC_310_259',
                        value = {-1:'( 0 if MT else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                        order = {'QCD':2})

UVGC_310_260 = Coupling(name = 'UVGC_310_260',
                        value = {-1:'( 0 if MTP1 else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MTP1/MU_R))/(12.*cmath.pi**2) if MTP1 else 0 )'},
                        order = {'QCD':2})

UVGC_310_261 = Coupling(name = 'UVGC_310_261',
                        value = {-1:'( 0 if MTP2 else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MTP2/MU_R))/(12.*cmath.pi**2) if MTP2 else 0 )'},
                        order = {'QCD':2})

UVGC_310_262 = Coupling(name = 'UVGC_310_262',
                        value = {-1:'( 0 if MTP3 else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MTP3/MU_R))/(12.*cmath.pi**2) if MTP3 else 0 )'},
                        order = {'QCD':2})

UVGC_310_263 = Coupling(name = 'UVGC_310_263',
                        value = {-1:'( 0 if MTP4 else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MTP4/MU_R))/(12.*cmath.pi**2) if MTP4 else 0 )'},
                        order = {'QCD':2})

UVGC_311_264 = Coupling(name = 'UVGC_311_264',
                        value = {-1:'( 0 if MB else -0.0625*G**3/cmath.pi**2 ) + G**3/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(G**3*reglog(MB/MU_R))/cmath.pi**2 if MB else 0 )'},
                        order = {'QCD':3})

UVGC_311_265 = Coupling(name = 'UVGC_311_265',
                        value = {-1:'( 0 if MBP1 else -0.0625*G**3/cmath.pi**2 ) + G**3/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(G**3*reglog(MBP1/MU_R))/cmath.pi**2 if MBP1 else 0 )'},
                        order = {'QCD':3})

UVGC_311_266 = Coupling(name = 'UVGC_311_266',
                        value = {-1:'( 0 if MBP2 else -0.0625*G**3/cmath.pi**2 ) + G**3/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(G**3*reglog(MBP2/MU_R))/cmath.pi**2 if MBP2 else 0 )'},
                        order = {'QCD':3})

UVGC_311_267 = Coupling(name = 'UVGC_311_267',
                        value = {-1:'( 0 if MBP3 else -0.0625*G**3/cmath.pi**2 ) + G**3/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(G**3*reglog(MBP3/MU_R))/cmath.pi**2 if MBP3 else 0 )'},
                        order = {'QCD':3})

UVGC_311_268 = Coupling(name = 'UVGC_311_268',
                        value = {-1:'-0.020833333333333332*G**3/cmath.pi**2'},
                        order = {'QCD':3})

UVGC_311_269 = Coupling(name = 'UVGC_311_269',
                        value = {-1:'( 0 if MSQ1 else -0.015625*G**3/cmath.pi**2 )',0:'( -0.010416666666666666*G**3/cmath.pi**2 - (G**3*reglog(MSQ1/MU_R))/(48.*cmath.pi**2) if MSQ1 else -0.010416666666666666*G**3/cmath.pi**2 ) + G**3/(96.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_311_270 = Coupling(name = 'UVGC_311_270',
                        value = {-1:'( 0 if MSQ2 else -0.015625*G**3/cmath.pi**2 )',0:'( -0.010416666666666666*G**3/cmath.pi**2 - (G**3*reglog(MSQ2/MU_R))/(48.*cmath.pi**2) if MSQ2 else -0.010416666666666666*G**3/cmath.pi**2 ) + G**3/(96.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_311_271 = Coupling(name = 'UVGC_311_271',
                        value = {-1:'( 0 if MSQ3 else -0.015625*G**3/cmath.pi**2 )',0:'( -0.010416666666666666*G**3/cmath.pi**2 - (G**3*reglog(MSQ3/MU_R))/(48.*cmath.pi**2) if MSQ3 else -0.010416666666666666*G**3/cmath.pi**2 ) + G**3/(96.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_311_272 = Coupling(name = 'UVGC_311_272',
                        value = {-1:'( 0 if MSQ4 else -0.015625*G**3/cmath.pi**2 )',0:'( -0.010416666666666666*G**3/cmath.pi**2 - (G**3*reglog(MSQ4/MU_R))/(48.*cmath.pi**2) if MSQ4 else -0.010416666666666666*G**3/cmath.pi**2 ) + G**3/(96.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_311_273 = Coupling(name = 'UVGC_311_273',
                        value = {-1:'( 0 if MT else -0.0625*G**3/cmath.pi**2 ) + G**3/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(G**3*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                        order = {'QCD':3})

UVGC_311_274 = Coupling(name = 'UVGC_311_274',
                        value = {-1:'( 0 if MTP1 else -0.0625*G**3/cmath.pi**2 ) + G**3/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(G**3*reglog(MTP1/MU_R))/cmath.pi**2 if MTP1 else 0 )'},
                        order = {'QCD':3})

UVGC_311_275 = Coupling(name = 'UVGC_311_275',
                        value = {-1:'( 0 if MTP2 else -0.0625*G**3/cmath.pi**2 ) + G**3/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(G**3*reglog(MTP2/MU_R))/cmath.pi**2 if MTP2 else 0 )'},
                        order = {'QCD':3})

UVGC_311_276 = Coupling(name = 'UVGC_311_276',
                        value = {-1:'( 0 if MTP3 else -0.0625*G**3/cmath.pi**2 ) + G**3/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(G**3*reglog(MTP3/MU_R))/cmath.pi**2 if MTP3 else 0 )'},
                        order = {'QCD':3})

UVGC_311_277 = Coupling(name = 'UVGC_311_277',
                        value = {-1:'( 0 if MTP4 else -0.0625*G**3/cmath.pi**2 ) + G**3/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(G**3*reglog(MTP4/MU_R))/cmath.pi**2 if MTP4 else 0 )'},
                        order = {'QCD':3})

UVGC_312_278 = Coupling(name = 'UVGC_312_278',
                        value = {-1:'( 0 if MB else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MB/MU_R))/cmath.pi**2 if MB else 0 )'},
                        order = {'QCD':4})

UVGC_312_279 = Coupling(name = 'UVGC_312_279',
                        value = {-1:'( 0 if MBP1 else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MBP1/MU_R))/cmath.pi**2 if MBP1 else 0 )'},
                        order = {'QCD':4})

UVGC_312_280 = Coupling(name = 'UVGC_312_280',
                        value = {-1:'( 0 if MBP2 else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MBP2/MU_R))/cmath.pi**2 if MBP2 else 0 )'},
                        order = {'QCD':4})

UVGC_312_281 = Coupling(name = 'UVGC_312_281',
                        value = {-1:'( 0 if MBP3 else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MBP3/MU_R))/cmath.pi**2 if MBP3 else 0 )'},
                        order = {'QCD':4})

UVGC_312_282 = Coupling(name = 'UVGC_312_282',
                        value = {-1:'(147*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_312_283 = Coupling(name = 'UVGC_312_283',
                        value = {-1:'(21*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_312_284 = Coupling(name = 'UVGC_312_284',
                        value = {-1:'( 0 if MSQ1 else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MSQ1/MU_R))/(48.*cmath.pi**2) if MSQ1 else -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_312_285 = Coupling(name = 'UVGC_312_285',
                        value = {-1:'( 0 if MSQ2 else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MSQ2/MU_R))/(48.*cmath.pi**2) if MSQ2 else -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_312_286 = Coupling(name = 'UVGC_312_286',
                        value = {-1:'( 0 if MSQ3 else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MSQ3/MU_R))/(48.*cmath.pi**2) if MSQ3 else -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_312_287 = Coupling(name = 'UVGC_312_287',
                        value = {-1:'( 0 if MSQ4 else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MSQ4/MU_R))/(48.*cmath.pi**2) if MSQ4 else -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_312_288 = Coupling(name = 'UVGC_312_288',
                        value = {-1:'( 0 if MT else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                        order = {'QCD':4})

UVGC_312_289 = Coupling(name = 'UVGC_312_289',
                        value = {-1:'( 0 if MTP1 else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MTP1/MU_R))/cmath.pi**2 if MTP1 else 0 )'},
                        order = {'QCD':4})

UVGC_312_290 = Coupling(name = 'UVGC_312_290',
                        value = {-1:'( 0 if MTP2 else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MTP2/MU_R))/cmath.pi**2 if MTP2 else 0 )'},
                        order = {'QCD':4})

UVGC_312_291 = Coupling(name = 'UVGC_312_291',
                        value = {-1:'( 0 if MTP3 else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MTP3/MU_R))/cmath.pi**2 if MTP3 else 0 )'},
                        order = {'QCD':4})

UVGC_312_292 = Coupling(name = 'UVGC_312_292',
                        value = {-1:'( 0 if MTP4 else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MTP4/MU_R))/cmath.pi**2 if MTP4 else 0 )'},
                        order = {'QCD':4})

UVGC_313_293 = Coupling(name = 'UVGC_313_293',
                        value = {-1:'(147*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_313_294 = Coupling(name = 'UVGC_313_294',
                        value = {-1:'(3*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_313_295 = Coupling(name = 'UVGC_313_295',
                        value = {-1:'( 0 if MSQ1 else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (5*complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MSQ1/MU_R))/(48.*cmath.pi**2) if MSQ1 else -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_313_296 = Coupling(name = 'UVGC_313_296',
                        value = {-1:'( 0 if MSQ2 else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (5*complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MSQ2/MU_R))/(48.*cmath.pi**2) if MSQ2 else -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_313_297 = Coupling(name = 'UVGC_313_297',
                        value = {-1:'( 0 if MSQ3 else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (5*complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MSQ3/MU_R))/(48.*cmath.pi**2) if MSQ3 else -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_313_298 = Coupling(name = 'UVGC_313_298',
                        value = {-1:'( 0 if MSQ4 else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (5*complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MSQ4/MU_R))/(48.*cmath.pi**2) if MSQ4 else -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_314_299 = Coupling(name = 'UVGC_314_299',
                        value = {-1:'( 0 if MB else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 )',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MB/MU_R))/cmath.pi**2 if MB else 0 )'},
                        order = {'QCD':4})

UVGC_314_300 = Coupling(name = 'UVGC_314_300',
                        value = {-1:'( 0 if MBP1 else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 )',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MBP1/MU_R))/cmath.pi**2 if MBP1 else 0 )'},
                        order = {'QCD':4})

UVGC_314_301 = Coupling(name = 'UVGC_314_301',
                        value = {-1:'( 0 if MBP2 else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 )',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MBP2/MU_R))/cmath.pi**2 if MBP2 else 0 )'},
                        order = {'QCD':4})

UVGC_314_302 = Coupling(name = 'UVGC_314_302',
                        value = {-1:'( 0 if MBP3 else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 )',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MBP3/MU_R))/cmath.pi**2 if MBP3 else 0 )'},
                        order = {'QCD':4})

UVGC_314_303 = Coupling(name = 'UVGC_314_303',
                        value = {-1:'-0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2'},
                        order = {'QCD':4})

UVGC_314_304 = Coupling(name = 'UVGC_314_304',
                        value = {-1:'(523*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_314_305 = Coupling(name = 'UVGC_314_305',
                        value = {-1:'(13*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_314_306 = Coupling(name = 'UVGC_314_306',
                        value = {-1:'( 0 if MSQ1 else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(32.*cmath.pi**2)',0:'( -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MSQ1/MU_R))/(48.*cmath.pi**2) if MSQ1 else -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_314_307 = Coupling(name = 'UVGC_314_307',
                        value = {-1:'( 0 if MSQ2 else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(32.*cmath.pi**2)',0:'( -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MSQ2/MU_R))/(48.*cmath.pi**2) if MSQ2 else -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_314_308 = Coupling(name = 'UVGC_314_308',
                        value = {-1:'( 0 if MSQ3 else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(32.*cmath.pi**2)',0:'( -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MSQ3/MU_R))/(48.*cmath.pi**2) if MSQ3 else -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_314_309 = Coupling(name = 'UVGC_314_309',
                        value = {-1:'( 0 if MSQ4 else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(32.*cmath.pi**2)',0:'( -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MSQ4/MU_R))/(48.*cmath.pi**2) if MSQ4 else -0.010416666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_314_310 = Coupling(name = 'UVGC_314_310',
                        value = {-1:'( 0 if MT else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 )',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                        order = {'QCD':4})

UVGC_314_311 = Coupling(name = 'UVGC_314_311',
                        value = {-1:'( 0 if MTP1 else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 )',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MTP1/MU_R))/cmath.pi**2 if MTP1 else 0 )'},
                        order = {'QCD':4})

UVGC_314_312 = Coupling(name = 'UVGC_314_312',
                        value = {-1:'( 0 if MTP2 else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 )',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MTP2/MU_R))/cmath.pi**2 if MTP2 else 0 )'},
                        order = {'QCD':4})

UVGC_314_313 = Coupling(name = 'UVGC_314_313',
                        value = {-1:'( 0 if MTP3 else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 )',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MTP3/MU_R))/cmath.pi**2 if MTP3 else 0 )'},
                        order = {'QCD':4})

UVGC_314_314 = Coupling(name = 'UVGC_314_314',
                        value = {-1:'( 0 if MTP4 else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 )',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MTP4/MU_R))/cmath.pi**2 if MTP4 else 0 )'},
                        order = {'QCD':4})

UVGC_315_315 = Coupling(name = 'UVGC_315_315',
                        value = {-1:'( 0 if MB else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MB/MU_R))/(12.*cmath.pi**2) if MB else 0 )'},
                        order = {'QCD':4})

UVGC_315_316 = Coupling(name = 'UVGC_315_316',
                        value = {-1:'( 0 if MBP1 else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MBP1/MU_R))/(12.*cmath.pi**2) if MBP1 else 0 )'},
                        order = {'QCD':4})

UVGC_315_317 = Coupling(name = 'UVGC_315_317',
                        value = {-1:'( 0 if MBP2 else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MBP2/MU_R))/(12.*cmath.pi**2) if MBP2 else 0 )'},
                        order = {'QCD':4})

UVGC_315_318 = Coupling(name = 'UVGC_315_318',
                        value = {-1:'( 0 if MBP3 else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MBP3/MU_R))/(12.*cmath.pi**2) if MBP3 else 0 )'},
                        order = {'QCD':4})

UVGC_315_319 = Coupling(name = 'UVGC_315_319',
                        value = {-1:'(-341*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_315_320 = Coupling(name = 'UVGC_315_320',
                        value = {-1:'(-11*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_315_321 = Coupling(name = 'UVGC_315_321',
                        value = {-1:'( 0 if MSQ1 else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(96.*cmath.pi**2) + (complex(0,1)*G**4*reglog(MSQ1/MU_R))/(48.*cmath.pi**2) if MSQ1 else (complex(0,1)*G**4)/(96.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_315_322 = Coupling(name = 'UVGC_315_322',
                        value = {-1:'( 0 if MSQ2 else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(96.*cmath.pi**2) + (complex(0,1)*G**4*reglog(MSQ2/MU_R))/(48.*cmath.pi**2) if MSQ2 else (complex(0,1)*G**4)/(96.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_315_323 = Coupling(name = 'UVGC_315_323',
                        value = {-1:'( 0 if MSQ3 else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(96.*cmath.pi**2) + (complex(0,1)*G**4*reglog(MSQ3/MU_R))/(48.*cmath.pi**2) if MSQ3 else (complex(0,1)*G**4)/(96.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_315_324 = Coupling(name = 'UVGC_315_324',
                        value = {-1:'( 0 if MSQ4 else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(96.*cmath.pi**2) + (complex(0,1)*G**4*reglog(MSQ4/MU_R))/(48.*cmath.pi**2) if MSQ4 else (complex(0,1)*G**4)/(96.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_315_325 = Coupling(name = 'UVGC_315_325',
                        value = {-1:'( 0 if MT else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                        order = {'QCD':4})

UVGC_315_326 = Coupling(name = 'UVGC_315_326',
                        value = {-1:'( 0 if MTP1 else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MTP1/MU_R))/(12.*cmath.pi**2) if MTP1 else 0 )'},
                        order = {'QCD':4})

UVGC_315_327 = Coupling(name = 'UVGC_315_327',
                        value = {-1:'( 0 if MTP2 else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MTP2/MU_R))/(12.*cmath.pi**2) if MTP2 else 0 )'},
                        order = {'QCD':4})

UVGC_315_328 = Coupling(name = 'UVGC_315_328',
                        value = {-1:'( 0 if MTP3 else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MTP3/MU_R))/(12.*cmath.pi**2) if MTP3 else 0 )'},
                        order = {'QCD':4})

UVGC_315_329 = Coupling(name = 'UVGC_315_329',
                        value = {-1:'( 0 if MTP4 else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MTP4/MU_R))/(12.*cmath.pi**2) if MTP4 else 0 )'},
                        order = {'QCD':4})

UVGC_316_330 = Coupling(name = 'UVGC_316_330',
                        value = {-1:'(-83*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_316_331 = Coupling(name = 'UVGC_316_331',
                        value = {-1:'(-5*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_317_332 = Coupling(name = 'UVGC_317_332',
                        value = {-1:'( 0 if MB else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MB/MU_R))/(12.*cmath.pi**2) if MB else 0 )'},
                        order = {'QCD':4})

UVGC_317_333 = Coupling(name = 'UVGC_317_333',
                        value = {-1:'( 0 if MBP1 else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MBP1/MU_R))/(12.*cmath.pi**2) if MBP1 else 0 )'},
                        order = {'QCD':4})

UVGC_317_334 = Coupling(name = 'UVGC_317_334',
                        value = {-1:'( 0 if MBP2 else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MBP2/MU_R))/(12.*cmath.pi**2) if MBP2 else 0 )'},
                        order = {'QCD':4})

UVGC_317_335 = Coupling(name = 'UVGC_317_335',
                        value = {-1:'( 0 if MBP3 else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MBP3/MU_R))/(12.*cmath.pi**2) if MBP3 else 0 )'},
                        order = {'QCD':4})

UVGC_317_336 = Coupling(name = 'UVGC_317_336',
                        value = {-1:'(complex(0,1)*G**4)/(12.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_317_337 = Coupling(name = 'UVGC_317_337',
                        value = {-1:'(-85*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_317_338 = Coupling(name = 'UVGC_317_338',
                        value = {-1:'(-19*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_317_339 = Coupling(name = 'UVGC_317_339',
                        value = {-1:'( 0 if MSQ1 else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) + (complex(0,1)*G**4)/(32.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(96.*cmath.pi**2) + (complex(0,1)*G**4*reglog(MSQ1/MU_R))/(48.*cmath.pi**2) if MSQ1 else (complex(0,1)*G**4)/(96.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_317_340 = Coupling(name = 'UVGC_317_340',
                        value = {-1:'( 0 if MSQ2 else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) + (complex(0,1)*G**4)/(32.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(96.*cmath.pi**2) + (complex(0,1)*G**4*reglog(MSQ2/MU_R))/(48.*cmath.pi**2) if MSQ2 else (complex(0,1)*G**4)/(96.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_317_341 = Coupling(name = 'UVGC_317_341',
                        value = {-1:'( 0 if MSQ3 else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) + (complex(0,1)*G**4)/(32.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(96.*cmath.pi**2) + (complex(0,1)*G**4*reglog(MSQ3/MU_R))/(48.*cmath.pi**2) if MSQ3 else (complex(0,1)*G**4)/(96.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_317_342 = Coupling(name = 'UVGC_317_342',
                        value = {-1:'( 0 if MSQ4 else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) + (complex(0,1)*G**4)/(32.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(96.*cmath.pi**2) + (complex(0,1)*G**4*reglog(MSQ4/MU_R))/(48.*cmath.pi**2) if MSQ4 else (complex(0,1)*G**4)/(96.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_317_343 = Coupling(name = 'UVGC_317_343',
                        value = {-1:'( 0 if MT else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                        order = {'QCD':4})

UVGC_317_344 = Coupling(name = 'UVGC_317_344',
                        value = {-1:'( 0 if MTP1 else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MTP1/MU_R))/(12.*cmath.pi**2) if MTP1 else 0 )'},
                        order = {'QCD':4})

UVGC_317_345 = Coupling(name = 'UVGC_317_345',
                        value = {-1:'( 0 if MTP2 else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MTP2/MU_R))/(12.*cmath.pi**2) if MTP2 else 0 )'},
                        order = {'QCD':4})

UVGC_317_346 = Coupling(name = 'UVGC_317_346',
                        value = {-1:'( 0 if MTP3 else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MTP3/MU_R))/(12.*cmath.pi**2) if MTP3 else 0 )'},
                        order = {'QCD':4})

UVGC_317_347 = Coupling(name = 'UVGC_317_347',
                        value = {-1:'( 0 if MTP4 else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MTP4/MU_R))/(12.*cmath.pi**2) if MTP4 else 0 )'},
                        order = {'QCD':4})

UVGC_318_348 = Coupling(name = 'UVGC_318_348',
                        value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MTP4 else -0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MTP4/MU_R))/(2.*cmath.pi**2) if MTP4 else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})

UVGC_319_349 = Coupling(name = 'UVGC_319_349',
                        value = {-1:'( -0.1111111111111111*(ee*complex(0,1)*G**2)/cmath.pi**2 if MTP4 else (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) )',0:'( (-5*ee*complex(0,1)*G**2)/(18.*cmath.pi**2) + (ee*complex(0,1)*G**2*reglog(MTP4/MU_R))/(3.*cmath.pi**2) if MTP4 else -0.05555555555555555*(ee*complex(0,1)*G**2)/cmath.pi**2 ) + (ee*complex(0,1)*G**2)/(18.*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

UVGC_320_350 = Coupling(name = 'UVGC_320_350',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2 if MTP4 else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MTP4/MU_R))/(2.*cmath.pi**2) if MTP4 else -0.08333333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_321_351 = Coupling(name = 'UVGC_321_351',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP1x4)/cmath.pi**2 if MTP1 else (complex(0,1)*G**2*KHTPTP1x4)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP1x4)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP1x4*reglog(MTP1/MU_R))/(4.*cmath.pi**2) if MTP1 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP1x4)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP1x4)/(24.*cmath.pi**2)'},
                        order = {'HT1T4':1,'QCD':2})

UVGC_321_352 = Coupling(name = 'UVGC_321_352',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP1x4)/cmath.pi**2 if MTP4 else (complex(0,1)*G**2*KHTPTP1x4)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP1x4)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP1x4*reglog(MTP4/MU_R))/(4.*cmath.pi**2) if MTP4 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP1x4)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP1x4)/(24.*cmath.pi**2)'},
                        order = {'HT1T4':1,'QCD':2})

UVGC_321_353 = Coupling(name = 'UVGC_321_353',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTPTP1x4)/cmath.pi**2'},
                        order = {'HT1T4':1,'QCD':2})

UVGC_322_354 = Coupling(name = 'UVGC_322_354',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP2x4)/cmath.pi**2 if MTP2 else (complex(0,1)*G**2*KHTPTP2x4)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP2x4)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP2x4*reglog(MTP2/MU_R))/(4.*cmath.pi**2) if MTP2 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP2x4)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP2x4)/(24.*cmath.pi**2)'},
                        order = {'HT2T4':1,'QCD':2})

UVGC_322_355 = Coupling(name = 'UVGC_322_355',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP2x4)/cmath.pi**2 if MTP4 else (complex(0,1)*G**2*KHTPTP2x4)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP2x4)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP2x4*reglog(MTP4/MU_R))/(4.*cmath.pi**2) if MTP4 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP2x4)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP2x4)/(24.*cmath.pi**2)'},
                        order = {'HT2T4':1,'QCD':2})

UVGC_322_356 = Coupling(name = 'UVGC_322_356',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTPTP2x4)/cmath.pi**2'},
                        order = {'HT2T4':1,'QCD':2})

UVGC_323_357 = Coupling(name = 'UVGC_323_357',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP3x4)/cmath.pi**2 if MTP3 else (complex(0,1)*G**2*KHTPTP3x4)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP3x4)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP3x4*reglog(MTP3/MU_R))/(4.*cmath.pi**2) if MTP3 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP3x4)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP3x4)/(24.*cmath.pi**2)'},
                        order = {'HT3T4':1,'QCD':2})

UVGC_323_358 = Coupling(name = 'UVGC_323_358',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP3x4)/cmath.pi**2 if MTP4 else (complex(0,1)*G**2*KHTPTP3x4)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP3x4)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP3x4*reglog(MTP4/MU_R))/(4.*cmath.pi**2) if MTP4 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP3x4)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP3x4)/(24.*cmath.pi**2)'},
                        order = {'HT3T4':1,'QCD':2})

UVGC_323_359 = Coupling(name = 'UVGC_323_359',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTPTP3x4)/cmath.pi**2'},
                        order = {'HT3T4':1,'QCD':2})

UVGC_324_360 = Coupling(name = 'UVGC_324_360',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP4x1)/cmath.pi**2 if MTP1 else (complex(0,1)*G**2*KHTPTP4x1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP4x1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP4x1*reglog(MTP1/MU_R))/(4.*cmath.pi**2) if MTP1 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP4x1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP4x1)/(24.*cmath.pi**2)'},
                        order = {'HT1T4':1,'QCD':2})

UVGC_324_361 = Coupling(name = 'UVGC_324_361',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP4x1)/cmath.pi**2 if MTP4 else (complex(0,1)*G**2*KHTPTP4x1)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP4x1)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP4x1*reglog(MTP4/MU_R))/(4.*cmath.pi**2) if MTP4 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP4x1)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP4x1)/(24.*cmath.pi**2)'},
                        order = {'HT1T4':1,'QCD':2})

UVGC_324_362 = Coupling(name = 'UVGC_324_362',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTPTP4x1)/cmath.pi**2'},
                        order = {'HT1T4':1,'QCD':2})

UVGC_325_363 = Coupling(name = 'UVGC_325_363',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP4x2)/cmath.pi**2 if MTP2 else (complex(0,1)*G**2*KHTPTP4x2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP4x2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP4x2*reglog(MTP2/MU_R))/(4.*cmath.pi**2) if MTP2 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP4x2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP4x2)/(24.*cmath.pi**2)'},
                        order = {'HT2T4':1,'QCD':2})

UVGC_325_364 = Coupling(name = 'UVGC_325_364',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP4x2)/cmath.pi**2 if MTP4 else (complex(0,1)*G**2*KHTPTP4x2)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP4x2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP4x2*reglog(MTP4/MU_R))/(4.*cmath.pi**2) if MTP4 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP4x2)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP4x2)/(24.*cmath.pi**2)'},
                        order = {'HT2T4':1,'QCD':2})

UVGC_325_365 = Coupling(name = 'UVGC_325_365',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTPTP4x2)/cmath.pi**2'},
                        order = {'HT2T4':1,'QCD':2})

UVGC_326_366 = Coupling(name = 'UVGC_326_366',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP4x3)/cmath.pi**2 if MTP3 else (complex(0,1)*G**2*KHTPTP4x3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP4x3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP4x3*reglog(MTP3/MU_R))/(4.*cmath.pi**2) if MTP3 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP4x3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP4x3)/(24.*cmath.pi**2)'},
                        order = {'HT3T4':1,'QCD':2})

UVGC_326_367 = Coupling(name = 'UVGC_326_367',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTPTP4x3)/cmath.pi**2 if MTP4 else (complex(0,1)*G**2*KHTPTP4x3)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTPTP4x3)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP4x3*reglog(MTP4/MU_R))/(4.*cmath.pi**2) if MTP4 else -0.041666666666666664*(complex(0,1)*G**2*KHTPTP4x3)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP4x3)/(24.*cmath.pi**2)'},
                        order = {'HT3T4':1,'QCD':2})

UVGC_326_368 = Coupling(name = 'UVGC_326_368',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTPTP4x3)/cmath.pi**2'},
                        order = {'HT3T4':1,'QCD':2})

UVGC_327_369 = Coupling(name = 'UVGC_327_369',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2*KHTPTP4x4)/cmath.pi**2 if MTP4 else (complex(0,1)*G**2*KHTPTP4x4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*KHTPTP4x4)/(3.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*KHTPTP4x4)/(12.*cmath.pi**2) + (complex(0,1)*G**2*KHTPTP4x4*reglog(MTP4/MU_R))/(2.*cmath.pi**2) if MTP4 else -0.08333333333333333*(complex(0,1)*G**2*KHTPTP4x4)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTPTP4x4)/(12.*cmath.pi**2)'},
                        order = {'HT4T4':1,'QCD':2})

UVGC_328_370 = Coupling(name = 'UVGC_328_370',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSML4)/cmath.pi**2 if MT else (complex(0,1)*G**2*KHTSML4)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSML4)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSML4*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else -0.041666666666666664*(complex(0,1)*G**2*KHTSML4)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSML4)/(24.*cmath.pi**2)'},
                        order = {'HT4T':1,'QCD':2})

UVGC_328_371 = Coupling(name = 'UVGC_328_371',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSML4)/cmath.pi**2 if MTP4 else (complex(0,1)*G**2*KHTSML4)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSML4)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSML4*reglog(MTP4/MU_R))/(4.*cmath.pi**2) if MTP4 else -0.041666666666666664*(complex(0,1)*G**2*KHTSML4)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSML4)/(24.*cmath.pi**2)'},
                        order = {'HT4T':1,'QCD':2})

UVGC_328_372 = Coupling(name = 'UVGC_328_372',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTSML4)/cmath.pi**2'},
                        order = {'HT4T':1,'QCD':2})

UVGC_329_373 = Coupling(name = 'UVGC_329_373',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSMR4)/cmath.pi**2 if MT else (complex(0,1)*G**2*KHTSMR4)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSMR4)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSMR4*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else -0.041666666666666664*(complex(0,1)*G**2*KHTSMR4)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSMR4)/(24.*cmath.pi**2)'},
                        order = {'HT4T':1,'QCD':2})

UVGC_329_374 = Coupling(name = 'UVGC_329_374',
                        value = {-1:'( -0.08333333333333333*(complex(0,1)*G**2*KHTSMR4)/cmath.pi**2 if MTP4 else (complex(0,1)*G**2*KHTSMR4)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*KHTSMR4)/(24.*cmath.pi**2) + (complex(0,1)*G**2*KHTSMR4*reglog(MTP4/MU_R))/(4.*cmath.pi**2) if MTP4 else -0.041666666666666664*(complex(0,1)*G**2*KHTSMR4)/cmath.pi**2 ) + (complex(0,1)*G**2*KHTSMR4)/(24.*cmath.pi**2)'},
                        order = {'HT4T':1,'QCD':2})

UVGC_329_375 = Coupling(name = 'UVGC_329_375',
                        value = {-1:'-0.3333333333333333*(complex(0,1)*G**2*KHTSMR4)/cmath.pi**2'},
                        order = {'HT4T':1,'QCD':2})

UVGC_330_376 = Coupling(name = 'UVGC_330_376',
                        value = {-1:'( (complex(0,1)*G**2*MTP4)/(6.*cmath.pi**2) if MTP4 else -0.08333333333333333*(complex(0,1)*G**2*MTP4)/cmath.pi**2 ) + (complex(0,1)*G**2*MTP4)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MTP4)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MTP4*reglog(MTP4/MU_R))/cmath.pi**2 if MTP4 else (complex(0,1)*G**2*MTP4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MTP4)/(12.*cmath.pi**2)'},
                        order = {'QCD':2})











# LP debug: couplings modified to correctly separate contributions, NLOct does not do it automatically

UVGC_2000_2001 = Coupling(name = 'UVGC_2000_2001',
                        value = {-1:'( (complex(0,1)*G**2*KHTT)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else -0.08333333333333333*(complex(0,1)*G**2*KHTT)/(cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*KHTT)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (5*complex(0,1)*G**2*KHTT)/(12.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*KHTT*reglog(MT/MU_R))/(2.*cmath.pi**2*cmath.sqrt(2)) if MT else (complex(0,1)*G**2*KHTT)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*KHTT)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                        order = {'HTTMOD':1,'QCD':2})

UVGC_2000_2002 = Coupling(name = 'UVGC_2000_2002',
                        value = {-1:'( (complex(0,1)*G**2*yt)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else - (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (3*complex(0,1)*G**2*yt)/(4.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yt*reglog(MT/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MT else (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                        order = {'QED':1,'QCD':2})

UVGC_2000_2003 = Coupling(name = 'UVGC_2000_2003',
                        value = {-1:'( (complex(0,1)*G**2*KHBB)/(6.*cmath.pi**2*cmath.sqrt(2)) if MB else -0.08333333333333333*(complex(0,1)*G**2*KHBB)/(cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*KHBB)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (5*complex(0,1)*G**2*KHBB)/(12.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*KHBB*reglog(MB/MU_R))/(2.*cmath.pi**2*cmath.sqrt(2)) if MB else (complex(0,1)*G**2*KHBB)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*KHBB)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                        order = {'HBBMOD':1,'QCD':2})

UVGC_2000_2004 = Coupling(name = 'UVGC_2000_2004',
                        value = {-1:'( (complex(0,1)*G**2*yb)/(6.*cmath.pi**2*cmath.sqrt(2)) if MB else - (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (3*complex(0,1)*G**2*yb)/(4.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yb*reglog(MB/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MB else (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                        order = {'QED':1,'QCD':2})
