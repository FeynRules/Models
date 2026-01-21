# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 13.2.0 for Linux x86 (64-bit) (December 7, 2022)
# Date: Thu 13 Apr 2023 07:48:11


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_1000_1021,(0,0,1):C.R2GC_1000_1022})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.s01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_228_143})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.s02 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_229_144})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.bp1__tilde__, P.bp1, P.s01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.bp1, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_240_150})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.bp1__tilde__, P.bp1, P.s02 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.bp1, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_241_151})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.bp2__tilde__, P.bp2, P.s01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.bp2, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_251_158})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.bp2__tilde__, P.bp2, P.s02 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.bp2, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_252_159})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_1000_1010,(0,0,1):C.R2GC_1000_1011})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.s01 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_272_173})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.s02 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_273_174})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.tp1__tilde__, P.tp1, P.s01 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp1] ] ],
                couplings = {(0,0,0):C.R2GC_285_180})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.tp1__tilde__, P.tp1, P.s02 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp1] ] ],
                couplings = {(0,0,0):C.R2GC_286_181})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.tp2__tilde__, P.tp2, P.s01 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp2] ] ],
                couplings = {(0,0,0):C.R2GC_296_188})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.tp2__tilde__, P.tp2, P.s02 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp2] ] ],
                couplings = {(0,0,0):C.R2GC_297_189})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV3 ],
                loop_particles = [ [ [P.b], [P.bp1], [P.bp2], [P.bp3], [P.c], [P.d], [P.s], [P.t], [P.tp1], [P.tp2], [P.tp3], [P.tp4], [P.u] ], [ [P.g] ] ],
                couplings = {(0,0,0):C.R2GC_311_199,(0,0,1):C.R2GC_311_200})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV10, L.VVVV15, L.VVVV7, L.VVVV8 ],
                loop_particles = [ [ [P.b], [P.bp1], [P.bp2], [P.bp3], [P.c], [P.d], [P.s], [P.t], [P.tp1], [P.tp2], [P.tp3], [P.tp4], [P.u] ], [ [P.g] ] ],
                couplings = {(0,2,0):C.R2GC_157_111,(0,2,1):C.R2GC_157_112,(2,2,0):C.R2GC_157_111,(2,2,1):C.R2GC_157_112,(5,2,0):C.R2GC_155_107,(5,2,1):C.R2GC_155_108,(1,2,0):C.R2GC_155_107,(1,2,1):C.R2GC_155_108,(7,2,0):C.R2GC_162_118,(7,2,1):C.R2GC_315_205,(4,2,0):C.R2GC_155_107,(4,2,1):C.R2GC_155_108,(3,2,0):C.R2GC_155_107,(3,2,1):C.R2GC_155_108,(8,2,0):C.R2GC_156_109,(8,2,1):C.R2GC_156_110,(6,2,0):C.R2GC_161_116,(6,2,1):C.R2GC_316_206,(11,1,0):C.R2GC_159_114,(11,1,1):C.R2GC_159_115,(10,1,0):C.R2GC_159_114,(10,1,1):C.R2GC_159_115,(9,1,1):C.R2GC_158_113,(0,3,0):C.R2GC_157_111,(0,3,1):C.R2GC_157_112,(2,3,0):C.R2GC_157_111,(2,3,1):C.R2GC_157_112,(5,3,0):C.R2GC_155_107,(5,3,1):C.R2GC_155_108,(1,3,0):C.R2GC_155_107,(1,3,1):C.R2GC_155_108,(7,3,0):C.R2GC_162_118,(7,3,1):C.R2GC_162_119,(4,3,0):C.R2GC_155_107,(4,3,1):C.R2GC_155_108,(3,3,0):C.R2GC_155_107,(3,3,1):C.R2GC_155_108,(8,3,0):C.R2GC_156_109,(8,3,1):C.R2GC_317_207,(6,3,0):C.R2GC_313_202,(6,3,1):C.R2GC_313_203,(0,0,0):C.R2GC_157_111,(0,0,1):C.R2GC_157_112,(2,0,0):C.R2GC_157_111,(2,0,1):C.R2GC_157_112,(7,0,0):C.R2GC_312_201,(7,0,1):C.R2GC_157_112,(5,0,0):C.R2GC_155_107,(5,0,1):C.R2GC_155_108,(1,0,0):C.R2GC_155_107,(1,0,1):C.R2GC_155_108,(4,0,0):C.R2GC_155_107,(4,0,1):C.R2GC_155_108,(3,0,0):C.R2GC_155_107,(3,0,1):C.R2GC_155_108,(8,0,0):C.R2GC_156_109,(8,0,1):C.R2GC_314_204,(6,0,0):C.R2GC_161_116,(6,0,1):C.R2GC_161_117})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.bp1__tilde__, P.bp1, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.bp1, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_163_120})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.bp2__tilde__, P.bp2, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.bp2, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_163_120})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.bp3__tilde__, P.bp3, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.bp3, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_163_120})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.tp1__tilde__, P.tp1, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.tp1] ] ],
                couplings = {(0,0,0):C.R2GC_114_3})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.tp2__tilde__, P.tp2, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.tp2] ] ],
                couplings = {(0,0,0):C.R2GC_114_3})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.tp3__tilde__, P.tp3, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.tp3] ] ],
                couplings = {(0,0,0):C.R2GC_114_3})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.tp4__tilde__, P.tp4, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.tp4] ] ],
                couplings = {(0,0,0):C.R2GC_114_3})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.bp1__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.b, P.bp1, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_239_149,(0,1,0):C.R2GC_238_148})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.bp2__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.b, P.bp2, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_250_157,(0,1,0):C.R2GC_249_156})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.bp3__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.b, P.bp3, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_263_167,(0,1,0):C.R2GC_262_166})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.tp1__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.t, P.tp1] ] ],
                couplings = {(0,0,0):C.R2GC_284_179,(0,1,0):C.R2GC_283_178})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.tp2__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.t, P.tp2] ] ],
                couplings = {(0,0,0):C.R2GC_295_187,(0,1,0):C.R2GC_294_186})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.tp3__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.t, P.tp3] ] ],
                couplings = {(0,0,0):C.R2GC_308_197,(0,1,0):C.R2GC_307_196})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.tp4__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.t, P.tp4] ] ],
                couplings = {(0,0,0):C.R2GC_329_216,(0,1,0):C.R2GC_328_215})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.bp1__tilde__, P.bp1, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.bp1, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_237_147})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.bp2__tilde__, P.bp1, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.bp1, P.bp2, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_246_153,(0,1,0):C.R2GC_247_154})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.bp3__tilde__, P.bp1, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.bp1, P.bp3, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_257_161,(0,1,0):C.R2GC_259_163})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.bp1__tilde__, P.bp2, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.bp1, P.bp2, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_247_154,(0,1,0):C.R2GC_246_153})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.bp2__tilde__, P.bp2, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.bp2, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_248_155})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.bp3__tilde__, P.bp2, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.bp2, P.bp3, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_258_162,(0,1,0):C.R2GC_260_164})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.bp1__tilde__, P.bp3, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.bp1, P.bp3, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_259_163,(0,1,0):C.R2GC_257_161})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.bp2__tilde__, P.bp3, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.bp2, P.bp3, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_260_164,(0,1,0):C.R2GC_258_162})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.bp3__tilde__, P.bp3, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.bp3, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_261_165})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp1, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.b, P.bp1, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_238_148,(0,1,0):C.R2GC_239_149})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp2, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.b, P.bp2, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_249_156,(0,1,0):C.R2GC_250_157})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.bp3, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.b, P.bp3, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_262_166,(0,1,0):C.R2GC_263_167})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.tp1__tilde__, P.tp1, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp1] ] ],
                couplings = {(0,0,0):C.R2GC_282_177})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.tp2__tilde__, P.tp1, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.tp1, P.tp2] ] ],
                couplings = {(0,0,0):C.R2GC_291_183,(0,1,0):C.R2GC_292_184})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.tp3__tilde__, P.tp1, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.tp1, P.tp3] ] ],
                couplings = {(0,0,0):C.R2GC_302_191,(0,1,0):C.R2GC_304_193})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.tp4__tilde__, P.tp1, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.tp1, P.tp4] ] ],
                couplings = {(0,0,0):C.R2GC_321_208,(0,1,0):C.R2GC_324_211})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.tp1__tilde__, P.tp2, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.tp1, P.tp2] ] ],
                couplings = {(0,0,0):C.R2GC_292_184,(0,1,0):C.R2GC_291_183})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.tp2__tilde__, P.tp2, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp2] ] ],
                couplings = {(0,0,0):C.R2GC_293_185})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.tp3__tilde__, P.tp2, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.tp2, P.tp3] ] ],
                couplings = {(0,0,0):C.R2GC_303_192,(0,1,0):C.R2GC_305_194})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.tp4__tilde__, P.tp2, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.tp2, P.tp4] ] ],
                couplings = {(0,0,0):C.R2GC_322_209,(0,1,0):C.R2GC_325_212})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.tp1__tilde__, P.tp3, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.tp1, P.tp3] ] ],
                couplings = {(0,0,0):C.R2GC_304_193,(0,1,0):C.R2GC_302_191})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.tp2__tilde__, P.tp3, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.tp2, P.tp3] ] ],
                couplings = {(0,0,0):C.R2GC_305_194,(0,1,0):C.R2GC_303_192})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.tp3__tilde__, P.tp3, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp3] ] ],
                couplings = {(0,0,0):C.R2GC_306_195})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.tp4__tilde__, P.tp3, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.tp3, P.tp4] ] ],
                couplings = {(0,0,0):C.R2GC_323_210,(0,1,0):C.R2GC_326_213})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.tp1__tilde__, P.tp4, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.tp1, P.tp4] ] ],
                couplings = {(0,0,0):C.R2GC_324_211,(0,1,0):C.R2GC_321_208})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.tp2__tilde__, P.tp4, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.tp2, P.tp4] ] ],
                couplings = {(0,0,0):C.R2GC_325_212,(0,1,0):C.R2GC_322_209})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.tp3__tilde__, P.tp4, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.tp3, P.tp4] ] ],
                couplings = {(0,0,0):C.R2GC_326_213,(0,1,0):C.R2GC_323_210})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.tp4__tilde__, P.tp4, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.tp4] ] ],
                couplings = {(0,0,0):C.R2GC_327_214})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp1, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.t, P.tp1] ] ],
                couplings = {(0,0,0):C.R2GC_283_178,(0,1,0):C.R2GC_284_179})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp2, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.t, P.tp2] ] ],
                couplings = {(0,0,0):C.R2GC_294_186,(0,1,0):C.R2GC_295_187})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp3, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.t, P.tp3] ] ],
                couplings = {(0,0,0):C.R2GC_307_196,(0,1,0):C.R2GC_308_197})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.t__tilde__, P.tp4, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS6, L.FFS7 ],
                loop_particles = [ [ [P.g, P.t, P.tp4] ] ],
                couplings = {(0,0,0):C.R2GC_328_215,(0,1,0):C.R2GC_329_216})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.s01, P.sq1__tilde__, P.sq1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq1] ] ],
                couplings = {(0,0,0):C.R2GC_181_128})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.s02, P.sq1__tilde__, P.sq1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq1] ] ],
                couplings = {(0,0,0):C.R2GC_182_129})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.s01, P.sq2__tilde__, P.sq2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq2] ] ],
                couplings = {(0,0,0):C.R2GC_188_131})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.s02, P.sq2__tilde__, P.sq2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq2] ] ],
                couplings = {(0,0,0):C.R2GC_189_132})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.s01, P.sq3__tilde__, P.sq3 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq3] ] ],
                couplings = {(0,0,0):C.R2GC_195_134})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.H, P.sq1__tilde__, P.sq1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq1] ] ],
                couplings = {(0,0,0):C.R2GC_180_127})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.H, P.sq1__tilde__, P.sq2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq1, P.sq2] ] ],
                couplings = {(0,0,0):C.R2GC_218_137})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.H, P.sq1__tilde__, P.sq3 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq1, P.sq3] ] ],
                couplings = {(0,0,0):C.R2GC_219_138})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.H, P.sq1__tilde__, P.sq4 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq1, P.sq4] ] ],
                couplings = {(0,0,0):C.R2GC_220_139})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.H, P.sq1, P.sq2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq1, P.sq2] ] ],
                couplings = {(0,0,0):C.R2GC_218_137})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.H, P.sq2__tilde__, P.sq2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq2] ] ],
                couplings = {(0,0,0):C.R2GC_187_130})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.H, P.sq2__tilde__, P.sq3 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq2, P.sq3] ] ],
                couplings = {(0,0,0):C.R2GC_221_140})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.H, P.sq2__tilde__, P.sq4 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq2, P.sq4] ] ],
                couplings = {(0,0,0):C.R2GC_222_141})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.H, P.sq1, P.sq3__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq1, P.sq3] ] ],
                couplings = {(0,0,0):C.R2GC_219_138})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.H, P.sq2, P.sq3__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq2, P.sq3] ] ],
                couplings = {(0,0,0):C.R2GC_221_140})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.H, P.sq3__tilde__, P.sq3 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq3] ] ],
                couplings = {(0,0,0):C.R2GC_194_133})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.H, P.sq3__tilde__, P.sq4 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq3, P.sq4] ] ],
                couplings = {(0,0,0):C.R2GC_223_142})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.H, P.sq1, P.sq4__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq1, P.sq4] ] ],
                couplings = {(0,0,0):C.R2GC_220_139})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.H, P.sq2, P.sq4__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq2, P.sq4] ] ],
                couplings = {(0,0,0):C.R2GC_222_141})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.H, P.sq3, P.sq4__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq3, P.sq4] ] ],
                couplings = {(0,0,0):C.R2GC_223_142})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.H, P.sq4__tilde__, P.sq4 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS2 ],
                loop_particles = [ [ [P.g, P.sq4] ] ],
                couplings = {(0,0,0):C.R2GC_200_135})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.bp1__tilde__, P.bp1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.bp1, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_164_121})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.bp2__tilde__, P.bp2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.bp2, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_164_121})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.bp3__tilde__, P.bp3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.bp3, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_164_121})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.tp1__tilde__, P.tp1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.tp1] ] ],
                couplings = {(0,0,0):C.R2GC_164_121})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.tp2__tilde__, P.tp2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.tp2] ] ],
                couplings = {(0,0,0):C.R2GC_164_121})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.tp3__tilde__, P.tp3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.tp3] ] ],
                couplings = {(0,0,0):C.R2GC_164_121})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.tp4__tilde__, P.tp4, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.tp4] ] ],
                couplings = {(0,0,0):C.R2GC_164_121})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.g, P.sq1__tilde__, P.sq1 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.sq1] ] ],
                couplings = {(0,0,0):C.R2GC_178_124})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.g, P.sq2__tilde__, P.sq2 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.sq2] ] ],
                couplings = {(0,0,0):C.R2GC_178_124})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.g, P.sq3__tilde__, P.sq3 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.sq3] ] ],
                couplings = {(0,0,0):C.R2GC_178_124})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.g, P.sq4__tilde__, P.sq4 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.sq4] ] ],
                couplings = {(0,0,0):C.R2GC_178_124})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.g, P.g, P.sq1__tilde__, P.sq1 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS2 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.sq1] ] ],
                couplings = {(2,0,0):C.R2GC_179_125,(2,0,1):C.R2GC_179_126,(1,0,0):C.R2GC_179_125,(1,0,1):C.R2GC_179_126,(0,0,0):C.R2GC_159_115,(0,0,1):C.R2GC_176_122})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.g, P.g, P.sq2__tilde__, P.sq2 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS2 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.sq2] ] ],
                couplings = {(2,0,0):C.R2GC_179_125,(2,0,1):C.R2GC_179_126,(1,0,0):C.R2GC_179_125,(1,0,1):C.R2GC_179_126,(0,0,0):C.R2GC_159_115,(0,0,1):C.R2GC_176_122})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.g, P.g, P.sq3__tilde__, P.sq3 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS2 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.sq3] ] ],
                couplings = {(2,0,0):C.R2GC_179_125,(2,0,1):C.R2GC_179_126,(1,0,0):C.R2GC_179_125,(1,0,1):C.R2GC_179_126,(0,0,0):C.R2GC_159_115,(0,0,1):C.R2GC_176_122})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.g, P.g, P.sq4__tilde__, P.sq4 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS2 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.sq4] ] ],
                couplings = {(2,0,0):C.R2GC_179_125,(2,0,1):C.R2GC_179_126,(1,0,0):C.R2GC_179_125,(1,0,1):C.R2GC_179_126,(0,0,0):C.R2GC_159_115,(0,0,1):C.R2GC_176_122})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_114_3})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_114_3})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_114_3})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_163_120})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_163_120})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_163_120})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_164_121})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_164_121})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_164_121})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_164_121})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_164_121})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_164_121})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_217_136})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_217_136})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_217_136})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_217_136})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_217_136})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_217_136})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_138_79,(0,1,0):C.R2GC_115_4})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_138_79,(0,1,0):C.R2GC_115_4})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_138_79,(0,1,0):C.R2GC_115_4})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_139_80,(0,1,0):C.R2GC_117_5})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_139_80,(0,1,0):C.R2GC_117_5})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_139_80,(0,1,0):C.R2GC_117_5})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_113_2})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_113_2})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_274_175,(0,1,0):C.R2GC_113_2})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_113_2})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_113_2})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_230_145,(0,1,0):C.R2GC_113_2})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.tp1__tilde__, P.tp1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp1] ] ],
                 couplings = {(0,0,0):C.R2GC_287_182,(0,1,0):C.R2GC_113_2})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.tp2__tilde__, P.tp2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp2] ] ],
                 couplings = {(0,0,0):C.R2GC_298_190,(0,1,0):C.R2GC_113_2})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.tp3__tilde__, P.tp3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp3] ] ],
                 couplings = {(0,0,0):C.R2GC_309_198,(0,1,0):C.R2GC_113_2})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.tp4__tilde__, P.tp4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp4] ] ],
                 couplings = {(0,0,0):C.R2GC_330_217,(0,1,0):C.R2GC_113_2})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.bp1__tilde__, P.bp1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.bp1, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_242_152,(0,1,0):C.R2GC_113_2})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.bp2__tilde__, P.bp2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.bp2, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_253_160,(0,1,0):C.R2GC_113_2})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.bp3__tilde__, P.bp3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.bp3, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_264_168,(0,1,0):C.R2GC_113_2})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.sq1__tilde__, P.sq1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.sq1] ] ],
                 couplings = {(0,0,0):C.R2GC_265_169,(0,1,0):C.R2GC_177_123})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.sq2__tilde__, P.sq2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.sq2] ] ],
                 couplings = {(0,0,0):C.R2GC_266_170,(0,1,0):C.R2GC_177_123})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.sq3__tilde__, P.sq3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.sq3] ] ],
                 couplings = {(0,0,0):C.R2GC_267_171,(0,1,0):C.R2GC_177_123})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.sq4__tilde__, P.sq4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.sq4] ] ],
                 couplings = {(0,0,0):C.R2GC_268_172,(0,1,0):C.R2GC_177_123})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV2, L.VV3, L.VV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.b], [P.bp1], [P.bp2], [P.bp3], [P.c], [P.d], [P.s], [P.t], [P.tp1], [P.tp2], [P.tp3], [P.tp4], [P.u] ], [ [P.g] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,2,5):C.R2GC_112_1,(0,0,0):C.R2GC_130_57,(0,0,1):C.R2GC_130_58,(0,0,2):C.R2GC_130_59,(0,0,3):C.R2GC_130_60,(0,0,6):C.R2GC_130_61,(0,0,7):C.R2GC_130_62,(0,0,8):C.R2GC_130_63,(0,0,9):C.R2GC_130_64,(0,0,10):C.R2GC_130_65,(0,1,4):C.R2GC_131_66})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ], [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_1000_1016,(0,0,1):C.R2GC_129_49,(0,0,2):C.R2GC_129_50,(0,0,3):C.R2GC_129_51,(0,0,4):C.R2GC_1000_1005,(0,0,5):C.R2GC_129_53,(0,0,6):C.R2GC_129_54,(0,0,7):C.R2GC_129_55,(0,0,8):C.R2GC_129_56,(0,0,0):C.R2GC_1000_1017,(0,0,4):C.R2GC_1000_1006})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s01 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ] ],
                 couplings = {(0,0,0):C.R2GC_127_36,(0,0,1):C.R2GC_127_37,(0,0,2):C.R2GC_127_38,(0,0,3):C.R2GC_127_39,(0,0,4):C.R2GC_127_40,(0,0,5):C.R2GC_127_41})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s02 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ] ],
                 couplings = {(0,0,0):C.R2GC_128_42,(0,0,1):C.R2GC_128_43,(0,0,2):C.R2GC_128_44,(0,0,3):C.R2GC_128_45,(0,0,4):C.R2GC_128_46,(0,0,5):C.R2GC_128_47})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV15 ],
                 loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_142_106})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV15 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_134_71,(0,0,1):C.R2GC_134_72})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV15 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_137_77,(0,0,1):C.R2GC_137_78})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV15 ],
                 loop_particles = [ [ [P.b], [P.bp1], [P.bp2], [P.bp3], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp1], [P.tp2], [P.tp3], [P.tp4], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_132_67,(0,0,1):C.R2GC_132_68})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV15, L.VVVV6 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(1,1,0):C.R2GC_136_75,(1,1,1):C.R2GC_136_76,(0,0,0):C.R2GC_135_73,(0,0,1):C.R2GC_135_74})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV15 ],
                 loop_particles = [ [ [P.b], [P.bp1], [P.bp2], [P.bp3], [P.d], [P.s] ], [ [P.c], [P.t], [P.tp1], [P.tp2], [P.tp3], [P.tp4], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_133_69,(0,0,1):C.R2GC_133_70})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp1, P.bp2] ], [ [P.bp1, P.bp3] ], [ [P.bp2] ], [ [P.bp2, P.bp3] ], [ [P.bp3] ], [ [P.b, P.bp1] ], [ [P.b, P.bp2] ], [ [P.b, P.bp3] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp1, P.tp2] ], [ [P.tp1, P.tp3] ], [ [P.tp1, P.tp4] ], [ [P.tp2] ], [ [P.tp2, P.tp3] ], [ [P.tp2, P.tp4] ], [ [P.tp3] ], [ [P.tp3, P.tp4] ], [ [P.tp4] ], [ [P.t, P.tp1] ], [ [P.t, P.tp2] ], [ [P.t, P.tp3] ], [ [P.t, P.tp4] ], [ [P.b] ], [ [P.b] ], [ [P.t] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_1000_1018,(0,0,1):C.R2GC_141_82,(0,0,4):C.R2GC_141_83,(0,0,6):C.R2GC_141_84,(0,0,10):C.R2GC_1000_1007,(0,0,11):C.R2GC_141_86,(0,0,15):C.R2GC_141_87,(0,0,18):C.R2GC_141_88,(0,0,20):C.R2GC_141_89,(0,0,7):C.R2GC_141_90,(0,0,8):C.R2GC_141_91,(0,0,9):C.R2GC_141_92,(0,0,2):C.R2GC_141_93,(0,0,3):C.R2GC_141_94,(0,0,5):C.R2GC_141_95,(0,0,21):C.R2GC_141_96,(0,0,22):C.R2GC_141_97,(0,0,23):C.R2GC_141_98,(0,0,24):C.R2GC_141_99,(0,0,12):C.R2GC_141_100,(0,0,13):C.R2GC_141_101,(0,0,14):C.R2GC_141_102,(0,0,16):C.R2GC_141_103,(0,0,17):C.R2GC_141_104,(0,0,19):C.R2GC_141_105,(0,0,25):C.R2GC_1000_1019,(0,0,26):C.R2GC_1000_1020,(0,0,27):C.R2GC_1000_1008,(0,0,28):C.R2GC_1000_1009})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.s01 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_1000_1012,(0,0,1):C.R2GC_122_7,(0,0,2):C.R2GC_122_8,(0,0,3):C.R2GC_1000_1001,(0,0,4):C.R2GC_122_10,(0,0,5):C.R2GC_122_11,(0,0,6):C.R2GC_1000_1013,(0,0,7):C.R2GC_1000_1002})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s01, P.s01 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ] ],
                 couplings = {(0,0,0):C.R2GC_123_12,(0,0,1):C.R2GC_123_13,(0,0,2):C.R2GC_123_14,(0,0,3):C.R2GC_123_15,(0,0,4):C.R2GC_123_16,(0,0,5):C.R2GC_123_17})

