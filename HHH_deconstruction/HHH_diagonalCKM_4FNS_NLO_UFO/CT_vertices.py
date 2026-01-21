# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 12.3.1 for Linux x86 (64-bit) (June 24, 2021)
# Date: Thu 9 Oct 2025 08:59:38


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_213_313,(0,0,1):C.R2GC_214_314})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               loop_particles = [ [ [P.g, P.t] ],[ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_201_301,(0,0,1):C.R2GC_202_302})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV3 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_100_1,(0,0,1):C.R2GC_100_2})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV15, L.VVVV7, L.VVVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,2,0):C.R2GC_71_46,(2,2,1):C.R2GC_102_6,(0,2,0):C.R2GC_71_46,(0,2,1):C.R2GC_102_6,(4,2,0):C.R2GC_69_43,(4,2,1):C.R2GC_69_44,(3,2,0):C.R2GC_69_43,(3,2,1):C.R2GC_69_44,(8,2,0):C.R2GC_103_7,(8,2,1):C.R2GC_70_45,(6,2,0):C.R2GC_105_11,(6,2,1):C.R2GC_105_12,(7,2,0):C.R2GC_104_9,(7,2,1):C.R2GC_104_10,(5,2,0):C.R2GC_69_43,(5,2,1):C.R2GC_69_44,(1,2,0):C.R2GC_69_43,(1,2,1):C.R2GC_69_44,(11,1,0):C.R2GC_73_48,(11,1,1):C.R2GC_73_49,(10,1,0):C.R2GC_73_48,(10,1,1):C.R2GC_73_49,(9,1,1):C.R2GC_72_47,(2,3,0):C.R2GC_71_46,(2,3,1):C.R2GC_102_6,(0,3,0):C.R2GC_71_46,(0,3,1):C.R2GC_102_6,(4,3,0):C.R2GC_69_43,(4,3,1):C.R2GC_69_44,(3,3,0):C.R2GC_69_43,(3,3,1):C.R2GC_69_44,(8,3,0):C.R2GC_103_7,(8,3,1):C.R2GC_106_13,(6,3,0):C.R2GC_101_3,(6,3,1):C.R2GC_101_4,(7,3,0):C.R2GC_104_9,(7,3,1):C.R2GC_75_51,(5,3,0):C.R2GC_69_43,(5,3,1):C.R2GC_69_44,(1,3,0):C.R2GC_69_43,(1,3,1):C.R2GC_69_44,(0,0,0):C.R2GC_71_46,(0,0,1):C.R2GC_102_6,(2,0,0):C.R2GC_71_46,(2,0,1):C.R2GC_102_6,(5,0,0):C.R2GC_69_43,(5,0,1):C.R2GC_69_44,(1,0,0):C.R2GC_69_43,(1,0,1):C.R2GC_69_44,(7,0,0):C.R2GC_102_5,(7,0,1):C.R2GC_102_6,(4,0,0):C.R2GC_69_43,(4,0,1):C.R2GC_69_44,(3,0,0):C.R2GC_69_43,(3,0,1):C.R2GC_69_44,(8,0,0):C.R2GC_103_7,(8,0,1):C.R2GC_103_8,(6,0,0):C.R2GC_105_11,(6,0,1):C.R2GC_74_50})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_34_21})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_34_21})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_34_21})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_76_52})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4 ],
               loop_particles = [ [ [P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_76_52})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_76_52})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_77_53})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_77_53})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_77_53})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_77_53})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_77_53})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_77_53})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_111_16})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_111_16})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_111_16})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_111_16})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_111_16})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_111_16})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV11, L.FFV5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,1,0):C.R2GC_112_17,(0,0,0):C.R2GC_113_18})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV11, L.FFV5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,1,0):C.R2GC_112_17,(0,0,0):C.R2GC_113_18})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV11, L.FFV5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,1,0):C.R2GC_112_17,(0,0,0):C.R2GC_113_18})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV7 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_38_22,(0,1,0):C.R2GC_113_18})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV7 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_38_22,(0,1,0):C.R2GC_113_18})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV7 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_38_22,(0,1,0):C.R2GC_113_18})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_107_14})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_107_14})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_110_15,(0,1,0):C.R2GC_107_14})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_107_14})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_107_14})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_95_54,(0,1,0):C.R2GC_107_14})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV2, L.VV3, L.VV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,2,2):C.R2GC_32_20,(0,0,0):C.R2GC_47_23,(0,0,3):C.R2GC_47_24,(0,1,1):C.R2GC_50_29})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS2 ],
                loop_particles = [ [ [P.b] ], [ [P.b] ], [ [P.t] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_203_303,(0,0,1):C.R2GC_204_304,(0,0,2):C.R2GC_205_305,(0,0,3):C.R2GC_206_306})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV15 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_57_42})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV15 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_53_34,(0,0,1):C.R2GC_53_35})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV15 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_56_40,(0,0,1):C.R2GC_56_41})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV15 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_51_30,(0,0,1):C.R2GC_51_31})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV15, L.VVVV6 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,1,0):C.R2GC_55_38,(1,1,1):C.R2GC_55_39,(0,0,0):C.R2GC_54_36,(0,0,1):C.R2GC_54_37})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV15 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_52_32,(0,0,1):C.R2GC_52_33})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS2 ],
                loop_particles = [ [ [P.b] ], [ [P.b] ], [ [P.b] ], [ [P.t] ], [ [P.t] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_207_307,(0,0,1):C.R2GC_208_308,(0,0,2):C.R2GC_209_309,(0,0,3):C.R2GC_210_310,(0,0,4):C.R2GC_211_311,(0,0,5):C.R2GC_212_312})

