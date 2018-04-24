#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Endocyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn"], products=["RnCyclic"], ownReverse=False)

reverse = "Ring_Open_Endo_Cycli_Radical"

recipe(actions=[
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*1', '1'],
])

boundaryAtoms = ["*1", "*2"]

entry(
    index = 0,
    label = "Rn",
    group = "OR{R3, R4, R5, R6plus, Rn_cyclic}",
    kinetics = None,
)

entry(
    index = 1,
    label = "multiplebond_intra",
    group = 
"""
1 *2 [Cd,Cdd,Ct,CO,N,CS]   u0 {2,[D,T]}
2 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "radadd_intra",
    group = 
"""
1 *1 R!H u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "R3",
    group = 
"""
1 *1 R!H                   u1 {2,S}
2 *2 [Cd,Ct,CO,N,CS]       u0 r0 {1,S} {3,[D,T]}
3 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "R3_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *2 Cd       u0 r0 {1,S} {3,D}
3 *3 [Cd,Cdd] u0 c0 r0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "R3_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *2 Ct  u0 r0 {1,S} {3,T}
3 *3 Ct  u0 c0 r0 {2,T}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "R3_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *2 CO  u0 r0 {1,S} {3,D}
3 *3 O2d u0 c0 r0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "R3_CS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *2 CS  u0 r0 {1,S} {3,D}
3 *3 S2d u0 p2 c0 r0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "R4",
    group = 
"""
1 *1 R!H                   u1 {2,[S,D,T,B]}
2 *4 R!H                   ux {1,[S,D,T,B]} {3,S}
3 *2 [Cd,Ct,CO,N,CS]       u0 r0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "R4_S",
    group = 
"""
1 *1 R!H                 u1 {2,S}
2 *4 R!H                 u0 {1,S} {3,S}
3 *2 [Cd,Ct,CO,CS]       u0 r0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 r0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "R4_S_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 R!H      u0 {1,S} {3,S}
3 *2 Cd       u0 r0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 c0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "R4_Cs_RR_D",
    group = 
"""
1 *1 Cs       u1 {2,S}
2 *4 Cs       u0 {1,S} {3,S} {5,S} {6,S}
3 *2 Cd       u0 r0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 c0 r0 {3,D}
5    R        u0 {2,S}
6    R        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "R4_Cs_HH_D",
    group = 
"""
1 *1 Cs       u1 {2,S}
2 *4 Cs       u0 {1,S} {3,S} {5,S} {6,S}
3 *2 Cd       u0 r0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 c0 r0 {3,D}
5    H        u0 {2,S}
6    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "R4_S_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *2 Ct  u0 r0 {2,S} {4,T}
4 *3 Ct  u0 c0 r0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "R4_S_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *2 CO  u0 r0 {2,S} {4,D}
4 *3 O2d u0 c0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "R4_S_CS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *2 CS  u0 r0 {2,S} {4,D}
4 *3 S2d u0 c0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "R4_D",
    group = 
"""
1 *1 Cd                  u1 {2,D}
2 *4 Cd                  u0 {1,D} {3,S}
3 *2 [Cd,Ct,CO,CS]       u0 r0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 r0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "R4_D_D",
    group = 
"""
1 *1 Cd       u1 {2,D}
2 *4 Cd       u0 {1,D} {3,S}
3 *2 Cd       u0 r0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 c0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "R4_D_T",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3 *2 Ct u0 r0 {2,S} {4,T}
4 *3 Ct u0 c0 r0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "R4_D_CO",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *2 CO  u0 r0 {2,S} {4,D}
4 *3 O2d u0 c0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "R4_D_CS",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *2 CS  u0 r0 {2,S} {4,D}
4 *3 S2d u0 c0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "R4_T",
    group = 
"""
1 *1 Ct                  u1 {2,T}
2 *4 Ct                  u0 {1,T} {3,S}
3 *2 [Cd,Ct,CO,CS]       u0 r0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 r0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "R4_T_D",
    group = 
"""
1 *1 Ct       u1 {2,T}
2 *4 Ct       u0 {1,T} {3,S}
3 *2 Cd       u0 r0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 c0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "R4_T_T",
    group = 
"""
1 *1 Ct u1 {2,T}
2 *4 Ct u0 {1,T} {3,S}
3 *2 Ct u0 r0 {2,S} {4,T}
4 *3 Ct u0 c0 r0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "R4_T_CO",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *2 CO  u0 r0 {2,S} {4,D}
4 *3 O2d u0 c0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "R4_T_CS",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *2 CS  u0 r0 {2,S} {4,D}
4 *3 S2d u0 c0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "R5",
    group = 
"""
1 *1 R!H                   u1 {2,[S,D,T,B]}
2 *4 R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *5 R!H                   ux {2,[S,D,T,B]} {4,S}
4 *2 [Cd,Ct,CO,N,CS]       u0 r0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
""",
)

entry(
    index = 27,
    label = "R5_SS",
    group = 
"""
1 *1 R!H                   u1 {2,S}
2 *4 R!H                   u0 {1,S} {3,S}
3 *5 R!H                   u0 {2,S} {4,S}
4 *2 [Cd,Ct,CO,N,CS]       u0 r0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
""",
)