V_153 = CTVertex(name = 'V_153',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.s02 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.b] ], [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_1000_1014,(0,0,1):C.R2GC_124_19,(0,0,2):C.R2GC_124_20,(0,0,3):C.R2GC_1000_1003,(0,0,4):C.R2GC_124_22,(0,0,5):C.R2GC_124_23,(0,0,6):C.R2GC_1000_1015,(0,0,7):C.R2GC_1000_1004})

V_154 = CTVertex(name = 'V_154',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s01, P.s02 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ] ],
                 couplings = {(0,0,0):C.R2GC_125_24,(0,0,1):C.R2GC_125_25,(0,0,2):C.R2GC_125_26,(0,0,3):C.R2GC_125_27,(0,0,4):C.R2GC_125_28,(0,0,5):C.R2GC_125_29})

V_155 = CTVertex(name = 'V_155',
                 type = 'R2',
                 particles = [ P.g, P.g, P.s02, P.s02 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ] ],
                 couplings = {(0,0,0):C.R2GC_126_30,(0,0,1):C.R2GC_126_31,(0,0,2):C.R2GC_126_32,(0,0,3):C.R2GC_126_33,(0,0,4):C.R2GC_126_34,(0,0,5):C.R2GC_126_35})

V_156 = CTVertex(name = 'V_156',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_2000_2003,(0,0,1):C.UVGC_2000_2004})