V_44 = CTVertex(name = 'V_44',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ],[ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_217_317,(0,0,1):C.UVGC_218_318})

V_45 = CTVertex(name = 'V_45',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t] ],[ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_215_315,(0,0,1):C.UVGC_216_316})

V_46 = CTVertex(name = 'V_46',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV2, L.VVV3, L.VVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,1,0):C.UVGC_100_1,(0,1,1):C.UVGC_100_2,(0,1,4):C.UVGC_100_3,(0,2,2):C.UVGC_58_42,(0,0,3):C.UVGC_59_43})

V_47 = CTVertex(name = 'V_47',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV10, L.VVVV15, L.VVVV7, L.VVVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,2,3):C.UVGC_70_52,(2,2,4):C.UVGC_70_51,(0,2,3):C.UVGC_70_52,(0,2,4):C.UVGC_70_51,(4,2,3):C.UVGC_69_49,(4,2,4):C.UVGC_69_50,(3,2,3):C.UVGC_69_49,(3,2,4):C.UVGC_69_50,(8,2,3):C.UVGC_70_51,(8,2,4):C.UVGC_70_52,(6,2,0):C.UVGC_104_15,(6,2,2):C.UVGC_104_16,(6,2,3):C.UVGC_105_20,(6,2,4):C.UVGC_105_21,(6,2,5):C.UVGC_104_19,(7,2,0):C.UVGC_104_15,(7,2,2):C.UVGC_104_16,(7,2,3):C.UVGC_104_17,(7,2,4):C.UVGC_104_18,(7,2,5):C.UVGC_104_19,(5,2,3):C.UVGC_69_49,(5,2,4):C.UVGC_69_50,(1,2,3):C.UVGC_69_49,(1,2,4):C.UVGC_69_50,(11,1,3):C.UVGC_73_55,(11,1,4):C.UVGC_73_56,(10,1,3):C.UVGC_73_55,(10,1,4):C.UVGC_73_56,(9,1,3):C.UVGC_72_53,(9,1,4):C.UVGC_72_54,(2,3,3):C.UVGC_70_52,(2,3,4):C.UVGC_70_51,(0,3,3):C.UVGC_70_52,(0,3,4):C.UVGC_70_51,(4,3,3):C.UVGC_69_49,(4,3,4):C.UVGC_69_50,(3,3,3):C.UVGC_69_49,(3,3,4):C.UVGC_69_50,(8,3,0):C.UVGC_106_22,(8,3,2):C.UVGC_106_23,(8,3,3):C.UVGC_106_24,(8,3,4):C.UVGC_106_25,(8,3,5):C.UVGC_106_26,(6,3,0):C.UVGC_101_4,(6,3,3):C.UVGC_101_5,(6,3,4):C.UVGC_101_6,(6,3,5):C.UVGC_101_7,(7,3,1):C.UVGC_74_57,(7,3,3):C.UVGC_75_59,(7,3,4):C.UVGC_75_60,(5,3,3):C.UVGC_69_49,(5,3,4):C.UVGC_69_50,(1,3,3):C.UVGC_69_49,(1,3,4):C.UVGC_69_50,(0,0,3):C.UVGC_70_52,(0,0,4):C.UVGC_70_51,(2,0,3):C.UVGC_70_52,(2,0,4):C.UVGC_70_51,(5,0,3):C.UVGC_69_49,(5,0,4):C.UVGC_69_50,(1,0,3):C.UVGC_69_49,(1,0,4):C.UVGC_69_50,(7,0,0):C.UVGC_101_4,(7,0,3):C.UVGC_102_8,(7,0,4):C.UVGC_102_9,(7,0,5):C.UVGC_101_7,(4,0,3):C.UVGC_69_49,(4,0,4):C.UVGC_69_50,(3,0,3):C.UVGC_69_49,(3,0,4):C.UVGC_69_50,(8,0,0):C.UVGC_103_10,(8,0,2):C.UVGC_103_11,(8,0,3):C.UVGC_103_12,(8,0,4):C.UVGC_103_13,(8,0,5):C.UVGC_103_14,(6,0,1):C.UVGC_74_57,(6,0,3):C.UVGC_74_58,(6,0,4):C.UVGC_72_53})

V_48 = CTVertex(name = 'V_48',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV8 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_61_45})

V_49 = CTVertex(name = 'V_49',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV8 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_61_45})

V_50 = CTVertex(name = 'V_50',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4, L.FFV9 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_61_45,(0,1,0):C.UVGC_108_28})