entry(
    index = 28,
    label = "R5_SS_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 R!H      u0 {1,S} {3,S}
3 *5 R!H      u0 {2,S} {4,S}
4 *2 Cd       u0 r0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 c0 r0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 29,
    label = "R5_CsCs_RR_D",
    group = 
"""
1 *1 Cs       u1 {2,S}
2 *4 Cs       u0 {1,S} {3,S} {6,S} {7,S}
3 *5 Cs       u0 {2,S} {4,S} {8,S} {9,S}
4 *2 Cd       u0 r0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 c0 r0 {4,D}
6    R        u0 {2,S}
7    R        u0 {2,S}
8    R        u0 {3,S}
9    R        u0 {3,S}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 30,
    label = "R5_CsCs_RH_D",
    group = 
"""
1 *1 Cs       u1 {2,S}
2 *4 Cs       u0 {1,S} {3,S} {6,S} {7,S}
3 *5 Cs       u0 {2,S} {4,S} {8,S} {9,S}
4 *2 Cd       u0 r0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 c0 r0 {4,D}
6    R        u0 {2,S}
7    H        u0 {2,S}
8    R        u0 {3,S}
9    H        u0 {3,S}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 31,
    label = "R5_CsCs_HH_D",
    group = 
"""
1 *1 Cs       u1 {2,S}
2 *4 Cs       u0 {1,S} {3,S} {6,S} {7,S}
3 *5 Cs       u0 {2,S} {4,S} {8,S} {9,S}
4 *2 Cd       u0 r0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 c0 r0 {4,D}
6    H        u0 {2,S}
7    H        u0 {2,S}
8    H        u0 {3,S}
9    H        u0 {3,S}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 32,
    label = "R5_SS_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 Ct  u0 r0 {3,S} {5,T}
5 *3 Ct  u0 c0 r0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 33,
    label = "R5_SS_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CO  u0 r0 {3,S} {5,D}
5 *3 O2d u0 c0 r0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 34,
    label = "R5_SS_CS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CS  u0 r0 {3,S} {5,D}
5 *3 S2d u0 c0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "Cs-R5_SS_CS",
    group = 
"""
1 *1 Cs  u1 {2,S} {6,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CS  u0 r0 {3,S} {5,D}
5 *3 S2d u0 c0 r0 {4,D}
6    Cs  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "H2-R5_SS_CS",
    group = 
"""
1 *1 Cs  u1 {2,S} {6,S} {7,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CS  u0 r0 {3,S} {5,D}
5 *3 S2d u0 c0 r0 {4,D}
6    H   u0 {1,S}
7    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "R5_SM",
    group = 
"""
1 *1 R!H                   u1 {2,S}
2 *4 [Cd,Ct,Cb]            u0 {1,S} {3,[D,T,B]}
3 *5 [Cd,Ct,Cb]            u0 {2,[D,T,B]} {4,S}
4 *2 [Cd,Ct,CO,N,CS]       u0 r0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "R5_SD",
    group = 
"""
1 *1 R!H                   u1 {2,S}
2 *4 Cd                    u0 {1,S} {3,D}
3 *5 Cd                    u0 {2,D} {4,S}
4 *2 [Cd,Ct,CO,N,CS]       u0 r0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
""",
)

entry(
    index = 39,
    label = "R5_SD_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 Cd       u0 {1,S} {3,D}
3 *5 Cd       u0 {2,D} {4,S}
4 *2 Cd       u0 r0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 c0 r0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 40,
    label = "R5_SD_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cd  u0 {1,S} {3,D}
3 *5 Cd  u0 {2,D} {4,S}
4 *2 Ct  u0 r0 {3,S} {5,T}
5 *3 Ct  u0 c0 r0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 41,
    label = "R5_SD_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cd  u0 {1,S} {3,D}
3 *5 Cd  u0 {2,D} {4,S}
4 *2 CO  u0 r0 {3,S} {5,D}
5 *3 O2d u0 c0 r0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 42,
    label = "R5_SD_CS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cd  u0 {1,S} {3,D}
3 *5 Cd  u0 {2,D} {4,S}
4 *2 CS  u0 r0 {3,S} {5,D}
5 *3 S2d u0 c0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "R5_ST",
    group = 
"""
1 *1 R!H                   u1 {2,S}
2 *4 Ct                    u0 {1,S} {3,T}
3 *5 Ct                    u0 {2,T} {4,S}
4 *2 [Cd,Ct,CO,N,CS]       u0 r0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
""",
)

entry(
    index = 44,
    label = "R5_ST_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 Ct       u0 {1,S} {3,T}
3 *5 Ct       u0 {2,T} {4,S}
4 *2 Cd       u0 r0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 c0 r0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 45,
    label = "R5_ST_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Ct  u0 {1,S} {3,T}
3 *5 Ct  u0 {2,T} {4,S}
4 *2 Ct  u0 r0 {3,S} {5,T}
5 *3 Ct  u0 c0 r0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 46,
    label = "R5_ST_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Ct  u0 {1,S} {3,T}
3 *5 Ct  u0 {2,T} {4,S}
4 *2 CO  u0 r0 {3,S} {5,D}
5 *3 O2d u0 c0 r0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 47,
    label = "R5_ST_CS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Ct  u0 {1,S} {3,T}
3 *5 Ct  u0 {2,T} {4,S}
4 *2 CS  u0 r0 {3,S} {5,D}
5 *3 S2d u0 c0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "R5_MS",
    group = 
"""
1 *1 [Cd,Ct,Cb]            u1 {2,[D,T,B]}
2 *4 [Cd,Ct,Cb]            u0 {1,[D,T,B]} {3,S}
3 *5 R!H                   u0 {2,S} {4,S}
4 *2 [Cd,Ct,CO,N,CS]       u0 r0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "R5_DS",
    group = 
"""
1 *1 Cd                    u1 {2,D}
2 *4 Cd                    u0 {1,D} {3,S}
3 *5 R!H                   u0 {2,S} {4,S}
4 *2 [Cd,Ct,CO,N,CS]       u0 r0 {3,S} {5,[D,T]}
5 *3 [Cd,Cdd,Ct,O2d,S2d,N] u0 c0 r0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
""",
)

entry(
    index = 50,
    label = "R5_DS_D",
    group = 
"""
1 *1 Cd       u1 {2,D}
2 *4 Cd       u0 {1,D} {3,S}
3 *5 R!H      u0 {2,S} {4,S}
4 *2 Cd       u0 r0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 c0 r0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 51,
    label = "R5_DS_T",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 Ct  u0 r0 {3,S} {5,T}
5 *3 Ct  u0 c0 r0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 52,
    label = "R5_DS_CO",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CO  u0 r0 {3,S} {5,D}
5 *3 O2d u0 c0 r0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 53,
    label = "R5_DS_CS",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CS  u0 r0 {3,S} {5,D}
5 *3 S2d u0 c0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "R5_TS",
    group = 
"""
1 *1 Ct                    u1 {2,T}
2 *4 Ct                    u0 {1,T} {3,S}
3 *5 R!H                   u0 {2,S} {4,S}
4 *2 [Cd,Ct,CO,N,CS]       u0 r0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
""",
)

entry(
    index = 55,
    label = "R5_TS_D",
    group = 
"""
1 *1 Ct       u1 {2,T}
2 *4 Ct       u0 {1,T} {3,S}
3 *5 R!H      u0 {2,S} {4,S}
4 *2 Cd       u0 r0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 c0 r0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 56,
    label = "R5_TS_T",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 Ct  u0 r0 {3,S} {5,T}
5 *3 Ct  u0 c0 r0 {4,T}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
The multiple bond being attacked is a triple bond (to another carbon).
""",
)

entry(
    index = 57,
    label = "R5_TS_CO",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CO  u0 r0 {3,S} {5,D}
5 *3 O2d u0 c0 r0 {4,D}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
The multiple bond being attacked is a C=O bond.
""",
)

entry(
    index = 58,
    label = "R5_MM",
    group = 
"""
1 *1 [Cd,Cb]               u1 {2,[D,B]}
2 *4 [Cdd,Cbf]             u0 {1,[D,B]} {3,[D,B]}
3 *5 [Cd,Cb]               u0 {2,[D,B]} {4,S}
4 *2 [Cd,Ct,CO,N,CS]       u0 r0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "R6plus",
    group = "OR{R6, R7, R8, R9}",
    kinetics = None,
)

entry(
    index = 60,
    label = "R6",
    group = 
"""
1 *1 R!H                   u1 {2,[S,D,T,B]}
2 *4 R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H                   ux {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,N,CS]       u0 r0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "R6_RSR",
    group = 
"""
1 *1 R!H                   u1 {2,[S,D,T,B]}
2 *4 R!H                   u0 {1,[S,D,T,B]} {3,S}
3 *6 R!H                   u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H                   u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,N,CS]       u0 r0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "R6_SSR",
    group = 
"""
1 *1 R!H                 u1 {2,S}
2 *4 R!H                 u0 {1,S} {3,S}
3 *6 R!H                 u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H                 u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 r0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 r0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "R6_SSS",
    group = 
"""
1 *1 R!H                 u1 {2,S}
2 *4 R!H                 u0 {1,S} {3,S}
3 *6 R!H                 u0 {2,S} {4,S}
4 *5 R!H                 u0 {3,S} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 r0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 r0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "R6_SSS_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 R!H      u0 {1,S} {3,S}
3 *6 R!H      u0 {2,S} {4,S}
4 *5 R!H      u0 {3,S} {5,S}
5 *2 Cd       u0 r0 {4,S} {6,D}
6 *3 [Cd,Cdd] u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "R6_CsCsCs_RR_D",
    group = 
"""
1  *1 Cs       u1 {2,S}
2  *4 Cs       u0 {1,S} {3,S} {7,S} {8,S}
3  *6 Cs       u0 {2,S} {4,S} {9,S} {10,S}
4  *5 Cs       u0 {3,S} {5,S} {11,S} {12,S}
5  *2 Cd       u0 r0 {4,S} {6,D}
6  *3 [Cd,Cdd] u0 c0 r0 {5,D}
7     R        u0 {2,S}
8     R        u0 {2,S}
9     R        u0 {3,S}
10    R        u0 {3,S}
11    R        u0 {4,S}
12    R        u0 {4,S}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 6 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 66,
    label = "R6_CsCsCs_RH_D",
    group = 
"""
1  *1 Cs       u1 {2,S}
2  *4 Cs       u0 {1,S} {3,S} {7,S} {8,S}
3  *6 Cs       u0 {2,S} {4,S} {9,S} {10,S}
4  *5 Cs       u0 {3,S} {5,S} {11,S} {12,S}
5  *2 Cd       u0 r0 {4,S} {6,D}
6  *3 [Cd,Cdd] u0 c0 r0 {5,D}
7     R        u0 {2,S}
8     H        u0 {2,S}
9     R        u0 {3,S}
10    H        u0 {3,S}
11    R        u0 {4,S}
12    H        u0 {4,S}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 6 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 67,
    label = "R6_CsCsCs_HH_D",
    group = 
"""
1  *1 Cs       u1 {2,S}
2  *4 Cs       u0 {1,S} {3,S} {7,S} {8,S}
3  *6 Cs       u0 {2,S} {4,S} {9,S} {10,S}
4  *5 Cs       u0 {3,S} {5,S} {11,S} {12,S}
5  *2 Cd       u0 r0 {4,S} {6,D}
6  *3 [Cd,Cdd] u0 c0 r0 {5,D}
7     H        u0 {2,S}
8     H        u0 {2,S}
9     H        u0 {3,S}
10    H        u0 {3,S}
11    H        u0 {4,S}
12    H        u0 {4,S}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 6 carbon atoms.
Starting at the radical site, the first two bonds are single, single.
The multiple bond being attacked is a double bond (to another carbon).
""",
)

