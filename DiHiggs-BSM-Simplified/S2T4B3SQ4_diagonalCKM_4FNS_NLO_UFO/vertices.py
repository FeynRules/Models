# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 13.2.0 for Linux x86 (64-bit) (December 7, 2022)
# Date: Thu 13 Apr 2023 07:48:10


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS2 ],
             couplings = {(0,0):C.GC_73})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS2 ],
             couplings = {(0,0):C.GC_88})

V_3 = Vertex(name = 'V_3',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS2 ],
             couplings = {(0,0):C.GC_100})

V_4 = Vertex(name = 'V_4',
             particles = [ P.H, P.H, P.s01 ],
             color = [ '1' ],
             lorentz = [ L.SSS2 ],
             couplings = {(0,0):C.GC_89})

V_5 = Vertex(name = 'V_5',
             particles = [ P.H, P.H, P.s02 ],
             color = [ '1' ],
             lorentz = [ L.SSS2 ],
             couplings = {(0,0):C.GC_90})

V_6 = Vertex(name = 'V_6',
             particles = [ P.b__tilde__, P.b, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS5, L.FFS8 ],
             couplings = {(0,0):C.GC_10,(0,1):C.GC_109})

V_7 = Vertex(name = 'V_7',
             particles = [ P.b__tilde__, P.b, P.s01 ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS5 ],
             couplings = {(0,0):C.GC_63})

V_8 = Vertex(name = 'V_8',
             particles = [ P.b__tilde__, P.b, P.s02 ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS5 ],
             couplings = {(0,0):C.GC_69})

V_9 = Vertex(name = 'V_9',
             particles = [ P.bp1__tilde__, P.bp1, P.s01 ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS5 ],
             couplings = {(0,0):C.GC_61})

V_10 = Vertex(name = 'V_10',
              particles = [ P.bp1__tilde__, P.bp1, P.s02 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_67})

V_11 = Vertex(name = 'V_11',
              particles = [ P.bp2__tilde__, P.bp2, P.s01 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_62})

V_12 = Vertex(name = 'V_12',
              particles = [ P.bp2__tilde__, P.bp2, P.s02 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_68})

V_13 = Vertex(name = 'V_13',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5, L.FFS8 ],
              couplings = {(0,0):C.GC_60,(0,1):C.GC_110})

V_14 = Vertex(name = 'V_14',
              particles = [ P.t__tilde__, P.t, P.s01 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_66})

V_15 = Vertex(name = 'V_15',
              particles = [ P.t__tilde__, P.t, P.s02 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_72})

V_16 = Vertex(name = 'V_16',
              particles = [ P.tp1__tilde__, P.tp1, P.s01 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_64})

V_17 = Vertex(name = 'V_17',
              particles = [ P.tp1__tilde__, P.tp1, P.s02 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_70})

V_18 = Vertex(name = 'V_18',
              particles = [ P.tp2__tilde__, P.tp2, P.s01 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_65})

V_19 = Vertex(name = 'V_19',
              particles = [ P.tp2__tilde__, P.tp2, P.s02 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_71})

V_20 = Vertex(name = 'V_20',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV2 ],
              couplings = {(0,0):C.GC_6})

V_21 = Vertex(name = 'V_21',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV3 ],
              couplings = {(0,0):C.GC_6})

V_22 = Vertex(name = 'V_22',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV12, L.VVVV13, L.VVVV9 ],
              couplings = {(1,0):C.GC_9,(0,2):C.GC_9,(2,1):C.GC_9})

V_23 = Vertex(name = 'V_23',
              particles = [ P.bp1__tilde__, P.bp1, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_1})

V_24 = Vertex(name = 'V_24',
              particles = [ P.bp2__tilde__, P.bp2, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_1})

V_25 = Vertex(name = 'V_25',
              particles = [ P.bp3__tilde__, P.bp3, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_1})

V_26 = Vertex(name = 'V_26',
              particles = [ P.tp1__tilde__, P.tp1, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_2})

V_27 = Vertex(name = 'V_27',
              particles = [ P.tp2__tilde__, P.tp2, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_2})

V_28 = Vertex(name = 'V_28',
              particles = [ P.tp3__tilde__, P.tp3, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_2})

