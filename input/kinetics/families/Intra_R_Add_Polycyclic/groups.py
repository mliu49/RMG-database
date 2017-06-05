#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Polycyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn_cyclic"], products=["RnCycle"], ownReverse=False)

reverse = "Ring_Open_Poly_Cycli_Radical"

recipe(actions=[
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['FORM_BOND', '*1', 1, '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['GAIN_RADICAL', '*3', '1'],
])

boundaryAtoms = ["*1", "*2"]

entry(
    index = 1,
    label = "Rn_cyclic",
    group = "OR{Rn1cx, Rn2cx, Rn3cx, Rn4cx}",
    kinetics = None,
)

entry(
    index = 2,
    label = "multiplebond_intra",
    group =
"""
1 *2 [Cd,Ct,Cb,Cbf,CO,N]        u0 {2,[D,T,B]}
2 *3 [Cd,Ct,Cb,Cbf,Od,Sd,Cdd,N] u0 {1,[D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "radadd_intra",
    group =
"""
1 *1 R!H u1
""",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn1cx",
    group = "OR{Rn1cx_alpha, Rn1cx_beta, Rn1cx_gamma, Rn1cx_delta}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn1cx_alpha",
    group = "OR{Rn1c3_alpha, Rn1c4_alpha, Rn1c5_alpha, Rn1c6_alpha, Rn1c7_alpha, Rn1c8_alpha}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn1cx_beta",
    group = "OR{Rn1c4_beta, Rn1cx_beta_short, Rn1cx_beta_long}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn1cx_beta_short",
    group = "OR{Rn1c5_beta_short, Rn1c6_beta_short, Rn1c7_beta_short, Rn1c8_beta_short}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn1cx_beta_long",
    group = "OR{Rn1c5_beta_long, Rn1c6_beta_long, Rn1c7_beta_long, Rn1c8_beta_long}",
    kinetics = None,
)

entry(
    index=290,
    label="Rn1cx_gamma",
    group="OR{Rn1c6_gamma, Rn1cx_gamma_short, Rn1cx_gamma_long}",
    kinetics=None,
)

entry(
    index=290,
    label="Rn1cx_gamma_short",
    group="OR{Rn1c7_gamma_short, Rn1c8_gamma_short}",
    kinetics=None,
)

entry(
    index=290,
    label="Rn1cx_gamma_long",
    group="OR{Rn1c7_gamma_long, Rn1c8_gamma_long}",
    kinetics=None,
)

entry(
    index=290,
    label="Rn1cx_delta",
    group="OR{Rn1c8_delta}",
    kinetics=None,
)



entry(
    index = 290,
    label = "Rn2cx",
    group = "OR{Rn2cx_alpha, Rn2cx_beta, Rn2cx_gamma}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn2cx_alpha",
    group = "OR{Rn2c3_alpha, Rn2c4_alpha, Rn2c5_alpha, Rn2c6_alpha, Rn2c7_alpha, Rn2c8_alpha}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn2cx_beta",
    group = "OR{Rn2c4_beta, Rn2cx_beta_short, Rn2cx_beta_long}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn2cx_beta_short",
    group = "OR{Rn2c5_beta_short, Rn2c6_beta_short, Rn2c7_beta_short, Rn2c8_beta_short}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn2cx_beta_long",
    group = "OR{Rn2c5_beta_long, Rn2c6_beta_long, Rn2c7_beta_long, Rn2c8_beta_long}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn2cx_gamma",
    group = "OR{Rn2c6_gamma, Rn2cx_gamma_short, Rn2cx_gamma_long}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn2cx_gamma_short",
    group = "OR{Rn2c7_gamma_short, Rn2c8_gamma_short}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn2cx_gamma_long",
    group = "OR{Rn2c7_gamma_long, Rn2c8_gamma_long}",
    kinetics = None,
)



entry(
    index = 290,
    label = "Rn3cx",
    group = "OR{Rn3cx_alpha, Rn3cx_beta}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn3cx_alpha",
    group = "OR{Rn3c3_alpha, Rn3c4_alpha, Rn3c5_alpha, Rn3c6_alpha, Rn3c7_alpha, Rn3c8_alpha}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn3cx_beta",
    group = "OR{Rn3c4_beta, Rn3cx_beta_short, Rn3cx_beta_long}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn3cx_beta_short",
    group = "OR{Rn3c5_beta_short, Rn3c6_beta_short, Rn3c7_beta_short, Rn3c8_beta_short}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn3cx_beta_long",
    group = "OR{Rn3c5_beta_long, Rn3c6_beta_long, Rn3c7_beta_long, Rn3c8_beta_long}",
    kinetics = None,
)


entry(
    index = 290,
    label = "Rn4cx",
    group = "OR{Rn4cx_alpha}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rn4cx_alpha",
    group = "OR{Rn4c3_alpha, Rn4c4_alpha, Rn4c5_alpha, Rn4c6_alpha, Rn4c7_alpha, Rn4c8_alpha}",
    kinetics = None,
)



entry(
    index = 254,
    label = "Rn4c3_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {3,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {1,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 255,
    label = "Rn3c3_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {3,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {1,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 256,
    label = "Rn2c3_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {3,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3 *5 R!H ux r1 {2,[S,D,T,B]} {1,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 257,
    label = "Rn1c3_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {3,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {1,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 r0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 260,
    label = "Rn4c4_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {4,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H ux r1 {3,[S,D,T,B]} {1,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 261,
    label = "Rn3c4_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {4,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H ux r1 {3,[S,D,T,B]} {1,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 262,
    label = "Rn2c4_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {4,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H ux r1 {3,[S,D,T,B]} {1,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 263,
    label = "Rn1c4_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {4,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {1,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 r0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 265,
    label = "Rn3c4_beta",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {4,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3 *7 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
4 *5 R!H ux r1 {3,[S,D,T,B]} {1,[S,D,T,B]}
5 *6 R!H ux r0 {3,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 266,
    label = "Rn2c4_beta",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {4,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3 *6 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
4 *5 R!H ux r1 {3,[S,D,T,B]} {1,[S,D,T,B]}
5 *4 R!H ux r0 {3,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 267,
    label = "Rn1c4_beta",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {4,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
4 *5 R!H ux r1 {3,[S,D,T,B]} {1,[S,D,T,B]}
5 *1 R!H u1 r0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 270,
    label = "Rn4c5_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux r1 {4,[S,D,T,B]} {1,[S,D,T,B]} {6,[S,D,T,B]}
6 *7 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *6 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 271,
    label = "Rn3c5_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux r1 {4,[S,D,T,B]} {1,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 272,
    label = "Rn2c5_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux r1 {4,[S,D,T,B]} {1,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 273,
    label = "Rn1c5_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r1 {4,[S,D,T,B]} {1,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 r0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 275,
    label = "Rn3c5_beta_long",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3 *7 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux r1 {4,[S,D,T,B]} {1,[S,D,T,B]}
6 *6 R!H ux r0 {3,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 276,
    label = "Rn2c5_beta_long",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3 *6 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux r1 {4,[S,D,T,B]} {1,[S,D,T,B]}
6 *4 R!H ux r0 {3,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 277,
    label = "Rn1c5_beta_long",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux r1 {4,[S,D,T,B]} {1,[S,D,T,B]}
6 *1 R!H u1 r0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 279,
    label = "Rn3c5_beta_short",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
5 *5 R!H ux r1 {4,[S,D,T,B]} {1,[S,D,T,B]}
6 *6 R!H ux r0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 280,
    label = "Rn2c5_beta_short",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
5 *5 R!H ux r1 {4,[S,D,T,B]} {1,[S,D,T,B]}
6 *4 R!H ux r0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 281,
    label = "Rn1c5_beta_short",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {5,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
5 *5 R!H ux r1 {4,[S,D,T,B]} {1,[S,D,T,B]}
6 *1 R!H u1 r0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 284,
    label = "Rn4c6_alpha",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *5 R!H ux r1 {5,[S,D,T,B]} {1,[S,D,T,B]} {7,[S,D,T,B]}
7  *7 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *6 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4 R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 285,
    label = "Rn3c6_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux r1 {5,[S,D,T,B]} {1,[S,D,T,B]} {7,[S,D,T,B]}
7 *6 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)
entry(
    index = 286,
    label = "Rn2c6_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux r1 {5,[S,D,T,B]} {1,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 287,
    label = "Rn1c6_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux r1 {5,[S,D,T,B]} {1,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 289,
    label = "Rn3c6_beta_long",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *7 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
4 *8 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *9 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux r1 {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *6 R!H ux r0 {3,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 291,
    label = "Rn2c6_beta_long",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *6 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
4 *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux r1 {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *4 R!H ux r0 {3,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 292,
    label = "Rn1c6_beta_long",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux r1 {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *1 R!H u1 r0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 294,
    label = "Rn3c6_beta_short",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
6 *5 R!H ux r1 {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *6 R!H ux r0 {5,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 295,
    label = "Rn2c6_beta_short",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
6 *5 R!H ux r1 {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *4 R!H ux r0 {5,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 296,
    label = "Rn1c6_beta_short",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
6 *5 R!H ux r1 {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *1 R!H u1 r0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 298,
    label = "Rn2c6_gamma",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
5 *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux r1 {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *4 R!H ux r0 {4,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 299,
    label = "Rn1c6_gamma",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
5 *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux r1 {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *1 R!H u1 r0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 302,
    label = "Rn4c7_alpha",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux r1 {6,[S,D,T,B]} {1,[S,D,T,B]} {8,[S,D,T,B]}
8  *7 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *6 R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *4 R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1 R!H u1 r0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 303,
    label = "Rn3c7_alpha",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux r1 {6,[S,D,T,B]} {1,[S,D,T,B]} {8,[S,D,T,B]}
8  *6 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4 R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 304,
    label = "Rn2c7_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *5 R!H ux r1 {6,[S,D,T,B]} {1,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux r0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 305,
    label = "Rn1c7_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux r1 {6,[S,D,T,B]} {1,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 307,
    label = "Rn3c7_beta_long",
    group =
"""
1  *2  R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2  *3  R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3  *7  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
4  *8  R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *10 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5  R!H ux r1 {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *6  R!H ux r0 {3,[S,D,T,B]} {9,[S,D,T,B]}
9  *4  R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 308,
    label = "Rn2c7_beta_long",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3  *6 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
4  *7 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux r1 {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *4 R!H ux r0 {3,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 309,
    label = "Rn1c7_beta_long",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3  *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
4  *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux r1 {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *1 R!H u1 r0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 311,
    label = "Rn3c7_beta_short",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *7 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
7  *5 R!H ux r1 {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *6 R!H ux r0 {6,[S,D,T,B]} {9,[S,D,T,B]}
9  *4 R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 312,
    label = "Rn2c7_beta_short",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *6 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
7  *5 R!H ux r1 {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *4 R!H ux r0 {6,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 313,
    label = "Rn1c7_beta_short",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
7  *5 R!H ux r1 {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 315,
    label = "Rn2c7_gamma_long",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {8,[S,D,T,B]}
5  *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux r1 {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *4 R!H ux r0 {4,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 316,
    label = "Rn1c7_gamma_long",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {8,[S,D,T,B]}
5  *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *7 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux r1 {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *1 R!H u1 r0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 318,
    label = "Rn2c7_gamma_short",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
6  *7 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux r1 {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *4 R!H ux r0 {5,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 319,
    label = "Rn1c7_gamma_short",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {7,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
6  *6 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux r1 {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *1 R!H u1 r0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 320,
    label = "Rn4c8_alpha",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]} {9,[S,D,T,B]}
9  *7 R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *6 R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *4 R!H ux r0 {10,[S,D,T,B]} {12,[S,D,T,B]}
12 *1 R!H u1 r0 {11,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 323,
    label = "Rn3c8_alpha",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]} {9,[S,D,T,B]}
9  *6 R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *4 R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1 R!H u1 r0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 324,
    label = "Rn2c8_alpha",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]} {9,[S,D,T,B]}
9  *4 R!H ux r0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 325,
    label = "Rn1c8_alpha",
    group =
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3    R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 r0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 327,
    label = "Rn3c8_beta_long",
    group =
"""
1  *2  R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *3  R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3  *7  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {9,[S,D,T,B]}
4  *8  R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *10 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *11 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5  R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *6  R!H ux r0 {3,[S,D,T,B]} {10,[S,D,T,B]}
10 *4  R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1  R!H u1 r0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 328,
    label = "Rn2c8_beta_long",
    group =
"""
1  *2  R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *3  R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3  *6  R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {9,[S,D,T,B]}
4  *7  R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8  R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9  R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *10 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5  R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *4  R!H ux r0 {3,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 329,
    label = "Rn1c8_beta_long",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3  *4 R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]} {9,[S,D,T,B]}
4  *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *9 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *1 R!H u1 r0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 331,
    label = "Rn3c8_beta_short",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *7 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]} {9,[S,D,T,B]}
8  *5 R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *6 R!H ux r0 {7,[S,D,T,B]} {10,[S,D,T,B]}
10 *4 R!H ux r0 {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1 R!H u1 r0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 332,
    label = "Rn2c8_beta_short",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *6 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]} {9,[S,D,T,B]}
8  *5 R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *4 R!H ux r0 {7,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 333,
    label = "Rn1c8_beta_short",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *4 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]} {9,[S,D,T,B]}
8  *5 R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *1 R!H u1 r0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 335,
    label = "Rn2c8_gamma_long",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {9,[S,D,T,B]}
5  *7 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *9 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *4 R!H ux r0 {4,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)
entry(
    index = 336,
    label = "Rn1c8_gamma_long",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *4 R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]} {9,[S,D,T,B]}
5  *6 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *7 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *8 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *1 R!H u1 r0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 338,
    label = "Rn2c8_gamma_short",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *6 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
7  *7 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *4 R!H ux r0 {6,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 r0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 339,
    label = "Rn1c8_gamma_short",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
7  *6 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *1 R!H u1 r0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 341,
    label = "Rn1c8_delta",
    group =
"""
1  *2 R!H u0 r1 {2,[D,T,B]} {8,[S,D,T,B]}
2  *3 R!H u0 r1 {1,[D,T,B]} {3,[S,D,T,B]}
3     R!H ux r1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux r1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux r1 {4,[S,D,T,B]} {6,[S,D,T,B]} {9,[S,D,T,B]}
6  *6 R!H ux r1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *7 R!H ux r1 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux r1 {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *1 R!H u1 r0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

################################################################################



entry(
    index = 194,
    label = "doublebond_intra",
    group =
"""
1 *2 Cd       u0 {2,D}
2 *3 [Cd,Cdd] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 219,
    label = "triplebond_intra",
    group =
"""
1 *2 Ct u0 {2,T}
2 *3 Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 400,
    label = "benzenebond_intra",
    group =
"""
1 *2 [Cb,Cbf] u0 {2,B}
2 *3 [Cb,Cbf] u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 401,
    label = "benzenebond_intra_R",
    group =
"""
1 *2 Cb  u0 {2,B} {3,S}
2 *3 Cb  u0 {1,B}
3    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 402,
    label = "benzenebond_intra_RH",
    group =
"""
1 *2 Cb  u0 {2,B} {3,S}
2 *3 Cb  u0 {1,B} {4,S}
3    R!H u0 {1,S}
4    H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 403,
    label = "benzenebond_intra_H",
    group =
"""
1 *2 Cb u0 {2,B} {3,S}
2 *3 Cb u0 {1,B}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 404,
    label = "benzenebond_intra_HH",
    group =
"""
1 *2 Cb u0 {2,B} {3,S}
2 *3 Cb u0 {1,B} {4,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 405,
    label = "benzenebond_intra_CbCbf",
    group =
"""
1 *2 Cb  u0 {2,B}
2 *3 Cbf u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 406,
    label = "benzenebond_intra_CbfCb",
    group =
"""
1 *2 Cbf u0 {2,B}
2 *3 Cb  u0 {1,B}
""",
    kinetics = None,
)

entry(
    index = 407,
    label = "benzenebond_intra_CbfCbf",
    group =
"""
1 *2 Cbf u0 {2,B}
2 *3 Cbf u0 {1,B}
""",
    kinetics = None,
)

################################################################################

entry(
    index = 227,
    label = "radadd_intra_cs",
    group =
"""
1 *1 Cs u1
""",
    kinetics = None,
)

entry(
    index = 228,
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
    index = 229,
    label = "radadd_intra_csHNd",
    group =
"""
1 *1 Cs     u1 {2,S} {3,S}
2    H      u0 {1,S}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 230,
    label = "radadd_intra_csHDe",
    group =
"""
1 *1 Cs            u1 {2,S} {3,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 235,
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
    index = 236,
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
    index = 237,
    label = "radadd_intra_csNdNd",
    group =
"""
1 *1 Cs     u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 232,
    label = "radadd_intra_csNdDe",
    group =
"""
1 *1 Cs            u1 {2,S} {3,S}
2    [Cs,O,S]      u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 239,
    label = "radadd_intra_csNdCd",
    group =
"""
1 *1 Cs     u1 {2,S} {3,S}
2    [Cs,O] u0 {1,S}
3    Cd     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 240,
    label = "radadd_intra_csNdCt",
    group =
"""
1 *1 Cs     u1 {2,S} {3,S}
2    [Cs,O] u0 {1,S}
3    Ct     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 241,
    label = "radadd_intra_csDeDe",
    group =
"""
1 *1 Cs            u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 234,
    label = "radadd_intra_O",
    group =
"""
1 *1 O u1
""",
    kinetics = None,
)

entry(
    index = 235,
    label = "radadd_intra_Cb",
    group =
"""
1 *1 Cb u1
""",
    kinetics = None,
)

entry(
    index = 236,
    label = "radadd_intra_cdsingle",
    group =
"""
1 *1 Cd u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 237,
    label = "radadd_intra_cdsingleH",
    group =
"""
1 *1 Cd u1 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 238,
    label = "radadd_intra_cdsingleNd",
    group =
"""
1 *1 Cd     u1 {2,S}
2    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 239,
    label = "radadd_intra_cdsingleDe",
    group =
"""
1 *1 Cd            u1 {2,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 240,
    label = "radadd_intra_cddouble",
    group =
"""
1 *1 Cd u1 {2,D}
2    Cd u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 241,
    label = "radadd_intra_CO",
    group =
"""
1 *1 CO u1 {2,D}
2    O  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 242,
    label = "radadd_intra_Ct",
    group =
"""
1 *1 Ct u1 {2,T}
2    Ct u0 {1,T}
""",
    kinetics = None,
)

################################################################################

tree(
"""
L1: Rn_cyclic
    L2: Rn1cx
        L3: Rn1cx_alpha
            L4: Rn1c3_alpha
            L4: Rn1c4_alpha
            L4: Rn1c5_alpha
            L4: Rn1c6_alpha
            L4: Rn1c7_alpha
            L4: Rn1c8_alpha
        L3: Rn1cx_beta
            L4: Rn1c4_beta
            L4: Rn1cx_beta_short
                L5: Rn1c5_beta_short
                L5: Rn1c6_beta_short
                L5: Rn1c7_beta_short
                L5: Rn1c8_beta_short
            L4: Rn1cx_beta_long
                L5: Rn1c5_beta_long
                L5: Rn1c6_beta_long
                L5: Rn1c7_beta_long
                L5: Rn1c8_beta_long
        L3: Rn1cx_gamma
            L4: Rn1c6_gamma
            L4: Rn1cx_gamma_short
                L5: Rn1c7_gamma_short
                L5: Rn1c8_gamma_short
            L4: Rn1cx_gamma_long
                L5: Rn1c7_gamma_long
                L5: Rn1c8_gamma_long
        L3: Rn1cx_delta
            L4: Rn1c8_delta
    L2: Rn2cx
        L3: Rn2cx_alpha
            L4: Rn2c3_alpha
            L4: Rn2c4_alpha
            L4: Rn2c5_alpha
            L4: Rn2c6_alpha
            L4: Rn2c7_alpha
            L4: Rn2c8_alpha
        L3: Rn2cx_beta
            L4: Rn2c4_beta
            L4: Rn2cx_beta_short
                L5: Rn2c5_beta_short
                L5: Rn2c6_beta_short
                L5: Rn2c7_beta_short
                L5: Rn2c8_beta_short
            L4: Rn2cx_beta_long
                L5: Rn2c5_beta_long
                L5: Rn2c6_beta_long
                L5: Rn2c7_beta_long
                L5: Rn2c8_beta_long
        L3: Rn2cx_gamma
            L4: Rn2c6_gamma
            L4: Rn2cx_gamma_short
                L5: Rn2c7_gamma_short
                L5: Rn2c8_gamma_short
            L4: Rn2cx_gamma_long
                L5: Rn2c7_gamma_long
                L5: Rn2c8_gamma_long
    L2: Rn3cx
        L3: Rn3cx_alpha
            L4: Rn3c3_alpha
            L4: Rn3c4_alpha
            L4: Rn3c5_alpha
            L4: Rn3c6_alpha
            L4: Rn3c7_alpha
            L4: Rn3c8_alpha
        L3: Rn3cx_beta
            L4: Rn3c4_beta
            L4: Rn3cx_beta_short
                L5: Rn3c5_beta_short
                L5: Rn3c6_beta_short
                L5: Rn3c7_beta_short
                L5: Rn3c8_beta_short
            L4: Rn3cx_beta_long
                L5: Rn3c5_beta_long
                L5: Rn3c6_beta_long
                L5: Rn3c7_beta_long
                L5: Rn3c8_beta_long
    L2: Rn4cx
        L3: Rn4cx_alpha
            L4: Rn4c3_alpha
            L4: Rn4c4_alpha
            L4: Rn4c5_alpha
            L4: Rn4c6_alpha
            L4: Rn4c7_alpha
            L4: Rn4c8_alpha
L1: multiplebond_intra
    L2: doublebond_intra
    L2: triplebond_intra
    L2: benzenebond_intra
        L3: benzenebond_intra_R
            L4: benzenebond_intra_RH
        L3: benzenebond_intra_H
            L4: benzenebond_intra_HH
        L3: benzenebond_intra_CbCbf
        L3: benzenebond_intra_CbfCb
        L3: benzenebond_intra_CbfCbf
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
