# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 27, 2023)
# Date: Thu 24 Sep 2026 04:59:33


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV8, L.VVV9 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_228_48,(0,0,1):C.R2GC_230_51,(0,1,0):C.R2GC_231_52,(0,1,1):C.R2GC_231_53,(0,3,0):C.R2GC_231_52,(0,3,1):C.R2GC_233_55,(0,5,0):C.R2GC_228_48,(0,5,1):C.R2GC_229_50,(0,6,0):C.R2GC_228_48,(0,6,1):C.R2GC_228_49,(0,7,0):C.R2GC_231_52,(0,7,1):C.R2GC_232_54,(0,2,1):C.R2GC_201_32,(0,4,1):C.R2GC_200_31})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_204_37,(2,0,1):C.R2GC_204_38,(0,0,0):C.R2GC_204_37,(0,0,1):C.R2GC_204_38,(4,0,0):C.R2GC_202_33,(4,0,1):C.R2GC_202_34,(3,0,0):C.R2GC_202_33,(3,0,1):C.R2GC_202_34,(8,0,0):C.R2GC_203_35,(8,0,1):C.R2GC_203_36,(6,0,0):C.R2GC_208_42,(6,0,1):C.R2GC_238_61,(7,0,0):C.R2GC_209_43,(7,0,1):C.R2GC_237_60,(5,0,0):C.R2GC_202_33,(5,0,1):C.R2GC_202_34,(1,0,0):C.R2GC_202_33,(1,0,1):C.R2GC_202_34,(11,0,0):C.R2GC_206_40,(11,0,1):C.R2GC_206_41,(10,0,0):C.R2GC_206_40,(10,0,1):C.R2GC_206_41,(9,0,1):C.R2GC_205_39,(0,1,0):C.R2GC_204_37,(0,1,1):C.R2GC_204_38,(2,1,0):C.R2GC_204_37,(2,1,1):C.R2GC_204_38,(5,1,0):C.R2GC_202_33,(5,1,1):C.R2GC_202_34,(1,1,0):C.R2GC_202_33,(1,1,1):C.R2GC_202_34,(7,1,0):C.R2GC_209_43,(7,1,1):C.R2GC_203_36,(4,1,0):C.R2GC_202_33,(4,1,1):C.R2GC_202_34,(3,1,0):C.R2GC_202_33,(3,1,1):C.R2GC_202_34,(8,1,0):C.R2GC_203_35,(8,1,1):C.R2GC_237_60,(6,1,0):C.R2GC_234_56,(6,1,1):C.R2GC_234_57,(11,1,0):C.R2GC_206_40,(11,1,1):C.R2GC_206_41,(10,1,0):C.R2GC_206_40,(10,1,1):C.R2GC_206_41,(9,1,1):C.R2GC_205_39,(0,2,0):C.R2GC_204_37,(0,2,1):C.R2GC_204_38,(2,2,0):C.R2GC_204_37,(2,2,1):C.R2GC_204_38,(5,2,0):C.R2GC_202_33,(5,2,1):C.R2GC_202_34,(1,2,0):C.R2GC_202_33,(1,2,1):C.R2GC_202_34,(7,2,0):C.R2GC_235_58,(7,2,1):C.R2GC_235_59,(4,2,0):C.R2GC_202_33,(4,2,1):C.R2GC_202_34,(3,2,0):C.R2GC_202_33,(3,2,1):C.R2GC_202_34,(8,2,0):C.R2GC_203_35,(8,2,1):C.R2GC_235_59,(6,2,0):C.R2GC_208_42,(11,2,0):C.R2GC_206_40,(11,2,1):C.R2GC_206_41,(10,2,0):C.R2GC_206_40,(10,2,1):C.R2GC_206_41,(9,2,1):C.R2GC_205_39})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_248_64,(0,1,0):C.R2GC_249_65})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_226_47})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_225_46})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_250_66,(0,1,0):C.R2GC_247_63})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_251_67})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_252_68})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_157_2})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_157_2})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_157_2})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_160_5})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_160_5})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_160_5})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_158_3})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_158_3})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_158_3})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_158_3})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_158_3})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_158_3})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_217_44})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_217_44})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_217_44})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_217_44})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_217_44})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_217_44})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_180_27,(0,1,0):C.R2GC_159_4})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_180_27,(0,1,0):C.R2GC_159_4})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_180_27,(0,1,0):C.R2GC_159_4})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_181_28,(0,1,0):C.R2GC_162_6})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_181_28,(0,1,0):C.R2GC_162_6})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_181_28,(0,1,0):C.R2GC_162_6})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_163_7})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_163_7})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_243_62,(0,2,0):C.R2GC_243_62,(0,1,0):C.R2GC_163_7,(0,3,0):C.R2GC_163_7})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_163_7})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_163_7})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF5, L.FF7 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_222_45,(0,1,0):C.R2GC_163_7})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV2, L.VV3, L.VV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,2,2):C.R2GC_156_1,(0,0,0):C.R2GC_170_8,(0,0,3):C.R2GC_170_9,(0,1,1):C.R2GC_173_14})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_171_10,(0,0,1):C.R2GC_171_11})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_184_30})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_176_19,(0,0,1):C.R2GC_176_20})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_179_25,(0,0,1):C.R2GC_179_26})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_174_15,(0,0,1):C.R2GC_174_16})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_178_23,(1,0,1):C.R2GC_178_24,(0,1,0):C.R2GC_177_21,(0,1,1):C.R2GC_177_22})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_175_17,(0,0,1):C.R2GC_175_18})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_172_12,(0,0,1):C.R2GC_172_13})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_172_12,(0,0,1):C.R2GC_172_13})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_183_29})