V_29 = Vertex(name = 'V_29',
              particles = [ P.tp4__tilde__, P.tp4, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV4 ],
              couplings = {(0,0):C.GC_2})

V_30 = Vertex(name = 'V_30',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS8 ],
              couplings = {(0,0):C.GC_111})

V_31 = Vertex(name = 'V_31',
              particles = [ P.bp1__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_23,(0,1):C.GC_20})

V_32 = Vertex(name = 'V_32',
              particles = [ P.bp2__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_24,(0,1):C.GC_21})

V_33 = Vertex(name = 'V_33',
              particles = [ P.bp3__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_25,(0,1):C.GC_22})

V_34 = Vertex(name = 'V_34',
              particles = [ P.tp1__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_56,(0,1):C.GC_52})

V_35 = Vertex(name = 'V_35',
              particles = [ P.tp2__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_57,(0,1):C.GC_53})

V_36 = Vertex(name = 'V_36',
              particles = [ P.tp3__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_58,(0,1):C.GC_54})

V_37 = Vertex(name = 'V_37',
              particles = [ P.tp4__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_59,(0,1):C.GC_55})

V_38 = Vertex(name = 'V_38',
              particles = [ P.bp1__tilde__, P.bp1, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_11,(0,1):C.GC_11})

V_39 = Vertex(name = 'V_39',
              particles = [ P.bp2__tilde__, P.bp1, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_12,(0,1):C.GC_14})

V_40 = Vertex(name = 'V_40',
              particles = [ P.bp3__tilde__, P.bp1, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_13,(0,1):C.GC_17})

V_41 = Vertex(name = 'V_41',
              particles = [ P.bp1__tilde__, P.bp2, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_14,(0,1):C.GC_12})

V_42 = Vertex(name = 'V_42',
              particles = [ P.bp2__tilde__, P.bp2, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_15,(0,1):C.GC_15})

V_43 = Vertex(name = 'V_43',
              particles = [ P.bp3__tilde__, P.bp2, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_16,(0,1):C.GC_18})

V_44 = Vertex(name = 'V_44',
              particles = [ P.bp1__tilde__, P.bp3, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_17,(0,1):C.GC_13})

V_45 = Vertex(name = 'V_45',
              particles = [ P.bp2__tilde__, P.bp3, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_18,(0,1):C.GC_16})

V_46 = Vertex(name = 'V_46',
              particles = [ P.bp3__tilde__, P.bp3, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_19,(0,1):C.GC_19})

V_47 = Vertex(name = 'V_47',
              particles = [ P.b__tilde__, P.bp1, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_20,(0,1):C.GC_23})

V_48 = Vertex(name = 'V_48',
              particles = [ P.b__tilde__, P.bp2, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_21,(0,1):C.GC_24})

V_49 = Vertex(name = 'V_49',
              particles = [ P.b__tilde__, P.bp3, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_22,(0,1):C.GC_25})

V_50 = Vertex(name = 'V_50',
              particles = [ P.tp1__tilde__, P.tp1, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_36,(0,1):C.GC_36})

V_51 = Vertex(name = 'V_51',
              particles = [ P.tp2__tilde__, P.tp1, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_37,(0,1):C.GC_40})

V_52 = Vertex(name = 'V_52',
              particles = [ P.tp3__tilde__, P.tp1, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_38,(0,1):C.GC_44})

V_53 = Vertex(name = 'V_53',
              particles = [ P.tp4__tilde__, P.tp1, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_39,(0,1):C.GC_48})

V_54 = Vertex(name = 'V_54',
              particles = [ P.tp1__tilde__, P.tp2, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_40,(0,1):C.GC_37})

V_55 = Vertex(name = 'V_55',
              particles = [ P.tp2__tilde__, P.tp2, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_41,(0,1):C.GC_41})

V_56 = Vertex(name = 'V_56',
              particles = [ P.tp3__tilde__, P.tp2, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_42,(0,1):C.GC_45})

V_57 = Vertex(name = 'V_57',
              particles = [ P.tp4__tilde__, P.tp2, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_43,(0,1):C.GC_49})

V_58 = Vertex(name = 'V_58',
              particles = [ P.tp1__tilde__, P.tp3, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_44,(0,1):C.GC_38})

V_59 = Vertex(name = 'V_59',
              particles = [ P.tp2__tilde__, P.tp3, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_45,(0,1):C.GC_42})