V_157 = CTVertex(name = 'V_157',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.s01 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_228_120})

V_158 = CTVertex(name = 'V_158',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.s02 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_229_121})

V_159 = CTVertex(name = 'V_159',
                 type = 'UV',
                 particles = [ P.bp1__tilde__, P.bp1, P.s01 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.bp1, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_240_136})

V_160 = CTVertex(name = 'V_160',
                 type = 'UV',
                 particles = [ P.bp1__tilde__, P.bp1, P.s02 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.bp1, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_241_137})

V_161 = CTVertex(name = 'V_161',
                 type = 'UV',
                 particles = [ P.bp2__tilde__, P.bp2, P.s01 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.bp2, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_251_155})

V_162 = CTVertex(name = 'V_162',
                 type = 'UV',
                 particles = [ P.bp2__tilde__, P.bp2, P.s02 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.bp2, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_252_156})

V_163 = CTVertex(name = 'V_163',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_2000_2001,(0,0,0):C.UVGC_2000_2002})

V_164 = CTVertex(name = 'V_164',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.s01 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_272_188})

V_165 = CTVertex(name = 'V_165',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.s02 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_273_189})

V_166 = CTVertex(name = 'V_166',
                 type = 'UV',
                 particles = [ P.tp1__tilde__, P.tp1, P.s01 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp1] ] ],
                 couplings = {(0,0,0):C.UVGC_285_206})

V_167 = CTVertex(name = 'V_167',
                 type = 'UV',
                 particles = [ P.tp1__tilde__, P.tp1, P.s02 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp1] ] ],
                 couplings = {(0,0,0):C.UVGC_286_207})

V_168 = CTVertex(name = 'V_168',
                 type = 'UV',
                 particles = [ P.tp2__tilde__, P.tp2, P.s01 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp2] ] ],
                 couplings = {(0,0,0):C.UVGC_296_225})

V_169 = CTVertex(name = 'V_169',
                 type = 'UV',
                 particles = [ P.tp2__tilde__, P.tp2, P.s02 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp2] ] ],
                 couplings = {(0,0,0):C.UVGC_297_226})

V_170 = CTVertex(name = 'V_170',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV2, L.VVV3, L.VVV4, L.VVV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.sq1] ], [ [P.sq1], [P.sq2], [P.sq3], [P.sq4] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,1,0):C.UVGC_311_264,(0,1,1):C.UVGC_311_265,(0,1,2):C.UVGC_311_266,(0,1,3):C.UVGC_311_267,(0,1,4):C.UVGC_311_268,(0,1,7):C.UVGC_311_269,(0,1,9):C.UVGC_311_270,(0,1,10):C.UVGC_311_271,(0,1,11):C.UVGC_311_272,(0,1,12):C.UVGC_311_273,(0,1,13):C.UVGC_311_274,(0,1,14):C.UVGC_311_275,(0,1,15):C.UVGC_311_276,(0,1,16):C.UVGC_311_277,(0,3,5):C.UVGC_144_1,(0,0,6):C.UVGC_145_2,(0,2,8):C.UVGC_160_16})

V_171 = CTVertex(name = 'V_171',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV10, L.VVVV15, L.VVVV7, L.VVVV8 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.b], [P.bp1], [P.bp2], [P.bp3], [P.c], [P.d], [P.s], [P.sq1], [P.sq2], [P.sq3], [P.sq4], [P.t], [P.tp1], [P.tp2], [P.tp3], [P.tp4], [P.u] ], [ [P.b], [P.bp1], [P.bp2], [P.bp3], [P.c], [P.d], [P.s], [P.t], [P.tp1], [P.tp2], [P.tp3], [P.tp4], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.sq1] ], [ [P.sq1], [P.sq2], [P.sq3], [P.sq4] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,2,7):C.UVGC_156_11,(0,2,8):C.UVGC_156_10,(2,2,7):C.UVGC_156_11,(2,2,8):C.UVGC_156_10,(5,2,7):C.UVGC_155_8,(5,2,8):C.UVGC_155_9,(1,2,7):C.UVGC_155_8,(1,2,8):C.UVGC_155_9,(7,2,0):C.UVGC_315_315,(7,2,1):C.UVGC_315_316,(7,2,2):C.UVGC_315_317,(7,2,3):C.UVGC_315_318,(7,2,6):C.UVGC_179_65,(7,2,7):C.UVGC_315_319,(7,2,8):C.UVGC_315_320,(7,2,9):C.UVGC_315_321,(7,2,11):C.UVGC_315_322,(7,2,12):C.UVGC_315_323,(7,2,13):C.UVGC_315_324,(7,2,14):C.UVGC_315_325,(7,2,15):C.UVGC_315_326,(7,2,16):C.UVGC_315_327,(7,2,17):C.UVGC_315_328,(7,2,18):C.UVGC_315_329,(4,2,7):C.UVGC_155_8,(4,2,8):C.UVGC_155_9,(3,2,7):C.UVGC_155_8,(3,2,8):C.UVGC_155_9,(8,2,7):C.UVGC_156_10,(8,2,8):C.UVGC_156_11,(6,2,0):C.UVGC_315_315,(6,2,1):C.UVGC_315_316,(6,2,2):C.UVGC_315_317,(6,2,3):C.UVGC_315_318,(6,2,6):C.UVGC_179_65,(6,2,7):C.UVGC_316_330,(6,2,8):C.UVGC_316_331,(6,2,9):C.UVGC_315_321,(6,2,11):C.UVGC_315_322,(6,2,12):C.UVGC_315_323,(6,2,13):C.UVGC_315_324,(6,2,14):C.UVGC_315_325,(6,2,15):C.UVGC_315_326,(6,2,16):C.UVGC_315_327,(6,2,17):C.UVGC_315_328,(6,2,18):C.UVGC_315_329,(11,1,7):C.UVGC_159_14,(11,1,8):C.UVGC_159_15,(10,1,7):C.UVGC_159_14,(10,1,8):C.UVGC_159_15,(9,1,7):C.UVGC_158_12,(9,1,8):C.UVGC_158_13,(0,3,7):C.UVGC_156_11,(0,3,8):C.UVGC_156_10,(2,3,7):C.UVGC_156_11,(2,3,8):C.UVGC_156_10,(5,3,7):C.UVGC_155_8,(5,3,8):C.UVGC_155_9,(1,3,7):C.UVGC_155_8,(1,3,8):C.UVGC_155_9,(7,3,4):C.UVGC_161_17,(7,3,7):C.UVGC_162_20,(7,3,8):C.UVGC_162_21,(4,3,7):C.UVGC_155_8,(4,3,8):C.UVGC_155_9,(3,3,7):C.UVGC_155_8,(3,3,8):C.UVGC_155_9,(8,3,0):C.UVGC_317_332,(8,3,1):C.UVGC_317_333,(8,3,2):C.UVGC_317_334,(8,3,3):C.UVGC_317_335,(8,3,6):C.UVGC_317_336,(8,3,7):C.UVGC_317_337,(8,3,8):C.UVGC_317_338,(8,3,9):C.UVGC_317_339,(8,3,11):C.UVGC_317_340,(8,3,12):C.UVGC_317_341,(8,3,13):C.UVGC_317_342,(8,3,14):C.UVGC_317_343,(8,3,15):C.UVGC_317_344,(8,3,16):C.UVGC_317_345,(8,3,17):C.UVGC_317_346,(8,3,18):C.UVGC_317_347,(6,3,0):C.UVGC_312_278,(6,3,1):C.UVGC_312_279,(6,3,2):C.UVGC_312_280,(6,3,3):C.UVGC_312_281,(6,3,7):C.UVGC_313_293,(6,3,8):C.UVGC_313_294,(6,3,9):C.UVGC_313_295,(6,3,11):C.UVGC_313_296,(6,3,12):C.UVGC_313_297,(6,3,13):C.UVGC_313_298,(6,3,14):C.UVGC_312_288,(6,3,15):C.UVGC_312_289,(6,3,16):C.UVGC_312_290,(6,3,17):C.UVGC_312_291,(6,3,18):C.UVGC_312_292,(0,0,7):C.UVGC_156_11,(0,0,8):C.UVGC_156_10,(2,0,7):C.UVGC_156_11,(2,0,8):C.UVGC_156_10,(7,0,0):C.UVGC_312_278,(7,0,1):C.UVGC_312_279,(7,0,2):C.UVGC_312_280,(7,0,3):C.UVGC_312_281,(7,0,7):C.UVGC_312_282,(7,0,8):C.UVGC_312_283,(7,0,9):C.UVGC_312_284,(7,0,11):C.UVGC_312_285,(7,0,12):C.UVGC_312_286,(7,0,13):C.UVGC_312_287,(7,0,14):C.UVGC_312_288,(7,0,15):C.UVGC_312_289,(7,0,16):C.UVGC_312_290,(7,0,17):C.UVGC_312_291,(7,0,18):C.UVGC_312_292,(5,0,7):C.UVGC_155_8,(5,0,8):C.UVGC_155_9,(1,0,7):C.UVGC_155_8,(1,0,8):C.UVGC_155_9,(4,0,7):C.UVGC_155_8,(4,0,8):C.UVGC_155_9,(3,0,7):C.UVGC_155_8,(3,0,8):C.UVGC_155_9,(8,0,0):C.UVGC_314_299,(8,0,1):C.UVGC_314_300,(8,0,2):C.UVGC_314_301,(8,0,3):C.UVGC_314_302,(8,0,6):C.UVGC_314_303,(8,0,7):C.UVGC_314_304,(8,0,8):C.UVGC_314_305,(8,0,9):C.UVGC_314_306,(8,0,11):C.UVGC_314_307,(8,0,12):C.UVGC_314_308,(8,0,13):C.UVGC_314_309,(8,0,14):C.UVGC_314_310,(8,0,15):C.UVGC_314_311,(8,0,16):C.UVGC_314_312,(8,0,17):C.UVGC_314_313,(8,0,18):C.UVGC_314_314,(6,0,5):C.UVGC_161_17,(6,0,7):C.UVGC_161_18,(6,0,8):C.UVGC_158_12,(6,0,10):C.UVGC_161_19})