entry(
    index = 68,
    label = "R6_SSS_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 Ct  u0 r0 {4,S} {6,T}
6 *3 Ct  u0 c0 r0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "R6_SSS_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CO  u0 r0 {4,S} {6,D}
6 *3 O2d u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "R6_SSM",
    group = 
"""
1 *1 R!H                 u1 {2,S}
2 *4 R!H                 u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb]          u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]          u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 r0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 r0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "R6_SSM_D",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Cd         u0 r0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "R6_SSM_T",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Ct         u0 r0 {4,S} {6,T}
6 *3 Ct         u0 c0 r0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "R6_SSM_CO",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CO         u0 r0 {4,S} {6,D}
6 *3 O2d        u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "R6_SSM_CS",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CS         u0 r0 {4,S} {6,D}
6 *3 S2d        u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "R6_MSR",
    group = 
"""
1 *1 [Cd,Ct,Cb]          u1 {2,[D,T,B]}
2 *4 [Cd,Ct,Cb]          u0 {1,[D,T,B]} {3,S}
3 *6 R!H                 u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H                 u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 r0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 r0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "R6_DSR",
    group = 
"""
1 *1 Cd                  u1 {2,D}
2 *4 Cd                  u0 {1,D} {3,S}
3 *6 R!H                 u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H                 u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 r0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 r0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "R6_DSS",
    group = 
"""
1 *1 Cd                  u1 {2,D}
2 *4 Cd                  u0 {1,D} {3,S}
3 *6 R!H                 u0 {2,S} {4,S}
4 *5 R!H                 u0 {3,S} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 r0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 r0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "R6_DSS_D",
    group = 
"""
1 *1 Cd       u1 {2,D}
2 *4 Cd       u0 {1,D} {3,S}
3 *6 R!H      u0 {2,S} {4,S}
4 *5 R!H      u0 {3,S} {5,S}
5 *2 Cd       u0 r0 {4,S} {6,D}
6 *3 [Cd,Cdd] u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "R6_DSS_T",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 Ct  u0 r0 {4,S} {6,T}
6 *3 Ct  u0 c0 r0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "R6_DSS_CO",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CO  u0 r0 {4,S} {6,D}
6 *3 O2d u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "R6_DSM",
    group = 
"""
1 *1 Cd                  u1 {2,D}
2 *4 Cd                  u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb]          u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]          u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 r0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 r0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "R6_DSM_D",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Cd         u0 r0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "R6_DSM_T",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Ct         u0 r0 {4,S} {6,T}
6 *3 Ct         u0 c0 r0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "R6_DSM_CO",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CO         u0 r0 {4,S} {6,D}
6 *3 O2d        u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "R6_DSM_CS",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CS         u0 r0 {4,S} {6,D}
6 *3 S2d        u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "R6_TSR",
    group = 
"""
1 *1 Ct                  u1 {2,T}
2 *4 Ct                  u0 {1,T} {3,S}
3 *6 R!H                 u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H                 u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 r0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 r0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "R6_TSS",
    group = 
"""
1 *1 Ct                  u1 {2,T}
2 *4 Ct                  u0 {1,T} {3,S}
3 *6 R!H                 u0 {2,S} {4,S}
4 *5 R!H                 u0 {3,S} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 r0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 r0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "R6_TSS_D",
    group = 
"""
1 *1 Ct       u1 {2,T}
2 *4 Ct       u0 {1,T} {3,S}
3 *6 R!H      u0 {2,S} {4,S}
4 *5 R!H      u0 {3,S} {5,S}
5 *2 Cd       u0 r0 {4,S} {6,D}
6 *3 [Cd,Cdd] u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "R6_TSS_T",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 Ct  u0 r0 {4,S} {6,T}
6 *3 Ct  u0 c0 r0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "R6_TSS_CO",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CO  u0 r0 {4,S} {6,D}
6 *3 O2d u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "R6_TSS_CS",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CS  u0 r0 {4,S} {6,D}
6 *3 S2d u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "R6_TSM",
    group = 
"""
1 *1 Ct                  u1 {2,T}
2 *4 Ct                  u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb]          u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]          u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]       u0 r0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd] u0 c0 r0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "R6_TSM_D",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Cd         u0 r0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "R6_TSM_T",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Ct         u0 r0 {4,S} {6,T}
6 *3 Ct         u0 c0 r0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "R6_TSM_CO",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CO         u0 r0 {4,S} {6,D}
6 *3 O2d        u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "R6_TSM_CS",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CS         u0 r0 {4,S} {6,D}
6 *3 S2d        u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "R6_SMS",
    group = 
"""
1 *1 R!H                   u1 {2,S}
2 *4 [Cd,Ct,Cb]            u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb]            u0 {2,[D,T,B]} {4,S}
4 *5 R!H                   u0 {3,S} {5,S}
5 *2 [Cd,Ct,CO,N,CS]       u0 r0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "R6_SMS_D",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *5 R!H        u0 {3,S} {5,S}
5 *2 Cd         u0 r0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "R6_SMS_T",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *5 R!H        u0 {3,S} {5,S}
5 *2 Ct         u0 r0 {4,S} {6,T}
6 *3 Ct         u0 c0 r0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "R6_SMS_CO",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *5 R!H        u0 {3,S} {5,S}
5 *2 CO         u0 r0 {4,S} {6,D}
6 *3 O2d        u0 c0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "R6_SMM",
    group = 
"""
1 *1 R!H             u1 {2,S}
2 *4 [Cd,Cb]         u0 {1,S} {3,[D,B]}
3 *6 [Cdd,Cbf]       u0 {2,[D,B]} {4,[D,B]}
4 *5 [Cd,Cb]         u0 {3,[D,B]} {5,S}
5 *2 [Cd,Ct,CO,CS]   u0 r0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,O2d,S2d] u0 c0 r0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "R7",
    group = 