V_60 = Vertex(name = 'V_60',
              particles = [ P.tp3__tilde__, P.tp3, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_46,(0,1):C.GC_46})

V_61 = Vertex(name = 'V_61',
              particles = [ P.tp4__tilde__, P.tp3, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_47,(0,1):C.GC_50})

V_62 = Vertex(name = 'V_62',
              particles = [ P.tp1__tilde__, P.tp4, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_48,(0,1):C.GC_39})

V_63 = Vertex(name = 'V_63',
              particles = [ P.tp2__tilde__, P.tp4, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_49,(0,1):C.GC_43})

V_64 = Vertex(name = 'V_64',
              particles = [ P.tp3__tilde__, P.tp4, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_50,(0,1):C.GC_47})

V_65 = Vertex(name = 'V_65',
              particles = [ P.tp4__tilde__, P.tp4, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_51,(0,1):C.GC_51})

V_66 = Vertex(name = 'V_66',
              particles = [ P.t__tilde__, P.tp1, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_52,(0,1):C.GC_56})

V_67 = Vertex(name = 'V_67',
              particles = [ P.t__tilde__, P.tp2, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_53,(0,1):C.GC_57})

V_68 = Vertex(name = 'V_68',
              particles = [ P.t__tilde__, P.tp3, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_54,(0,1):C.GC_58})

V_69 = Vertex(name = 'V_69',
              particles = [ P.t__tilde__, P.tp4, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6, L.FFS7 ],
              couplings = {(0,0):C.GC_55,(0,1):C.GC_59})

V_70 = Vertex(name = 'V_70',
              particles = [ P.s01, P.sq1__tilde__, P.sq1 ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_95})

V_71 = Vertex(name = 'V_71',
              particles = [ P.s02, P.sq1__tilde__, P.sq1 ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_98})

V_72 = Vertex(name = 'V_72',
              particles = [ P.s01, P.sq2__tilde__, P.sq2 ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_96})

V_73 = Vertex(name = 'V_73',
              particles = [ P.s02, P.sq2__tilde__, P.sq2 ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_99})

V_74 = Vertex(name = 'V_74',
              particles = [ P.s01, P.sq3__tilde__, P.sq3 ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_97})

V_75 = Vertex(name = 'V_75',
              particles = [ P.H, P.H, P.sq1__tilde__, P.sq1 ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_26})

V_76 = Vertex(name = 'V_76',
              particles = [ P.H, P.H, P.sq1__tilde__, P.sq2 ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_27})

V_77 = Vertex(name = 'V_77',
              particles = [ P.H, P.H, P.sq1__tilde__, P.sq3 ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_29})

V_78 = Vertex(name = 'V_78',
              particles = [ P.H, P.H, P.sq1__tilde__, P.sq4 ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_32})

V_79 = Vertex(name = 'V_79',
              particles = [ P.H, P.H, P.sq1, P.sq2__tilde__ ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_27})

V_80 = Vertex(name = 'V_80',
              particles = [ P.H, P.H, P.sq2__tilde__, P.sq2 ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_28})

V_81 = Vertex(name = 'V_81',
              particles = [ P.H, P.H, P.sq2__tilde__, P.sq3 ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_30})

V_82 = Vertex(name = 'V_82',
              particles = [ P.H, P.H, P.sq2__tilde__, P.sq4 ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_33})

V_83 = Vertex(name = 'V_83',
              particles = [ P.H, P.H, P.sq1, P.sq3__tilde__ ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_29})

V_84 = Vertex(name = 'V_84',
              particles = [ P.H, P.H, P.sq2, P.sq3__tilde__ ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_30})

V_85 = Vertex(name = 'V_85',
              particles = [ P.H, P.H, P.sq3__tilde__, P.sq3 ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_31})

V_86 = Vertex(name = 'V_86',
              particles = [ P.H, P.H, P.sq3__tilde__, P.sq4 ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_34})

V_87 = Vertex(name = 'V_87',
              particles = [ P.H, P.H, P.sq1, P.sq4__tilde__ ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_32})

V_88 = Vertex(name = 'V_88',
              particles = [ P.H, P.H, P.sq2, P.sq4__tilde__ ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_33})