V_51 = CTVertex(name = 'V_51',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_76_61,(0,1,0):C.UVGC_63_46,(0,2,0):C.UVGC_63_46})

V_52 = CTVertex(name = 'V_52',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_76_61,(0,1,0):C.UVGC_63_46,(0,2,0):C.UVGC_63_46})

V_53 = CTVertex(name = 'V_53',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_76_61,(0,1,0):C.UVGC_93_66,(0,2,0):C.UVGC_93_66})

V_54 = CTVertex(name = 'V_54',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_77_62,(0,1,0):C.UVGC_109_29,(0,1,1):C.UVGC_109_30,(0,1,2):C.UVGC_109_31,(0,1,3):C.UVGC_109_32,(0,1,5):C.UVGC_109_33,(0,1,4):C.UVGC_78_63,(0,2,0):C.UVGC_109_29,(0,2,1):C.UVGC_109_30,(0,2,2):C.UVGC_109_31,(0,2,3):C.UVGC_109_32,(0,2,5):C.UVGC_109_33,(0,2,4):C.UVGC_78_63})

V_55 = CTVertex(name = 'V_55',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_77_62,(0,1,0):C.UVGC_109_29,(0,1,1):C.UVGC_109_30,(0,1,3):C.UVGC_109_31,(0,1,4):C.UVGC_109_32,(0,1,5):C.UVGC_109_33,(0,1,2):C.UVGC_78_63,(0,2,0):C.UVGC_109_29,(0,2,1):C.UVGC_109_30,(0,2,3):C.UVGC_109_31,(0,2,4):C.UVGC_109_32,(0,2,5):C.UVGC_109_33,(0,2,2):C.UVGC_78_63})

V_56 = CTVertex(name = 'V_56',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_77_62,(0,1,0):C.UVGC_109_29,(0,1,1):C.UVGC_109_30,(0,1,2):C.UVGC_109_31,(0,1,3):C.UVGC_109_32,(0,1,5):C.UVGC_109_33,(0,1,4):C.UVGC_109_34,(0,2,0):C.UVGC_109_29,(0,2,1):C.UVGC_109_30,(0,2,2):C.UVGC_109_31,(0,2,3):C.UVGC_109_32,(0,2,5):C.UVGC_109_33,(0,2,4):C.UVGC_109_34})

V_57 = CTVertex(name = 'V_57',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_77_62,(0,1,0):C.UVGC_109_29,(0,1,1):C.UVGC_109_30,(0,1,3):C.UVGC_109_31,(0,1,4):C.UVGC_109_32,(0,1,5):C.UVGC_109_33,(0,1,2):C.UVGC_78_63,(0,2,0):C.UVGC_109_29,(0,2,1):C.UVGC_109_30,(0,2,3):C.UVGC_109_31,(0,2,4):C.UVGC_109_32,(0,2,5):C.UVGC_109_33,(0,2,2):C.UVGC_78_63})

V_58 = CTVertex(name = 'V_58',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_77_62,(0,1,0):C.UVGC_109_29,(0,1,1):C.UVGC_109_30,(0,1,2):C.UVGC_109_31,(0,1,3):C.UVGC_109_32,(0,1,5):C.UVGC_109_33,(0,1,4):C.UVGC_78_63,(0,2,0):C.UVGC_109_29,(0,2,1):C.UVGC_109_30,(0,2,2):C.UVGC_109_31,(0,2,3):C.UVGC_109_32,(0,2,5):C.UVGC_109_33,(0,2,4):C.UVGC_78_63})

V_59 = CTVertex(name = 'V_59',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_77_62,(0,1,0):C.UVGC_109_29,(0,1,2):C.UVGC_109_30,(0,1,3):C.UVGC_109_31,(0,1,4):C.UVGC_109_32,(0,1,5):C.UVGC_109_33,(0,1,1):C.UVGC_94_67,(0,2,0):C.UVGC_109_29,(0,2,2):C.UVGC_109_30,(0,2,3):C.UVGC_109_31,(0,2,4):C.UVGC_109_32,(0,2,5):C.UVGC_109_33,(0,2,1):C.UVGC_94_67})

V_60 = CTVertex(name = 'V_60',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_90_64,(0,0,1):C.UVGC_111_38})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_90_64,(0,0,1):C.UVGC_111_38})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_111_36,(0,0,2):C.UVGC_111_37,(0,0,1):C.UVGC_111_38})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_90_64,(0,0,1):C.UVGC_111_38})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_90_64,(0,0,1):C.UVGC_111_38})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_111_36,(0,0,2):C.UVGC_111_37,(0,0,1):C.UVGC_111_38})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV11, L.FFV5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,1,0):C.UVGC_112_39,(0,0,0):C.UVGC_113_40})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV7 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_96_69,(0,1,0):C.UVGC_97_70})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_60_44})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_60_44})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_110_35,(0,1,0):C.UVGC_107_27})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_60_44})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_60_44})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_95_68,(0,1,0):C.UVGC_92_65})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV5 ],
                loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,1,0):C.UVGC_99_72,(0,1,3):C.UVGC_99_73,(0,0,1):C.UVGC_68_47,(0,0,2):C.UVGC_68_48})

