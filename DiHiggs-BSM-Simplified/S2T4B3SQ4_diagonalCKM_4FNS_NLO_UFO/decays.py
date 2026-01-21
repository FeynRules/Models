# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 13.2.0 for Linux x86 (64-bit) (December 7, 2022)
# Date: Thu 13 Apr 2023 07:48:10


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.H,P.bp1):'((3*KHBSML1**2*MB**2 + 3*KHBSMR1**2*MB**2 + 12*KHBSML1*KHBSMR1*MB*MBP1 + 3*KHBSML1**2*MBP1**2 + 3*KHBSMR1**2*MBP1**2 - 3*KHBSML1**2*MH**2 - 3*KHBSMR1**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP1**2 + MBP1**4 - 2*MB**2*MH**2 - 2*MBP1**2*MH**2 + MH**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.H,P.bp2):'((3*KHBSML2**2*MB**2 + 3*KHBSMR2**2*MB**2 + 12*KHBSML2*KHBSMR2*MB*MBP2 + 3*KHBSML2**2*MBP2**2 + 3*KHBSMR2**2*MBP2**2 - 3*KHBSML2**2*MH**2 - 3*KHBSMR2**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP2**2 + MBP2**4 - 2*MB**2*MH**2 - 2*MBP2**2*MH**2 + MH**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.H,P.bp3):'((3*KHBSML3**2*MB**2 + 3*KHBSMR3**2*MB**2 + 12*KHBSML3*KHBSMR3*MB*MBP3 + 3*KHBSML3**2*MBP3**2 + 3*KHBSMR3**2*MBP3**2 - 3*KHBSML3**2*MH**2 - 3*KHBSMR3**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP3**2 + MBP3**4 - 2*MB**2*MH**2 - 2*MBP3**2*MH**2 + MH**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_bp1 = Decay(name = 'Decay_bp1',
                  particle = P.bp1,
                  partial_widths = {(P.H,P.b):'((3*KHBSML1**2*MB**2 + 3*KHBSMR1**2*MB**2 + 12*KHBSML1*KHBSMR1*MB*MBP1 + 3*KHBSML1**2*MBP1**2 + 3*KHBSMR1**2*MBP1**2 - 3*KHBSML1**2*MH**2 - 3*KHBSMR1**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP1**2 + MBP1**4 - 2*MB**2*MH**2 - 2*MBP1**2*MH**2 + MH**4))/(96.*cmath.pi*abs(MBP1)**3)',
                                    (P.H,P.bp2):'((3*KHBPBP1x2**2*MBP1**2 + 3*KHBPBP2x1**2*MBP1**2 + 12*KHBPBP1x2*KHBPBP2x1*MBP1*MBP2 + 3*KHBPBP1x2**2*MBP2**2 + 3*KHBPBP2x1**2*MBP2**2 - 3*KHBPBP1x2**2*MH**2 - 3*KHBPBP2x1**2*MH**2)*cmath.sqrt(MBP1**4 - 2*MBP1**2*MBP2**2 + MBP2**4 - 2*MBP1**2*MH**2 - 2*MBP2**2*MH**2 + MH**4))/(96.*cmath.pi*abs(MBP1)**3)',
                                    (P.H,P.bp3):'((3*KHBPBP1x3**2*MBP1**2 + 3*KHBPBP3x1**2*MBP1**2 + 12*KHBPBP1x3*KHBPBP3x1*MBP1*MBP3 + 3*KHBPBP1x3**2*MBP3**2 + 3*KHBPBP3x1**2*MBP3**2 - 3*KHBPBP1x3**2*MH**2 - 3*KHBPBP3x1**2*MH**2)*cmath.sqrt(MBP1**4 - 2*MBP1**2*MBP3**2 + MBP3**4 - 2*MBP1**2*MH**2 - 2*MBP3**2*MH**2 + MH**4))/(96.*cmath.pi*abs(MBP1)**3)'})

Decay_bp2 = Decay(name = 'Decay_bp2',
                  particle = P.bp2,
                  partial_widths = {(P.H,P.b):'((3*KHBSML2**2*MB**2 + 3*KHBSMR2**2*MB**2 + 12*KHBSML2*KHBSMR2*MB*MBP2 + 3*KHBSML2**2*MBP2**2 + 3*KHBSMR2**2*MBP2**2 - 3*KHBSML2**2*MH**2 - 3*KHBSMR2**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP2**2 + MBP2**4 - 2*MB**2*MH**2 - 2*MBP2**2*MH**2 + MH**4))/(96.*cmath.pi*abs(MBP2)**3)',
                                    (P.H,P.bp1):'((3*KHBPBP1x2**2*MBP1**2 + 3*KHBPBP2x1**2*MBP1**2 + 12*KHBPBP1x2*KHBPBP2x1*MBP1*MBP2 + 3*KHBPBP1x2**2*MBP2**2 + 3*KHBPBP2x1**2*MBP2**2 - 3*KHBPBP1x2**2*MH**2 - 3*KHBPBP2x1**2*MH**2)*cmath.sqrt(MBP1**4 - 2*MBP1**2*MBP2**2 + MBP2**4 - 2*MBP1**2*MH**2 - 2*MBP2**2*MH**2 + MH**4))/(96.*cmath.pi*abs(MBP2)**3)',
                                    (P.H,P.bp3):'((3*KHBPBP2x3**2*MBP2**2 + 3*KHBPBP3x2**2*MBP2**2 + 12*KHBPBP2x3*KHBPBP3x2*MBP2*MBP3 + 3*KHBPBP2x3**2*MBP3**2 + 3*KHBPBP3x2**2*MBP3**2 - 3*KHBPBP2x3**2*MH**2 - 3*KHBPBP3x2**2*MH**2)*cmath.sqrt(MBP2**4 - 2*MBP2**2*MBP3**2 + MBP3**4 - 2*MBP2**2*MH**2 - 2*MBP3**2*MH**2 + MH**4))/(96.*cmath.pi*abs(MBP2)**3)'})