V_89 = Vertex(name = 'V_89',
              particles = [ P.H, P.H, P.sq3, P.sq4__tilde__ ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_34})

V_90 = Vertex(name = 'V_90',
              particles = [ P.H, P.H, P.sq4__tilde__, P.sq4 ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.SSSS2 ],
              couplings = {(0,0):C.GC_35})

V_91 = Vertex(name = 'V_91',
              particles = [ P.H, P.sq1__tilde__, P.sq1 ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_91})

V_92 = Vertex(name = 'V_92',
              particles = [ P.H, P.sq1__tilde__, P.sq2 ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_102})

V_93 = Vertex(name = 'V_93',
              particles = [ P.H, P.sq1__tilde__, P.sq3 ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_103})

V_94 = Vertex(name = 'V_94',
              particles = [ P.H, P.sq1__tilde__, P.sq4 ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_105})

V_95 = Vertex(name = 'V_95',
              particles = [ P.H, P.sq1, P.sq2__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_102})

V_96 = Vertex(name = 'V_96',
              particles = [ P.H, P.sq2__tilde__, P.sq2 ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_92})

V_97 = Vertex(name = 'V_97',
              particles = [ P.H, P.sq2__tilde__, P.sq3 ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_104})

V_98 = Vertex(name = 'V_98',
              particles = [ P.H, P.sq2__tilde__, P.sq4 ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_106})

V_99 = Vertex(name = 'V_99',
              particles = [ P.H, P.sq1, P.sq3__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_103})

V_100 = Vertex(name = 'V_100',
               particles = [ P.H, P.sq2, P.sq3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS2 ],
               couplings = {(0,0):C.GC_104})

V_101 = Vertex(name = 'V_101',
               particles = [ P.H, P.sq3__tilde__, P.sq3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS2 ],
               couplings = {(0,0):C.GC_93})

V_102 = Vertex(name = 'V_102',
               particles = [ P.H, P.sq3__tilde__, P.sq4 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS2 ],
               couplings = {(0,0):C.GC_107})

V_103 = Vertex(name = 'V_103',
               particles = [ P.H, P.sq1, P.sq4__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS2 ],
               couplings = {(0,0):C.GC_105})

V_104 = Vertex(name = 'V_104',
               particles = [ P.H, P.sq2, P.sq4__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS2 ],
               couplings = {(0,0):C.GC_106})

V_105 = Vertex(name = 'V_105',
               particles = [ P.H, P.sq3, P.sq4__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS2 ],
               couplings = {(0,0):C.GC_107})

V_106 = Vertex(name = 'V_106',
               particles = [ P.H, P.sq4__tilde__, P.sq4 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.SSS2 ],
               couplings = {(0,0):C.GC_94})

V_107 = Vertex(name = 'V_107',
               particles = [ P.bp1__tilde__, P.bp1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_8})

V_108 = Vertex(name = 'V_108',
               particles = [ P.bp2__tilde__, P.bp2, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_8})

V_109 = Vertex(name = 'V_109',
               particles = [ P.bp3__tilde__, P.bp3, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_8})

V_110 = Vertex(name = 'V_110',
               particles = [ P.tp1__tilde__, P.tp1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_8})

V_111 = Vertex(name = 'V_111',
               particles = [ P.tp2__tilde__, P.tp2, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_8})

V_112 = Vertex(name = 'V_112',
               particles = [ P.tp3__tilde__, P.tp3, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_8})

V_113 = Vertex(name = 'V_113',
               particles = [ P.tp4__tilde__, P.tp4, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_8})

V_114 = Vertex(name = 'V_114',
               particles = [ P.g, P.sq1__tilde__, P.sq1 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_7})

V_115 = Vertex(name = 'V_115',
               particles = [ P.g, P.sq2__tilde__, P.sq2 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_7})

V_116 = Vertex(name = 'V_116',
               particles = [ P.g, P.sq3__tilde__, P.sq3 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_7})

V_117 = Vertex(name = 'V_117',
               particles = [ P.g, P.sq4__tilde__, P.sq4 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_7})

V_118 = Vertex(name = 'V_118',
               particles = [ P.g, P.g, P.sq1__tilde__, P.sq1 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS2 ],
               couplings = {(1,0):C.GC_9,(0,0):C.GC_9})

