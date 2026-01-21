# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 13.2.0 for Linux x86 (64-bit) (December 7, 2022)
# Date: Thu 13 Apr 2023 07:48:10


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.WZ,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 82,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghG__tilde__ = ghG.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.ZERO,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.ZERO,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

ta__plus__ = ta__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

b__tilde__ = b.anti()

H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.WZ,
              texname = 'G0',
              antitexname = 'G0',
              goldstone = True,
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'G+',
                     antitexname = 'G-',
                     goldstone = True,
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

G__minus__ = G__plus__.anti()

s01 = Particle(pdg_code = 6100001,
               name = 's01',
               antiname = 's01',
               spin = 1,
               color = 1,
               mass = Param.MS01,
               width = Param.WS01,
               texname = 's01',
               antitexname = 's01',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

s02 = Particle(pdg_code = 6100002,
               name = 's02',
               antiname = 's02',
               spin = 1,
               color = 1,
               mass = Param.MS02,
               width = Param.WS02,
               texname = 's02',
               antitexname = 's02',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

tp1 = Particle(pdg_code = 6000101,
               name = 'tp1',
               antiname = 'tp1~',
               spin = 2,
               color = 3,
               mass = Param.MTP1,
               width = Param.ZERO,
               texname = 'tp1',
               antitexname = 'tp1~',
               charge = 2/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

tp1__tilde__ = tp1.anti()

tp2 = Particle(pdg_code = 6000102,
               name = 'tp2',
               antiname = 'tp2~',
               spin = 2,
               color = 3,
               mass = Param.MTP2,
               width = Param.ZERO,
               texname = 'tp2',
               antitexname = 'tp2~',
               charge = 2/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

tp2__tilde__ = tp2.anti()

tp3 = Particle(pdg_code = 6000103,
               name = 'tp3',
               antiname = 'tp3~',
               spin = 2,
               color = 3,
               mass = Param.MTP3,
               width = Param.ZERO,
               texname = 'tp3',
               antitexname = 'tp3~',
               charge = 2/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

tp3__tilde__ = tp3.anti()

tp4 = Particle(pdg_code = 6000104,
               name = 'tp4',
               antiname = 'tp4~',
               spin = 2,
               color = 3,
               mass = Param.MTP4,
               width = Param.ZERO,
               texname = 'tp4',
               antitexname = 'tp4~',
               charge = 2/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

tp4__tilde__ = tp4.anti()

bp1 = Particle(pdg_code = 6000201,
               name = 'bp1',
               antiname = 'bp1~',
               spin = 2,
               color = 3,
               mass = Param.MBP1,
               width = Param.ZERO,
               texname = 'bp1',
               antitexname = 'bp1~',
               charge = -1/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

bp1__tilde__ = bp1.anti()

bp2 = Particle(pdg_code = 6000202,
               name = 'bp2',
               antiname = 'bp2~',
               spin = 2,
               color = 3,
               mass = Param.MBP2,
               width = Param.ZERO,
               texname = 'bp2',
               antitexname = 'bp2~',
               charge = -1/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

bp2__tilde__ = bp2.anti()

bp3 = Particle(pdg_code = 6000203,
               name = 'bp3',
               antiname = 'bp3~',
               spin = 2,
               color = 3,
               mass = Param.MBP3,
               width = Param.ZERO,
               texname = 'bp3',
               antitexname = 'bp3~',
               charge = -1/3,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

bp3__tilde__ = bp3.anti()

sq1 = Particle(pdg_code = 6000001,
               name = 'sq1',
               antiname = 'sq1~',
               spin = 1,
               color = 3,
               mass = Param.MSQ1,
               width = Param.ZERO,
               texname = 'sq1',
               antitexname = 'sq1~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

sq1__tilde__ = sq1.anti()

sq2 = Particle(pdg_code = 6000002,
               name = 'sq2',
               antiname = 'sq2~',
               spin = 1,
               color = 3,
               mass = Param.MSQ2,
               width = Param.ZERO,
               texname = 'sq2',
               antitexname = 'sq2~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

sq2__tilde__ = sq2.anti()

sq3 = Particle(pdg_code = 6000003,
               name = 'sq3',
               antiname = 'sq3~',
               spin = 1,
               color = 3,
               mass = Param.MSQ3,
               width = Param.ZERO,
               texname = 'sq3',
               antitexname = 'sq3~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

sq3__tilde__ = sq3.anti()

sq4 = Particle(pdg_code = 6000004,
               name = 'sq4',
               antiname = 'sq4~',
               spin = 1,
               color = 3,
               mass = Param.MSQ4,
               width = Param.ZERO,
               texname = 'sq4',
               antitexname = 'sq4~',
               charge = 0,
               GhostNumber = 0,
               LeptonNumber = 0,
               Y = 0)

sq4__tilde__ = sq4.anti()