V_172 = CTVertex(name = 'V_172',
                 type = 'UV',
                 particles = [ P.bp1__tilde__, P.bp1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.bp1, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_163_22,(0,1,0):C.UVGC_235_127})

V_173 = CTVertex(name = 'V_173',
                 type = 'UV',
                 particles = [ P.bp2__tilde__, P.bp2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.bp2, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_163_22,(0,1,0):C.UVGC_244_140})

V_174 = CTVertex(name = 'V_174',
                 type = 'UV',
                 particles = [ P.bp3__tilde__, P.bp3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.bp3, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_163_22,(0,1,0):C.UVGC_255_159})

V_175 = CTVertex(name = 'V_175',
                 type = 'UV',
                 particles = [ P.tp1__tilde__, P.tp1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.g, P.tp1] ] ],
                 couplings = {(0,0,0):C.UVGC_147_4,(0,1,0):C.UVGC_280_197})

V_176 = CTVertex(name = 'V_176',
                 type = 'UV',
                 particles = [ P.tp2__tilde__, P.tp2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.g, P.tp2] ] ],
                 couplings = {(0,0,0):C.UVGC_147_4,(0,1,0):C.UVGC_289_210})

V_177 = CTVertex(name = 'V_177',
                 type = 'UV',
                 particles = [ P.tp3__tilde__, P.tp3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.g, P.tp3] ] ],
                 couplings = {(0,0,0):C.UVGC_147_4,(0,1,0):C.UVGC_300_229})

V_178 = CTVertex(name = 'V_178',
                 type = 'UV',
                 particles = [ P.tp4__tilde__, P.tp4, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.g, P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_147_4,(0,1,0):C.UVGC_319_349})

V_179 = CTVertex(name = 'V_179',
                 type = 'UV',
                 particles = [ P.bp1__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.bp1, P.g] ], [ [P.b, P.bp1, P.g] ], [ [P.b, P.g] ] ],
                 couplings = {(0,0,2):C.UVGC_239_133,(0,0,0):C.UVGC_239_134,(0,0,1):C.UVGC_239_135,(0,1,2):C.UVGC_238_130,(0,1,0):C.UVGC_238_131,(0,1,1):C.UVGC_238_132})

V_180 = CTVertex(name = 'V_180',
                 type = 'UV',
                 particles = [ P.bp2__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.bp2, P.g] ], [ [P.b, P.bp2, P.g] ], [ [P.b, P.g] ] ],
                 couplings = {(0,0,2):C.UVGC_250_152,(0,0,0):C.UVGC_250_153,(0,0,1):C.UVGC_250_154,(0,1,2):C.UVGC_249_149,(0,1,0):C.UVGC_249_150,(0,1,1):C.UVGC_249_151})

V_181 = CTVertex(name = 'V_181',
                 type = 'UV',
                 particles = [ P.bp3__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.bp3, P.g] ], [ [P.b, P.bp3, P.g] ], [ [P.b, P.g] ] ],
                 couplings = {(0,0,2):C.UVGC_263_177,(0,0,0):C.UVGC_263_178,(0,0,1):C.UVGC_263_179,(0,1,2):C.UVGC_262_174,(0,1,0):C.UVGC_262_175,(0,1,1):C.UVGC_262_176})

V_182 = CTVertex(name = 'V_182',
                 type = 'UV',
                 particles = [ P.tp1__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp1] ], [ [P.g, P.t, P.tp1] ] ],
                 couplings = {(0,0,0):C.UVGC_284_203,(0,0,1):C.UVGC_284_204,(0,0,2):C.UVGC_284_205,(0,1,0):C.UVGC_283_200,(0,1,1):C.UVGC_283_201,(0,1,2):C.UVGC_283_202})

V_183 = CTVertex(name = 'V_183',
                 type = 'UV',
                 particles = [ P.tp2__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp2] ], [ [P.g, P.t, P.tp2] ] ],
                 couplings = {(0,0,0):C.UVGC_295_222,(0,0,1):C.UVGC_295_223,(0,0,2):C.UVGC_295_224,(0,1,0):C.UVGC_294_219,(0,1,1):C.UVGC_294_220,(0,1,2):C.UVGC_294_221})

V_184 = CTVertex(name = 'V_184',
                 type = 'UV',
                 particles = [ P.tp3__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp3] ], [ [P.g, P.t, P.tp3] ] ],
                 couplings = {(0,0,0):C.UVGC_308_247,(0,0,1):C.UVGC_308_248,(0,0,2):C.UVGC_308_249,(0,1,0):C.UVGC_307_244,(0,1,1):C.UVGC_307_245,(0,1,2):C.UVGC_307_246})

V_185 = CTVertex(name = 'V_185',
                 type = 'UV',
                 particles = [ P.tp4__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp4] ], [ [P.g, P.t, P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_329_373,(0,0,1):C.UVGC_329_374,(0,0,2):C.UVGC_329_375,(0,1,0):C.UVGC_328_370,(0,1,1):C.UVGC_328_371,(0,1,2):C.UVGC_328_372})

V_186 = CTVertex(name = 'V_186',
                 type = 'UV',
                 particles = [ P.bp1__tilde__, P.bp1, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.bp1, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_237_129})

V_187 = CTVertex(name = 'V_187',
                 type = 'UV',
                 particles = [ P.bp2__tilde__, P.bp1, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.bp1, P.bp2, P.g] ], [ [P.bp1, P.g] ], [ [P.bp2, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_246_142,(0,0,2):C.UVGC_246_143,(0,0,0):C.UVGC_246_144,(0,1,1):C.UVGC_247_145,(0,1,2):C.UVGC_247_146,(0,1,0):C.UVGC_247_147})

V_188 = CTVertex(name = 'V_188',
                 type = 'UV',
                 particles = [ P.bp3__tilde__, P.bp1, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.bp1, P.bp3, P.g] ], [ [P.bp1, P.g] ], [ [P.bp3, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_257_161,(0,0,2):C.UVGC_257_162,(0,0,0):C.UVGC_257_163,(0,1,1):C.UVGC_259_167,(0,1,2):C.UVGC_259_168,(0,1,0):C.UVGC_259_169})

V_189 = CTVertex(name = 'V_189',
                 type = 'UV',
                 particles = [ P.bp1__tilde__, P.bp2, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.bp1, P.bp2, P.g] ], [ [P.bp1, P.g] ], [ [P.bp2, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_247_145,(0,0,2):C.UVGC_247_146,(0,0,0):C.UVGC_247_147,(0,1,1):C.UVGC_246_142,(0,1,2):C.UVGC_246_143,(0,1,0):C.UVGC_246_144})

V_190 = CTVertex(name = 'V_190',
                 type = 'UV',
                 particles = [ P.bp2__tilde__, P.bp2, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.bp2, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_248_148})

V_191 = CTVertex(name = 'V_191',
                 type = 'UV',
                 particles = [ P.bp3__tilde__, P.bp2, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.bp2, P.bp3, P.g] ], [ [P.bp2, P.g] ], [ [P.bp3, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_258_164,(0,0,2):C.UVGC_258_165,(0,0,0):C.UVGC_258_166,(0,1,1):C.UVGC_260_170,(0,1,2):C.UVGC_260_171,(0,1,0):C.UVGC_260_172})

V_192 = CTVertex(name = 'V_192',
                 type = 'UV',
                 particles = [ P.bp1__tilde__, P.bp3, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.bp1, P.bp3, P.g] ], [ [P.bp1, P.g] ], [ [P.bp3, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_259_167,(0,0,2):C.UVGC_259_168,(0,0,0):C.UVGC_259_169,(0,1,1):C.UVGC_257_161,(0,1,2):C.UVGC_257_162,(0,1,0):C.UVGC_257_163})

V_193 = CTVertex(name = 'V_193',
                 type = 'UV',
                 particles = [ P.bp2__tilde__, P.bp3, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.bp2, P.bp3, P.g] ], [ [P.bp2, P.g] ], [ [P.bp3, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_260_170,(0,0,2):C.UVGC_260_171,(0,0,0):C.UVGC_260_172,(0,1,1):C.UVGC_258_164,(0,1,2):C.UVGC_258_165,(0,1,0):C.UVGC_258_166})

V_194 = CTVertex(name = 'V_194',
                 type = 'UV',
                 particles = [ P.bp3__tilde__, P.bp3, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.bp3, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_261_173})

V_195 = CTVertex(name = 'V_195',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp1, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.bp1, P.g] ], [ [P.b, P.bp1, P.g] ], [ [P.b, P.g] ] ],
                 couplings = {(0,0,2):C.UVGC_238_130,(0,0,0):C.UVGC_238_131,(0,0,1):C.UVGC_238_132,(0,1,2):C.UVGC_239_133,(0,1,0):C.UVGC_239_134,(0,1,1):C.UVGC_239_135})

V_196 = CTVertex(name = 'V_196',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp2, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.bp2, P.g] ], [ [P.b, P.bp2, P.g] ], [ [P.b, P.g] ] ],
                 couplings = {(0,0,2):C.UVGC_249_149,(0,0,0):C.UVGC_249_150,(0,0,1):C.UVGC_249_151,(0,1,2):C.UVGC_250_152,(0,1,0):C.UVGC_250_153,(0,1,1):C.UVGC_250_154})

V_197 = CTVertex(name = 'V_197',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.bp3, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.bp3, P.g] ], [ [P.b, P.bp3, P.g] ], [ [P.b, P.g] ] ],
                 couplings = {(0,0,2):C.UVGC_262_174,(0,0,0):C.UVGC_262_175,(0,0,1):C.UVGC_262_176,(0,1,2):C.UVGC_263_177,(0,1,0):C.UVGC_263_178,(0,1,1):C.UVGC_263_179})

V_198 = CTVertex(name = 'V_198',
                 type = 'UV',
                 particles = [ P.tp1__tilde__, P.tp1, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp1] ] ],
                 couplings = {(0,0,0):C.UVGC_282_199})

V_199 = CTVertex(name = 'V_199',
                 type = 'UV',
                 particles = [ P.tp2__tilde__, P.tp1, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.tp1] ], [ [P.g, P.tp1, P.tp2] ], [ [P.g, P.tp2] ] ],
                 couplings = {(0,0,0):C.UVGC_291_212,(0,0,2):C.UVGC_291_213,(0,0,1):C.UVGC_291_214,(0,1,0):C.UVGC_292_215,(0,1,2):C.UVGC_292_216,(0,1,1):C.UVGC_292_217})

V_200 = CTVertex(name = 'V_200',
                 type = 'UV',
                 particles = [ P.tp3__tilde__, P.tp1, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.tp1] ], [ [P.g, P.tp1, P.tp3] ], [ [P.g, P.tp3] ] ],
                 couplings = {(0,0,0):C.UVGC_302_231,(0,0,2):C.UVGC_302_232,(0,0,1):C.UVGC_302_233,(0,1,0):C.UVGC_304_237,(0,1,2):C.UVGC_304_238,(0,1,1):C.UVGC_304_239})