"""
1 *1 R!H                   u1 {2,[S,D,T,B]}
2 *4 R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H                   ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H                   ux {4,[S,D,T,B]} {6,S}
6 *2 [Cd,Ct,CO,N,CS]       u0 r0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "R8",
    group = 
"""
1 *1 R!H                   u1 {2,[S,D,T,B]}
2 *4 R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H                   ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H                   ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H                   ux {5,[S,D,T,B]} {7,S}
7 *2 [Cd,Ct,CO,N,CS]       u0 r0 {6,S} {8,[D,T]}
8 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {7,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "R9",
    group = 
"""
1 *1 R!H                   u1 {2,[S,D,T,B]}
2 *4 R!H                   ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                   ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H                   ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H                   ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *9 R!H                   ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *5 R!H                   ux {6,[S,D,T,B]} {8,S}
8 *2 [Cd,Ct,CO,N,CS]       u0 r0 {7,S} {9,[D,T]}
9 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {8,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "R9_SSSSSD",
    group = 
"""
1 *1 R!H                   u1 {2,S}
2 *4 R!H                   u0 {1,S} {3,S}
3 *6 R!H                   u0 {2,S} {4,S}
4 *7 R!H                   u0 {3,S} {5,S}
5 *8 R!H                   u0 {4,S} {6,S}
6 *9 R!H                   u0 {5,S} {7,D}
7 *5 R!H                   u0 {6,D} {8,S}
8 *2 [Cd,Ct,CO,N,CS]       u0 r0 {7,S} {9,[D,T]}
9 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {8,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "R9_SDSSSD",
    group = 
"""
1 *1 R!H                   u1 {2,S}
2 *4 R!H                   u0 {1,S} {3,D}
3 *6 R!H                   u0 {2,D} {4,S}
4 *7 R!H                   u0 {3,S} {5,S}
5 *8 R!H                   u0 {4,S} {6,S}
6 *9 R!H                   u0 {5,S} {7,D}
7 *5 R!H                   u0 {6,D} {8,S}
8 *2 [Cd,Ct,CO,N,CS]       u0 r0 {7,S} {9,[D,T]}
9 *3 [Cd,Ct,O2d,S2d,Cdd,N] u0 c0 r0 {8,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "Rn_cyclic",
    group = "OR{Rn0cx, Rn1cx, Rn2cx, Rn3cx, Rn4cx, Rn5cx}",
    kinetics = None,
)

entry(
    index = 108,
    label = "Rn0cx",
    group = "OR{Rn0cx_beta, Rn0cx_gamma, Rn0cx_delta}",
    kinetics = None,
)

entry(
    index = 109,
    label = "Rn0cx_beta",
    group = "OR{Rn0c4_beta, Rn0c5_beta, Rn0c6_beta, Rn0c7_beta, Rn0c8_beta}",
    kinetics = None,
)

entry(
    index = 110,
    label = "Rn0c4_beta",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "Rn0c5_beta",
    group = "OR{Rn0c5_beta_short, Rn0c5_beta_long}",
    kinetics = None,
)

entry(
    index = 112,
    label = "Rn0c5_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {5,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {3,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "Rn0c5_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "Rn0c6_beta",
    group = "OR{Rn0c6_beta_short, Rn0c6_beta_long}",
    kinetics = None,
)

entry(
    index = 115,
    label = "Rn0c6_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {6,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "Rn0c6_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "Rn0c7_beta",
    group = "OR{Rn0c7_beta_short, Rn0c7_beta_long}",
    kinetics = None,
)

entry(
    index = 118,
    label = "Rn0c7_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {7,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {3,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "Rn0c7_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "Rn0c8_beta",
    group = "OR{Rn0c8_beta_short, Rn0c8_beta_long}",
    kinetics = None,
)

entry(
    index = 121,
    label = "Rn0c8_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *1 R!H u1 r1 {2,[S,D,T,B]} {8,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {3,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "Rn0c8_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "Rn0cx_gamma",
    group = "OR{Rn0c6_gamma, Rn0c7_gamma, Rn0c8_gamma}",
    kinetics = None,
)

entry(
    index = 124,
    label = "Rn0c6_gamma",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r1 {3,[S,D,T,B]} {6,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {4,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "Rn0c7_gamma",
    group = "OR{Rn0c7_gamma_short, Rn0c7_gamma_long}",
    kinetics = None,
)

entry(
    index = 126,
    label = "Rn0c7_gamma_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r1 {3,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "Rn0c7_gamma_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {7,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "Rn0c8_gamma",
    group = "OR{Rn0c8_gamma_short, Rn0c8_gamma_long}",
    kinetics = None,
)

entry(
    index = 129,
    label = "Rn0c8_gamma_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r1 {3,[S,D,T,B]} {8,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {4,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "Rn0c8_gamma_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r1 {5,[S,D,T,B]} {8,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "Rn0cx_delta",
    group = "OR{Rn0c8_delta}",
    kinetics = None,
)

entry(
    index = 132,
    label = "Rn0c8_delta",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r1 {4,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "Rn1cx",
    group = "OR{Rn1cx_alpha}",
    kinetics = None,
)

entry(
    index = 134,
    label = "Rn1cx_alpha",
    group = "OR{Rn1c3_alpha, Rn1c4_alpha, Rn1c5_alpha, Rn1c6_alpha, Rn1c7_alpha, Rn1c8_alpha}",
    kinetics = None,
)

entry(
    index = 135,
    label = "Rn1c3_alpha",
    group = "OR{Rn1c3_alpha_short, Rn1c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 136,
    label = "Rn1c3_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "Rn1c3_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {3,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "Rn1c4_alpha",
    group = "OR{Rn1c4_alpha_short, Rn1c4_alpha_long}",
    kinetics = None,
)

entry(
    index = 139,
    label = "Rn1c4_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {5,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "Rn1c4_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "Rn1c5_alpha",
    group = "OR{Rn1c5_alpha_short, Rn1c5_alpha_long}",
    kinetics = None,
)

entry(
    index = 142,
    label = "Rn1c5_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "Rn1c5_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "Rn1c6_alpha",
    group = "OR{Rn1c6_alpha_short, Rn1c6_alpha_long}",
    kinetics = None,
)

entry(
    index = 145,
    label = "Rn1c6_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T,B]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]} {7,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {2,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "Rn1c6_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "Rn1c7_alpha",
    group = "OR{Rn1c7_alpha_short, Rn1c7_alpha_long}",
    kinetics = None,
)

entry(
    index = 148,
    label = "Rn1c7_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {8,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {2,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "Rn1c7_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "Rn1c8_alpha",
    group = "OR{Rn1c8_alpha_short, Rn1c8_alpha_long}",
    kinetics = None,
)

entry(
    index = 151,
    label = "Rn1c8_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {9,[S,D,T,B]}
3 *1 R!H u1 {2,[S,D,T,B]}
4    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {2,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "Rn1c8_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *7 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *6 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "Rn2cx",
    group = "OR{Rn2cx_alpha, Rn2cx_beta}",
    kinetics = None,
)

entry(
    index = 154,
    label = "Rn2cx_alpha",
    group = "OR{Rn2c3_alpha, Rn2c4_alpha, Rn2c5_alpha, Rn2c6_alpha, Rn2c7_alpha, Rn2c8_alpha}",
    kinetics = None,
)

entry(
    index = 155,
    label = "Rn2c3_alpha",
    group = "OR{Rn2c3_alpha_short, Rn2c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 156,
    label = "Rn2c3_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {5,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r0 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "Rn2c3_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {3,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "Rn2c4_alpha",
    group = "OR{Rn2c4_alpha_short, Rn2c4_alpha_long}",
    kinetics = None,
)

entry(
    index = 159,
    label = "Rn2c4_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r0 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "Rn2c4_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "Rn2c5_alpha",
    group = "OR{Rn2c5_alpha_short, Rn2c5_alpha_long}",
    kinetics = None,
)

entry(
    index = 162,
    label = "Rn2c5_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {7,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r0 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {2,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "Rn2c5_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "Rn2c6_alpha",
    group = "OR{Rn2c6_alpha_short, Rn2c6_alpha_long}",
    kinetics = None,
)

entry(
    index = 165,
    label = "Rn2c6_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]} {8,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r0 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {2,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "Rn2c6_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "Rn2c7_alpha",
    group = "OR{Rn2c7_alpha_short, Rn2c7_alpha_long}",
    kinetics = None,
)

entry(
    index = 168,
    label = "Rn2c7_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {9,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r0 {3,[S,D,T,B]}
5    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {2,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "Rn2c7_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *7 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *6 R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "Rn2c8_alpha",
    group = "OR{Rn2c8_alpha_short, Rn2c8_alpha_long}",
    kinetics = None,
)

entry(
    index = 171,
    label = "Rn2c8_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {10,[S,D,T,B]}
3  *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *1 R!H u1 r0 {3,[S,D,T,B]}
5     R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {2,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "Rn2c8_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *7  R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *6  R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4  R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "Rn2cx_beta",
    group = "OR{Rn2c4_beta, Rn2c5_beta, Rn2c6_beta, Rn2c7_beta, Rn2c8_beta}",
    kinetics = None,
)

entry(
    index = 174,
    label = "Rn2c4_beta",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 175,
    label = "Rn2c5_beta",
    group = "OR{Rn2c5_beta_short, Rn2c5_beta_long}",
    kinetics = None,
)

entry(
    index = 176,
    label = "Rn2c5_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {3,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 177,
    label = "Rn2c5_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
5 *4 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 178,
    label = "Rn2c6_beta",
    group = "OR{Rn2c6_beta_short, Rn2c6_beta_long}",
    kinetics = None,
)

entry(
    index = 179,
    label = "Rn2c6_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {3,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "Rn2c6_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
6 *4 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "Rn2c7_beta",
    group = "OR{Rn2c7_beta_short, Rn2c7_beta_long}",
    kinetics = None,
)

entry(
    index = 182,
    label = "Rn2c7_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {9,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "Rn2c7_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {9,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
7 *4 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
9    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "Rn2c8_beta",
    group = "OR{Rn2c8_beta_short, Rn2c8_beta_long}",
    kinetics = None,
)

entry(
    index = 185,
    label = "Rn2c8_beta_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {10,[S,D,T,B]}
4  *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *1 R!H u1 r0 {4,[S,D,T,B]}
6     R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {3,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "Rn2c8_beta_long",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {10,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *7 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *6 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]} {10,[S,D,T,B]}
8  *4 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 r0 {8,[S,D,T,B]}
10    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "Rn3cx",
    group = "OR{Rn3cx_alpha, Rn3cx_beta, Rn3cx_gamma}",
    kinetics = None,
)

entry(
    index = 188,
    label = "Rn3cx_alpha",
    group = "OR{Rn3c3_alpha, Rn3c4_alpha, Rn3c5_alpha, Rn3c6_alpha, Rn3c7_alpha, Rn3c8_alpha}",
    kinetics = None,
)

entry(
    index = 189,
    label = "Rn3c3_alpha",
    group = "OR{Rn3c3_alpha_short, Rn3c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 190,
    label = "Rn3c3_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "Rn3c3_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {3,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 192,
    label = "Rn3c4_alpha",
    group = "OR{Rn3c4_alpha_short, Rn3c4_alpha_long}",
    kinetics = None,
)

entry(
    index = 193,
    label = "Rn3c4_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {7,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {2,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 194,
    label = "Rn3c4_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 195,
    label = "Rn3c5_alpha",
    group = "OR{Rn3c5_alpha_short, Rn3c5_alpha_long}",
    kinetics = None,
)

entry(
    index = 196,
    label = "Rn3c5_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {8,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {2,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 197,
    label = "Rn3c5_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "Rn3c6_alpha",
    group = "OR{Rn3c6_alpha_short, Rn3c6_alpha_long}",
    kinetics = None,
)

entry(
    index = 199,
    label = "Rn3c6_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]} {9,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
6    R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {2,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 200,
    label = "Rn3c6_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *7 R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *6 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 201,
    label = "Rn3c7_alpha",
    group = "OR{Rn3c7_alpha_short, Rn3c7_alpha_long}",
    kinetics = None,
)

entry(
    index = 202,
    label = "Rn3c7_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {10,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *1 R!H u1 r0 {4,[S,D,T,B]}
6     R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {2,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 203,
    label = "Rn3c7_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *7  R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *6  R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 204,
    label = "Rn3c8_alpha",
    group = "OR{Rn3c8_alpha_short, Rn3c8_alpha_long}",
    kinetics = None,
)

entry(
    index = 205,
    label = "Rn3c8_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {11,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *1 R!H u1 r0 {4,[S,D,T,B]}
6     R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {2,[S,D,T,B]} {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 206,
    label = "Rn3c8_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *11 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *10 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *8  R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *7  R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *6  R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *4  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1  R!H u1 r0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 207,
    label = "Rn3cx_beta",
    group = "OR{Rn3c4_beta, Rn3c5_beta, Rn3c6_beta, Rn3c7_beta, Rn3c8_beta}",
    kinetics = None,
)

entry(
    index = 208,
    label = "Rn3c4_beta",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 209,
    label = "Rn3c5_beta",
    group = "OR{Rn3c5_beta_short, Rn3c5_beta_long}",
    kinetics = None,
)

entry(
    index = 210,
    label = "Rn3c5_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {3,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 211,
    label = "Rn3c5_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {8,[S,D,T,B]}
5 *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "Rn3c6_beta",
    group = "OR{Rn3c6_beta_short, Rn3c6_beta_long}",
    kinetics = None,
)

entry(
    index = 213,
    label = "Rn3c6_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {9,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 214,
    label = "Rn3c6_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {9,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {9,[S,D,T,B]}
6 *6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
9    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 215,
    label = "Rn3c7_beta",
    group = "OR{Rn3c7_beta_short, Rn3c7_beta_long}",
    kinetics = None,
)

entry(
    index = 216,
    label = "Rn3c7_beta_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {10,[S,D,T,B]}
4  *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 R!H u1 r0 {5,[S,D,T,B]}
7     R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {3,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 217,
    label = "Rn3c7_beta_long",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {10,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *7 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {10,[S,D,T,B]}
7  *6 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 r0 {8,[S,D,T,B]}
10    R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 218,
    label = "Rn3c8_beta",
    group = "OR{Rn3c8_beta_short, Rn3c8_beta_long}",
    kinetics = None,
)

entry(
    index = 219,
    label = "Rn3c8_beta_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {11,[S,D,T,B]}
4  *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 R!H u1 r0 {5,[S,D,T,B]}
7     R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {3,[S,D,T,B]} {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 220,
    label = "Rn3c8_beta_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {11,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *7  R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]} {11,[S,D,T,B]}
8  *6  R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 r0 {9,[S,D,T,B]}
11     R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 221,
    label = "Rn3cx_gamma",
    group = "OR{Rn3c6_gamma, Rn3c7_gamma, Rn3c8_gamma}",
    kinetics = None,
)

entry(
    index = 222,
    label = "Rn3c6_gamma",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {9,[S,D,T,B]}
5 *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {4,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 223,
    label = "Rn3c7_gamma",
    group = "OR{Rn3c7_gamma_short, Rn3c7_gamma_long}",
    kinetics = None,
)

entry(
    index = 224,
    label = "Rn3c7_gamma_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {10,[S,D,T,B]}
5  *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {4,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 225,
    label = "Rn3c7_gamma_long",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {9,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {10,[S,D,T,B]}
6  *6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *1 R!H u1 r0 {7,[S,D,T,B]}
9     R!H ux r1 {1,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {5,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 226,
    label = "Rn3c8_gamma",
    group = "OR{Rn3c8_gamma_short, Rn3c8_gamma_long}",
    kinetics = None,
)

entry(
    index = 227,
    label = "Rn3c8_gamma_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {11,[S,D,T,B]}
5  *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {4,[S,D,T,B]} {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 228,
    label = "Rn3c8_gamma_long",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {10,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *7 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {11,[S,D,T,B]}
7  *6 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 r0 {8,[S,D,T,B]}
10    R!H ux r1 {1,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {6,[S,D,T,B]} {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 229,
    label = "Rn4cx",
    group = "OR{Rn4cx_alpha, Rn4cx_beta}",
    kinetics = None,
)

entry(
    index = 230,
    label = "Rn4cx_alpha",
    group = "OR{Rn4c3_alpha, Rn4c4_alpha, Rn4c5_alpha, Rn4c6_alpha, Rn4c7_alpha, Rn4c8_alpha}",
    kinetics = None,
)

entry(
    index = 231,
    label = "Rn4c3_alpha",
    group = "OR{Rn4c3_alpha_short, Rn4c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 232,
    label = "Rn4c3_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {7,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 233,
    label = "Rn4c3_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {3,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 234,
    label = "Rn4c4_alpha",
    group = "OR{Rn4c4_alpha_short, Rn4c4_alpha_long}",
    kinetics = None,
)

entry(
    index = 235,
    label = "Rn4c4_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {8,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {2,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 236,
    label = "Rn4c4_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 237,
    label = "Rn4c5_alpha",
    group = "OR{Rn4c5_alpha_short, Rn4c5_alpha_long}",
    kinetics = None,
)

entry(
    index = 238,
    label = "Rn4c5_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {9,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
7    R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8    R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {2,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 239,
    label = "Rn4c5_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *7 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *6 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 240,
    label = "Rn4c6_alpha",
    group = "OR{Rn4c6_alpha_short, Rn4c6_alpha_long}",
    kinetics = None,
)

entry(
    index = 241,
    label = "Rn4c6_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]} {10,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 R!H u1 r0 {5,[S,D,T,B]}
7     R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {2,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 242,
    label = "Rn4c6_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8  R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *7  R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *6  R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 243,
    label = "Rn4c7_alpha",
    group = "OR{Rn4c7_alpha_short, Rn4c7_alpha_long}",
    kinetics = None,
)

entry(
    index = 244,
    label = "Rn4c7_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {11,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 R!H u1 r0 {5,[S,D,T,B]}
7     R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {2,[S,D,T,B]} {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 245,
    label = "Rn4c7_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *11 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *10 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *8  R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *7  R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *6  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *4  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1  R!H u1 r0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 246,
    label = "Rn4c8_alpha",
    group = "OR{Rn4c8_alpha_short, Rn4c8_alpha_long}",
    kinetics = None,
)

entry(
    index = 247,
    label = "Rn4c8_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {12,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *1 R!H u1 r0 {5,[S,D,T,B]}
7     R!H ux r1 {1,[S,D,T,B]} {8,[S,D,T,B]}
8     R!H ux r1 {7,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {10,[S,D,T,B]} {12,[S,D,T,B]}
12    R!H ux r1 {2,[S,D,T,B]} {11,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 248,
    label = "Rn4c8_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *12 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *11 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *10 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *9  R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *8  R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *7  R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *6  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *4  R!H ux r0 {10,[S,D,T,B]} {12,[S,D,T,B]}
12 *1  R!H u1 r0 {11,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 249,
    label = "Rn4cx_beta",
    group = "OR{Rn4c4_beta, Rn4c5_beta, Rn4c6_beta, Rn4c7_beta, Rn4c8_beta}",
    kinetics = None,
)

entry(
    index = 250,
    label = "Rn4c4_beta",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
4 *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 251,
    label = "Rn4c5_beta",
    group = "OR{Rn4c5_beta_short, Rn4c5_beta_long}",
    kinetics = None,
)

entry(
    index = 252,
    label = "Rn4c5_beta_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {9,[S,D,T,B]}
4 *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 253,
    label = "Rn4c5_beta_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {9,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {9,[S,D,T,B]}
5 *7 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
9    R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 254,
    label = "Rn4c6_beta",
    group = "OR{Rn4c6_beta_short, Rn4c6_beta_long}",
    kinetics = None,
)

entry(
    index = 255,
    label = "Rn4c6_beta_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {10,[S,D,T,B]}
4  *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {3,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 256,
    label = "Rn4c6_beta_long",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {10,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *9 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {10,[S,D,T,B]}
6  *7 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *6 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 r0 {8,[S,D,T,B]}
10    R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 257,
    label = "Rn4c7_beta",
    group = "OR{Rn4c7_beta_short, Rn4c7_beta_long}",
    kinetics = None,
)

entry(
    index = 258,
    label = "Rn4c7_beta_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {11,[S,D,T,B]}
4  *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {3,[S,D,T,B]} {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 259,
    label = "Rn4c7_beta_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {11,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {11,[S,D,T,B]}
7  *7  R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *6  R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 r0 {9,[S,D,T,B]}
11     R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 260,
    label = "Rn4c8_beta",
    group = "OR{Rn4c8_beta_short, Rn4c8_beta_long}",
    kinetics = None,
)

entry(
    index = 261,
    label = "Rn4c8_beta_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {12,[S,D,T,B]}
4  *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {10,[S,D,T,B]} {12,[S,D,T,B]}
12    R!H ux r1 {3,[S,D,T,B]} {11,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 262,
    label = "Rn4c8_beta_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {12,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *11 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *10 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *8  R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]} {12,[S,D,T,B]}
8  *7  R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *6  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *4  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1  R!H u1 r0 {10,[S,D,T,B]}
12     R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 263,
    label = "Rn5cx",
    group = "OR{Rn5cx_alpha}",
    kinetics = None,
)

entry(
    index = 264,
    label = "Rn5cx_alpha",
    group = "OR{Rn5c3_alpha, Rn5c4_alpha, Rn5c5_alpha, Rn5c6_alpha, Rn5c7_alpha, Rn5c8_alpha}",
    kinetics = None,
)

entry(
    index = 265,
    label = "Rn5c3_alpha",
    group = "OR{Rn5c3_alpha_short, Rn5c3_alpha_long}",
    kinetics = None,
)

entry(
    index = 266,
    label = "Rn5c3_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {8,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 267,
    label = "Rn5c3_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {3,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *8 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 268,
    label = "Rn5c4_alpha",
    group = "OR{Rn5c4_alpha_short, Rn5c4_alpha_long}",
    kinetics = None,
)

entry(
    index = 269,
    label = "Rn5c4_alpha_short",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {9,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
8    R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9    R!H ux r1 {2,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 270,
    label = "Rn5c4_alpha_long",
    group = 
"""
1 *3 R!H u0 r1 {2,[D,T]} {4,[S,D,T,B]}
2 *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *9 R!H ux r1 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *7 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *6 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 271,
    label = "Rn5c5_alpha",
    group = "OR{Rn5c5_alpha_short, Rn5c5_alpha_long}",
    kinetics = None,
)

entry(
    index = 272,
    label = "Rn5c5_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {10,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {2,[S,D,T,B]} {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 273,
    label = "Rn5c5_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {5,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *10 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8  R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *7  R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *6  R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 274,
    label = "Rn5c6_alpha",
    group = "OR{Rn5c6_alpha_short, Rn5c6_alpha_long}",
    kinetics = None,
)

entry(
    index = 275,
    label = "Rn5c6_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]} {11,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {2,[S,D,T,B]} {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 276,
    label = "Rn5c6_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *11 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *10 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9  R!H ux r1 {1,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *8  R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *7  R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *6  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *4  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1  R!H u1 r0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 277,
    label = "Rn5c7_alpha",
    group = "OR{Rn5c7_alpha_short, Rn5c7_alpha_long}",
    kinetics = None,
)

entry(
    index = 278,
    label = "Rn5c7_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {12,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {10,[S,D,T,B]} {12,[S,D,T,B]}
12    R!H ux r1 {2,[S,D,T,B]} {11,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 279,
    label = "Rn5c7_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {7,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *12 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *11 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *10 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *9  R!H ux r1 {1,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *8  R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *7  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *6  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *4  R!H ux r0 {10,[S,D,T,B]} {12,[S,D,T,B]}
12 *1  R!H u1 r0 {11,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 280,
    label = "Rn5c8_alpha",
    group = "OR{Rn5c8_alpha_short, Rn5c8_alpha_long}",
    kinetics = None,
)

entry(
    index = 281,
    label = "Rn5c8_alpha_short",
    group = 
"""
1  *3 R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]} {13,[S,D,T,B]}
3  *5 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *7 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *1 R!H u1 r0 {6,[S,D,T,B]}
8     R!H ux r1 {1,[S,D,T,B]} {9,[S,D,T,B]}
9     R!H ux r1 {8,[S,D,T,B]} {10,[S,D,T,B]}
10    R!H ux r1 {9,[S,D,T,B]} {11,[S,D,T,B]}
11    R!H ux r1 {10,[S,D,T,B]} {12,[S,D,T,B]}
12    R!H ux r1 {11,[S,D,T,B]} {13,[S,D,T,B]}
13    R!H ux r1 {2,[S,D,T,B]} {12,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 282,
    label = "Rn5c8_alpha_long",
    group = 
"""
1  *3  R!H u0 r1 {2,[D,T]} {8,[S,D,T,B]}
2  *2  R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3  *5  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *13 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *12 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *11 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *10 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *9  R!H ux r1 {1,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *8  R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *7  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *6  R!H ux r0 {10,[S,D,T,B]} {12,[S,D,T,B]}
12 *4  R!H ux r0 {11,[S,D,T,B]} {13,[S,D,T,B]}
13 *1  R!H u1 r0 {12,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 283,
    label = "doublebond_intra",
    group = 
"""
1 *2 Cd       u0 {2,D}
2 *3 [Cd,Cdd] u0 c0 {1,D}
""",
    kinetics = None,
    longDesc = 
u"""
Note that nodes below this currently do not match allenic type Cdd atoms for *3,
so this is the most specific group that will match such a molecule.
""",
)

entry(
    index = 284,
    label = "doublebond_intra_pri",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S}
2 *3 Cd u0 c0 {1,D}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 285,
    label = "doublebond_intra_pri_2H",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 286,
    label = "doublebond_intra_pri_HNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D} {4,S} {5,S}
3    H        u0 {1,S}
4    H        u0 {2,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 287,
    label = "doublebond_intra_pri_HDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    H                u0 {1,S}
4    H                u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 288,
    label = "doublebond_intra_pri_HCd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
5    Cd u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 289,
    label = "doublebond_intra_pri_HCt",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S}
2 *3 Cd u0 c0 {1,D} {4,S} {5,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
5    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 290,
    label = "doublebond_intra_pri_NdNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D} {4,S} {5,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 291,
    label = "doublebond_intra_pri_NdDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    H                u0 {1,S}
4    [Cs,O,S]         u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 292,
    label = "doublebond_intra_pri_NdCd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D} {4,S} {5,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    Cd       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 293,
    label = "doublebond_intra_pri_NdCt",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D} {4,S} {5,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    Ct       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 294,
    label = "doublebond_intra_pri_DeDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    H                u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 295,
    label = "doublebond_intra_secNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 296,
    label = "doublebond_intra_secNd_2H",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {2,S}
5    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 297,
    label = "doublebond_intra_secNd_HNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {2,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 298,
    label = "doublebond_intra_secNd_HDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    [Cs,O,S]         u0 {1,S}
4    H                u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 299,
    label = "doublebond_intra_secNd_HCd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {2,S}
5    Cd       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 300,
    label = "doublebond_intra_secNd_HCt",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {2,S}
5    Ct       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 301,
    label = "doublebond_intra_secNd_NdNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 302,
    label = "doublebond_intra_secNd_NdDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cs,O,S]         u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 303,
    label = "doublebond_intra_secNd_NdCd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    Cd       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 304,
    label = "doublebond_intra_secNd_NdCt",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 c0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    Ct       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 305,
    label = "doublebond_intra_secNd_DeDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    [Cs,O,S]         u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 306,
    label = "doublebond_intra_secDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 307,
    label = "doublebond_intra_secDe_2H",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
5    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 308,
    label = "doublebond_intra_secDe_HNd",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
5    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 309,
    label = "doublebond_intra_secDe_HDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 310,
    label = "doublebond_intra_secDe_HCd",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
5    Cd               u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 311,
    label = "doublebond_intra_secDe_HCt",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {2,S}
5    Ct               u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 312,
    label = "doublebond_intra_secDe_NdNd",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {2,S}
5    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 313,
    label = "doublebond_intra_secDe_NdDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 314,
    label = "doublebond_intra_secDe_NdCd",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {2,S}
5    Cd               u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 315,
    label = "doublebond_intra_secDe_NdCt",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O,S]         u0 {2,S}
5    Ct               u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 316,
    label = "doublebond_intra_secDe_DeDe",
    group = 
"""
1 *2 Cd               u0 {2,D} {3,S}
2 *3 Cd               u0 c0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {2,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 317,
    label = "triplebond_intra",
    group = 
"""
1 *2 Ct u0 {2,T}
2 *3 Ct u0 c0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 318,
    label = "triplebond_intra_H",
    group = 
"""
1 *2 Ct u0 {2,T}
2 *3 Ct u0 c0 {1,T} {3,S}
3    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 319,
    label = "triplebond_intra_Nd",
    group = 
"""
1 *2 Ct       u0 {2,T}
2 *3 Ct       u0 c0 {1,T} {3,S}
3    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 320,
    label = "triplebond_intra_De",
    group = 
"""
1 *2 Ct               u0 {2,T}
2 *3 Ct               u0 c0 {1,T} {3,S}
3    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 321,
    label = "carbonyl_intra",
    group = 
"""
1 *2 CO  u0 {2,D}
2 *3 O2d u0 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 322,
    label = "carbonyl_intra_H",
    group = 
"""
1 *2 CO  u0 {2,D} {3,S}
2 *3 O2d u0 c0 {1,D}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 323,
    label = "carbonyl_intra_Nd",
    group = 
"""
1 *2 CO       u0 {2,D} {3,S}
2 *3 O2d      u0 c0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 324,
    label = "carbonyl_intra_De",
    group = 
"""
1 *2 CO               u0 {2,D} {3,S}
2 *3 O2d              u0 c0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 325,
    label = "thiyl_intra",
    group = 
"""
1 *2 CS  u0 {2,D}
2 *3 S2d u0 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 326,
    label = "thiyl_intra_H",
    group = 
"""
1 *2 CS  u0 {2,D} {3,S}
2 *3 S2d u0 c0 {1,D}
3    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 327,
    label = "thiyl_intra_Nd",
    group = 
"""
1 *2 CS       u0 {2,D} {3,S}
2 *3 S2d      u0 c0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 328,
    label = "thiyl_intra_De",
    group = 
"""
1 *2 CS               u0 {2,D} {3,S}
2 *3 S2d              u0 c0 {1,D}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 329,
    label = "radadd_intra_cs",
    group = 
"""
1 *1 Cs u1
""",
    kinetics = None,
)

entry(
    index = 330,
    label = "radadd_intra_cs2H",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 331,
    label = "radadd_intra_csHNd",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    H        u0 {1,S}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 332,
    label = "radadd_intra_csHDe",
    group = 
"""
1 *1 Cs               u1 {2,S} {3,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 333,
    label = "radadd_intra_csHCd",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 334,
    label = "radadd_intra_csHCt",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 335,
    label = "radadd_intra_csNdNd",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 336,
    label = "radadd_intra_csNdDe",
    group = 
"""
1 *1 Cs               u1 {2,S} {3,S}
2    [Cs,O,S]         u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 337,
    label = "radadd_intra_csNdCd",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    Cd       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 338,
    label = "radadd_intra_csNdCt",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    Ct       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 339,
    label = "radadd_intra_csDeDe",
    group = 
"""
1 *1 Cs               u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 340,
    label = "radadd_intra_O",
    group = 
"""
1 *1 O u1
""",
    kinetics = None,
)

entry(
    index = 341,
    label = "radadd_intra_S",
    group = 
"""
1 *1 S u1
""",
    kinetics = None,
)

entry(
    index = 342,
    label = "radadd_intra_Cb",
    group = 
"""
1 *1 Cb u1
""",
    kinetics = None,
)

entry(
    index = 343,
    label = "radadd_intra_cdsingle",
    group = 
"""
1 *1 Cd u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 344,
    label = "radadd_intra_cdsingleH",
    group = 
"""
1 *1 Cd u1 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 345,
    label = "radadd_intra_cdsingleNd",
    group = 
"""
1 *1 Cd       u1 {2,S}
2    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 346,
    label = "radadd_intra_cdsingleDe",
    group = 
"""
1 *1 Cd               u1 {2,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 347,
    label = "radadd_intra_cddouble",
    group = 
"""
1 *1 Cd u1 {2,D}
2    Cd u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 348,
    label = "radadd_intra_CO",
    group = 
"""
1 *1 CO u1 {2,D}
2    O  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 349,
    label = "radadd_intra_Ct",
    group = 
"""
1 *1 Ct u1 {2,T}
2    Ct u0 {1,T}
""",
    kinetics = None,
)

tree(
"""
L1: Rn
    L2: R3
        L3: R3_D
        L3: R3_T
        L3: R3_CO
        L3: R3_CS
    L2: R4
        L3: R4_S
            L4: R4_S_D
                L5: R4_Cs_RR_D
                    L6: R4_Cs_HH_D
            L4: R4_S_T
            L4: R4_S_CO
            L4: R4_S_CS
        L3: R4_D
            L4: R4_D_D
            L4: R4_D_T
            L4: R4_D_CO
            L4: R4_D_CS
        L3: R4_T
            L4: R4_T_D
            L4: R4_T_T
            L4: R4_T_CO
            L4: R4_T_CS
    L2: R5
        L3: R5_SS
            L4: R5_SS_D
                L5: R5_CsCs_RR_D
                    L6: R5_CsCs_RH_D
                        L7: R5_CsCs_HH_D
            L4: R5_SS_T
            L4: R5_SS_CO
            L4: R5_SS_CS
                L5: Cs-R5_SS_CS
                L5: H2-R5_SS_CS
        L3: R5_SM
            L4: R5_SD
                L5: R5_SD_D
                L5: R5_SD_T
                L5: R5_SD_CO
                L5: R5_SD_CS
            L4: R5_ST
                L5: R5_ST_D
                L5: R5_ST_T
                L5: R5_ST_CO
                L5: R5_ST_CS
        L3: R5_MS
            L4: R5_DS
                L5: R5_DS_D
                L5: R5_DS_T
                L5: R5_DS_CO
                L5: R5_DS_CS
            L4: R5_TS
                L5: R5_TS_D
                L5: R5_TS_T
                L5: R5_TS_CO
        L3: R5_MM
    L2: R6plus
        L3: R6
            L4: R6_RSR
                L5: R6_SSR
                    L6: R6_SSS
                        L7: R6_SSS_D
                            L8: R6_CsCsCs_RR_D
                                L9: R6_CsCsCs_RH_D
                                    L10: R6_CsCsCs_HH_D
                        L7: R6_SSS_T
                        L7: R6_SSS_CO
                    L6: R6_SSM
                        L7: R6_SSM_D
                        L7: R6_SSM_T
                        L7: R6_SSM_CO
                        L7: R6_SSM_CS
                L5: R6_MSR
                    L6: R6_DSR
                        L7: R6_DSS
                            L8: R6_DSS_D
                            L8: R6_DSS_T
                            L8: R6_DSS_CO
                        L7: R6_DSM
                            L8: R6_DSM_D
                            L8: R6_DSM_T
                            L8: R6_DSM_CO
                            L8: R6_DSM_CS
                    L6: R6_TSR
                        L7: R6_TSS
                            L8: R6_TSS_D
                            L8: R6_TSS_T
                            L8: R6_TSS_CO
                            L8: R6_TSS_CS
                        L7: R6_TSM
                            L8: R6_TSM_D
                            L8: R6_TSM_T
                            L8: R6_TSM_CO
                            L8: R6_TSM_CS
            L4: R6_SMS
                L5: R6_SMS_D
                L5: R6_SMS_T
                L5: R6_SMS_CO
            L4: R6_SMM
        L3: R7
        L3: R8
        L3: R9
            L4: R9_SSSSSD
            L4: R9_SDSSSD
    L2: Rn_cyclic
        L3: Rn0cx
            L4: Rn0cx_beta
                L5: Rn0c4_beta
                L5: Rn0c5_beta
                    L6: Rn0c5_beta_short
                    L6: Rn0c5_beta_long
                L5: Rn0c6_beta
                    L6: Rn0c6_beta_short
                    L6: Rn0c6_beta_long
                L5: Rn0c7_beta
                    L6: Rn0c7_beta_short
                    L6: Rn0c7_beta_long
                L5: Rn0c8_beta
                    L6: Rn0c8_beta_short
                    L6: Rn0c8_beta_long
            L4: Rn0cx_gamma
                L5: Rn0c6_gamma
                L5: Rn0c7_gamma
                    L6: Rn0c7_gamma_short
                    L6: Rn0c7_gamma_long
                L5: Rn0c8_gamma
                    L6: Rn0c8_gamma_short
                    L6: Rn0c8_gamma_long
            L4: Rn0cx_delta
                L5: Rn0c8_delta
        L3: Rn1cx
            L4: Rn1cx_alpha
                L5: Rn1c3_alpha
                    L6: Rn1c3_alpha_short
                    L6: Rn1c3_alpha_long
                L5: Rn1c4_alpha
                    L6: Rn1c4_alpha_short
                    L6: Rn1c4_alpha_long
                L5: Rn1c5_alpha
                    L6: Rn1c5_alpha_short
                    L6: Rn1c5_alpha_long
                L5: Rn1c6_alpha
                    L6: Rn1c6_alpha_short
                    L6: Rn1c6_alpha_long
                L5: Rn1c7_alpha
                    L6: Rn1c7_alpha_short
                    L6: Rn1c7_alpha_long
                L5: Rn1c8_alpha
                    L6: Rn1c8_alpha_short
                    L6: Rn1c8_alpha_long
        L3: Rn2cx
            L4: Rn2cx_alpha
                L5: Rn2c3_alpha
                    L6: Rn2c3_alpha_short
                    L6: Rn2c3_alpha_long
                L5: Rn2c4_alpha
                    L6: Rn2c4_alpha_short
                    L6: Rn2c4_alpha_long
                L5: Rn2c5_alpha
                    L6: Rn2c5_alpha_short
                    L6: Rn2c5_alpha_long
                L5: Rn2c6_alpha
                    L6: Rn2c6_alpha_short
                    L6: Rn2c6_alpha_long
                L5: Rn2c7_alpha
                    L6: Rn2c7_alpha_short
                    L6: Rn2c7_alpha_long
                L5: Rn2c8_alpha
                    L6: Rn2c8_alpha_short
                    L6: Rn2c8_alpha_long
            L4: Rn2cx_beta
                L5: Rn2c4_beta
                L5: Rn2c5_beta
                    L6: Rn2c5_beta_short
                    L6: Rn2c5_beta_long
                L5: Rn2c6_beta
                    L6: Rn2c6_beta_short
                    L6: Rn2c6_beta_long
                L5: Rn2c7_beta
                    L6: Rn2c7_beta_short
                    L6: Rn2c7_beta_long
                L5: Rn2c8_beta
                    L6: Rn2c8_beta_short
                    L6: Rn2c8_beta_long
        L3: Rn3cx
            L4: Rn3cx_alpha
                L5: Rn3c3_alpha
                    L6: Rn3c3_alpha_short
                    L6: Rn3c3_alpha_long
                L5: Rn3c4_alpha
                    L6: Rn3c4_alpha_short
                    L6: Rn3c4_alpha_long
                L5: Rn3c5_alpha
                    L6: Rn3c5_alpha_short
                    L6: Rn3c5_alpha_long
                L5: Rn3c6_alpha
                    L6: Rn3c6_alpha_short
                    L6: Rn3c6_alpha_long
                L5: Rn3c7_alpha
                    L6: Rn3c7_alpha_short
                    L6: Rn3c7_alpha_long
                L5: Rn3c8_alpha
                    L6: Rn3c8_alpha_short
                    L6: Rn3c8_alpha_long
            L4: Rn3cx_beta
                L5: Rn3c4_beta
                L5: Rn3c5_beta
                    L6: Rn3c5_beta_short
                    L6: Rn3c5_beta_long
                L5: Rn3c6_beta
                    L6: Rn3c6_beta_short
                    L6: Rn3c6_beta_long
                L5: Rn3c7_beta
                    L6: Rn3c7_beta_short
                    L6: Rn3c7_beta_long
                L5: Rn3c8_beta
                    L6: Rn3c8_beta_short
                    L6: Rn3c8_beta_long
            L4: Rn3cx_gamma
                L5: Rn3c6_gamma
                L5: Rn3c7_gamma
                    L6: Rn3c7_gamma_short
                    L6: Rn3c7_gamma_long
                L5: Rn3c8_gamma
                    L6: Rn3c8_gamma_short
                    L6: Rn3c8_gamma_long
        L3: Rn4cx
            L4: Rn4cx_alpha
                L5: Rn4c3_alpha
                    L6: Rn4c3_alpha_short
                    L6: Rn4c3_alpha_long
                L5: Rn4c4_alpha
                    L6: Rn4c4_alpha_short
                    L6: Rn4c4_alpha_long
                L5: Rn4c5_alpha
                    L6: Rn4c5_alpha_short
                    L6: Rn4c5_alpha_long
                L5: Rn4c6_alpha
                    L6: Rn4c6_alpha_short
                    L6: Rn4c6_alpha_long
                L5: Rn4c7_alpha
                    L6: Rn4c7_alpha_short
                    L6: Rn4c7_alpha_long
                L5: Rn4c8_alpha
                    L6: Rn4c8_alpha_short
                    L6: Rn4c8_alpha_long
            L4: Rn4cx_beta
                L5: Rn4c4_beta
                L5: Rn4c5_beta
                    L6: Rn4c5_beta_short
                    L6: Rn4c5_beta_long
                L5: Rn4c6_beta
                    L6: Rn4c6_beta_short
                    L6: Rn4c6_beta_long
                L5: Rn4c7_beta
                    L6: Rn4c7_beta_short
                    L6: Rn4c7_beta_long
                L5: Rn4c8_beta
                    L6: Rn4c8_beta_short
                    L6: Rn4c8_beta_long
        L3: Rn5cx
            L4: Rn5cx_alpha
                L5: Rn5c3_alpha
                    L6: Rn5c3_alpha_short
                    L6: Rn5c3_alpha_long
                L5: Rn5c4_alpha
                    L6: Rn5c4_alpha_short
                    L6: Rn5c4_alpha_long
                L5: Rn5c5_alpha
                    L6: Rn5c5_alpha_short
                    L6: Rn5c5_alpha_long
                L5: Rn5c6_alpha
                    L6: Rn5c6_alpha_short
                    L6: Rn5c6_alpha_long
                L5: Rn5c7_alpha
                    L6: Rn5c7_alpha_short
                    L6: Rn5c7_alpha_long
                L5: Rn5c8_alpha
                    L6: Rn5c8_alpha_short
                    L6: Rn5c8_alpha_long
L1: multiplebond_intra
    L2: doublebond_intra
        L3: doublebond_intra_pri
            L4: doublebond_intra_pri_2H
            L4: doublebond_intra_pri_HNd
            L4: doublebond_intra_pri_HDe
                L5: doublebond_intra_pri_HCd
                L5: doublebond_intra_pri_HCt
            L4: doublebond_intra_pri_NdNd
            L4: doublebond_intra_pri_NdDe
                L5: doublebond_intra_pri_NdCd
                L5: doublebond_intra_pri_NdCt
            L4: doublebond_intra_pri_DeDe
        L3: doublebond_intra_secNd
            L4: doublebond_intra_secNd_2H
            L4: doublebond_intra_secNd_HNd
            L4: doublebond_intra_secNd_HDe
                L5: doublebond_intra_secNd_HCd
                L5: doublebond_intra_secNd_HCt
            L4: doublebond_intra_secNd_NdNd
            L4: doublebond_intra_secNd_NdDe
                L5: doublebond_intra_secNd_NdCd
                L5: doublebond_intra_secNd_NdCt
            L4: doublebond_intra_secNd_DeDe
        L3: doublebond_intra_secDe
            L4: doublebond_intra_secDe_2H
            L4: doublebond_intra_secDe_HNd
            L4: doublebond_intra_secDe_HDe
                L5: doublebond_intra_secDe_HCd
                L5: doublebond_intra_secDe_HCt
            L4: doublebond_intra_secDe_NdNd
            L4: doublebond_intra_secDe_NdDe
                L5: doublebond_intra_secDe_NdCd
                L5: doublebond_intra_secDe_NdCt
            L4: doublebond_intra_secDe_DeDe
    L2: triplebond_intra
        L3: triplebond_intra_H
        L3: triplebond_intra_Nd
        L3: triplebond_intra_De
    L2: carbonyl_intra
        L3: carbonyl_intra_H
        L3: carbonyl_intra_Nd
        L3: carbonyl_intra_De
    L2: thiyl_intra
        L3: thiyl_intra_H
        L3: thiyl_intra_Nd
        L3: thiyl_intra_De
L1: radadd_intra
    L2: radadd_intra_cs
        L3: radadd_intra_cs2H
        L3: radadd_intra_csHNd
        L3: radadd_intra_csHDe
            L4: radadd_intra_csHCd
            L4: radadd_intra_csHCt
        L3: radadd_intra_csNdNd
        L3: radadd_intra_csNdDe
            L4: radadd_intra_csNdCd
            L4: radadd_intra_csNdCt
        L3: radadd_intra_csDeDe
    L2: radadd_intra_O
    L2: radadd_intra_S
    L2: radadd_intra_Cb
    L2: radadd_intra_cdsingle
        L3: radadd_intra_cdsingleH
        L3: radadd_intra_cdsingleNd
        L3: radadd_intra_cdsingleDe
    L2: radadd_intra_cddouble
    L2: radadd_intra_CO
    L2: radadd_intra_Ct
"""
)

forbidden(
    label = "bond31",
    group = 
"""
1 *3 R!H u0 c0 {2,[S,D]}
2 *1 R!H u1 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "bond31rad",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *1 R!H u1 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

