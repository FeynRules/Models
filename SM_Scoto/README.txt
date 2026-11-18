# SM_Scoto UFO Libraries
# M. Boukidi, C. Ramos, and R. Ruiz
# September 2026 [Updated Nov 2026]
# Mohammed Boukidi, Camila Ramos, and Richard Ruiz [arXiv:2609.26876]
# Contact: mboukidi@ifj.edu.pl, camila.ramos@ifj.edu.pl, rruiz@ifj.edu.pl
# URL: https://gitlab.cern.ch/riruiz/public-projects/-/tree/master/ScotoLHC/
# URL: https://github.com/FeynRules/Models/tree/main/SM_Scoto

1. Synopsis: The SM_Scoto UFO libraries are a set 
of Universal FeynRules Object libraires for simulating
high-energy processes in the Scotogenic model 
in contemporary high energy software environments

2. References: The UFO is based on the Scotogenic model by 
- Tao, PRD54 (1996) 5693 [arXiv:hep-ph/9603309]
- Ma, PRD73 (2006) 077301 [arXiv:hep-ph/0601225]
as implemented in 
- Boukidi, Ramos, and Ruiz [arXiv:2609.26876]
Please also consider citing Alloul, et al
- Comput.Phys.Commun.185:2250-2300,2014 (arXiv:1310.1921)
- Comput.Phys.Commun.180:1614-1641,2009 (arXiv:0806.4194)

3. File directory:
- Mass_Basis [folder]: UFO model where model parameters are expressed in terms of masses of new scalar particles
- Coupling_Basis [folder]: UFO model where model parameters are expressed in terms of couplings of new scalar potential

4. Contents of Mass_Basis folder:
a. SM_Scotogenic_NLO (.tgz) (flagship UFO)
- includes NLO in QCD UV/R2 counter terms (capable of one-loop QCD computations)
- nf=5 active quark flavors
- diagonal CKM
- no charged lepton masses
b. SM_Scotogenic_XLO (.tgz)
- 4.a but without QCD counter terms
c. SM_Scotogenic_MassiveLeptons_4fs_NLO (.tgz)
- version of 3.a with nf=4 and three massive charged leptons
d. SM_Scotogenic_MassiveLeptons_4fs_XLO (.tgz)
- 4.c but without QCD counter terms
e. FeynRules / Mathematica Contents:
- scotogenic_NLO_public.nb (example notebook for generating all UFOs)
- sm.fr (Standard Model fr file, sans scalar potential)
- scotogenic_bsm_main.fr (header file; calls objects in Parts)
- SM_Scotogenic.nlo (UV/R2 counter terms)
- Parts [directory], contains actual FeynRules files for Scotogenic model

5. Contents of Coupling_Basis folder:
- same as 4 but for coupling basis

6. README Contents:
- this file
- have a great day!