V_201 = CTVertex(name = 'V_201',
                 type = 'UV',
                 particles = [ P.tp4__tilde__, P.tp1, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.tp1] ], [ [P.g, P.tp1, P.tp4] ], [ [P.g, P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_321_351,(0,0,2):C.UVGC_321_352,(0,0,1):C.UVGC_321_353,(0,1,0):C.UVGC_324_360,(0,1,2):C.UVGC_324_361,(0,1,1):C.UVGC_324_362})

V_202 = CTVertex(name = 'V_202',
                 type = 'UV',
                 particles = [ P.tp1__tilde__, P.tp2, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.tp1] ], [ [P.g, P.tp1, P.tp2] ], [ [P.g, P.tp2] ] ],
                 couplings = {(0,0,0):C.UVGC_292_215,(0,0,2):C.UVGC_292_216,(0,0,1):C.UVGC_292_217,(0,1,0):C.UVGC_291_212,(0,1,2):C.UVGC_291_213,(0,1,1):C.UVGC_291_214})

V_203 = CTVertex(name = 'V_203',
                 type = 'UV',
                 particles = [ P.tp2__tilde__, P.tp2, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp2] ] ],
                 couplings = {(0,0,0):C.UVGC_293_218})

V_204 = CTVertex(name = 'V_204',
                 type = 'UV',
                 particles = [ P.tp3__tilde__, P.tp2, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.tp2] ], [ [P.g, P.tp2, P.tp3] ], [ [P.g, P.tp3] ] ],
                 couplings = {(0,0,0):C.UVGC_303_234,(0,0,2):C.UVGC_303_235,(0,0,1):C.UVGC_303_236,(0,1,0):C.UVGC_305_240,(0,1,2):C.UVGC_305_241,(0,1,1):C.UVGC_305_242})

V_205 = CTVertex(name = 'V_205',
                 type = 'UV',
                 particles = [ P.tp4__tilde__, P.tp2, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.tp2] ], [ [P.g, P.tp2, P.tp4] ], [ [P.g, P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_322_354,(0,0,2):C.UVGC_322_355,(0,0,1):C.UVGC_322_356,(0,1,0):C.UVGC_325_363,(0,1,2):C.UVGC_325_364,(0,1,1):C.UVGC_325_365})

V_206 = CTVertex(name = 'V_206',
                 type = 'UV',
                 particles = [ P.tp1__tilde__, P.tp3, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.tp1] ], [ [P.g, P.tp1, P.tp3] ], [ [P.g, P.tp3] ] ],
                 couplings = {(0,0,0):C.UVGC_304_237,(0,0,2):C.UVGC_304_238,(0,0,1):C.UVGC_304_239,(0,1,0):C.UVGC_302_231,(0,1,2):C.UVGC_302_232,(0,1,1):C.UVGC_302_233})

V_207 = CTVertex(name = 'V_207',
                 type = 'UV',
                 particles = [ P.tp2__tilde__, P.tp3, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.tp2] ], [ [P.g, P.tp2, P.tp3] ], [ [P.g, P.tp3] ] ],
                 couplings = {(0,0,0):C.UVGC_305_240,(0,0,2):C.UVGC_305_241,(0,0,1):C.UVGC_305_242,(0,1,0):C.UVGC_303_234,(0,1,2):C.UVGC_303_235,(0,1,1):C.UVGC_303_236})

V_208 = CTVertex(name = 'V_208',
                 type = 'UV',
                 particles = [ P.tp3__tilde__, P.tp3, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp3] ] ],
                 couplings = {(0,0,0):C.UVGC_306_243})

V_209 = CTVertex(name = 'V_209',
                 type = 'UV',
                 particles = [ P.tp4__tilde__, P.tp3, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.tp3] ], [ [P.g, P.tp3, P.tp4] ], [ [P.g, P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_323_357,(0,0,2):C.UVGC_323_358,(0,0,1):C.UVGC_323_359,(0,1,0):C.UVGC_326_366,(0,1,2):C.UVGC_326_367,(0,1,1):C.UVGC_326_368})

V_210 = CTVertex(name = 'V_210',
                 type = 'UV',
                 particles = [ P.tp1__tilde__, P.tp4, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.tp1] ], [ [P.g, P.tp1, P.tp4] ], [ [P.g, P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_324_360,(0,0,2):C.UVGC_324_361,(0,0,1):C.UVGC_324_362,(0,1,0):C.UVGC_321_351,(0,1,2):C.UVGC_321_352,(0,1,1):C.UVGC_321_353})

V_211 = CTVertex(name = 'V_211',
                 type = 'UV',
                 particles = [ P.tp2__tilde__, P.tp4, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.tp2] ], [ [P.g, P.tp2, P.tp4] ], [ [P.g, P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_325_363,(0,0,2):C.UVGC_325_364,(0,0,1):C.UVGC_325_365,(0,1,0):C.UVGC_322_354,(0,1,2):C.UVGC_322_355,(0,1,1):C.UVGC_322_356})

V_212 = CTVertex(name = 'V_212',
                 type = 'UV',
                 particles = [ P.tp3__tilde__, P.tp4, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.tp3] ], [ [P.g, P.tp3, P.tp4] ], [ [P.g, P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_326_366,(0,0,2):C.UVGC_326_367,(0,0,1):C.UVGC_326_368,(0,1,0):C.UVGC_323_357,(0,1,2):C.UVGC_323_358,(0,1,1):C.UVGC_323_359})

V_213 = CTVertex(name = 'V_213',
                 type = 'UV',
                 particles = [ P.tp4__tilde__, P.tp4, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_327_369})

V_214 = CTVertex(name = 'V_214',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp1, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp1] ], [ [P.g, P.t, P.tp1] ] ],
                 couplings = {(0,0,0):C.UVGC_283_200,(0,0,1):C.UVGC_283_201,(0,0,2):C.UVGC_283_202,(0,1,0):C.UVGC_284_203,(0,1,1):C.UVGC_284_204,(0,1,2):C.UVGC_284_205})

V_215 = CTVertex(name = 'V_215',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp2, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp2] ], [ [P.g, P.t, P.tp2] ] ],
                 couplings = {(0,0,0):C.UVGC_294_219,(0,0,1):C.UVGC_294_220,(0,0,2):C.UVGC_294_221,(0,1,0):C.UVGC_295_222,(0,1,1):C.UVGC_295_223,(0,1,2):C.UVGC_295_224})

V_216 = CTVertex(name = 'V_216',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp3, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp3] ], [ [P.g, P.t, P.tp3] ] ],
                 couplings = {(0,0,0):C.UVGC_307_244,(0,0,1):C.UVGC_307_245,(0,0,2):C.UVGC_307_246,(0,1,0):C.UVGC_308_247,(0,1,1):C.UVGC_308_248,(0,1,2):C.UVGC_308_249})

V_217 = CTVertex(name = 'V_217',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.tp4, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS6, L.FFS7 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.tp4] ], [ [P.g, P.t, P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_328_370,(0,0,1):C.UVGC_328_371,(0,0,2):C.UVGC_328_372,(0,1,0):C.UVGC_329_373,(0,1,1):C.UVGC_329_374,(0,1,2):C.UVGC_329_375})

V_218 = CTVertex(name = 'V_218',
                 type = 'UV',
                 particles = [ P.s01, P.sq1__tilde__, P.sq1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq1] ] ],
                 couplings = {(0,0,0):C.UVGC_181_79})

V_219 = CTVertex(name = 'V_219',
                 type = 'UV',
                 particles = [ P.s02, P.sq1__tilde__, P.sq1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq1] ] ],
                 couplings = {(0,0,0):C.UVGC_182_80})

V_220 = CTVertex(name = 'V_220',
                 type = 'UV',
                 particles = [ P.s01, P.sq2__tilde__, P.sq2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq2] ] ],
                 couplings = {(0,0,0):C.UVGC_188_85})

V_221 = CTVertex(name = 'V_221',
                 type = 'UV',
                 particles = [ P.s02, P.sq2__tilde__, P.sq2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq2] ] ],
                 couplings = {(0,0,0):C.UVGC_189_86})

V_222 = CTVertex(name = 'V_222',
                 type = 'UV',
                 particles = [ P.s01, P.sq3__tilde__, P.sq3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq3] ] ],
                 couplings = {(0,0,0):C.UVGC_195_91})

V_223 = CTVertex(name = 'V_223',
                 type = 'UV',
                 particles = [ P.H, P.sq1__tilde__, P.sq1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq1] ] ],
                 couplings = {(0,0,0):C.UVGC_180_78})

V_224 = CTVertex(name = 'V_224',
                 type = 'UV',
                 particles = [ P.H, P.sq1__tilde__, P.sq2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq1] ], [ [P.g, P.sq1, P.sq2] ], [ [P.g, P.sq2] ] ],
                 couplings = {(0,0,0):C.UVGC_218_99,(0,0,2):C.UVGC_218_100,(0,0,1):C.UVGC_218_101})

V_225 = CTVertex(name = 'V_225',
                 type = 'UV',
                 particles = [ P.H, P.sq1__tilde__, P.sq3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq1] ], [ [P.g, P.sq1, P.sq3] ], [ [P.g, P.sq3] ] ],
                 couplings = {(0,0,0):C.UVGC_219_102,(0,0,2):C.UVGC_219_103,(0,0,1):C.UVGC_219_104})

V_226 = CTVertex(name = 'V_226',
                 type = 'UV',
                 particles = [ P.H, P.sq1__tilde__, P.sq4 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq1] ], [ [P.g, P.sq1, P.sq4] ], [ [P.g, P.sq4] ] ],
                 couplings = {(0,0,0):C.UVGC_220_105,(0,0,2):C.UVGC_220_106,(0,0,1):C.UVGC_220_107})

V_227 = CTVertex(name = 'V_227',
                 type = 'UV',
                 particles = [ P.H, P.sq1, P.sq2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq1] ], [ [P.g, P.sq1, P.sq2] ], [ [P.g, P.sq2] ] ],
                 couplings = {(0,0,0):C.UVGC_218_99,(0,0,2):C.UVGC_218_100,(0,0,1):C.UVGC_218_101})

V_228 = CTVertex(name = 'V_228',
                 type = 'UV',
                 particles = [ P.H, P.sq2__tilde__, P.sq2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq2] ] ],
                 couplings = {(0,0,0):C.UVGC_187_84})

V_229 = CTVertex(name = 'V_229',
                 type = 'UV',
                 particles = [ P.H, P.sq2__tilde__, P.sq3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq2] ], [ [P.g, P.sq2, P.sq3] ], [ [P.g, P.sq3] ] ],
                 couplings = {(0,0,0):C.UVGC_221_108,(0,0,2):C.UVGC_221_109,(0,0,1):C.UVGC_221_110})

V_230 = CTVertex(name = 'V_230',
                 type = 'UV',
                 particles = [ P.H, P.sq2__tilde__, P.sq4 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq2] ], [ [P.g, P.sq2, P.sq4] ], [ [P.g, P.sq4] ] ],
                 couplings = {(0,0,0):C.UVGC_222_111,(0,0,2):C.UVGC_222_112,(0,0,1):C.UVGC_222_113})

V_231 = CTVertex(name = 'V_231',
                 type = 'UV',
                 particles = [ P.H, P.sq1, P.sq3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq1] ], [ [P.g, P.sq1, P.sq3] ], [ [P.g, P.sq3] ] ],
                 couplings = {(0,0,0):C.UVGC_219_102,(0,0,2):C.UVGC_219_103,(0,0,1):C.UVGC_219_104})