V_119 = Vertex(name = 'V_119',
               particles = [ P.g, P.g, P.sq2__tilde__, P.sq2 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS2 ],
               couplings = {(1,0):C.GC_9,(0,0):C.GC_9})

V_120 = Vertex(name = 'V_120',
               particles = [ P.g, P.g, P.sq3__tilde__, P.sq3 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS2 ],
               couplings = {(1,0):C.GC_9,(0,0):C.GC_9})

V_121 = Vertex(name = 'V_121',
               particles = [ P.g, P.g, P.sq4__tilde__, P.sq4 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS2 ],
               couplings = {(1,0):C.GC_9,(0,0):C.GC_9})

V_122 = Vertex(name = 'V_122',
               particles = [ P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV3 ],
               couplings = {(0,0):C.GC_4})

V_123 = Vertex(name = 'V_123',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS2 ],
               couplings = {(0,0):C.GC_74})

V_124 = Vertex(name = 'V_124',
               particles = [ P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS2 ],
               couplings = {(0,0):C.GC_101})

V_125 = Vertex(name = 'V_125',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_5})

V_126 = Vertex(name = 'V_126',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV3 ],
               couplings = {(0,0):C.GC_78})

V_127 = Vertex(name = 'V_127',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_75})

V_128 = Vertex(name = 'V_128',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV14 ],
               couplings = {(0,0):C.GC_79})

V_129 = Vertex(name = 'V_129',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS2 ],
               couplings = {(0,0):C.GC_87})

V_130 = Vertex(name = 'V_130',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS2 ],
               couplings = {(0,0):C.GC_108})

V_131 = Vertex(name = 'V_131',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_76})

V_132 = Vertex(name = 'V_132',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_3})

V_133 = Vertex(name = 'V_133',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_3})

V_134 = Vertex(name = 'V_134',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_3})

V_135 = Vertex(name = 'V_135',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_2})

V_136 = Vertex(name = 'V_136',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_2})

V_137 = Vertex(name = 'V_137',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_2})

V_138 = Vertex(name = 'V_138',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_1})

V_139 = Vertex(name = 'V_139',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_1})

V_140 = Vertex(name = 'V_140',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_1})

V_141 = Vertex(name = 'V_141',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_8})

V_142 = Vertex(name = 'V_142',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_8})

V_143 = Vertex(name = 'V_143',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_8})

V_144 = Vertex(name = 'V_144',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_8})

V_145 = Vertex(name = 'V_145',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_8})

V_146 = Vertex(name = 'V_146',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV4 ],
               couplings = {(0,0):C.GC_8})

V_147 = Vertex(name = 'V_147',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_77})

V_148 = Vertex(name = 'V_148',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_77})

V_149 = Vertex(name = 'V_149',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_77})

V_150 = Vertex(name = 'V_150',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_77})

V_151 = Vertex(name = 'V_151',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_77})

V_152 = Vertex(name = 'V_152',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_77})

V_153 = Vertex(name = 'V_153',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_77})

V_154 = Vertex(name = 'V_154',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_77})

V_155 = Vertex(name = 'V_155',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_77})

V_156 = Vertex(name = 'V_156',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_77})

V_157 = Vertex(name = 'V_157',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_77})

V_158 = Vertex(name = 'V_158',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_77})

V_159 = Vertex(name = 'V_159',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_84,(0,1):C.GC_81})

V_160 = Vertex(name = 'V_160',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_84,(0,1):C.GC_81})

V_161 = Vertex(name = 'V_161',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_84,(0,1):C.GC_81})

V_162 = Vertex(name = 'V_162',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_83,(0,1):C.GC_80})

V_163 = Vertex(name = 'V_163',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_83,(0,1):C.GC_80})

V_164 = Vertex(name = 'V_164',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_83,(0,1):C.GC_80})

V_165 = Vertex(name = 'V_165',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_86})

V_166 = Vertex(name = 'V_166',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_86})

V_167 = Vertex(name = 'V_167',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV5 ],
               couplings = {(0,0):C.GC_86})

V_168 = Vertex(name = 'V_168',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_85,(0,1):C.GC_82})

V_169 = Vertex(name = 'V_169',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_85,(0,1):C.GC_82})

V_170 = Vertex(name = 'V_170',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_85,(0,1):C.GC_82})