V_50 = CTVertex(name = 'V_50',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8, L.VVV9 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_228_40,(0,0,1):C.UVGC_228_41,(0,0,2):C.UVGC_230_46,(0,0,3):C.UVGC_230_47,(0,0,4):C.UVGC_228_43,(0,1,0):C.UVGC_231_48,(0,1,1):C.UVGC_231_49,(0,1,2):C.UVGC_231_50,(0,1,4):C.UVGC_231_51,(0,3,0):C.UVGC_231_48,(0,3,1):C.UVGC_231_49,(0,3,2):C.UVGC_233_54,(0,3,3):C.UVGC_233_55,(0,3,4):C.UVGC_231_51,(0,5,0):C.UVGC_228_40,(0,5,1):C.UVGC_228_41,(0,5,2):C.UVGC_229_44,(0,5,3):C.UVGC_229_45,(0,5,4):C.UVGC_228_43,(0,7,0):C.UVGC_228_40,(0,7,1):C.UVGC_228_41,(0,7,2):C.UVGC_228_42,(0,7,3):C.UVGC_201_11,(0,7,4):C.UVGC_228_43,(0,8,0):C.UVGC_231_48,(0,8,1):C.UVGC_231_49,(0,8,2):C.UVGC_232_52,(0,8,3):C.UVGC_232_53,(0,8,4):C.UVGC_231_51,(0,2,2):C.UVGC_201_10,(0,2,3):C.UVGC_201_11,(0,4,2):C.UVGC_200_8,(0,4,3):C.UVGC_200_9,(0,6,2):C.UVGC_186_1})