V_232 = CTVertex(name = 'V_232',
                 type = 'UV',
                 particles = [ P.H, P.sq2, P.sq3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq2] ], [ [P.g, P.sq2, P.sq3] ], [ [P.g, P.sq3] ] ],
                 couplings = {(0,0,0):C.UVGC_221_108,(0,0,2):C.UVGC_221_109,(0,0,1):C.UVGC_221_110})

V_233 = CTVertex(name = 'V_233',
                 type = 'UV',
                 particles = [ P.H, P.sq3__tilde__, P.sq3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq3] ] ],
                 couplings = {(0,0,0):C.UVGC_194_90})

V_234 = CTVertex(name = 'V_234',
                 type = 'UV',
                 particles = [ P.H, P.sq3__tilde__, P.sq4 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq3] ], [ [P.g, P.sq3, P.sq4] ], [ [P.g, P.sq4] ] ],
                 couplings = {(0,0,0):C.UVGC_223_114,(0,0,2):C.UVGC_223_115,(0,0,1):C.UVGC_223_116})

V_235 = CTVertex(name = 'V_235',
                 type = 'UV',
                 particles = [ P.H, P.sq1, P.sq4__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq1] ], [ [P.g, P.sq1, P.sq4] ], [ [P.g, P.sq4] ] ],
                 couplings = {(0,0,0):C.UVGC_220_105,(0,0,2):C.UVGC_220_106,(0,0,1):C.UVGC_220_107})

V_236 = CTVertex(name = 'V_236',
                 type = 'UV',
                 particles = [ P.H, P.sq2, P.sq4__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq2] ], [ [P.g, P.sq2, P.sq4] ], [ [P.g, P.sq4] ] ],
                 couplings = {(0,0,0):C.UVGC_222_111,(0,0,2):C.UVGC_222_112,(0,0,1):C.UVGC_222_113})

V_237 = CTVertex(name = 'V_237',
                 type = 'UV',
                 particles = [ P.H, P.sq3, P.sq4__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq3] ], [ [P.g, P.sq3, P.sq4] ], [ [P.g, P.sq4] ] ],
                 couplings = {(0,0,0):C.UVGC_223_114,(0,0,2):C.UVGC_223_115,(0,0,1):C.UVGC_223_116})

V_238 = CTVertex(name = 'V_238',
                 type = 'UV',
                 particles = [ P.H, P.sq4__tilde__, P.sq4 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS2 ],
                 loop_particles = [ [ [P.g, P.sq4] ] ],
                 couplings = {(0,0,0):C.UVGC_200_95})

V_239 = CTVertex(name = 'V_239',
                 type = 'UV',
                 particles = [ P.bp1__tilde__, P.bp1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp1, P.g] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,2):C.UVGC_164_23,(0,1,0):C.UVGC_171_24,(0,1,1):C.UVGC_171_25,(0,1,3):C.UVGC_171_26,(0,1,4):C.UVGC_171_27,(0,1,5):C.UVGC_171_28,(0,1,6):C.UVGC_171_29,(0,1,7):C.UVGC_171_30,(0,1,8):C.UVGC_171_31,(0,1,9):C.UVGC_171_32,(0,1,10):C.UVGC_171_33,(0,1,11):C.UVGC_171_34,(0,1,12):C.UVGC_171_35,(0,1,13):C.UVGC_171_36,(0,1,14):C.UVGC_171_37,(0,1,15):C.UVGC_171_38,(0,1,16):C.UVGC_171_39,(0,1,2):C.UVGC_236_128})

V_240 = CTVertex(name = 'V_240',
                 type = 'UV',
                 particles = [ P.bp2__tilde__, P.bp2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp2, P.g] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,3):C.UVGC_164_23,(0,1,0):C.UVGC_171_24,(0,1,1):C.UVGC_171_25,(0,1,2):C.UVGC_171_26,(0,1,4):C.UVGC_171_27,(0,1,5):C.UVGC_171_28,(0,1,6):C.UVGC_171_29,(0,1,7):C.UVGC_171_30,(0,1,8):C.UVGC_171_31,(0,1,9):C.UVGC_171_32,(0,1,10):C.UVGC_171_33,(0,1,11):C.UVGC_171_34,(0,1,12):C.UVGC_171_35,(0,1,13):C.UVGC_171_36,(0,1,14):C.UVGC_171_37,(0,1,15):C.UVGC_171_38,(0,1,16):C.UVGC_171_39,(0,1,3):C.UVGC_245_141})

V_241 = CTVertex(name = 'V_241',
                 type = 'UV',
                 particles = [ P.bp3__tilde__, P.bp3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.bp3, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,4):C.UVGC_164_23,(0,1,0):C.UVGC_171_24,(0,1,1):C.UVGC_171_25,(0,1,2):C.UVGC_171_26,(0,1,3):C.UVGC_171_27,(0,1,5):C.UVGC_171_28,(0,1,6):C.UVGC_171_29,(0,1,7):C.UVGC_171_30,(0,1,8):C.UVGC_171_31,(0,1,9):C.UVGC_171_32,(0,1,10):C.UVGC_171_33,(0,1,11):C.UVGC_171_34,(0,1,12):C.UVGC_171_35,(0,1,13):C.UVGC_171_36,(0,1,14):C.UVGC_171_37,(0,1,15):C.UVGC_171_38,(0,1,16):C.UVGC_171_39,(0,1,4):C.UVGC_256_160})

V_242 = CTVertex(name = 'V_242',
                 type = 'UV',
                 particles = [ P.tp1__tilde__, P.tp1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.tp1] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,7):C.UVGC_164_23,(0,1,0):C.UVGC_171_24,(0,1,1):C.UVGC_171_25,(0,1,2):C.UVGC_171_26,(0,1,3):C.UVGC_171_27,(0,1,4):C.UVGC_171_28,(0,1,5):C.UVGC_171_29,(0,1,6):C.UVGC_171_30,(0,1,8):C.UVGC_171_31,(0,1,9):C.UVGC_171_32,(0,1,10):C.UVGC_171_33,(0,1,11):C.UVGC_171_34,(0,1,12):C.UVGC_171_35,(0,1,13):C.UVGC_171_36,(0,1,14):C.UVGC_171_37,(0,1,15):C.UVGC_171_38,(0,1,16):C.UVGC_171_39,(0,1,7):C.UVGC_281_198})

V_243 = CTVertex(name = 'V_243',
                 type = 'UV',
                 particles = [ P.tp2__tilde__, P.tp2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.tp2] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,7):C.UVGC_164_23,(0,1,0):C.UVGC_171_24,(0,1,1):C.UVGC_171_25,(0,1,2):C.UVGC_171_26,(0,1,3):C.UVGC_171_27,(0,1,4):C.UVGC_171_28,(0,1,5):C.UVGC_171_29,(0,1,6):C.UVGC_171_30,(0,1,8):C.UVGC_171_31,(0,1,9):C.UVGC_171_32,(0,1,10):C.UVGC_171_33,(0,1,11):C.UVGC_171_34,(0,1,12):C.UVGC_171_35,(0,1,13):C.UVGC_171_36,(0,1,14):C.UVGC_171_37,(0,1,15):C.UVGC_171_38,(0,1,16):C.UVGC_171_39,(0,1,7):C.UVGC_290_211})

V_244 = CTVertex(name = 'V_244',
                 type = 'UV',
                 particles = [ P.tp3__tilde__, P.tp3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.tp3] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,7):C.UVGC_164_23,(0,1,0):C.UVGC_171_24,(0,1,1):C.UVGC_171_25,(0,1,2):C.UVGC_171_26,(0,1,3):C.UVGC_171_27,(0,1,4):C.UVGC_171_28,(0,1,5):C.UVGC_171_29,(0,1,6):C.UVGC_171_30,(0,1,8):C.UVGC_171_31,(0,1,9):C.UVGC_171_32,(0,1,10):C.UVGC_171_33,(0,1,11):C.UVGC_171_34,(0,1,12):C.UVGC_171_35,(0,1,13):C.UVGC_171_36,(0,1,14):C.UVGC_171_37,(0,1,15):C.UVGC_171_38,(0,1,16):C.UVGC_171_39,(0,1,7):C.UVGC_301_230})

V_245 = CTVertex(name = 'V_245',
                 type = 'UV',
                 particles = [ P.tp4__tilde__, P.tp4, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.tp4] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,7):C.UVGC_164_23,(0,1,0):C.UVGC_171_24,(0,1,1):C.UVGC_171_25,(0,1,2):C.UVGC_171_26,(0,1,3):C.UVGC_171_27,(0,1,4):C.UVGC_171_28,(0,1,5):C.UVGC_171_29,(0,1,6):C.UVGC_171_30,(0,1,8):C.UVGC_171_31,(0,1,9):C.UVGC_171_32,(0,1,10):C.UVGC_171_33,(0,1,11):C.UVGC_171_34,(0,1,12):C.UVGC_171_35,(0,1,13):C.UVGC_171_36,(0,1,14):C.UVGC_171_37,(0,1,15):C.UVGC_171_38,(0,1,16):C.UVGC_171_39,(0,1,7):C.UVGC_320_350})

V_246 = CTVertex(name = 'V_246',
                 type = 'UV',
                 particles = [ P.g, P.sq1__tilde__, P.sq1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sq1] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_178_44,(0,0,1):C.UVGC_178_45,(0,0,2):C.UVGC_178_46,(0,0,3):C.UVGC_178_47,(0,0,4):C.UVGC_178_48,(0,0,5):C.UVGC_178_49,(0,0,6):C.UVGC_178_50,(0,0,8):C.UVGC_178_51,(0,0,9):C.UVGC_178_52,(0,0,10):C.UVGC_178_53,(0,0,11):C.UVGC_178_54,(0,0,12):C.UVGC_178_55,(0,0,13):C.UVGC_178_56,(0,0,14):C.UVGC_178_57,(0,0,15):C.UVGC_178_58,(0,0,16):C.UVGC_178_59,(0,0,7):C.UVGC_178_60})

V_247 = CTVertex(name = 'V_247',
                 type = 'UV',
                 particles = [ P.g, P.sq2__tilde__, P.sq2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sq2] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_178_44,(0,0,1):C.UVGC_178_45,(0,0,2):C.UVGC_178_46,(0,0,3):C.UVGC_178_47,(0,0,4):C.UVGC_178_48,(0,0,5):C.UVGC_178_49,(0,0,6):C.UVGC_178_50,(0,0,8):C.UVGC_178_51,(0,0,9):C.UVGC_178_52,(0,0,10):C.UVGC_178_53,(0,0,11):C.UVGC_178_54,(0,0,12):C.UVGC_178_55,(0,0,13):C.UVGC_178_56,(0,0,14):C.UVGC_178_57,(0,0,15):C.UVGC_178_58,(0,0,16):C.UVGC_178_59,(0,0,7):C.UVGC_185_82})

V_248 = CTVertex(name = 'V_248',
                 type = 'UV',
                 particles = [ P.g, P.sq3__tilde__, P.sq3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sq3] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_178_44,(0,0,1):C.UVGC_178_45,(0,0,2):C.UVGC_178_46,(0,0,3):C.UVGC_178_47,(0,0,4):C.UVGC_178_48,(0,0,5):C.UVGC_178_49,(0,0,6):C.UVGC_178_50,(0,0,8):C.UVGC_178_51,(0,0,9):C.UVGC_178_52,(0,0,10):C.UVGC_178_53,(0,0,11):C.UVGC_178_54,(0,0,12):C.UVGC_178_55,(0,0,13):C.UVGC_178_56,(0,0,14):C.UVGC_178_57,(0,0,15):C.UVGC_178_58,(0,0,16):C.UVGC_178_59,(0,0,7):C.UVGC_192_88})