Decay_bp3 = Decay(name = 'Decay_bp3',
                  particle = P.bp3,
                  partial_widths = {(P.H,P.b):'((3*KHBSML3**2*MB**2 + 3*KHBSMR3**2*MB**2 + 12*KHBSML3*KHBSMR3*MB*MBP3 + 3*KHBSML3**2*MBP3**2 + 3*KHBSMR3**2*MBP3**2 - 3*KHBSML3**2*MH**2 - 3*KHBSMR3**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP3**2 + MBP3**4 - 2*MB**2*MH**2 - 2*MBP3**2*MH**2 + MH**4))/(96.*cmath.pi*abs(MBP3)**3)',
                                    (P.H,P.bp1):'((3*KHBPBP1x3**2*MBP1**2 + 3*KHBPBP3x1**2*MBP1**2 + 12*KHBPBP1x3*KHBPBP3x1*MBP1*MBP3 + 3*KHBPBP1x3**2*MBP3**2 + 3*KHBPBP3x1**2*MBP3**2 - 3*KHBPBP1x3**2*MH**2 - 3*KHBPBP3x1**2*MH**2)*cmath.sqrt(MBP1**4 - 2*MBP1**2*MBP3**2 + MBP3**4 - 2*MBP1**2*MH**2 - 2*MBP3**2*MH**2 + MH**4))/(96.*cmath.pi*abs(MBP3)**3)',
                                    (P.H,P.bp2):'((3*KHBPBP2x3**2*MBP2**2 + 3*KHBPBP3x2**2*MBP2**2 + 12*KHBPBP2x3*KHBPBP3x2*MBP2*MBP3 + 3*KHBPBP2x3**2*MBP3**2 + 3*KHBPBP3x2**2*MBP3**2 - 3*KHBPBP2x3**2*MH**2 - 3*KHBPBP3x2**2*MH**2)*cmath.sqrt(MBP2**4 - 2*MBP2**2*MBP3**2 + MBP3**4 - 2*MBP2**2*MH**2 - 2*MBP3**2*MH**2 + MH**4))/(96.*cmath.pi*abs(MBP3)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*KHBB**2*MB**2 + 3*KHBB**2*MH**2 - 24*KHBB*MB**2*yb + 6*KHBB*MH**2*yb - 12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.b,P.bp1__tilde__):'((-3*KHBSML1**2*MB**2 - 3*KHBSMR1**2*MB**2 - 12*KHBSML1*KHBSMR1*MB*MBP1 - 3*KHBSML1**2*MBP1**2 - 3*KHBSMR1**2*MBP1**2 + 3*KHBSML1**2*MH**2 + 3*KHBSMR1**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP1**2 + MBP1**4 - 2*MB**2*MH**2 - 2*MBP1**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.b,P.bp2__tilde__):'((-3*KHBSML2**2*MB**2 - 3*KHBSMR2**2*MB**2 - 12*KHBSML2*KHBSMR2*MB*MBP2 - 3*KHBSML2**2*MBP2**2 - 3*KHBSMR2**2*MBP2**2 + 3*KHBSML2**2*MH**2 + 3*KHBSMR2**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP2**2 + MBP2**4 - 2*MB**2*MH**2 - 2*MBP2**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.b,P.bp3__tilde__):'((-3*KHBSML3**2*MB**2 - 3*KHBSMR3**2*MB**2 - 12*KHBSML3*KHBSMR3*MB*MBP3 - 3*KHBSML3**2*MBP3**2 - 3*KHBSMR3**2*MBP3**2 + 3*KHBSML3**2*MH**2 + 3*KHBSMR3**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP3**2 + MBP3**4 - 2*MB**2*MH**2 - 2*MBP3**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.bp1,P.b__tilde__):'((-3*KHBSML1**2*MB**2 - 3*KHBSMR1**2*MB**2 - 12*KHBSML1*KHBSMR1*MB*MBP1 - 3*KHBSML1**2*MBP1**2 - 3*KHBSMR1**2*MBP1**2 + 3*KHBSML1**2*MH**2 + 3*KHBSMR1**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP1**2 + MBP1**4 - 2*MB**2*MH**2 - 2*MBP1**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.bp1,P.bp1__tilde__):'((-24*KHBPBP1x1**2*MBP1**2 + 6*KHBPBP1x1**2*MH**2)*cmath.sqrt(-4*MBP1**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.bp1,P.bp2__tilde__):'((-3*KHBPBP1x2**2*MBP1**2 - 3*KHBPBP2x1**2*MBP1**2 - 12*KHBPBP1x2*KHBPBP2x1*MBP1*MBP2 - 3*KHBPBP1x2**2*MBP2**2 - 3*KHBPBP2x1**2*MBP2**2 + 3*KHBPBP1x2**2*MH**2 + 3*KHBPBP2x1**2*MH**2)*cmath.sqrt(MBP1**4 - 2*MBP1**2*MBP2**2 + MBP2**4 - 2*MBP1**2*MH**2 - 2*MBP2**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.bp1,P.bp3__tilde__):'((-3*KHBPBP1x3**2*MBP1**2 - 3*KHBPBP3x1**2*MBP1**2 - 12*KHBPBP1x3*KHBPBP3x1*MBP1*MBP3 - 3*KHBPBP1x3**2*MBP3**2 - 3*KHBPBP3x1**2*MBP3**2 + 3*KHBPBP1x3**2*MH**2 + 3*KHBPBP3x1**2*MH**2)*cmath.sqrt(MBP1**4 - 2*MBP1**2*MBP3**2 + MBP3**4 - 2*MBP1**2*MH**2 - 2*MBP3**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.bp2,P.b__tilde__):'((-3*KHBSML2**2*MB**2 - 3*KHBSMR2**2*MB**2 - 12*KHBSML2*KHBSMR2*MB*MBP2 - 3*KHBSML2**2*MBP2**2 - 3*KHBSMR2**2*MBP2**2 + 3*KHBSML2**2*MH**2 + 3*KHBSMR2**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP2**2 + MBP2**4 - 2*MB**2*MH**2 - 2*MBP2**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.bp2,P.bp1__tilde__):'((-3*KHBPBP1x2**2*MBP1**2 - 3*KHBPBP2x1**2*MBP1**2 - 12*KHBPBP1x2*KHBPBP2x1*MBP1*MBP2 - 3*KHBPBP1x2**2*MBP2**2 - 3*KHBPBP2x1**2*MBP2**2 + 3*KHBPBP1x2**2*MH**2 + 3*KHBPBP2x1**2*MH**2)*cmath.sqrt(MBP1**4 - 2*MBP1**2*MBP2**2 + MBP2**4 - 2*MBP1**2*MH**2 - 2*MBP2**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.bp2,P.bp2__tilde__):'((-24*KHBPBP2x2**2*MBP2**2 + 6*KHBPBP2x2**2*MH**2)*cmath.sqrt(-4*MBP2**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.bp2,P.bp3__tilde__):'((-3*KHBPBP2x3**2*MBP2**2 - 3*KHBPBP3x2**2*MBP2**2 - 12*KHBPBP2x3*KHBPBP3x2*MBP2*MBP3 - 3*KHBPBP2x3**2*MBP3**2 - 3*KHBPBP3x2**2*MBP3**2 + 3*KHBPBP2x3**2*MH**2 + 3*KHBPBP3x2**2*MH**2)*cmath.sqrt(MBP2**4 - 2*MBP2**2*MBP3**2 + MBP3**4 - 2*MBP2**2*MH**2 - 2*MBP3**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.bp3,P.b__tilde__):'((-3*KHBSML3**2*MB**2 - 3*KHBSMR3**2*MB**2 - 12*KHBSML3*KHBSMR3*MB*MBP3 - 3*KHBSML3**2*MBP3**2 - 3*KHBSMR3**2*MBP3**2 + 3*KHBSML3**2*MH**2 + 3*KHBSMR3**2*MH**2)*cmath.sqrt(MB**4 - 2*MB**2*MBP3**2 + MBP3**4 - 2*MB**2*MH**2 - 2*MBP3**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.bp3,P.bp1__tilde__):'((-3*KHBPBP1x3**2*MBP1**2 - 3*KHBPBP3x1**2*MBP1**2 - 12*KHBPBP1x3*KHBPBP3x1*MBP1*MBP3 - 3*KHBPBP1x3**2*MBP3**2 - 3*KHBPBP3x1**2*MBP3**2 + 3*KHBPBP1x3**2*MH**2 + 3*KHBPBP3x1**2*MH**2)*cmath.sqrt(MBP1**4 - 2*MBP1**2*MBP3**2 + MBP3**4 - 2*MBP1**2*MH**2 - 2*MBP3**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.bp3,P.bp2__tilde__):'((-3*KHBPBP2x3**2*MBP2**2 - 3*KHBPBP3x2**2*MBP2**2 - 12*KHBPBP2x3*KHBPBP3x2*MBP2*MBP3 - 3*KHBPBP2x3**2*MBP3**2 - 3*KHBPBP3x2**2*MBP3**2 + 3*KHBPBP2x3**2*MH**2 + 3*KHBPBP3x2**2*MH**2)*cmath.sqrt(MBP2**4 - 2*MBP2**2*MBP3**2 + MBP3**4 - 2*MBP2**2*MH**2 - 2*MBP3**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.bp3,P.bp3__tilde__):'((-24*KHBPBP3x3**2*MBP3**2 + 6*KHBPBP3x3**2*MH**2)*cmath.sqrt(-4*MBP3**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq1,P.sq2__tilde__):'(((3*KHSQSQ1x2**2*vev**2)/4. + (3*KHSQSQ1x2*KHSQSQ2x1*vev**2)/2. + (3*KHSQSQ2x1**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ1**2 + MSQ1**4 - 2*MH**2*MSQ2**2 - 2*MSQ1**2*MSQ2**2 + MSQ2**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq1,P.sq3__tilde__):'(((3*KHSQSQ1x3**2*vev**2)/4. + (3*KHSQSQ1x3*KHSQSQ3x1*vev**2)/2. + (3*KHSQSQ3x1**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ1**2 + MSQ1**4 - 2*MH**2*MSQ3**2 - 2*MSQ1**2*MSQ3**2 + MSQ3**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq1,P.sq4__tilde__):'(((3*KHSQSQ1x4**2*vev**2)/4. + (3*KHSQSQ1x4*KHSQSQ4x1*vev**2)/2. + (3*KHSQSQ4x1**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ1**2 + MSQ1**4 - 2*MH**2*MSQ4**2 - 2*MSQ1**2*MSQ4**2 + MSQ4**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq1__tilde__,P.sq1):'(3*KHSQSQ1x1**2*vev**2*cmath.sqrt(MH**4 - 4*MH**2*MSQ1**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq1__tilde__,P.sq2):'(((3*KHSQSQ1x2**2*vev**2)/4. + (3*KHSQSQ1x2*KHSQSQ2x1*vev**2)/2. + (3*KHSQSQ2x1**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ1**2 + MSQ1**4 - 2*MH**2*MSQ2**2 - 2*MSQ1**2*MSQ2**2 + MSQ2**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq1__tilde__,P.sq3):'(((3*KHSQSQ1x3**2*vev**2)/4. + (3*KHSQSQ1x3*KHSQSQ3x1*vev**2)/2. + (3*KHSQSQ3x1**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ1**2 + MSQ1**4 - 2*MH**2*MSQ3**2 - 2*MSQ1**2*MSQ3**2 + MSQ3**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq1__tilde__,P.sq4):'(((3*KHSQSQ1x4**2*vev**2)/4. + (3*KHSQSQ1x4*KHSQSQ4x1*vev**2)/2. + (3*KHSQSQ4x1**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ1**2 + MSQ1**4 - 2*MH**2*MSQ4**2 - 2*MSQ1**2*MSQ4**2 + MSQ4**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq2,P.sq3__tilde__):'(((3*KHSQSQ2x3**2*vev**2)/4. + (3*KHSQSQ2x3*KHSQSQ3x2*vev**2)/2. + (3*KHSQSQ3x2**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ2**2 + MSQ2**4 - 2*MH**2*MSQ3**2 - 2*MSQ2**2*MSQ3**2 + MSQ3**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq2,P.sq4__tilde__):'(((3*KHSQSQ2x4**2*vev**2)/4. + (3*KHSQSQ2x4*KHSQSQ4x2*vev**2)/2. + (3*KHSQSQ4x2**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ2**2 + MSQ2**4 - 2*MH**2*MSQ4**2 - 2*MSQ2**2*MSQ4**2 + MSQ4**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq2__tilde__,P.sq2):'(3*KHSQSQ2x2**2*vev**2*cmath.sqrt(MH**4 - 4*MH**2*MSQ2**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq2__tilde__,P.sq3):'(((3*KHSQSQ2x3**2*vev**2)/4. + (3*KHSQSQ2x3*KHSQSQ3x2*vev**2)/2. + (3*KHSQSQ3x2**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ2**2 + MSQ2**4 - 2*MH**2*MSQ3**2 - 2*MSQ2**2*MSQ3**2 + MSQ3**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq2__tilde__,P.sq4):'(((3*KHSQSQ2x4**2*vev**2)/4. + (3*KHSQSQ2x4*KHSQSQ4x2*vev**2)/2. + (3*KHSQSQ4x2**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ2**2 + MSQ2**4 - 2*MH**2*MSQ4**2 - 2*MSQ2**2*MSQ4**2 + MSQ4**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq3,P.sq4__tilde__):'(((3*KHSQSQ3x4**2*vev**2)/4. + (3*KHSQSQ3x4*KHSQSQ4x3*vev**2)/2. + (3*KHSQSQ4x3**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ3**2 + MSQ3**4 - 2*MH**2*MSQ4**2 - 2*MSQ3**2*MSQ4**2 + MSQ4**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq3__tilde__,P.sq3):'(3*KHSQSQ3x3**2*vev**2*cmath.sqrt(MH**4 - 4*MH**2*MSQ3**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq3__tilde__,P.sq4):'(((3*KHSQSQ3x4**2*vev**2)/4. + (3*KHSQSQ3x4*KHSQSQ4x3*vev**2)/2. + (3*KHSQSQ4x3**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ3**2 + MSQ3**4 - 2*MH**2*MSQ4**2 - 2*MSQ3**2*MSQ4**2 + MSQ4**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.sq4__tilde__,P.sq4):'(3*KHSQSQ4x4**2*vev**2*cmath.sqrt(MH**4 - 4*MH**2*MSQ4**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*KHTT**2*MH**2 - 12*KHTT**2*MT**2 + 6*KHTT*MH**2*yt - 24*KHTT*MT**2*yt + 3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.tp1__tilde__):'((3*KHTSML1**2*MH**2 + 3*KHTSMR1**2*MH**2 - 3*KHTSML1**2*MT**2 - 3*KHTSMR1**2*MT**2 - 12*KHTSML1*KHTSMR1*MT*MTP1 - 3*KHTSML1**2*MTP1**2 - 3*KHTSMR1**2*MTP1**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP1**2 - 2*MT**2*MTP1**2 + MTP1**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.tp2__tilde__):'((3*KHTSML2**2*MH**2 + 3*KHTSMR2**2*MH**2 - 3*KHTSML2**2*MT**2 - 3*KHTSMR2**2*MT**2 - 12*KHTSML2*KHTSMR2*MT*MTP2 - 3*KHTSML2**2*MTP2**2 - 3*KHTSMR2**2*MTP2**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP2**2 - 2*MT**2*MTP2**2 + MTP2**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.tp3__tilde__):'((3*KHTSML3**2*MH**2 + 3*KHTSMR3**2*MH**2 - 3*KHTSML3**2*MT**2 - 3*KHTSMR3**2*MT**2 - 12*KHTSML3*KHTSMR3*MT*MTP3 - 3*KHTSML3**2*MTP3**2 - 3*KHTSMR3**2*MTP3**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP3**2 - 2*MT**2*MTP3**2 + MTP3**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.tp4__tilde__):'((3*KHTSML4**2*MH**2 + 3*KHTSMR4**2*MH**2 - 3*KHTSML4**2*MT**2 - 3*KHTSMR4**2*MT**2 - 12*KHTSML4*KHTSMR4*MT*MTP4 - 3*KHTSML4**2*MTP4**2 - 3*KHTSMR4**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP4**2 - 2*MT**2*MTP4**2 + MTP4**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp1,P.t__tilde__):'((3*KHTSML1**2*MH**2 + 3*KHTSMR1**2*MH**2 - 3*KHTSML1**2*MT**2 - 3*KHTSMR1**2*MT**2 - 12*KHTSML1*KHTSMR1*MT*MTP1 - 3*KHTSML1**2*MTP1**2 - 3*KHTSMR1**2*MTP1**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP1**2 - 2*MT**2*MTP1**2 + MTP1**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp1,P.tp1__tilde__):'((6*KHTPTP1x1**2*MH**2 - 24*KHTPTP1x1**2*MTP1**2)*cmath.sqrt(MH**4 - 4*MH**2*MTP1**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp1,P.tp2__tilde__):'((3*KHTPTP1x2**2*MH**2 + 3*KHTPTP2x1**2*MH**2 - 3*KHTPTP1x2**2*MTP1**2 - 3*KHTPTP2x1**2*MTP1**2 - 12*KHTPTP1x2*KHTPTP2x1*MTP1*MTP2 - 3*KHTPTP1x2**2*MTP2**2 - 3*KHTPTP2x1**2*MTP2**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP1**2 + MTP1**4 - 2*MH**2*MTP2**2 - 2*MTP1**2*MTP2**2 + MTP2**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp1,P.tp3__tilde__):'((3*KHTPTP1x3**2*MH**2 + 3*KHTPTP3x1**2*MH**2 - 3*KHTPTP1x3**2*MTP1**2 - 3*KHTPTP3x1**2*MTP1**2 - 12*KHTPTP1x3*KHTPTP3x1*MTP1*MTP3 - 3*KHTPTP1x3**2*MTP3**2 - 3*KHTPTP3x1**2*MTP3**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP1**2 + MTP1**4 - 2*MH**2*MTP3**2 - 2*MTP1**2*MTP3**2 + MTP3**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp1,P.tp4__tilde__):'((3*KHTPTP1x4**2*MH**2 + 3*KHTPTP4x1**2*MH**2 - 3*KHTPTP1x4**2*MTP1**2 - 3*KHTPTP4x1**2*MTP1**2 - 12*KHTPTP1x4*KHTPTP4x1*MTP1*MTP4 - 3*KHTPTP1x4**2*MTP4**2 - 3*KHTPTP4x1**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP1**2 + MTP1**4 - 2*MH**2*MTP4**2 - 2*MTP1**2*MTP4**2 + MTP4**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp2,P.t__tilde__):'((3*KHTSML2**2*MH**2 + 3*KHTSMR2**2*MH**2 - 3*KHTSML2**2*MT**2 - 3*KHTSMR2**2*MT**2 - 12*KHTSML2*KHTSMR2*MT*MTP2 - 3*KHTSML2**2*MTP2**2 - 3*KHTSMR2**2*MTP2**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP2**2 - 2*MT**2*MTP2**2 + MTP2**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp2,P.tp1__tilde__):'((3*KHTPTP1x2**2*MH**2 + 3*KHTPTP2x1**2*MH**2 - 3*KHTPTP1x2**2*MTP1**2 - 3*KHTPTP2x1**2*MTP1**2 - 12*KHTPTP1x2*KHTPTP2x1*MTP1*MTP2 - 3*KHTPTP1x2**2*MTP2**2 - 3*KHTPTP2x1**2*MTP2**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP1**2 + MTP1**4 - 2*MH**2*MTP2**2 - 2*MTP1**2*MTP2**2 + MTP2**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp2,P.tp2__tilde__):'((6*KHTPTP2x2**2*MH**2 - 24*KHTPTP2x2**2*MTP2**2)*cmath.sqrt(MH**4 - 4*MH**2*MTP2**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp2,P.tp3__tilde__):'((3*KHTPTP2x3**2*MH**2 + 3*KHTPTP3x2**2*MH**2 - 3*KHTPTP2x3**2*MTP2**2 - 3*KHTPTP3x2**2*MTP2**2 - 12*KHTPTP2x3*KHTPTP3x2*MTP2*MTP3 - 3*KHTPTP2x3**2*MTP3**2 - 3*KHTPTP3x2**2*MTP3**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP2**2 + MTP2**4 - 2*MH**2*MTP3**2 - 2*MTP2**2*MTP3**2 + MTP3**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp2,P.tp4__tilde__):'((3*KHTPTP2x4**2*MH**2 + 3*KHTPTP4x2**2*MH**2 - 3*KHTPTP2x4**2*MTP2**2 - 3*KHTPTP4x2**2*MTP2**2 - 12*KHTPTP2x4*KHTPTP4x2*MTP2*MTP4 - 3*KHTPTP2x4**2*MTP4**2 - 3*KHTPTP4x2**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP2**2 + MTP2**4 - 2*MH**2*MTP4**2 - 2*MTP2**2*MTP4**2 + MTP4**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp3,P.t__tilde__):'((3*KHTSML3**2*MH**2 + 3*KHTSMR3**2*MH**2 - 3*KHTSML3**2*MT**2 - 3*KHTSMR3**2*MT**2 - 12*KHTSML3*KHTSMR3*MT*MTP3 - 3*KHTSML3**2*MTP3**2 - 3*KHTSMR3**2*MTP3**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP3**2 - 2*MT**2*MTP3**2 + MTP3**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp3,P.tp1__tilde__):'((3*KHTPTP1x3**2*MH**2 + 3*KHTPTP3x1**2*MH**2 - 3*KHTPTP1x3**2*MTP1**2 - 3*KHTPTP3x1**2*MTP1**2 - 12*KHTPTP1x3*KHTPTP3x1*MTP1*MTP3 - 3*KHTPTP1x3**2*MTP3**2 - 3*KHTPTP3x1**2*MTP3**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP1**2 + MTP1**4 - 2*MH**2*MTP3**2 - 2*MTP1**2*MTP3**2 + MTP3**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp3,P.tp2__tilde__):'((3*KHTPTP2x3**2*MH**2 + 3*KHTPTP3x2**2*MH**2 - 3*KHTPTP2x3**2*MTP2**2 - 3*KHTPTP3x2**2*MTP2**2 - 12*KHTPTP2x3*KHTPTP3x2*MTP2*MTP3 - 3*KHTPTP2x3**2*MTP3**2 - 3*KHTPTP3x2**2*MTP3**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP2**2 + MTP2**4 - 2*MH**2*MTP3**2 - 2*MTP2**2*MTP3**2 + MTP3**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp3,P.tp3__tilde__):'((6*KHTPTP3x3**2*MH**2 - 24*KHTPTP3x3**2*MTP3**2)*cmath.sqrt(MH**4 - 4*MH**2*MTP3**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp3,P.tp4__tilde__):'((3*KHTPTP3x4**2*MH**2 + 3*KHTPTP4x3**2*MH**2 - 3*KHTPTP3x4**2*MTP3**2 - 3*KHTPTP4x3**2*MTP3**2 - 12*KHTPTP3x4*KHTPTP4x3*MTP3*MTP4 - 3*KHTPTP3x4**2*MTP4**2 - 3*KHTPTP4x3**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP3**2 + MTP3**4 - 2*MH**2*MTP4**2 - 2*MTP3**2*MTP4**2 + MTP4**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp4,P.t__tilde__):'((3*KHTSML4**2*MH**2 + 3*KHTSMR4**2*MH**2 - 3*KHTSML4**2*MT**2 - 3*KHTSMR4**2*MT**2 - 12*KHTSML4*KHTSMR4*MT*MTP4 - 3*KHTSML4**2*MTP4**2 - 3*KHTSMR4**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP4**2 - 2*MT**2*MTP4**2 + MTP4**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp4,P.tp1__tilde__):'((3*KHTPTP1x4**2*MH**2 + 3*KHTPTP4x1**2*MH**2 - 3*KHTPTP1x4**2*MTP1**2 - 3*KHTPTP4x1**2*MTP1**2 - 12*KHTPTP1x4*KHTPTP4x1*MTP1*MTP4 - 3*KHTPTP1x4**2*MTP4**2 - 3*KHTPTP4x1**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP1**2 + MTP1**4 - 2*MH**2*MTP4**2 - 2*MTP1**2*MTP4**2 + MTP4**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp4,P.tp2__tilde__):'((3*KHTPTP2x4**2*MH**2 + 3*KHTPTP4x2**2*MH**2 - 3*KHTPTP2x4**2*MTP2**2 - 3*KHTPTP4x2**2*MTP2**2 - 12*KHTPTP2x4*KHTPTP4x2*MTP2*MTP4 - 3*KHTPTP2x4**2*MTP4**2 - 3*KHTPTP4x2**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP2**2 + MTP2**4 - 2*MH**2*MTP4**2 - 2*MTP2**2*MTP4**2 + MTP4**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp4,P.tp3__tilde__):'((3*KHTPTP3x4**2*MH**2 + 3*KHTPTP4x3**2*MH**2 - 3*KHTPTP3x4**2*MTP3**2 - 3*KHTPTP4x3**2*MTP3**2 - 12*KHTPTP3x4*KHTPTP4x3*MTP3*MTP4 - 3*KHTPTP3x4**2*MTP4**2 - 3*KHTPTP4x3**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP3**2 + MTP3**4 - 2*MH**2*MTP4**2 - 2*MTP3**2*MTP4**2 + MTP4**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.tp4,P.tp4__tilde__):'((6*KHTPTP4x4**2*MH**2 - 24*KHTPTP4x4**2*MTP4**2)*cmath.sqrt(MH**4 - 4*MH**2*MTP4**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_s01 = Decay(name = 'Decay_s01',
                  particle = P.s01,
                  partial_widths = {(P.b,P.b__tilde__):'((-24*KS01BB**2*MB**2 + 6*KS01BB**2*MS01**2)*cmath.sqrt(-4*MB**2*MS01**2 + MS01**4))/(16.*cmath.pi*abs(MS01)**3)',
                                    (P.bp1,P.bp1__tilde__):'((-24*KS01B1B1**2*MBP1**2 + 6*KS01B1B1**2*MS01**2)*cmath.sqrt(-4*MBP1**2*MS01**2 + MS01**4))/(16.*cmath.pi*abs(MS01)**3)',
                                    (P.bp2,P.bp2__tilde__):'((-24*KS01B2B2**2*MBP2**2 + 6*KS01B2B2**2*MS01**2)*cmath.sqrt(-4*MBP2**2*MS01**2 + MS01**4))/(16.*cmath.pi*abs(MS01)**3)',
                                    (P.H,P.H):'(KHHS01**2*vev**2*cmath.sqrt(-4*MH**2*MS01**2 + MS01**4))/(8.*cmath.pi*abs(MS01)**3)',
                                    (P.sq1__tilde__,P.sq1):'(3*KS01SQ1SQ1**2*vev**2*cmath.sqrt(MS01**4 - 4*MS01**2*MSQ1**2))/(16.*cmath.pi*abs(MS01)**3)',
                                    (P.sq2__tilde__,P.sq2):'(3*KS01SQ2SQ2**2*vev**2*cmath.sqrt(MS01**4 - 4*MS01**2*MSQ2**2))/(16.*cmath.pi*abs(MS01)**3)',
                                    (P.sq3__tilde__,P.sq3):'(3*KS01SQ3SQ3**2*vev**2*cmath.sqrt(MS01**4 - 4*MS01**2*MSQ3**2))/(16.*cmath.pi*abs(MS01)**3)',
                                    (P.t,P.t__tilde__):'((6*KS01TT**2*MS01**2 - 24*KS01TT**2*MT**2)*cmath.sqrt(MS01**4 - 4*MS01**2*MT**2))/(16.*cmath.pi*abs(MS01)**3)',
                                    (P.tp1,P.tp1__tilde__):'((6*KS01T1T1**2*MS01**2 - 24*KS01T1T1**2*MTP1**2)*cmath.sqrt(MS01**4 - 4*MS01**2*MTP1**2))/(16.*cmath.pi*abs(MS01)**3)',
                                    (P.tp2,P.tp2__tilde__):'((6*KS01T2T2**2*MS01**2 - 24*KS01T2T2**2*MTP2**2)*cmath.sqrt(MS01**4 - 4*MS01**2*MTP2**2))/(16.*cmath.pi*abs(MS01)**3)'})

Decay_s02 = Decay(name = 'Decay_s02',
                  particle = P.s02,
                  partial_widths = {(P.b,P.b__tilde__):'((-24*KS02BB**2*MB**2 + 6*KS02BB**2*MS02**2)*cmath.sqrt(-4*MB**2*MS02**2 + MS02**4))/(16.*cmath.pi*abs(MS02)**3)',
                                    (P.bp1,P.bp1__tilde__):'((-24*KS02B1B1**2*MBP1**2 + 6*KS02B1B1**2*MS02**2)*cmath.sqrt(-4*MBP1**2*MS02**2 + MS02**4))/(16.*cmath.pi*abs(MS02)**3)',
                                    (P.bp2,P.bp2__tilde__):'((-24*KS02B2B2**2*MBP2**2 + 6*KS02B2B2**2*MS02**2)*cmath.sqrt(-4*MBP2**2*MS02**2 + MS02**4))/(16.*cmath.pi*abs(MS02)**3)',
                                    (P.H,P.H):'(KHHS02**2*vev**2*cmath.sqrt(-4*MH**2*MS02**2 + MS02**4))/(8.*cmath.pi*abs(MS02)**3)',
                                    (P.sq1__tilde__,P.sq1):'(3*KS02SQ1SQ1**2*vev**2*cmath.sqrt(MS02**4 - 4*MS02**2*MSQ1**2))/(16.*cmath.pi*abs(MS02)**3)',
                                    (P.sq2__tilde__,P.sq2):'(3*KS02SQ2SQ2**2*vev**2*cmath.sqrt(MS02**4 - 4*MS02**2*MSQ2**2))/(16.*cmath.pi*abs(MS02)**3)',
                                    (P.t,P.t__tilde__):'((6*KS02TT**2*MS02**2 - 24*KS02TT**2*MT**2)*cmath.sqrt(MS02**4 - 4*MS02**2*MT**2))/(16.*cmath.pi*abs(MS02)**3)',
                                    (P.tp1,P.tp1__tilde__):'((6*KS02T1T1**2*MS02**2 - 24*KS02T1T1**2*MTP1**2)*cmath.sqrt(MS02**4 - 4*MS02**2*MTP1**2))/(16.*cmath.pi*abs(MS02)**3)',
                                    (P.tp2,P.tp2__tilde__):'((6*KS02T2T2**2*MS02**2 - 24*KS02T2T2**2*MTP2**2)*cmath.sqrt(MS02**4 - 4*MS02**2*MTP2**2))/(16.*cmath.pi*abs(MS02)**3)'})

Decay_sq1 = Decay(name = 'Decay_sq1',
                  particle = P.sq1,
                  partial_widths = {(P.H,P.sq2):'(((3*KHSQSQ1x2**2*vev**2)/4. + (3*KHSQSQ1x2*KHSQSQ2x1*vev**2)/2. + (3*KHSQSQ2x1**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ1**2 + MSQ1**4 - 2*MH**2*MSQ2**2 - 2*MSQ1**2*MSQ2**2 + MSQ2**4))/(48.*cmath.pi*abs(MSQ1)**3)',
                                    (P.H,P.sq3):'(((3*KHSQSQ1x3**2*vev**2)/4. + (3*KHSQSQ1x3*KHSQSQ3x1*vev**2)/2. + (3*KHSQSQ3x1**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ1**2 + MSQ1**4 - 2*MH**2*MSQ3**2 - 2*MSQ1**2*MSQ3**2 + MSQ3**4))/(48.*cmath.pi*abs(MSQ1)**3)',
                                    (P.H,P.sq4):'(((3*KHSQSQ1x4**2*vev**2)/4. + (3*KHSQSQ1x4*KHSQSQ4x1*vev**2)/2. + (3*KHSQSQ4x1**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ1**2 + MSQ1**4 - 2*MH**2*MSQ4**2 - 2*MSQ1**2*MSQ4**2 + MSQ4**4))/(48.*cmath.pi*abs(MSQ1)**3)'})

Decay_sq2 = Decay(name = 'Decay_sq2',
                  particle = P.sq2,
                  partial_widths = {(P.H,P.sq1):'(((3*KHSQSQ1x2**2*vev**2)/4. + (3*KHSQSQ1x2*KHSQSQ2x1*vev**2)/2. + (3*KHSQSQ2x1**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ1**2 + MSQ1**4 - 2*MH**2*MSQ2**2 - 2*MSQ1**2*MSQ2**2 + MSQ2**4))/(48.*cmath.pi*abs(MSQ2)**3)',
                                    (P.H,P.sq3):'(((3*KHSQSQ2x3**2*vev**2)/4. + (3*KHSQSQ2x3*KHSQSQ3x2*vev**2)/2. + (3*KHSQSQ3x2**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ2**2 + MSQ2**4 - 2*MH**2*MSQ3**2 - 2*MSQ2**2*MSQ3**2 + MSQ3**4))/(48.*cmath.pi*abs(MSQ2)**3)',
                                    (P.H,P.sq4):'(((3*KHSQSQ2x4**2*vev**2)/4. + (3*KHSQSQ2x4*KHSQSQ4x2*vev**2)/2. + (3*KHSQSQ4x2**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ2**2 + MSQ2**4 - 2*MH**2*MSQ4**2 - 2*MSQ2**2*MSQ4**2 + MSQ4**4))/(48.*cmath.pi*abs(MSQ2)**3)'})

Decay_sq3 = Decay(name = 'Decay_sq3',
                  particle = P.sq3,
                  partial_widths = {(P.H,P.sq1):'(((3*KHSQSQ1x3**2*vev**2)/4. + (3*KHSQSQ1x3*KHSQSQ3x1*vev**2)/2. + (3*KHSQSQ3x1**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ1**2 + MSQ1**4 - 2*MH**2*MSQ3**2 - 2*MSQ1**2*MSQ3**2 + MSQ3**4))/(48.*cmath.pi*abs(MSQ3)**3)',
                                    (P.H,P.sq2):'(((3*KHSQSQ2x3**2*vev**2)/4. + (3*KHSQSQ2x3*KHSQSQ3x2*vev**2)/2. + (3*KHSQSQ3x2**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ2**2 + MSQ2**4 - 2*MH**2*MSQ3**2 - 2*MSQ2**2*MSQ3**2 + MSQ3**4))/(48.*cmath.pi*abs(MSQ3)**3)',
                                    (P.H,P.sq4):'(((3*KHSQSQ3x4**2*vev**2)/4. + (3*KHSQSQ3x4*KHSQSQ4x3*vev**2)/2. + (3*KHSQSQ4x3**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ3**2 + MSQ3**4 - 2*MH**2*MSQ4**2 - 2*MSQ3**2*MSQ4**2 + MSQ4**4))/(48.*cmath.pi*abs(MSQ3)**3)'})

Decay_sq4 = Decay(name = 'Decay_sq4',
                  particle = P.sq4,
                  partial_widths = {(P.H,P.sq1):'(((3*KHSQSQ1x4**2*vev**2)/4. + (3*KHSQSQ1x4*KHSQSQ4x1*vev**2)/2. + (3*KHSQSQ4x1**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ1**2 + MSQ1**4 - 2*MH**2*MSQ4**2 - 2*MSQ1**2*MSQ4**2 + MSQ4**4))/(48.*cmath.pi*abs(MSQ4)**3)',
                                    (P.H,P.sq2):'(((3*KHSQSQ2x4**2*vev**2)/4. + (3*KHSQSQ2x4*KHSQSQ4x2*vev**2)/2. + (3*KHSQSQ4x2**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ2**2 + MSQ2**4 - 2*MH**2*MSQ4**2 - 2*MSQ2**2*MSQ4**2 + MSQ4**4))/(48.*cmath.pi*abs(MSQ4)**3)',
                                    (P.H,P.sq3):'(((3*KHSQSQ3x4**2*vev**2)/4. + (3*KHSQSQ3x4*KHSQSQ4x3*vev**2)/2. + (3*KHSQSQ4x3**2*vev**2)/4.)*cmath.sqrt(MH**4 - 2*MH**2*MSQ3**2 + MSQ3**4 - 2*MH**2*MSQ4**2 - 2*MSQ3**2*MSQ4**2 + MSQ4**4))/(48.*cmath.pi*abs(MSQ4)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.H,P.tp1):'((-3*KHTSML1**2*MH**2 - 3*KHTSMR1**2*MH**2 + 3*KHTSML1**2*MT**2 + 3*KHTSMR1**2*MT**2 + 12*KHTSML1*KHTSMR1*MT*MTP1 + 3*KHTSML1**2*MTP1**2 + 3*KHTSMR1**2*MTP1**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP1**2 - 2*MT**2*MTP1**2 + MTP1**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.H,P.tp2):'((-3*KHTSML2**2*MH**2 - 3*KHTSMR2**2*MH**2 + 3*KHTSML2**2*MT**2 + 3*KHTSMR2**2*MT**2 + 12*KHTSML2*KHTSMR2*MT*MTP2 + 3*KHTSML2**2*MTP2**2 + 3*KHTSMR2**2*MTP2**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP2**2 - 2*MT**2*MTP2**2 + MTP2**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.H,P.tp3):'((-3*KHTSML3**2*MH**2 - 3*KHTSMR3**2*MH**2 + 3*KHTSML3**2*MT**2 + 3*KHTSMR3**2*MT**2 + 12*KHTSML3*KHTSMR3*MT*MTP3 + 3*KHTSML3**2*MTP3**2 + 3*KHTSMR3**2*MTP3**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP3**2 - 2*MT**2*MTP3**2 + MTP3**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.H,P.tp4):'((-3*KHTSML4**2*MH**2 - 3*KHTSMR4**2*MH**2 + 3*KHTSML4**2*MT**2 + 3*KHTSMR4**2*MT**2 + 12*KHTSML4*KHTSMR4*MT*MTP4 + 3*KHTSML4**2*MTP4**2 + 3*KHTSMR4**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP4**2 - 2*MT**2*MTP4**2 + MTP4**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_tp1 = Decay(name = 'Decay_tp1',
                  particle = P.tp1,
                  partial_widths = {(P.H,P.t):'((-3*KHTSML1**2*MH**2 - 3*KHTSMR1**2*MH**2 + 3*KHTSML1**2*MT**2 + 3*KHTSMR1**2*MT**2 + 12*KHTSML1*KHTSMR1*MT*MTP1 + 3*KHTSML1**2*MTP1**2 + 3*KHTSMR1**2*MTP1**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP1**2 - 2*MT**2*MTP1**2 + MTP1**4))/(96.*cmath.pi*abs(MTP1)**3)',
                                    (P.H,P.tp2):'((-3*KHTPTP1x2**2*MH**2 - 3*KHTPTP2x1**2*MH**2 + 3*KHTPTP1x2**2*MTP1**2 + 3*KHTPTP2x1**2*MTP1**2 + 12*KHTPTP1x2*KHTPTP2x1*MTP1*MTP2 + 3*KHTPTP1x2**2*MTP2**2 + 3*KHTPTP2x1**2*MTP2**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP1**2 + MTP1**4 - 2*MH**2*MTP2**2 - 2*MTP1**2*MTP2**2 + MTP2**4))/(96.*cmath.pi*abs(MTP1)**3)',
                                    (P.H,P.tp3):'((-3*KHTPTP1x3**2*MH**2 - 3*KHTPTP3x1**2*MH**2 + 3*KHTPTP1x3**2*MTP1**2 + 3*KHTPTP3x1**2*MTP1**2 + 12*KHTPTP1x3*KHTPTP3x1*MTP1*MTP3 + 3*KHTPTP1x3**2*MTP3**2 + 3*KHTPTP3x1**2*MTP3**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP1**2 + MTP1**4 - 2*MH**2*MTP3**2 - 2*MTP1**2*MTP3**2 + MTP3**4))/(96.*cmath.pi*abs(MTP1)**3)',
                                    (P.H,P.tp4):'((-3*KHTPTP1x4**2*MH**2 - 3*KHTPTP4x1**2*MH**2 + 3*KHTPTP1x4**2*MTP1**2 + 3*KHTPTP4x1**2*MTP1**2 + 12*KHTPTP1x4*KHTPTP4x1*MTP1*MTP4 + 3*KHTPTP1x4**2*MTP4**2 + 3*KHTPTP4x1**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP1**2 + MTP1**4 - 2*MH**2*MTP4**2 - 2*MTP1**2*MTP4**2 + MTP4**4))/(96.*cmath.pi*abs(MTP1)**3)'})

Decay_tp2 = Decay(name = 'Decay_tp2',
                  particle = P.tp2,
                  partial_widths = {(P.H,P.t):'((-3*KHTSML2**2*MH**2 - 3*KHTSMR2**2*MH**2 + 3*KHTSML2**2*MT**2 + 3*KHTSMR2**2*MT**2 + 12*KHTSML2*KHTSMR2*MT*MTP2 + 3*KHTSML2**2*MTP2**2 + 3*KHTSMR2**2*MTP2**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP2**2 - 2*MT**2*MTP2**2 + MTP2**4))/(96.*cmath.pi*abs(MTP2)**3)',
                                    (P.H,P.tp1):'((-3*KHTPTP1x2**2*MH**2 - 3*KHTPTP2x1**2*MH**2 + 3*KHTPTP1x2**2*MTP1**2 + 3*KHTPTP2x1**2*MTP1**2 + 12*KHTPTP1x2*KHTPTP2x1*MTP1*MTP2 + 3*KHTPTP1x2**2*MTP2**2 + 3*KHTPTP2x1**2*MTP2**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP1**2 + MTP1**4 - 2*MH**2*MTP2**2 - 2*MTP1**2*MTP2**2 + MTP2**4))/(96.*cmath.pi*abs(MTP2)**3)',
                                    (P.H,P.tp3):'((-3*KHTPTP2x3**2*MH**2 - 3*KHTPTP3x2**2*MH**2 + 3*KHTPTP2x3**2*MTP2**2 + 3*KHTPTP3x2**2*MTP2**2 + 12*KHTPTP2x3*KHTPTP3x2*MTP2*MTP3 + 3*KHTPTP2x3**2*MTP3**2 + 3*KHTPTP3x2**2*MTP3**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP2**2 + MTP2**4 - 2*MH**2*MTP3**2 - 2*MTP2**2*MTP3**2 + MTP3**4))/(96.*cmath.pi*abs(MTP2)**3)',
                                    (P.H,P.tp4):'((-3*KHTPTP2x4**2*MH**2 - 3*KHTPTP4x2**2*MH**2 + 3*KHTPTP2x4**2*MTP2**2 + 3*KHTPTP4x2**2*MTP2**2 + 12*KHTPTP2x4*KHTPTP4x2*MTP2*MTP4 + 3*KHTPTP2x4**2*MTP4**2 + 3*KHTPTP4x2**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP2**2 + MTP2**4 - 2*MH**2*MTP4**2 - 2*MTP2**2*MTP4**2 + MTP4**4))/(96.*cmath.pi*abs(MTP2)**3)'})

Decay_tp3 = Decay(name = 'Decay_tp3',
                  particle = P.tp3,
                  partial_widths = {(P.H,P.t):'((-3*KHTSML3**2*MH**2 - 3*KHTSMR3**2*MH**2 + 3*KHTSML3**2*MT**2 + 3*KHTSMR3**2*MT**2 + 12*KHTSML3*KHTSMR3*MT*MTP3 + 3*KHTSML3**2*MTP3**2 + 3*KHTSMR3**2*MTP3**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP3**2 - 2*MT**2*MTP3**2 + MTP3**4))/(96.*cmath.pi*abs(MTP3)**3)',
                                    (P.H,P.tp1):'((-3*KHTPTP1x3**2*MH**2 - 3*KHTPTP3x1**2*MH**2 + 3*KHTPTP1x3**2*MTP1**2 + 3*KHTPTP3x1**2*MTP1**2 + 12*KHTPTP1x3*KHTPTP3x1*MTP1*MTP3 + 3*KHTPTP1x3**2*MTP3**2 + 3*KHTPTP3x1**2*MTP3**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP1**2 + MTP1**4 - 2*MH**2*MTP3**2 - 2*MTP1**2*MTP3**2 + MTP3**4))/(96.*cmath.pi*abs(MTP3)**3)',
                                    (P.H,P.tp2):'((-3*KHTPTP2x3**2*MH**2 - 3*KHTPTP3x2**2*MH**2 + 3*KHTPTP2x3**2*MTP2**2 + 3*KHTPTP3x2**2*MTP2**2 + 12*KHTPTP2x3*KHTPTP3x2*MTP2*MTP3 + 3*KHTPTP2x3**2*MTP3**2 + 3*KHTPTP3x2**2*MTP3**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP2**2 + MTP2**4 - 2*MH**2*MTP3**2 - 2*MTP2**2*MTP3**2 + MTP3**4))/(96.*cmath.pi*abs(MTP3)**3)',
                                    (P.H,P.tp4):'((-3*KHTPTP3x4**2*MH**2 - 3*KHTPTP4x3**2*MH**2 + 3*KHTPTP3x4**2*MTP3**2 + 3*KHTPTP4x3**2*MTP3**2 + 12*KHTPTP3x4*KHTPTP4x3*MTP3*MTP4 + 3*KHTPTP3x4**2*MTP4**2 + 3*KHTPTP4x3**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP3**2 + MTP3**4 - 2*MH**2*MTP4**2 - 2*MTP3**2*MTP4**2 + MTP4**4))/(96.*cmath.pi*abs(MTP3)**3)'})

Decay_tp4 = Decay(name = 'Decay_tp4',
                  particle = P.tp4,
                  partial_widths = {(P.H,P.t):'((-3*KHTSML4**2*MH**2 - 3*KHTSMR4**2*MH**2 + 3*KHTSML4**2*MT**2 + 3*KHTSMR4**2*MT**2 + 12*KHTSML4*KHTSMR4*MT*MTP4 + 3*KHTSML4**2*MTP4**2 + 3*KHTSMR4**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MT**2 + MT**4 - 2*MH**2*MTP4**2 - 2*MT**2*MTP4**2 + MTP4**4))/(96.*cmath.pi*abs(MTP4)**3)',
                                    (P.H,P.tp1):'((-3*KHTPTP1x4**2*MH**2 - 3*KHTPTP4x1**2*MH**2 + 3*KHTPTP1x4**2*MTP1**2 + 3*KHTPTP4x1**2*MTP1**2 + 12*KHTPTP1x4*KHTPTP4x1*MTP1*MTP4 + 3*KHTPTP1x4**2*MTP4**2 + 3*KHTPTP4x1**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP1**2 + MTP1**4 - 2*MH**2*MTP4**2 - 2*MTP1**2*MTP4**2 + MTP4**4))/(96.*cmath.pi*abs(MTP4)**3)',
                                    (P.H,P.tp2):'((-3*KHTPTP2x4**2*MH**2 - 3*KHTPTP4x2**2*MH**2 + 3*KHTPTP2x4**2*MTP2**2 + 3*KHTPTP4x2**2*MTP2**2 + 12*KHTPTP2x4*KHTPTP4x2*MTP2*MTP4 + 3*KHTPTP2x4**2*MTP4**2 + 3*KHTPTP4x2**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP2**2 + MTP2**4 - 2*MH**2*MTP4**2 - 2*MTP2**2*MTP4**2 + MTP4**4))/(96.*cmath.pi*abs(MTP4)**3)',
                                    (P.H,P.tp3):'((-3*KHTPTP3x4**2*MH**2 - 3*KHTPTP4x3**2*MH**2 + 3*KHTPTP3x4**2*MTP3**2 + 3*KHTPTP4x3**2*MTP3**2 + 12*KHTPTP3x4*KHTPTP4x3*MTP3*MTP4 + 3*KHTPTP3x4**2*MTP4**2 + 3*KHTPTP4x3**2*MTP4**2)*cmath.sqrt(MH**4 - 2*MH**2*MTP3**2 + MTP3**4 - 2*MH**2*MTP4**2 - 2*MTP3**2*MTP4**2 + MTP4**4))/(96.*cmath.pi*abs(MTP4)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-0.5*(ee**2*MTA**2)/sw**2 - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

