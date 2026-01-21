# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 12.3.1 for Linux x86 (64-bit) (June 24, 2021)
# Date: Thu 9 Oct 2025 08:59:38


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



R2GC_100_1 = Coupling(name = 'R2GC_100_1',
                      value = 'G**3/(24.*cmath.pi**2)',
                      order = {'QCD':3})

R2GC_100_2 = Coupling(name = 'R2GC_100_2',
                      value = '(11*G**3)/(64.*cmath.pi**2)',
                      order = {'QCD':3})

R2GC_101_3 = Coupling(name = 'R2GC_101_3',
                      value = '(5*complex(0,1)*G**4)/(48.*cmath.pi**2)',
                      order = {'QCD':4})

R2GC_101_4 = Coupling(name = 'R2GC_101_4',
                      value = '(19*complex(0,1)*G**4)/(32.*cmath.pi**2)',
                      order = {'QCD':4})

R2GC_102_5 = Coupling(name = 'R2GC_102_5',
                      value = '(23*complex(0,1)*G**4)/(192.*cmath.pi**2)',
                      order = {'QCD':4})

R2GC_102_6 = Coupling(name = 'R2GC_102_6',
                      value = '-0.015625*(complex(0,1)*G**4)/cmath.pi**2',
                      order = {'QCD':4})

R2GC_103_7 = Coupling(name = 'R2GC_103_7',
                      value = '-0.005208333333333333*(complex(0,1)*G**4)/cmath.pi**2',
                      order = {'QCD':4})