V_249 = CTVertex(name = 'V_249',
                 type = 'UV',
                 particles = [ P.g, P.sq4__tilde__, P.sq4 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sq4] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_178_44,(0,0,1):C.UVGC_178_45,(0,0,2):C.UVGC_178_46,(0,0,3):C.UVGC_178_47,(0,0,4):C.UVGC_178_48,(0,0,5):C.UVGC_178_49,(0,0,6):C.UVGC_178_50,(0,0,8):C.UVGC_178_51,(0,0,9):C.UVGC_178_52,(0,0,10):C.UVGC_178_53,(0,0,11):C.UVGC_178_54,(0,0,12):C.UVGC_178_55,(0,0,13):C.UVGC_178_56,(0,0,14):C.UVGC_178_57,(0,0,15):C.UVGC_178_58,(0,0,16):C.UVGC_178_59,(0,0,7):C.UVGC_198_93})

V_250 = CTVertex(name = 'V_250',
                 type = 'UV',
                 particles = [ P.g, P.g, P.sq1__tilde__, P.sq1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sq1] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(2,0,0):C.UVGC_179_61,(2,0,1):C.UVGC_179_62,(2,0,2):C.UVGC_179_63,(2,0,3):C.UVGC_179_64,(2,0,4):C.UVGC_179_65,(2,0,5):C.UVGC_179_66,(2,0,6):C.UVGC_179_67,(2,0,8):C.UVGC_179_68,(2,0,9):C.UVGC_179_69,(2,0,10):C.UVGC_179_70,(2,0,11):C.UVGC_179_71,(2,0,12):C.UVGC_179_72,(2,0,13):C.UVGC_179_73,(2,0,14):C.UVGC_179_74,(2,0,15):C.UVGC_179_75,(2,0,16):C.UVGC_179_76,(2,0,7):C.UVGC_179_77,(1,0,0):C.UVGC_179_61,(1,0,1):C.UVGC_179_62,(1,0,2):C.UVGC_179_63,(1,0,3):C.UVGC_179_64,(1,0,4):C.UVGC_179_65,(1,0,5):C.UVGC_179_66,(1,0,6):C.UVGC_179_67,(1,0,8):C.UVGC_179_68,(1,0,9):C.UVGC_179_69,(1,0,10):C.UVGC_179_70,(1,0,11):C.UVGC_179_71,(1,0,12):C.UVGC_179_72,(1,0,13):C.UVGC_179_73,(1,0,14):C.UVGC_179_74,(1,0,15):C.UVGC_179_75,(1,0,16):C.UVGC_179_76,(1,0,7):C.UVGC_179_77,(0,0,5):C.UVGC_176_41,(0,0,7):C.UVGC_176_42})

V_251 = CTVertex(name = 'V_251',
                 type = 'UV',
                 particles = [ P.g, P.g, P.sq2__tilde__, P.sq2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sq2] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(2,0,0):C.UVGC_179_61,(2,0,1):C.UVGC_179_62,(2,0,2):C.UVGC_179_63,(2,0,3):C.UVGC_179_64,(2,0,4):C.UVGC_179_65,(2,0,5):C.UVGC_179_66,(2,0,6):C.UVGC_179_67,(2,0,8):C.UVGC_179_68,(2,0,9):C.UVGC_179_69,(2,0,10):C.UVGC_179_70,(2,0,11):C.UVGC_179_71,(2,0,12):C.UVGC_179_72,(2,0,13):C.UVGC_179_73,(2,0,14):C.UVGC_179_74,(2,0,15):C.UVGC_179_75,(2,0,16):C.UVGC_179_76,(2,0,7):C.UVGC_186_83,(1,0,0):C.UVGC_179_61,(1,0,1):C.UVGC_179_62,(1,0,2):C.UVGC_179_63,(1,0,3):C.UVGC_179_64,(1,0,4):C.UVGC_179_65,(1,0,5):C.UVGC_179_66,(1,0,6):C.UVGC_179_67,(1,0,8):C.UVGC_179_68,(1,0,9):C.UVGC_179_69,(1,0,10):C.UVGC_179_70,(1,0,11):C.UVGC_179_71,(1,0,12):C.UVGC_179_72,(1,0,13):C.UVGC_179_73,(1,0,14):C.UVGC_179_74,(1,0,15):C.UVGC_179_75,(1,0,16):C.UVGC_179_76,(1,0,7):C.UVGC_186_83,(0,0,5):C.UVGC_176_41,(0,0,7):C.UVGC_176_42})

V_252 = CTVertex(name = 'V_252',
                 type = 'UV',
                 particles = [ P.g, P.g, P.sq3__tilde__, P.sq3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sq3] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(2,0,0):C.UVGC_179_61,(2,0,1):C.UVGC_179_62,(2,0,2):C.UVGC_179_63,(2,0,3):C.UVGC_179_64,(2,0,4):C.UVGC_179_65,(2,0,5):C.UVGC_179_66,(2,0,6):C.UVGC_179_67,(2,0,8):C.UVGC_179_68,(2,0,9):C.UVGC_179_69,(2,0,10):C.UVGC_179_70,(2,0,11):C.UVGC_179_71,(2,0,12):C.UVGC_179_72,(2,0,13):C.UVGC_179_73,(2,0,14):C.UVGC_179_74,(2,0,15):C.UVGC_179_75,(2,0,16):C.UVGC_179_76,(2,0,7):C.UVGC_193_89,(1,0,0):C.UVGC_179_61,(1,0,1):C.UVGC_179_62,(1,0,2):C.UVGC_179_63,(1,0,3):C.UVGC_179_64,(1,0,4):C.UVGC_179_65,(1,0,5):C.UVGC_179_66,(1,0,6):C.UVGC_179_67,(1,0,8):C.UVGC_179_68,(1,0,9):C.UVGC_179_69,(1,0,10):C.UVGC_179_70,(1,0,11):C.UVGC_179_71,(1,0,12):C.UVGC_179_72,(1,0,13):C.UVGC_179_73,(1,0,14):C.UVGC_179_74,(1,0,15):C.UVGC_179_75,(1,0,16):C.UVGC_179_76,(1,0,7):C.UVGC_193_89,(0,0,5):C.UVGC_176_41,(0,0,7):C.UVGC_176_42})

V_253 = CTVertex(name = 'V_253',
                 type = 'UV',
                 particles = [ P.g, P.g, P.sq4__tilde__, P.sq4 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.sq4] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(2,0,0):C.UVGC_179_61,(2,0,1):C.UVGC_179_62,(2,0,2):C.UVGC_179_63,(2,0,3):C.UVGC_179_64,(2,0,4):C.UVGC_179_65,(2,0,5):C.UVGC_179_66,(2,0,6):C.UVGC_179_67,(2,0,8):C.UVGC_179_68,(2,0,9):C.UVGC_179_69,(2,0,10):C.UVGC_179_70,(2,0,11):C.UVGC_179_71,(2,0,12):C.UVGC_179_72,(2,0,13):C.UVGC_179_73,(2,0,14):C.UVGC_179_74,(2,0,15):C.UVGC_179_75,(2,0,16):C.UVGC_179_76,(2,0,7):C.UVGC_199_94,(1,0,0):C.UVGC_179_61,(1,0,1):C.UVGC_179_62,(1,0,2):C.UVGC_179_63,(1,0,3):C.UVGC_179_64,(1,0,4):C.UVGC_179_65,(1,0,5):C.UVGC_179_66,(1,0,6):C.UVGC_179_67,(1,0,8):C.UVGC_179_68,(1,0,9):C.UVGC_179_69,(1,0,10):C.UVGC_179_70,(1,0,11):C.UVGC_179_71,(1,0,12):C.UVGC_179_72,(1,0,13):C.UVGC_179_73,(1,0,14):C.UVGC_179_74,(1,0,15):C.UVGC_179_75,(1,0,16):C.UVGC_179_76,(1,0,7):C.UVGC_199_94,(0,0,5):C.UVGC_176_41,(0,0,7):C.UVGC_176_42})

V_254 = CTVertex(name = 'V_254',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV7 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_147_4})

V_255 = CTVertex(name = 'V_255',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV7 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_147_4})

V_256 = CTVertex(name = 'V_256',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4, L.FFV8 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_147_4,(0,1,0):C.UVGC_270_186})

V_257 = CTVertex(name = 'V_257',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_163_22,(0,1,0):C.UVGC_149_5,(0,2,0):C.UVGC_149_5})

V_258 = CTVertex(name = 'V_258',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_163_22,(0,1,0):C.UVGC_149_5,(0,2,0):C.UVGC_149_5})

V_259 = CTVertex(name = 'V_259',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_163_22,(0,1,0):C.UVGC_226_118,(0,2,0):C.UVGC_226_118})

V_260 = CTVertex(name = 'V_260',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,7):C.UVGC_164_23,(0,1,0):C.UVGC_171_24,(0,1,1):C.UVGC_171_25,(0,1,2):C.UVGC_171_26,(0,1,3):C.UVGC_171_27,(0,1,4):C.UVGC_171_28,(0,1,5):C.UVGC_171_29,(0,1,6):C.UVGC_171_30,(0,1,8):C.UVGC_171_31,(0,1,9):C.UVGC_171_32,(0,1,10):C.UVGC_171_33,(0,1,11):C.UVGC_171_34,(0,1,12):C.UVGC_171_35,(0,1,13):C.UVGC_171_36,(0,1,14):C.UVGC_171_37,(0,1,15):C.UVGC_171_38,(0,1,16):C.UVGC_171_39,(0,1,7):C.UVGC_171_40,(0,2,0):C.UVGC_171_24,(0,2,1):C.UVGC_171_25,(0,2,2):C.UVGC_171_26,(0,2,3):C.UVGC_171_27,(0,2,4):C.UVGC_171_28,(0,2,5):C.UVGC_171_29,(0,2,6):C.UVGC_171_30,(0,2,8):C.UVGC_171_31,(0,2,9):C.UVGC_171_32,(0,2,10):C.UVGC_171_33,(0,2,11):C.UVGC_171_34,(0,2,12):C.UVGC_171_35,(0,2,13):C.UVGC_171_36,(0,2,14):C.UVGC_171_37,(0,2,15):C.UVGC_171_38,(0,2,16):C.UVGC_171_39,(0,2,7):C.UVGC_171_40})

V_261 = CTVertex(name = 'V_261',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,5):C.UVGC_164_23,(0,1,0):C.UVGC_171_24,(0,1,1):C.UVGC_171_25,(0,1,2):C.UVGC_171_26,(0,1,3):C.UVGC_171_27,(0,1,4):C.UVGC_171_28,(0,1,6):C.UVGC_171_29,(0,1,7):C.UVGC_171_30,(0,1,8):C.UVGC_171_31,(0,1,9):C.UVGC_171_32,(0,1,10):C.UVGC_171_33,(0,1,11):C.UVGC_171_34,(0,1,12):C.UVGC_171_35,(0,1,13):C.UVGC_171_36,(0,1,14):C.UVGC_171_37,(0,1,15):C.UVGC_171_38,(0,1,16):C.UVGC_171_39,(0,1,5):C.UVGC_171_40,(0,2,0):C.UVGC_171_24,(0,2,1):C.UVGC_171_25,(0,2,2):C.UVGC_171_26,(0,2,3):C.UVGC_171_27,(0,2,4):C.UVGC_171_28,(0,2,6):C.UVGC_171_29,(0,2,7):C.UVGC_171_30,(0,2,8):C.UVGC_171_31,(0,2,9):C.UVGC_171_32,(0,2,10):C.UVGC_171_33,(0,2,11):C.UVGC_171_34,(0,2,12):C.UVGC_171_35,(0,2,13):C.UVGC_171_36,(0,2,14):C.UVGC_171_37,(0,2,15):C.UVGC_171_38,(0,2,16):C.UVGC_171_39,(0,2,5):C.UVGC_171_40})

