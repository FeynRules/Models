# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.1 for Linux x86 (64-bit) (January 27, 2023)
# Date: Mon 21 Sep 2026 20:49:52



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
m2Eta = Parameter(name = 'm2Eta',
                  nature = 'external',
                  type = 'real',
                  value = 22500.,
                  texname = '\\text{m2Eta}',
                  lhablock = 'SCOTOINERT',
                  lhacode = [ 1 ])

lam2Eta = Parameter(name = 'lam2Eta',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{lam2Eta}',
                    lhablock = 'SCOTOINERT',
                    lhacode = [ 2 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.955,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.000011663785,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.118,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

YeN1 = Parameter(name = 'YeN1',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\text{YeN1}',
                 lhablock = 'YSCOTO',
                 lhacode = [ 1 ])

YeN2 = Parameter(name = 'YeN2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{YeN2}',
                 lhablock = 'YSCOTO',
                 lhacode = [ 2 ])

YeN3 = Parameter(name = 'YeN3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{YeN3}',
                 lhablock = 'YSCOTO',
                 lhacode = [ 3 ])

YmuN1 = Parameter(name = 'YmuN1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{YmuN1}',
                  lhablock = 'YSCOTO',
                  lhacode = [ 4 ])

YmuN2 = Parameter(name = 'YmuN2',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{YmuN2}',
                  lhablock = 'YSCOTO',
                  lhacode = [ 5 ])

YmuN3 = Parameter(name = 'YmuN3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{YmuN3}',
                  lhablock = 'YSCOTO',
                  lhacode = [ 6 ])

YtaN1 = Parameter(name = 'YtaN1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{YtaN1}',
                  lhablock = 'YSCOTO',
                  lhacode = [ 7 ])

YtaN2 = Parameter(name = 'YtaN2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{YtaN2}',
                  lhablock = 'YSCOTO',
                  lhacode = [ 8 ])

YtaN3 = Parameter(name = 'YtaN3',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\text{YtaN3}',
                  lhablock = 'YSCOTO',
                  lhacode = [ 9 ])

deN1 = Parameter(name = 'deN1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{deN1}',
                 lhablock = 'YSCOTOPHASE',
                 lhacode = [ 1 ])

deN2 = Parameter(name = 'deN2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{deN2}',
                 lhablock = 'YSCOTOPHASE',
                 lhacode = [ 2 ])

deN3 = Parameter(name = 'deN3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{deN3}',
                 lhablock = 'YSCOTOPHASE',
                 lhacode = [ 3 ])

dmuN1 = Parameter(name = 'dmuN1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{dmuN1}',
                  lhablock = 'YSCOTOPHASE',
                  lhacode = [ 4 ])

dmuN2 = Parameter(name = 'dmuN2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{dmuN2}',
                  lhablock = 'YSCOTOPHASE',
                  lhacode = [ 5 ])

dmuN3 = Parameter(name = 'dmuN3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{dmuN3}',
                  lhablock = 'YSCOTOPHASE',
                  lhacode = [ 6 ])

dtaN1 = Parameter(name = 'dtaN1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{dtaN1}',
                  lhablock = 'YSCOTOPHASE',
                  lhacode = [ 7 ])

dtaN2 = Parameter(name = 'dtaN2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{dtaN2}',
                  lhablock = 'YSCOTOPHASE',
                  lhacode = [ 8 ])

dtaN3 = Parameter(name = 'dtaN3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{dtaN3}',
                  lhablock = 'YSCOTOPHASE',
                  lhacode = [ 9 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172.6,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1879,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172.6,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.13,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MetaR = Parameter(name = 'MetaR',
                  nature = 'external',
                  type = 'real',
                  value = 153.9886,
                  texname = '\\text{MetaR}',
                  lhablock = 'MASS',
                  lhacode = [ 9900035 ])

MetaI = Parameter(name = 'MetaI',
                  nature = 'external',
                  type = 'real',
                  value = 155.9447,
                  texname = '\\text{MetaI}',
                  lhablock = 'MASS',
                  lhacode = [ 9900036 ])

Metap = Parameter(name = 'Metap',
                  nature = 'external',
                  type = 'real',
                  value = 159.7849,
                  texname = '\\text{Metap}',
                  lhablock = 'MASS',
                  lhacode = [ 9900037 ])

MN1 = Parameter(name = 'MN1',
                nature = 'external',
                type = 'real',
                value = 300.,
                texname = '\\text{MN1}',
                lhablock = 'MASS',
                lhacode = [ 9900012 ])

MN2 = Parameter(name = 'MN2',
                nature = 'external',
                type = 'real',
                value = 500.,
                texname = '\\text{MN2}',
                lhablock = 'MASS',
                lhacode = [ 9900014 ])

MN3 = Parameter(name = 'MN3',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{MN3}',
                lhablock = 'MASS',
                lhacode = [ 9900016 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4955,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.14,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.42,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.003,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WetaR = Parameter(name = 'WetaR',
                  nature = 'external',
                  type = 'real',
                  value = 10.,
                  texname = '\\text{WetaR}',
                  lhablock = 'DECAY',
                  lhacode = [ 9900035 ])

WetaI = Parameter(name = 'WetaI',
                  nature = 'external',
                  type = 'real',
                  value = 10.,
                  texname = '\\text{WetaI}',
                  lhablock = 'DECAY',
                  lhacode = [ 9900036 ])

WetaP = Parameter(name = 'WetaP',
                  nature = 'external',
                  type = 'real',
                  value = 10.,
                  texname = '\\text{WetaP}',
                  lhablock = 'DECAY',
                  lhacode = [ 9900037 ])

WN1 = Parameter(name = 'WN1',
                nature = 'external',
                type = 'real',
                value = 6.3e-8,
                texname = '\\text{WN1}',
                lhablock = 'DECAY',
                lhacode = [ 9900012 ])

WN2 = Parameter(name = 'WN2',
                nature = 'external',
                type = 'real',
                value = 1.6e-7,
                texname = '\\text{WN2}',
                lhablock = 'DECAY',
                lhacode = [ 9900014 ])

WN3 = Parameter(name = 'WN3',
                nature = 'external',
                type = 'real',
                value = 3.8e-7,
                texname = '\\text{WN3}',
                lhablock = 'DECAY',
                lhacode = [ 9900016 ])

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

Ysc1x1 = Parameter(name = 'Ysc1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'YeN1*cmath.exp(deN1*complex(0,1))',
                   texname = '\\text{Ysc1x1}')

Ysc1x2 = Parameter(name = 'Ysc1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'YeN2*cmath.exp(deN2*complex(0,1))',
                   texname = '\\text{Ysc1x2}')

Ysc1x3 = Parameter(name = 'Ysc1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'YeN3*cmath.exp(deN3*complex(0,1))',
                   texname = '\\text{Ysc1x3}')

Ysc2x1 = Parameter(name = 'Ysc2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'YmuN1*cmath.exp(dmuN1*complex(0,1))',
                   texname = '\\text{Ysc2x1}')

Ysc2x2 = Parameter(name = 'Ysc2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'YmuN2*cmath.exp(dmuN2*complex(0,1))',
                   texname = '\\text{Ysc2x2}')

Ysc2x3 = Parameter(name = 'Ysc2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'YmuN3*cmath.exp(dmuN3*complex(0,1))',
                   texname = '\\text{Ysc2x3}')

Ysc3x1 = Parameter(name = 'Ysc3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'YtaN1*cmath.exp(dtaN1*complex(0,1))',
                   texname = '\\text{Ysc3x1}')

Ysc3x2 = Parameter(name = 'Ysc3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'YtaN2*cmath.exp(dtaN2*complex(0,1))',
                   texname = '\\text{Ysc3x2}')

Ysc3x3 = Parameter(name = 'Ysc3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'YtaN3*cmath.exp(dtaN3*complex(0,1))',
                   texname = '\\text{Ysc3x3}')

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

lam3Eta = Parameter(name = 'lam3Eta',
                    nature = 'internal',
                    type = 'real',
                    value = '(2*(-m2Eta + Metap**2))/vev**2',
                    texname = '\\text{lam3Eta}')

lam4Eta = Parameter(name = 'lam4Eta',
                    nature = 'internal',
                    type = 'real',
                    value = '(MetaI**2 - 2*Metap**2 + MetaR**2)/vev**2',
                    texname = '\\text{lam4Eta}')

lam5Eta = Parameter(name = 'lam5Eta',
                    nature = 'internal',
                    type = 'real',
                    value = '(-MetaI**2 + MetaR**2)/vev**2',
                    texname = '\\text{lam5Eta}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

lambdaL = Parameter(name = 'lambdaL',
                    nature = 'internal',
                    type = 'real',
                    value = '(lam3Eta + lam4Eta + lam5Eta)/2.',
                    texname = '\\text{lambdaL}')