R2GC_103_8 = Coupling(name = 'R2GC_103_8',
                      value = '(31*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                      order = {'QCD':4})

R2GC_104_9 = Coupling(name = 'R2GC_104_9',
                      value = '(-3*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                      order = {'QCD':4})

R2GC_104_10 = Coupling(name = 'R2GC_104_10',
                       value = '(-17*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_105_11 = Coupling(name = 'R2GC_105_11',
                       value = '-0.0625*(complex(0,1)*G**4)/cmath.pi**2',
                       order = {'QCD':4})

R2GC_105_12 = Coupling(name = 'R2GC_105_12',
                       value = '(-7*complex(0,1)*G**4)/(32.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_106_13 = Coupling(name = 'R2GC_106_13',
                       value = '(7*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_107_14 = Coupling(name = 'R2GC_107_14',
                       value = '(complex(0,1)*G**2)/(12.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_110_15 = Coupling(name = 'R2GC_110_15',
                       value = '(complex(0,1)*G**2*MT)/(6.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_111_16 = Coupling(name = 'R2GC_111_16',
                       value = '-0.16666666666666666*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_112_17 = Coupling(name = 'R2GC_112_17',
                       value = '-0.08333333333333333*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw)',
                       order = {'QCD':2,'QED':1})

R2GC_113_18 = Coupling(name = 'R2GC_113_18',
                       value = '(ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

# R2GC_114_19 = Coupling(name = 'R2GC_114_19',
#                        value = '(complex(0,1)*G**2*KHTT)/(3.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
#                        order = {'HTTMOD':1,'QCD':2})

R2GC_32_20 = Coupling(name = 'R2GC_32_20',
                      value = '-0.0625*(complex(0,1)*G**2)/cmath.pi**2',
                      order = {'QCD':2})

R2GC_34_21 = Coupling(name = 'R2GC_34_21',
                      value = '-0.1111111111111111*(ee*complex(0,1)*G**2)/cmath.pi**2',
                      order = {'QCD':2,'QED':1})

R2GC_38_22 = Coupling(name = 'R2GC_38_22',
                      value = '(cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw)',
                      order = {'QCD':2,'QED':1})

R2GC_47_23 = Coupling(name = 'R2GC_47_23',
                      value = '-0.125*(complex(0,1)*G**2*MB**2)/cmath.pi**2',
                      order = {'QCD':2})

R2GC_47_24 = Coupling(name = 'R2GC_47_24',
                      value = '-0.125*(complex(0,1)*G**2*MT**2)/cmath.pi**2',
                      order = {'QCD':2})

# R2GC_48_25 = Coupling(name = 'R2GC_48_25',
#                       value = '-0.125*(complex(0,1)*G**2*KHBB*MB)/(cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*MB*yb)/(8.*cmath.pi**2*cmath.sqrt(2))',
#                       order = {'HBBMOD':1,'QCD':2})

# R2GC_48_26 = Coupling(name = 'R2GC_48_26',
#                       value = '-0.125*(complex(0,1)*G**2*KHTT*MT)/(cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*MT*yt)/(8.*cmath.pi**2*cmath.sqrt(2))',
#                       order = {'HTTMOD':1,'QCD':2})

# R2GC_49_27 = Coupling(name = 'R2GC_49_27',
#                       value = '-0.0625*(complex(0,1)*G**2*KHBB**2)/cmath.pi**2 - (complex(0,1)*G**2*KHBB*yb)/(8.*cmath.pi**2) - (complex(0,1)*G**2*yb**2)/(16.*cmath.pi**2)',
#                       order = {'HBBMOD':2,'QCD':2})

# R2GC_49_28 = Coupling(name = 'R2GC_49_28',
#                       value = '-0.0625*(complex(0,1)*G**2*KHTT**2)/cmath.pi**2 - (complex(0,1)*G**2*KHTT*yt)/(8.*cmath.pi**2) - (complex(0,1)*G**2*yt**2)/(16.*cmath.pi**2)',
#                       order = {'HTTMOD':2,'QCD':2})

R2GC_50_29 = Coupling(name = 'R2GC_50_29',
                      value = '(complex(0,1)*G**2)/(48.*cmath.pi**2)',
                      order = {'QCD':2})

R2GC_51_30 = Coupling(name = 'R2GC_51_30',
                      value = '(ee**2*complex(0,1)*G**2)/(216.*cmath.pi**2)',
                      order = {'QCD':2,'QED':2})

R2GC_51_31 = Coupling(name = 'R2GC_51_31',
                      value = '(ee**2*complex(0,1)*G**2)/(54.*cmath.pi**2)',
                      order = {'QCD':2,'QED':2})

R2GC_52_32 = Coupling(name = 'R2GC_52_32',
                      value = '-0.006944444444444444*(ee*complex(0,1)*G**3)/cmath.pi**2',
                      order = {'QCD':3,'QED':1})

R2GC_52_33 = Coupling(name = 'R2GC_52_33',
                      value = '(ee*complex(0,1)*G**3)/(72.*cmath.pi**2)',
                      order = {'QCD':3,'QED':1})

R2GC_53_34 = Coupling(name = 'R2GC_53_34',
                      value = '(cw*ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2*sw) - (ee**2*complex(0,1)*G**2*sw)/(864.*cw*cmath.pi**2)',
                      order = {'QCD':2,'QED':2})

R2GC_53_35 = Coupling(name = 'R2GC_53_35',
                      value = '(cw*ee**2*complex(0,1)*G**2)/(144.*cmath.pi**2*sw) - (5*ee**2*complex(0,1)*G**2*sw)/(432.*cw*cmath.pi**2)',
                      order = {'QCD':2,'QED':2})

R2GC_54_36 = Coupling(name = 'R2GC_54_36',
                      value = '-0.005208333333333333*(cw*ee*complex(0,1)*G**3)/(cmath.pi**2*sw) + (ee*complex(0,1)*G**3*sw)/(576.*cw*cmath.pi**2)',
                      order = {'QCD':3,'QED':1})

R2GC_54_37 = Coupling(name = 'R2GC_54_37',
                      value = '(cw*ee*complex(0,1)*G**3)/(192.*cmath.pi**2*sw) - (5*ee*complex(0,1)*G**3*sw)/(576.*cw*cmath.pi**2)',
                      order = {'QCD':3,'QED':1})

R2GC_55_38 = Coupling(name = 'R2GC_55_38',
                      value = '(-3*cw*ee*complex(0,1)*G**3)/(64.*cmath.pi**2*sw) - (3*ee*complex(0,1)*G**3*sw)/(64.*cw*cmath.pi**2)',
                      order = {'QCD':3,'QED':1})

R2GC_55_39 = Coupling(name = 'R2GC_55_39',
                      value = '(3*cw*ee*complex(0,1)*G**3)/(64.*cmath.pi**2*sw) + (3*ee*complex(0,1)*G**3*sw)/(64.*cw*cmath.pi**2)',
                      order = {'QCD':3,'QED':1})

R2GC_56_40 = Coupling(name = 'R2GC_56_40',
                      value = '(ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2) + (cw**2*ee**2*complex(0,1)*G**2)/(192.*cmath.pi**2*sw**2) + (5*ee**2*complex(0,1)*G**2*sw**2)/(1728.*cw**2*cmath.pi**2)',
                      order = {'QCD':2,'QED':2})

R2GC_56_41 = Coupling(name = 'R2GC_56_41',
                      value = '-0.003472222222222222*(ee**2*complex(0,1)*G**2)/cmath.pi**2 + (cw**2*ee**2*complex(0,1)*G**2)/(192.*cmath.pi**2*sw**2) + (17*ee**2*complex(0,1)*G**2*sw**2)/(1728.*cw**2*cmath.pi**2)',
                      order = {'QCD':2,'QED':2})

R2GC_57_42 = Coupling(name = 'R2GC_57_42',
                      value = '(ee**2*complex(0,1)*G**2)/(96.*cmath.pi**2*sw**2)',
                      order = {'QCD':2,'QED':2})

R2GC_69_43 = Coupling(name = 'R2GC_69_43',
                      value = '-0.005208333333333333*G**4/cmath.pi**2',
                      order = {'QCD':4})

R2GC_69_44 = Coupling(name = 'R2GC_69_44',
                      value = 'G**4/(64.*cmath.pi**2)',
                      order = {'QCD':4})

R2GC_70_45 = Coupling(name = 'R2GC_70_45',
                      value = '(complex(0,1)*G**4)/(64.*cmath.pi**2)',
                      order = {'QCD':4})

R2GC_71_46 = Coupling(name = 'R2GC_71_46',
                      value = '(complex(0,1)*G**4)/(192.*cmath.pi**2)',
                      order = {'QCD':4})

R2GC_72_47 = Coupling(name = 'R2GC_72_47',
                      value = '-0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2',
                      order = {'QCD':4})

R2GC_73_48 = Coupling(name = 'R2GC_73_48',
                      value = '(complex(0,1)*G**4)/(288.*cmath.pi**2)',
                      order = {'QCD':4})

R2GC_73_49 = Coupling(name = 'R2GC_73_49',
                      value = '-0.03125*(complex(0,1)*G**4)/cmath.pi**2',
                      order = {'QCD':4})

R2GC_74_50 = Coupling(name = 'R2GC_74_50',
                      value = '(complex(0,1)*G**4)/(4.*cmath.pi**2)',
                      order = {'QCD':4})

R2GC_75_51 = Coupling(name = 'R2GC_75_51',
                      value = '(-23*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                      order = {'QCD':4})

R2GC_76_52 = Coupling(name = 'R2GC_76_52',
                      value = '(ee*complex(0,1)*G**2)/(18.*cmath.pi**2)',
                      order = {'QCD':2,'QED':1})

R2GC_77_53 = Coupling(name = 'R2GC_77_53',
                      value = '-0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2',
                      order = {'QCD':3})

R2GC_95_54 = Coupling(name = 'R2GC_95_54',
                      value = '(complex(0,1)*G**2*MB)/(6.*cmath.pi**2)',
                      order = {'QCD':2})

# R2GC_98_55 = Coupling(name = 'R2GC_98_55',
#                       value = '(complex(0,1)*G**2*KHBB)/(3.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',
#                       order = {'HBBMOD':1,'QCD':2})



R2GC_201_301 = Coupling(name = 'R2GC_201_301',
                       value = '(complex(0,1)*G**2*KHTT)/(3.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'HTTMOD':1,'QCD':2})
R2GC_202_302 = Coupling(name = 'R2GC_202_302',
                       value = '(complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QED':1,'QCD':2})

R2GC_203_303 = Coupling(name = 'R2GC_203_303',
                      value = '-0.125*(complex(0,1)*G**2*KHBB*MB)/(cmath.pi**2*cmath.sqrt(2))',
                      order = {'HBBMOD':1,'QCD':2})
R2GC_204_304 = Coupling(name = 'R2GC_204_304',
                      value = '- (complex(0,1)*G**2*MB*yb)/(8.*cmath.pi**2*cmath.sqrt(2))',
                      order = {'QED':1,'QCD':2})

R2GC_205_305 = Coupling(name = 'R2GC_205_305',
                      value = '-0.125*(complex(0,1)*G**2*KHTT*MT)/(cmath.pi**2*cmath.sqrt(2))',
                      order = {'HTTMOD':1,'QCD':2})
R2GC_206_306 = Coupling(name = 'R2GC_206_306',
                      value = '- (complex(0,1)*G**2*MT*yt)/(8.*cmath.pi**2*cmath.sqrt(2))',
                      order = {'QED':1,'QCD':2})

R2GC_207_307 = Coupling(name = 'R2GC_207_307',
                      value = '-0.0625*(complex(0,1)*G**2*KHBB**2)/cmath.pi**2',
                      order = {'HBBMOD':2,'QCD':2})
R2GC_208_308 = Coupling(name = 'R2GC_208_308',
                      value = '- (complex(0,1)*G**2*yb**2)/(16.*cmath.pi**2)',
                      order = {'QED':2,'QCD':2})
R2GC_209_309 = Coupling(name = 'R2GC_209_309',
                      value = '- (complex(0,1)*G**2*KHBB*yb)/(8.*cmath.pi**2)',
                      order = {'HBBMOD':1,'QED':1,'QCD':2})

R2GC_210_310 = Coupling(name = 'R2GC_210_310',
                      value = '-0.0625*(complex(0,1)*G**2*KHTT**2)/cmath.pi**2',
                      order = {'HTTMOD':2,'QCD':2})
R2GC_211_311 = Coupling(name = 'R2GC_211_311',
                      value = '- (complex(0,1)*G**2*yt**2)/(16.*cmath.pi**2)',
                      order = {'QED':2,'QCD':2})
R2GC_212_312 = Coupling(name = 'R2GC_212_312',
                      value = '- (complex(0,1)*G**2*KHTT*yt)/(8.*cmath.pi**2)',
                      order = {'HTTMOD':1,'QED':1,'QCD':2})

R2GC_213_313 = Coupling(name = 'R2GC_213_313',
                      value = '(complex(0,1)*G**2*KHBB)/(3.*cmath.pi**2*cmath.sqrt(2))',
                      order = {'HBBMOD':1,'QCD':2})
R2GC_214_314 = Coupling(name = 'R2GC_214_314',
                      value = '(complex(0,1)*G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',
                      order = {'QED':1,'QCD':2})






















UVGC_100_1 = Coupling(name = 'UVGC_100_1',
                      value = {-1:'( 0 if MB else -0.0625*G**3/cmath.pi**2 ) + G**3/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(G**3*reglog(MB/MU_R))/cmath.pi**2 if MB else 0 )'},
                      order = {'QCD':3})

UVGC_100_2 = Coupling(name = 'UVGC_100_2',
                      value = {-1:'-0.020833333333333332*G**3/cmath.pi**2'},
                      order = {'QCD':3})

UVGC_100_3 = Coupling(name = 'UVGC_100_3',
                      value = {-1:'( 0 if MT else -0.0625*G**3/cmath.pi**2 ) + G**3/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(G**3*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                      order = {'QCD':3})

UVGC_101_4 = Coupling(name = 'UVGC_101_4',
                      value = {-1:'( 0 if MB else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MB/MU_R))/cmath.pi**2 if MB else 0 )'},
                      order = {'QCD':4})

UVGC_101_5 = Coupling(name = 'UVGC_101_5',
                      value = {-1:'(147*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_101_6 = Coupling(name = 'UVGC_101_6',
                      value = {-1:'(3*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_101_7 = Coupling(name = 'UVGC_101_7',
                      value = {-1:'( 0 if MT else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                      order = {'QCD':4})

UVGC_102_8 = Coupling(name = 'UVGC_102_8',
                      value = {-1:'(147*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_102_9 = Coupling(name = 'UVGC_102_9',
                      value = {-1:'(21*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_103_10 = Coupling(name = 'UVGC_103_10',
                       value = {-1:'( 0 if MB else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 )',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MB/MU_R))/cmath.pi**2 if MB else 0 )'},
                       order = {'QCD':4})

UVGC_103_11 = Coupling(name = 'UVGC_103_11',
                       value = {-1:'-0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2'},
                       order = {'QCD':4})

UVGC_103_12 = Coupling(name = 'UVGC_103_12',
                       value = {-1:'(523*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_103_13 = Coupling(name = 'UVGC_103_13',
                       value = {-1:'(13*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_103_14 = Coupling(name = 'UVGC_103_14',
                       value = {-1:'( 0 if MT else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 )',0:'( -0.08333333333333333*(complex(0,1)*G**4*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                       order = {'QCD':4})

UVGC_104_15 = Coupling(name = 'UVGC_104_15',
                       value = {-1:'( 0 if MB else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MB/MU_R))/(12.*cmath.pi**2) if MB else 0 )'},
                       order = {'QCD':4})

UVGC_104_16 = Coupling(name = 'UVGC_104_16',
                       value = {-1:'(complex(0,1)*G**4)/(24.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_104_17 = Coupling(name = 'UVGC_104_17',
                       value = {-1:'(-341*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_104_18 = Coupling(name = 'UVGC_104_18',
                       value = {-1:'(-11*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_104_19 = Coupling(name = 'UVGC_104_19',
                       value = {-1:'( 0 if MT else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                       order = {'QCD':4})

UVGC_105_20 = Coupling(name = 'UVGC_105_20',
                       value = {-1:'(-83*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_105_21 = Coupling(name = 'UVGC_105_21',
                       value = {-1:'(-5*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_106_22 = Coupling(name = 'UVGC_106_22',
                       value = {-1:'( 0 if MB else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MB/MU_R))/(12.*cmath.pi**2) if MB else 0 )'},
                       order = {'QCD':4})

UVGC_106_23 = Coupling(name = 'UVGC_106_23',
                       value = {-1:'(complex(0,1)*G**4)/(12.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_106_24 = Coupling(name = 'UVGC_106_24',
                       value = {-1:'(-85*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_106_25 = Coupling(name = 'UVGC_106_25',
                       value = {-1:'(-19*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_106_26 = Coupling(name = 'UVGC_106_26',
                       value = {-1:'( 0 if MT else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                       order = {'QCD':4})

UVGC_107_27 = Coupling(name = 'UVGC_107_27',
                       value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MT/MU_R))/(2.*cmath.pi**2) if MT else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_108_28 = Coupling(name = 'UVGC_108_28',
                       value = {-1:'( -0.1111111111111111*(ee*complex(0,1)*G**2)/cmath.pi**2 if MT else (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) )',0:'( (-5*ee*complex(0,1)*G**2)/(18.*cmath.pi**2) + (ee*complex(0,1)*G**2*reglog(MT/MU_R))/(3.*cmath.pi**2) if MT else -0.05555555555555555*(ee*complex(0,1)*G**2)/cmath.pi**2 ) + (ee*complex(0,1)*G**2)/(18.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_109_29 = Coupling(name = 'UVGC_109_29',
                       value = {-1:'( 0 if MB else (complex(0,1)*G**3)/(48.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_109_30 = Coupling(name = 'UVGC_109_30',
                       value = {-1:'(complex(0,1)*G**3)/(48.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_109_31 = Coupling(name = 'UVGC_109_31',
                       value = {-1:'(-19*complex(0,1)*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_109_32 = Coupling(name = 'UVGC_109_32',
                       value = {-1:'-0.0078125*(complex(0,1)*G**3)/cmath.pi**2'},
                       order = {'QCD':3})

UVGC_109_33 = Coupling(name = 'UVGC_109_33',
                       value = {-1:'( 0 if MT else (complex(0,1)*G**3)/(48.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_109_34 = Coupling(name = 'UVGC_109_34',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2 if MT else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MT/MU_R))/(2.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_110_35 = Coupling(name = 'UVGC_110_35',
                       value = {-1:'( (complex(0,1)*G**2*MT)/(6.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**2*MT)/cmath.pi**2 ) + (complex(0,1)*G**2*MT)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MT)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MT*reglog(MT/MU_R))/cmath.pi**2 if MT else (complex(0,1)*G**2*MT)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MT)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_111_36 = Coupling(name = 'UVGC_111_36',
                       value = {-1:'( -0.08333333333333333*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2)) if MB else (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) )',0:'( (-5*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*G**2*reglog(MB/MU_R))/(4.*cmath.pi**2*sw*cmath.sqrt(2)) if MB else -0.041666666666666664*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2)) ) + (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_111_37 = Coupling(name = 'UVGC_111_37',
                       value = {-1:'( -0.08333333333333333*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2)) if MT else (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) )',0:'( (-5*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*G**2*reglog(MT/MU_R))/(4.*cmath.pi**2*sw*cmath.sqrt(2)) if MT else -0.041666666666666664*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2)) ) + (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_111_38 = Coupling(name = 'UVGC_111_38',
                       value = {-1:'-0.08333333333333333*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_112_39 = Coupling(name = 'UVGC_112_39',
                       value = {-1:'( -0.08333333333333333*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw) if MT else (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) ) - (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw)',0:'( (-5*cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (cw*ee*complex(0,1)*G**2*reglog(MT/MU_R))/(4.*cmath.pi**2*sw) if MT else -0.041666666666666664*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw) ) + (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw)'},
                       order = {'QCD':2,'QED':1})

UVGC_113_40 = Coupling(name = 'UVGC_113_40',
                       value = {-1:'( (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2) if MT else -0.013888888888888888*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) ) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)',0:'( (5*ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) - (ee*complex(0,1)*G**2*sw*reglog(MT/MU_R))/(12.*cw*cmath.pi**2) if MT else (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

# UVGC_114_41 = Coupling(name = 'UVGC_114_41',
#                        value = {-1:'( (complex(0,1)*G**2*KHTT)/(6.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yt)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else -0.08333333333333333*(complex(0,1)*G**2*KHTT)/(cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*KHTT)/(3.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (5*complex(0,1)*G**2*KHTT)/(12.*cmath.pi**2*cmath.sqrt(2)) + (3*complex(0,1)*G**2*yt)/(4.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*KHTT*reglog(MT/MU_R))/(2.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yt*reglog(MT/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MT else (complex(0,1)*G**2*KHTT)/(12.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*KHTT)/(12.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2))'},
#                        order = {'HTTMOD':1,'QCD':2})

UVGC_58_42 = Coupling(name = 'UVGC_58_42',
                      value = {-1:'(51*G**3)/(128.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_59_43 = Coupling(name = 'UVGC_59_43',
                      value = {-1:'G**3/(128.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_60_44 = Coupling(name = 'UVGC_60_44',
                      value = {-1:'-0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2'},
                      order = {'QCD':2})

UVGC_61_45 = Coupling(name = 'UVGC_61_45',
                      value = {-1:'-0.05555555555555555*(ee*complex(0,1)*G**2)/cmath.pi**2'},
                      order = {'QCD':2,'QED':1})

UVGC_63_46 = Coupling(name = 'UVGC_63_46',
                      value = {-1:'-0.027777777777777776*(ee*complex(0,1)*G**2)/cmath.pi**2'},
                      order = {'QCD':2,'QED':1})

UVGC_68_47 = Coupling(name = 'UVGC_68_47',
                      value = {-1:'(3*complex(0,1)*G**2)/(64.*cmath.pi**2)'},
                      order = {'QCD':2})

UVGC_68_48 = Coupling(name = 'UVGC_68_48',
                      value = {-1:'(-3*complex(0,1)*G**2)/(64.*cmath.pi**2)'},
                      order = {'QCD':2})

UVGC_69_49 = Coupling(name = 'UVGC_69_49',
                      value = {-1:'(3*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_69_50 = Coupling(name = 'UVGC_69_50',
                      value = {-1:'(-3*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_70_51 = Coupling(name = 'UVGC_70_51',
                      value = {-1:'(3*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_70_52 = Coupling(name = 'UVGC_70_52',
                      value = {-1:'(-3*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_72_53 = Coupling(name = 'UVGC_72_53',
                      value = {-1:'-0.0078125*(complex(0,1)*G**4)/cmath.pi**2'},
                      order = {'QCD':4})

UVGC_72_54 = Coupling(name = 'UVGC_72_54',
                      value = {-1:'(complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_73_55 = Coupling(name = 'UVGC_73_55',
                      value = {-1:'(-3*complex(0,1)*G**4)/(256.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_73_56 = Coupling(name = 'UVGC_73_56',
                      value = {-1:'(3*complex(0,1)*G**4)/(256.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_74_57 = Coupling(name = 'UVGC_74_57',
                      value = {-1:'-0.041666666666666664*(complex(0,1)*G**4)/cmath.pi**2'},
                      order = {'QCD':4})

UVGC_74_58 = Coupling(name = 'UVGC_74_58',
                      value = {-1:'(47*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_75_59 = Coupling(name = 'UVGC_75_59',
                      value = {-1:'(-253*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_75_60 = Coupling(name = 'UVGC_75_60',
                      value = {-1:'(5*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_76_61 = Coupling(name = 'UVGC_76_61',
                      value = {-1:'(ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                      order = {'QCD':2,'QED':1})

UVGC_77_62 = Coupling(name = 'UVGC_77_62',
                      value = {-1:'(-13*complex(0,1)*G**3)/(48.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_78_63 = Coupling(name = 'UVGC_78_63',
                      value = {-1:'(complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_90_64 = Coupling(name = 'UVGC_90_64',
                      value = {-1:'(ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                      order = {'QCD':2,'QED':1})

UVGC_92_65 = Coupling(name = 'UVGC_92_65',
                      value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MB else -0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MB/MU_R))/(2.*cmath.pi**2) if MB else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                      order = {'QCD':2})

UVGC_93_66 = Coupling(name = 'UVGC_93_66',
                      value = {-1:'( (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) if MB else -0.027777777777777776*(ee*complex(0,1)*G**2)/cmath.pi**2 )',0:'( (5*ee*complex(0,1)*G**2)/(36.*cmath.pi**2) - (ee*complex(0,1)*G**2*reglog(MB/MU_R))/(6.*cmath.pi**2) if MB else (ee*complex(0,1)*G**2)/(36.*cmath.pi**2) ) - (ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                      order = {'QCD':2,'QED':1})

UVGC_94_67 = Coupling(name = 'UVGC_94_67',
                      value = {-1:'( -0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2 if MB else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MB/MU_R))/(2.*cmath.pi**2) if MB else -0.08333333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_95_68 = Coupling(name = 'UVGC_95_68',
                      value = {-1:'( (complex(0,1)*G**2*MB)/(6.*cmath.pi**2) if MB else -0.08333333333333333*(complex(0,1)*G**2*MB)/cmath.pi**2 ) + (complex(0,1)*G**2*MB)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MB)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MB*reglog(MB/MU_R))/cmath.pi**2 if MB else (complex(0,1)*G**2*MB)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MB)/(12.*cmath.pi**2)'},
                      order = {'QCD':2})

UVGC_96_69 = Coupling(name = 'UVGC_96_69',
                      value = {-1:'( (cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw) if MB else -0.041666666666666664*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw) ) + (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw)',0:'( (5*cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) - (cw*ee*complex(0,1)*G**2*reglog(MB/MU_R))/(4.*cmath.pi**2*sw) if MB else (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) ) - (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw)'},
                      order = {'QCD':2,'QED':1})

UVGC_97_70 = Coupling(name = 'UVGC_97_70',
                      value = {-1:'( (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2) if MB else -0.013888888888888888*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) ) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)',0:'( (5*ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) - (ee*complex(0,1)*G**2*sw*reglog(MB/MU_R))/(12.*cw*cmath.pi**2) if MB else (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)'},
                      order = {'QCD':2,'QED':1})

# UVGC_98_71 = Coupling(name = 'UVGC_98_71',
#                       value = {-1:'( (complex(0,1)*G**2*KHBB)/(6.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yb)/(6.*cmath.pi**2*cmath.sqrt(2)) if MB else -0.08333333333333333*(complex(0,1)*G**2*KHBB)/(cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*KHBB)/(3.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (5*complex(0,1)*G**2*KHBB)/(12.*cmath.pi**2*cmath.sqrt(2)) + (3*complex(0,1)*G**2*yb)/(4.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*KHBB*reglog(MB/MU_R))/(2.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yb*reglog(MB/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MB else (complex(0,1)*G**2*KHBB)/(12.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*KHBB)/(12.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2))'},
#                       order = {'HBBMOD':1,'QCD':2})


UVGC_99_72 = Coupling(name = 'UVGC_99_72',
                      value = {-1:'( 0 if MB else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MB/MU_R))/(12.*cmath.pi**2) if MB else 0 )'},
                      order = {'QCD':2})

UVGC_99_73 = Coupling(name = 'UVGC_99_73',
                      value = {-1:'( 0 if MT else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                      order = {'QCD':2})




UVGC_215_315 = Coupling(name = 'UVGC_215_315',
                       value = {-1:'( (complex(0,1)*G**2*KHTT)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else -0.08333333333333333*(complex(0,1)*G**2*KHTT)/(cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*KHTT)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (5*complex(0,1)*G**2*KHTT)/(12.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*KHTT*reglog(MT/MU_R))/(2.*cmath.pi**2*cmath.sqrt(2)) if MT else (complex(0,1)*G**2*KHTT)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*KHTT)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'HTTMOD':1,'QCD':2})
UVGC_216_316 = Coupling(name = 'UVGC_216_316',
                       value = {-1:'( (complex(0,1)*G**2*yt)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else - (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (3*complex(0,1)*G**2*yt)/(4.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yt*reglog(MT/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MT else (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'QED':1,'QCD':2})

UVGC_217_317 = Coupling(name = 'UVGC_217_317',
                      value = {-1:'( (complex(0,1)*G**2*KHBB)/(6.*cmath.pi**2*cmath.sqrt(2)) if MB else -0.08333333333333333*(complex(0,1)*G**2*KHBB)/(cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*KHBB)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (5*complex(0,1)*G**2*KHBB)/(12.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*KHBB*reglog(MB/MU_R))/(2.*cmath.pi**2*cmath.sqrt(2)) if MB else (complex(0,1)*G**2*KHBB)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*KHBB)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                      order = {'HBBMOD':1,'QCD':2})
UVGC_218_318 = Coupling(name = 'UVGC_218_318',
                      value = {-1:'( (complex(0,1)*G**2*yb)/(6.*cmath.pi**2*cmath.sqrt(2)) if MB else - (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (3*complex(0,1)*G**2*yb)/(4.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yb*reglog(MB/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MB else (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                      order = {'QED':1,'QCD':2})