V_51 = CTVertex(name = 'V_51',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,3):C.UVGC_203_15,(2,0,4):C.UVGC_203_14,(0,0,3):C.UVGC_203_15,(0,0,4):C.UVGC_203_14,(4,0,3):C.UVGC_202_12,(4,0,4):C.UVGC_202_13,(3,0,3):C.UVGC_202_12,(3,0,4):C.UVGC_202_13,(8,0,3):C.UVGC_203_14,(8,0,4):C.UVGC_203_15,(6,0,0):C.UVGC_237_66,(6,0,2):C.UVGC_237_67,(6,0,3):C.UVGC_238_71,(6,0,4):C.UVGC_238_72,(6,0,5):C.UVGC_237_70,(7,0,0):C.UVGC_237_66,(7,0,2):C.UVGC_237_67,(7,0,3):C.UVGC_237_68,(7,0,4):C.UVGC_237_69,(7,0,5):C.UVGC_237_70,(5,0,3):C.UVGC_202_12,(5,0,4):C.UVGC_202_13,(1,0,3):C.UVGC_202_12,(1,0,4):C.UVGC_202_13,(11,0,3):C.UVGC_206_18,(11,0,4):C.UVGC_206_19,(10,0,3):C.UVGC_206_18,(10,0,4):C.UVGC_206_19,(9,0,3):C.UVGC_205_16,(9,0,4):C.UVGC_205_17,(0,1,3):C.UVGC_203_15,(0,1,4):C.UVGC_203_14,(2,1,3):C.UVGC_203_15,(2,1,4):C.UVGC_203_14,(5,1,3):C.UVGC_202_12,(5,1,4):C.UVGC_202_13,(1,1,3):C.UVGC_202_12,(1,1,4):C.UVGC_202_13,(7,1,1):C.UVGC_208_25,(7,1,3):C.UVGC_203_14,(7,1,4):C.UVGC_209_26,(4,1,3):C.UVGC_202_12,(4,1,4):C.UVGC_202_13,(3,1,3):C.UVGC_202_12,(3,1,4):C.UVGC_202_13,(8,1,0):C.UVGC_239_73,(8,1,2):C.UVGC_239_74,(8,1,3):C.UVGC_237_68,(8,1,4):C.UVGC_239_75,(8,1,5):C.UVGC_239_76,(6,1,0):C.UVGC_234_56,(6,1,3):C.UVGC_234_57,(6,1,4):C.UVGC_234_58,(6,1,5):C.UVGC_234_59,(11,1,3):C.UVGC_206_18,(11,1,4):C.UVGC_206_19,(10,1,3):C.UVGC_206_18,(10,1,4):C.UVGC_206_19,(9,1,3):C.UVGC_205_16,(9,1,4):C.UVGC_205_17,(0,2,3):C.UVGC_203_15,(0,2,4):C.UVGC_203_14,(2,2,3):C.UVGC_203_15,(2,2,4):C.UVGC_203_14,(5,2,3):C.UVGC_202_12,(5,2,4):C.UVGC_202_13,(1,2,3):C.UVGC_202_12,(1,2,4):C.UVGC_202_13,(7,2,0):C.UVGC_234_56,(7,2,3):C.UVGC_235_60,(7,2,4):C.UVGC_235_61,(7,2,5):C.UVGC_234_59,(4,2,3):C.UVGC_202_12,(4,2,4):C.UVGC_202_13,(3,2,3):C.UVGC_202_12,(3,2,4):C.UVGC_202_13,(8,2,0):C.UVGC_236_62,(8,2,2):C.UVGC_236_63,(8,2,3):C.UVGC_235_60,(8,2,4):C.UVGC_236_64,(8,2,5):C.UVGC_236_65,(6,2,1):C.UVGC_208_25,(6,2,4):C.UVGC_205_16,(11,2,3):C.UVGC_206_18,(11,2,4):C.UVGC_206_19,(10,2,3):C.UVGC_206_18,(10,2,4):C.UVGC_206_19,(9,2,3):C.UVGC_205_16,(9,2,4):C.UVGC_205_17})

V_52 = CTVertex(name = 'V_52',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_248_88,(0,0,2):C.UVGC_248_89,(0,0,1):C.UVGC_248_90,(0,1,0):C.UVGC_249_91,(0,1,2):C.UVGC_249_92,(0,1,1):C.UVGC_249_93})