V_262 = CTVertex(name = 'V_262',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,7):C.UVGC_164_23,(0,1,0):C.UVGC_171_24,(0,1,1):C.UVGC_171_25,(0,1,2):C.UVGC_171_26,(0,1,3):C.UVGC_171_27,(0,1,4):C.UVGC_171_28,(0,1,5):C.UVGC_171_29,(0,1,6):C.UVGC_171_30,(0,1,8):C.UVGC_171_31,(0,1,9):C.UVGC_171_32,(0,1,10):C.UVGC_171_33,(0,1,11):C.UVGC_171_34,(0,1,12):C.UVGC_171_35,(0,1,13):C.UVGC_171_36,(0,1,14):C.UVGC_171_37,(0,1,15):C.UVGC_171_38,(0,1,16):C.UVGC_171_39,(0,1,7):C.UVGC_271_187,(0,2,0):C.UVGC_171_24,(0,2,1):C.UVGC_171_25,(0,2,2):C.UVGC_171_26,(0,2,3):C.UVGC_171_27,(0,2,4):C.UVGC_171_28,(0,2,5):C.UVGC_171_29,(0,2,6):C.UVGC_171_30,(0,2,8):C.UVGC_171_31,(0,2,9):C.UVGC_171_32,(0,2,10):C.UVGC_171_33,(0,2,11):C.UVGC_171_34,(0,2,12):C.UVGC_171_35,(0,2,13):C.UVGC_171_36,(0,2,14):C.UVGC_171_37,(0,2,15):C.UVGC_171_38,(0,2,16):C.UVGC_171_39,(0,2,7):C.UVGC_271_187})

V_263 = CTVertex(name = 'V_263',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,5):C.UVGC_164_23,(0,1,0):C.UVGC_171_24,(0,1,1):C.UVGC_171_25,(0,1,2):C.UVGC_171_26,(0,1,3):C.UVGC_171_27,(0,1,4):C.UVGC_171_28,(0,1,6):C.UVGC_171_29,(0,1,7):C.UVGC_171_30,(0,1,8):C.UVGC_171_31,(0,1,9):C.UVGC_171_32,(0,1,10):C.UVGC_171_33,(0,1,11):C.UVGC_171_34,(0,1,12):C.UVGC_171_35,(0,1,13):C.UVGC_171_36,(0,1,14):C.UVGC_171_37,(0,1,15):C.UVGC_171_38,(0,1,16):C.UVGC_171_39,(0,1,5):C.UVGC_171_40,(0,2,0):C.UVGC_171_24,(0,2,1):C.UVGC_171_25,(0,2,2):C.UVGC_171_26,(0,2,3):C.UVGC_171_27,(0,2,4):C.UVGC_171_28,(0,2,6):C.UVGC_171_29,(0,2,7):C.UVGC_171_30,(0,2,8):C.UVGC_171_31,(0,2,9):C.UVGC_171_32,(0,2,10):C.UVGC_171_33,(0,2,11):C.UVGC_171_34,(0,2,12):C.UVGC_171_35,(0,2,13):C.UVGC_171_36,(0,2,14):C.UVGC_171_37,(0,2,15):C.UVGC_171_38,(0,2,16):C.UVGC_171_39,(0,2,5):C.UVGC_171_40})

V_264 = CTVertex(name = 'V_264',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,7):C.UVGC_164_23,(0,1,0):C.UVGC_171_24,(0,1,1):C.UVGC_171_25,(0,1,2):C.UVGC_171_26,(0,1,3):C.UVGC_171_27,(0,1,4):C.UVGC_171_28,(0,1,5):C.UVGC_171_29,(0,1,6):C.UVGC_171_30,(0,1,8):C.UVGC_171_31,(0,1,9):C.UVGC_171_32,(0,1,10):C.UVGC_171_33,(0,1,11):C.UVGC_171_34,(0,1,12):C.UVGC_171_35,(0,1,13):C.UVGC_171_36,(0,1,14):C.UVGC_171_37,(0,1,15):C.UVGC_171_38,(0,1,16):C.UVGC_171_39,(0,1,7):C.UVGC_171_40,(0,2,0):C.UVGC_171_24,(0,2,1):C.UVGC_171_25,(0,2,2):C.UVGC_171_26,(0,2,3):C.UVGC_171_27,(0,2,4):C.UVGC_171_28,(0,2,5):C.UVGC_171_29,(0,2,6):C.UVGC_171_30,(0,2,8):C.UVGC_171_31,(0,2,9):C.UVGC_171_32,(0,2,10):C.UVGC_171_33,(0,2,11):C.UVGC_171_34,(0,2,12):C.UVGC_171_35,(0,2,13):C.UVGC_171_36,(0,2,14):C.UVGC_171_37,(0,2,15):C.UVGC_171_38,(0,2,16):C.UVGC_171_39,(0,2,7):C.UVGC_171_40})

V_265 = CTVertex(name = 'V_265',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV4, L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,0,4):C.UVGC_164_23,(0,1,0):C.UVGC_171_24,(0,1,1):C.UVGC_171_25,(0,1,2):C.UVGC_171_26,(0,1,3):C.UVGC_171_27,(0,1,5):C.UVGC_171_28,(0,1,6):C.UVGC_171_29,(0,1,7):C.UVGC_171_30,(0,1,8):C.UVGC_171_31,(0,1,9):C.UVGC_171_32,(0,1,10):C.UVGC_171_33,(0,1,11):C.UVGC_171_34,(0,1,12):C.UVGC_171_35,(0,1,13):C.UVGC_171_36,(0,1,14):C.UVGC_171_37,(0,1,15):C.UVGC_171_38,(0,1,16):C.UVGC_171_39,(0,1,4):C.UVGC_227_119,(0,2,0):C.UVGC_171_24,(0,2,1):C.UVGC_171_25,(0,2,2):C.UVGC_171_26,(0,2,3):C.UVGC_171_27,(0,2,5):C.UVGC_171_28,(0,2,6):C.UVGC_171_29,(0,2,7):C.UVGC_171_30,(0,2,8):C.UVGC_171_31,(0,2,9):C.UVGC_171_32,(0,2,10):C.UVGC_171_33,(0,2,11):C.UVGC_171_34,(0,2,12):C.UVGC_171_35,(0,2,13):C.UVGC_171_36,(0,2,14):C.UVGC_171_37,(0,2,15):C.UVGC_171_38,(0,2,16):C.UVGC_171_39,(0,2,4):C.UVGC_227_119})

V_266 = CTVertex(name = 'V_266',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_217_97,(0,0,1):C.UVGC_217_98})

V_267 = CTVertex(name = 'V_267',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_217_97,(0,0,1):C.UVGC_217_98})

V_268 = CTVertex(name = 'V_268',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_275_191,(0,0,2):C.UVGC_275_192,(0,0,1):C.UVGC_217_98})

V_269 = CTVertex(name = 'V_269',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_217_97,(0,0,1):C.UVGC_217_98})

V_270 = CTVertex(name = 'V_270',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_217_97,(0,0,1):C.UVGC_217_98})

V_271 = CTVertex(name = 'V_271',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_275_191,(0,0,2):C.UVGC_275_192,(0,0,1):C.UVGC_217_98})

V_272 = CTVertex(name = 'V_272',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_276_193,(0,1,0):C.UVGC_277_194})

V_273 = CTVertex(name = 'V_273',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_231_123,(0,1,0):C.UVGC_232_124})

V_274 = CTVertex(name = 'V_274',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_214_96,(0,1,0):C.UVGC_146_3,(0,2,0):C.UVGC_146_3})

V_275 = CTVertex(name = 'V_275',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF6 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_146_3})

V_276 = CTVertex(name = 'V_276',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_274_190,(0,1,0):C.UVGC_269_185})

V_277 = CTVertex(name = 'V_277',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF6 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_146_3})

V_278 = CTVertex(name = 'V_278',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF6 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_146_3})

V_279 = CTVertex(name = 'V_279',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_230_122,(0,1,0):C.UVGC_225_117})

V_280 = CTVertex(name = 'V_280',
                 type = 'UV',
                 particles = [ P.tp1__tilde__, P.tp1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp1] ] ],
                 couplings = {(0,0,0):C.UVGC_287_208,(0,1,0):C.UVGC_279_196})

V_281 = CTVertex(name = 'V_281',
                 type = 'UV',
                 particles = [ P.tp2__tilde__, P.tp2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp2] ] ],
                 couplings = {(0,0,0):C.UVGC_298_227,(0,1,0):C.UVGC_288_209})

V_282 = CTVertex(name = 'V_282',
                 type = 'UV',
                 particles = [ P.tp3__tilde__, P.tp3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp3] ] ],
                 couplings = {(0,0,0):C.UVGC_309_250,(0,1,0):C.UVGC_299_228})

V_283 = CTVertex(name = 'V_283',
                 type = 'UV',
                 particles = [ P.tp4__tilde__, P.tp4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.tp4] ] ],
                 couplings = {(0,0,0):C.UVGC_330_376,(0,1,0):C.UVGC_318_348})

V_284 = CTVertex(name = 'V_284',
                 type = 'UV',
                 particles = [ P.bp1__tilde__, P.bp1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.bp1, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_242_138,(0,1,0):C.UVGC_234_126})

V_285 = CTVertex(name = 'V_285',
                 type = 'UV',
                 particles = [ P.bp2__tilde__, P.bp2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.bp2, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_253_157,(0,1,0):C.UVGC_243_139})

V_286 = CTVertex(name = 'V_286',
                 type = 'UV',
                 particles = [ P.bp3__tilde__, P.bp3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.bp3, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_264_180,(0,1,0):C.UVGC_254_158})

V_287 = CTVertex(name = 'V_287',
                 type = 'UV',
                 particles = [ P.sq1__tilde__, P.sq1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.sq1] ] ],
                 couplings = {(0,0,0):C.UVGC_265_181,(0,1,0):C.UVGC_177_43})

V_288 = CTVertex(name = 'V_288',
                 type = 'UV',
                 particles = [ P.sq2__tilde__, P.sq2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.sq2] ] ],
                 couplings = {(0,0,0):C.UVGC_266_182,(0,1,0):C.UVGC_184_81})

V_289 = CTVertex(name = 'V_289',
                 type = 'UV',
                 particles = [ P.sq3__tilde__, P.sq3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.sq3] ] ],
                 couplings = {(0,0,0):C.UVGC_267_183,(0,1,0):C.UVGC_191_87})

V_290 = CTVertex(name = 'V_290',
                 type = 'UV',
                 particles = [ P.sq4__tilde__, P.sq4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.sq4] ] ],
                 couplings = {(0,0,0):C.UVGC_268_184,(0,1,0):C.UVGC_197_92})

V_291 = CTVertex(name = 'V_291',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.bp1] ], [ [P.bp2] ], [ [P.bp3] ], [ [P.g] ], [ [P.ghG] ], [ [P.sq1] ], [ [P.sq2] ], [ [P.sq3] ], [ [P.sq4] ], [ [P.t] ], [ [P.tp1] ], [ [P.tp2] ], [ [P.tp3] ], [ [P.tp4] ] ],
                 couplings = {(0,1,0):C.UVGC_310_251,(0,1,1):C.UVGC_310_252,(0,1,2):C.UVGC_310_253,(0,1,3):C.UVGC_310_254,(0,1,6):C.UVGC_310_255,(0,1,7):C.UVGC_310_256,(0,1,8):C.UVGC_310_257,(0,1,9):C.UVGC_310_258,(0,1,10):C.UVGC_310_259,(0,1,11):C.UVGC_310_260,(0,1,12):C.UVGC_310_261,(0,1,13):C.UVGC_310_262,(0,1,14):C.UVGC_310_263,(0,0,4):C.UVGC_154_6,(0,0,5):C.UVGC_154_7})