V_53 = CTVertex(name = 'V_53',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_226_37})

V_54 = CTVertex(name = 'V_54',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_225_36})

V_55 = CTVertex(name = 'V_55',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_250_94,(0,0,2):C.UVGC_250_95,(0,0,1):C.UVGC_250_96,(0,1,0):C.UVGC_247_85,(0,1,2):C.UVGC_247_86,(0,1,1):C.UVGC_247_87})

V_56 = CTVertex(name = 'V_56',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_251_97})

V_57 = CTVertex(name = 'V_57',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_252_98})

V_58 = CTVertex(name = 'V_58',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_188_3})

V_59 = CTVertex(name = 'V_59',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_188_3,(0,1,0):C.UVGC_241_78})

V_60 = CTVertex(name = 'V_60',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_188_3})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV6 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_191_5,(0,1,0):C.UVGC_220_31})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_191_5})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_191_5})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_189_4,(0,1,0):C.UVGC_207_20,(0,1,1):C.UVGC_207_21,(0,1,3):C.UVGC_207_22,(0,1,4):C.UVGC_207_23,(0,1,5):C.UVGC_207_24})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_189_4,(0,1,0):C.UVGC_207_20,(0,1,1):C.UVGC_207_21,(0,1,2):C.UVGC_207_22,(0,1,3):C.UVGC_207_23,(0,1,5):C.UVGC_207_24,(0,1,4):C.UVGC_242_79})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_189_4,(0,1,0):C.UVGC_207_20,(0,1,1):C.UVGC_207_21,(0,1,2):C.UVGC_207_22,(0,1,3):C.UVGC_207_23,(0,1,5):C.UVGC_207_24})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_189_4,(0,1,0):C.UVGC_207_20,(0,1,2):C.UVGC_207_21,(0,1,3):C.UVGC_207_22,(0,1,4):C.UVGC_207_23,(0,1,5):C.UVGC_207_24,(0,1,1):C.UVGC_221_32})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_189_4,(0,1,0):C.UVGC_207_20,(0,1,1):C.UVGC_207_21,(0,1,3):C.UVGC_207_22,(0,1,4):C.UVGC_207_23,(0,1,5):C.UVGC_207_24})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_189_4,(0,1,0):C.UVGC_207_20,(0,1,1):C.UVGC_207_21,(0,1,2):C.UVGC_207_22,(0,1,3):C.UVGC_207_23,(0,1,5):C.UVGC_207_24})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_217_28,(0,0,1):C.UVGC_217_29})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_244_81,(0,0,2):C.UVGC_244_82,(0,0,1):C.UVGC_217_29})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_217_28,(0,0,1):C.UVGC_217_29})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_244_81,(0,0,2):C.UVGC_244_82,(0,0,1):C.UVGC_217_29})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_217_28,(0,0,1):C.UVGC_217_29})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_217_28,(0,0,1):C.UVGC_217_29})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_245_83,(0,1,0):C.UVGC_246_84})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_223_34,(0,1,0):C.UVGC_224_35})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF6 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_212_27,(0,1,0):C.UVGC_187_2,(0,2,0):C.UVGC_187_2})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF6 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_212_27,(0,1,0):C.UVGC_187_2,(0,2,0):C.UVGC_187_2})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_243_80,(0,2,0):C.UVGC_243_80,(0,1,0):C.UVGC_240_77,(0,3,0):C.UVGC_240_77})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF6 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_212_27,(0,1,0):C.UVGC_187_2,(0,2,0):C.UVGC_187_2})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF8 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_187_2})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF5, L.FF7 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_222_33,(0,1,0):C.UVGC_219_30})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV5 ],
                loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,1,0):C.UVGC_227_38,(0,1,3):C.UVGC_227_39,(0,0,1):C.UVGC_199_6,(0,0,2):C.UVGC_199_7})

