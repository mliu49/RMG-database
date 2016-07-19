#!/usr/bin/env python
# encoding: utf-8

name = "PAHLibrary"
shortDesc = u""
longDesc = u"""
Blanquart, G.; Pitsch, H. Thermochemical Properties of Polycyclic Aromatic Hydrocarbons (PAH) from G3MP2B3 Calculations. 2007.
"""
entry(
    index = 1,
    label = "A1",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {1,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.51558,0.0645453,-4.41403e-05,7.47712e-09,3.10282e-12,9110.31,46.5332], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-0.206241,0.0464122,-2.77654e-05,7.88911e-09,-8.60365e-13,8098.84,20.6567], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "A1-",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,D} {5,S} {9,S}
4  C u0 p0 c0 {2,D} {6,S} {10,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  C u1 p0 c0 {4,S} {5,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.87655,0.0626806,-4.87402e-05,1.41122e-08,5.18518e-13,39926.9,45.9964], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.38016,0.0404032,-2.42251e-05,6.88723e-09,-7.50961e-13,38697.4,15.5221], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "A1C2H",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {6,D} {13,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  C u0 p0 c0 {3,D} {5,S} {12,S}
7  C u0 p0 c0 {1,S} {8,T}
8  C u0 p0 c0 {7,T} {14,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.21037,0.0865552,-8.45007e-05,4.21921e-08,-8.16766e-12,35248.9,46.9445], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.8152,0.0440873,-2.52054e-05,6.90275e-09,-7.31379e-13,33027.2,-6.49321], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "A1C2H-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,D} {7,S}
2  C u0 p0 c0 {3,D} {4,S} {10,S}
3  C u0 p0 c0 {1,S} {2,D} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  C u1 p0 c0 {1,D} {5,S}
7  C u0 p0 c0 {1,S} {8,T}
8  C u0 p0 c0 {7,T} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.42758,0.0836669,-8.70106e-05,4.70286e-08,-1.01817e-11,67330.2,44.8118], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.23812,0.0383812,-2.18851e-05,5.97161e-09,-6.30351e-13,64952.8,-11.7513], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "A1C2H-3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,D} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  C u0 p0 c0 {1,D} {6,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {12,S}
6  C u1 p0 c0 {4,S} {5,D}
7  C u0 p0 c0 {1,S} {8,T}
8  C u0 p0 c0 {7,T} {13,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.56829,0.0844648,-8.8469e-05,4.81804e-08,-1.05215e-11,67893.9,45.3532], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.31642,0.0382474,-2.17939e-05,5.94358e-09,-6.27138e-13,65473.2,-12.2582], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "A1C2H-4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {3,D} {6,S} {12,S}
6  C u1 p0 c0 {4,D} {5,S}
7  C u0 p0 c0 {1,S} {8,T}
8  C u0 p0 c0 {7,T} {13,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.49497,0.0839558,-8.74232e-05,4.72828e-08,-1.02393e-11,67844.8,44.3195], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.24043,0.0383971,-2.19039e-05,5.97895e-09,-6.3131e-13,65453.4,-12.5807], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "A1C2H3",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {10,S}
3  C u0 p0 c0 {1,S} {7,D} {14,S}
4  C u0 p0 c0 {1,S} {8,D} {9,S}
5  C u0 p0 c0 {2,S} {6,D} {11,S}
6  C u0 p0 c0 {5,D} {7,S} {12,S}
7  C u0 p0 c0 {3,D} {6,S} {13,S}
8  C u0 p0 c0 {4,D} {15,S} {16,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.385,0.0820365,-5.34462e-05,5.59095e-09,5.61139e-12,16085.8,50.1105], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.540554,0.0617302,-3.73947e-05,1.07047e-08,-1.17305e-12,15041.3,21.4503], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "i-A1C2H2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {8,S}
2  C u0 p0 c0 {1,D} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {6,D} {13,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  C u0 p0 c0 {3,D} {5,S} {12,S}
7  C u0 p0 c0 {8,D} {14,S} {15,S}
8  C u1 p0 c0 {1,S} {7,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.58086,0.0850864,-7.39246e-05,3.03984e-08,-3.9291e-12,41966.4,45.8553], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.68084,0.0504138,-2.93059e-05,8.13188e-09,-8.70429e-13,40123,0.898426], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "n-A1C2H2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {6,D} {13,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  C u0 p0 c0 {3,D} {5,S} {12,S}
7  C u0 p0 c0 {1,S} {8,D} {14,S}
8  C u1 p0 c0 {7,D} {15,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.31199,0.0951098,-9.56352e-05,4.9778e-08,-1.02324e-11,45733.1,53.5475], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.85935,0.0472571,-2.69865e-05,7.35312e-09,-7.74901e-13,43319.9,-5.22359], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "A1C2H3-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,D}
2  C u0 p0 c0 {1,S} {3,D} {12,S}
3  C u0 p0 c0 {2,D} {5,S} {11,S}
4  C u0 p0 c0 {1,S} {7,D} {9,S}
5  C u0 p0 c0 {3,S} {6,D} {10,S}
6  C u0 p0 c0 {5,D} {8,S} {13,S}
7  C u0 p0 c0 {4,D} {14,S} {15,S}
8  C u1 p0 c0 {1,D} {6,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.36215,0.0867033,-7.54298e-05,3.0114e-08,-3.40681e-12,47781.8,50.7408], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.90115,0.0515894,-3.05081e-05,8.55911e-09,-9.23047e-13,45993.5,5.96931], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "A1(C2H)2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,D} {5,S} {11,S}
4  C u0 p0 c0 {2,D} {6,S} {14,S}
5  C u0 p0 c0 {3,S} {6,D} {12,S}
6  C u0 p0 c0 {4,S} {5,D} {13,S}
7  C u0 p0 c0 {1,S} {9,T}
8  C u0 p0 c0 {2,S} {10,T}
9  C u0 p0 c0 {7,T} {15,S}
10 C u0 p0 c0 {8,T} {16,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.36135,0.112369,-0.000135377,8.87717e-08,-2.41127e-11,61868.6,47.3893], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.7021,0.0375307,-1.92386e-05,4.75486e-09,-4.59816e-13,57785,-45.4355], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "A2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {5,S} {6,D}
3  C u0 p0 c0 {1,D} {8,S} {13,S}
4  C u0 p0 c0 {1,S} {9,D} {14,S}
5  C u0 p0 c0 {2,S} {10,D} {17,S}
6  C u0 p0 c0 {2,D} {7,S} {18,S}
7  C u0 p0 c0 {6,S} {8,D} {11,S}
8  C u0 p0 c0 {3,S} {7,D} {12,S}
9  C u0 p0 c0 {4,D} {10,S} {15,S}
10 C u0 p0 c0 {5,D} {9,S} {16,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.72435,0.105376,-8.01711e-05,2.18546e-08,1.42067e-12,14806,61.9828], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.76826,0.0689144,-4.14322e-05,1.17914e-08,-1.28597e-12,12688.4,10.6257], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "A2-1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,D}
2  C u0 p0 c0 {1,S} {5,S} {10,D}
3  C u0 p0 c0 {1,S} {7,D} {15,S}
4  C u0 p0 c0 {1,D} {8,S} {16,S}
5  C u0 p0 c0 {2,S} {6,D} {12,S}
6  C u0 p0 c0 {5,D} {7,S} {13,S}
7  C u0 p0 c0 {3,D} {6,S} {14,S}
8  C u0 p0 c0 {4,S} {9,D} {11,S}
9  C u0 p0 c0 {8,D} {10,S} {17,S}
10 C u1 p0 c0 {2,D} {9,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.02718,0.102925,-8.34272e-05,2.72135e-08,-7.2456e-13,50136.3,60.8902], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.22892,0.0631264,-3.80582e-05,1.08454e-08,-1.18343e-12,47840.1,5.82017], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "A2-2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,D}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {6,D} {11,S}
4  C u0 p0 c0 {1,S} {7,D} {14,S}
5  C u0 p0 c0 {1,D} {9,S} {15,S}
6  C u0 p0 c0 {3,D} {7,S} {12,S}
7  C u0 p0 c0 {4,D} {6,S} {13,S}
8  C u0 p0 c0 {2,D} {10,S} {17,S}
9  C u0 p0 c0 {5,S} {10,D} {16,S}
10 C u1 p0 c0 {8,S} {9,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.00769,0.103041,-8.38191e-05,2.76492e-08,-8.88842e-13,49974.1,60.7299], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.29951,0.0630133,-3.7976e-05,1.08181e-08,-1.18008e-12,47665.8,5.41216], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "A2C2HB",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,D} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {4,S} {8,D} {11,S}
4  C u0 p0 c0 {2,D} {3,S} {19,S}
5  C u0 p0 c0 {1,D} {8,S} {14,S}
6  C u0 p0 c0 {1,S} {9,D} {15,S}
7  C u0 p0 c0 {2,S} {10,D} {18,S}
8  C u0 p0 c0 {3,D} {5,S} {13,S}
9  C u0 p0 c0 {6,D} {10,S} {16,S}
10 C u0 p0 c0 {7,D} {9,S} {17,S}
11 C u0 p0 c0 {3,S} {12,T}
12 C u0 p0 c0 {11,T} {20,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.2258,0.126248,-0.000118141,5.43987e-08,-9.12585e-12,42549.5,61.1604], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.639,0.0669336,-3.915e-05,1.09e-08,-1.16866e-12,39294.7,-16.1008], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "A2C2HB-",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {6,S} {10,D}
3  C u0 p0 c0 {1,D} {7,S} {14,S}
4  C u0 p0 c0 {1,S} {8,D} {15,S}
5  C u0 p0 c0 {7,D} {10,S} {11,S}
6  C u0 p0 c0 {2,S} {9,D} {18,S}
7  C u0 p0 c0 {3,S} {5,D} {13,S}
8  C u0 p0 c0 {4,D} {9,S} {16,S}
9  C u0 p0 c0 {6,D} {8,S} {17,S}
10 C u1 p0 c0 {2,D} {5,S}
11 C u0 p0 c0 {5,S} {12,T}
12 C u0 p0 c0 {11,T} {19,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.35511,0.122525,-0.000118741,5.74311e-08,-1.05233e-11,77335.5,58.0873], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.8879,0.0615504,-3.60749e-05,1.0051e-08,-1.07768e-12,73980.4,-21.0417], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "A2C2HA",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,D}
2  C u0 p0 c0 {1,S} {4,S} {5,D}
3  C u0 p0 c0 {1,S} {7,D} {11,S}
4  C u0 p0 c0 {2,S} {8,D} {15,S}
5  C u0 p0 c0 {2,D} {9,S} {16,S}
6  C u0 p0 c0 {1,D} {10,S} {19,S}
7  C u0 p0 c0 {3,D} {8,S} {13,S}
8  C u0 p0 c0 {4,D} {7,S} {14,S}
9  C u0 p0 c0 {5,S} {10,D} {17,S}
10 C u0 p0 c0 {6,S} {9,D} {18,S}
11 C u0 p0 c0 {3,S} {12,T}
12 C u0 p0 c0 {11,T} {20,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.23048,0.126053,-0.000117499,5.36791e-08,-8.85462e-12,42374.8,61.0992], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.55691,0.0671073,-3.92896e-05,1.0948e-08,-1.17461e-12,39137.2,-15.7914], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "A2C2HA-",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,D} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {5,D}
3  C u0 p0 c0 {2,S} {10,D} {11,S}
4  C u0 p0 c0 {1,D} {7,S} {14,S}
5  C u0 p0 c0 {2,D} {8,S} {17,S}
6  C u0 p0 c0 {1,S} {9,D} {13,S}
7  C u0 p0 c0 {4,S} {8,D} {15,S}
8  C u0 p0 c0 {5,S} {7,D} {16,S}
9  C u0 p0 c0 {6,D} {10,S} {18,S}
10 C u1 p0 c0 {3,D} {9,S}
11 C u0 p0 c0 {3,S} {12,T}
12 C u0 p0 c0 {11,T} {19,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.36585,0.122558,-0.000118737,5.7394e-08,-1.05059e-11,76983.7,57.9534], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.8846,0.0615767,-3.60989e-05,1.00593e-08,-1.07868e-12,73626,-21.2171], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "A2C2H3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,D}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {6,D}
4  C u0 p0 c0 {2,D} {9,S} {14,S}
5  C u0 p0 c0 {3,S} {9,D} {16,S}
6  C u0 p0 c0 {3,D} {10,S} {17,S}
7  C u0 p0 c0 {1,D} {11,S} {20,S}
8  C u0 p0 c0 {2,S} {12,D} {13,S}
9  C u0 p0 c0 {4,S} {5,D} {15,S}
10 C u0 p0 c0 {6,S} {11,D} {18,S}
11 C u0 p0 c0 {7,S} {10,D} {19,S}
12 C u0 p0 c0 {8,D} {21,S} {22,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {11,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {12,S}
22 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-11.8619,0.153033,-0.000170232,1.05826e-07,-2.81087e-11,24363.3,77.4596], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.2976,0.0593511,-3.09958e-05,7.76037e-09,-7.5738e-13,18678.7,-46.4218], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "A2C2H2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,D}
2  C u0 p0 c0 {1,S} {5,S} {6,D}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {8,S} {13,S}
5  C u0 p0 c0 {2,S} {8,D} {15,S}
6  C u0 p0 c0 {2,D} {9,S} {16,S}
7  C u0 p0 c0 {1,D} {10,S} {19,S}
8  C u0 p0 c0 {4,S} {5,D} {14,S}
9  C u0 p0 c0 {6,S} {10,D} {17,S}
10 C u0 p0 c0 {7,S} {9,D} {18,S}
11 C u0 p0 c0 {3,S} {12,D} {20,S}
12 C u1 p0 c0 {11,D} {21,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.26785,0.135043,-0.000129792,6.2722e-08,-1.16349e-11,56483.3,67.1407], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.53385,0.0687543,-4.0175e-05,1.11481e-08,-1.19062e-12,52758.3,-19.7684], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "A2(C2H)2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u0 p0 c0 {1,D} {4,S} {12,S}
4  C u0 p0 c0 {3,S} {8,D} {11,S}
5  C u0 p0 c0 {2,D} {8,S} {16,S}
6  C u0 p0 c0 {2,S} {9,D} {17,S}
7  C u0 p0 c0 {1,S} {10,D} {20,S}
8  C u0 p0 c0 {4,D} {5,S} {15,S}
9  C u0 p0 c0 {6,D} {10,S} {18,S}
10 C u0 p0 c0 {7,D} {9,S} {19,S}
11 C u0 p0 c0 {4,S} {13,T}
12 C u0 p0 c0 {3,S} {14,T}
13 C u0 p0 c0 {11,T} {21,S}
14 C u0 p0 c0 {12,T} {22,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {13,S}
22 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.96307,0.15638,-0.000180578,1.13936e-07,-3.01979e-11,68906.3,63.8788], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.1258,0.0543541,-2.82849e-05,7.07124e-09,-6.89827e-13,62880.5,-69.1207], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "A2R5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {5,S} {6,D}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {9,S} {10,D}
5  C u0 p0 c0 {2,S} {11,D} {14,S}
6  C u0 p0 c0 {2,D} {12,S} {15,S}
7  C u0 p0 c0 {3,S} {12,D} {17,S}
8  C u0 p0 c0 {3,S} {9,D} {18,S}
9  C u0 p0 c0 {4,S} {8,D} {19,S}
10 C u0 p0 c0 {4,D} {11,S} {20,S}
11 C u0 p0 c0 {5,D} {10,S} {13,S}
12 C u0 p0 c0 {6,S} {7,D} {16,S}
13 H u0 p0 c0 {11,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {12,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-10.5498,0.125537,-0.000103646,3.52989e-08,-1.64508e-12,29442.7,70.2667], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.65433,0.0752647,-4.54865e-05,1.29795e-08,-1.41731e-12,26522.3,0.723303], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "A2R5-",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {7,S} {9,D}
4  C u0 p0 c0 {1,S} {8,D} {12,S}
5  C u0 p0 c0 {2,S} {10,D} {15,S}
6  C u0 p0 c0 {2,S} {7,D} {16,S}
7  C u0 p0 c0 {3,S} {6,D} {17,S}
8  C u0 p0 c0 {4,D} {10,S} {13,S}
9  C u0 p0 c0 {3,D} {11,S} {18,S}
10 C u0 p0 c0 {5,D} {8,S} {14,S}
11 C u0 p0 c0 {9,S} {12,D} {19,S}
12 C u1 p0 c0 {4,S} {11,D}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {10,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.79699,0.122277,-0.000104933,3.87946e-08,-3.1629e-12,62484,68.2744], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.90109,0.0698932,-4.24226e-05,1.21346e-08,-1.32684e-12,59439.1,-3.69961], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "A2R5C2H",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {10,S}
3  C u0 p0 c0 {1,S} {6,D} {7,S}
4  C u0 p0 c0 {1,S} {8,S} {9,D}
5  C u0 p0 c0 {2,S} {11,D} {13,S}
6  C u0 p0 c0 {3,D} {11,S} {16,S}
7  C u0 p0 c0 {3,S} {8,D} {17,S}
8  C u0 p0 c0 {4,S} {7,D} {18,S}
9  C u0 p0 c0 {4,D} {12,S} {19,S}
10 C u0 p0 c0 {2,S} {12,D} {21,S}
11 C u0 p0 c0 {5,D} {6,S} {15,S}
12 C u0 p0 c0 {9,S} {10,D} {20,S}
13 C u0 p0 c0 {5,S} {14,T}
14 C u0 p0 c0 {13,T} {22,S}
15 H u0 p0 c0 {11,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {12,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.952,0.145414,-0.000139201,6.55033e-08,-1.13837e-11,55399.4,68.302], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.29417,0.0737696,-4.35833e-05,1.22154e-08,-1.31549e-12,51411,-25.5651], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "A2R5C2H-",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {7,S} {8,D}
3  C u0 p0 c0 {1,D} {5,S} {9,S}
4  C u0 p0 c0 {1,S} {6,S} {11,D}
5  C u0 p0 c0 {3,S} {12,D} {13,S}
6  C u0 p0 c0 {4,S} {7,D} {15,S}
7  C u0 p0 c0 {2,S} {6,D} {16,S}
8  C u0 p0 c0 {2,D} {10,S} {17,S}
9  C u0 p0 c0 {3,S} {10,D} {19,S}
10 C u0 p0 c0 {8,S} {9,D} {18,S}
11 C u0 p0 c0 {4,D} {12,S} {20,S}
12 C u1 p0 c0 {5,D} {11,S}
13 C u0 p0 c0 {5,S} {14,T}
14 C u0 p0 c0 {13,T} {21,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.0909,0.141918,-0.000140371,6.90982e-08,-1.29788e-11,89221.2,65.2159], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.6117,0.0682676,-4.04202e-05,1.13372e-08,-1.22096e-12,85115.5,-30.8959], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "A2R5(C2H)2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {5,D} {11,S}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {9,S} {10,D}
5  C u0 p0 c0 {2,D} {6,S} {14,S}
6  C u0 p0 c0 {5,S} {7,D} {13,S}
7  C u0 p0 c0 {3,S} {6,D} {17,S}
8  C u0 p0 c0 {3,S} {9,D} {18,S}
9  C u0 p0 c0 {4,S} {8,D} {19,S}
10 C u0 p0 c0 {4,D} {12,S} {20,S}
11 C u0 p0 c0 {2,S} {12,D} {22,S}
12 C u0 p0 c0 {10,S} {11,D} {21,S}
13 C u0 p0 c0 {6,S} {15,T}
14 C u0 p0 c0 {5,S} {16,T}
15 C u0 p0 c0 {13,T} {23,S}
16 C u0 p0 c0 {14,T} {24,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {12,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {15,S}
24 H u0 p0 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-10.8001,0.176997,-0.000205947,1.29983e-07,-3.44118e-11,81964.4,71.512], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.6921,0.0591433,-3.10722e-05,7.82499e-09,-7.67637e-13,74918,-83.3041], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "A2R5C2H2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {11,S}
3  C u0 p0 c0 {1,S} {7,D} {8,S}
4  C u0 p0 c0 {1,S} {9,S} {10,D}
5  C u0 p0 c0 {2,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {7,S} {15,S}
7  C u0 p0 c0 {3,D} {6,S} {16,S}
8  C u0 p0 c0 {3,S} {9,D} {17,S}
9  C u0 p0 c0 {4,S} {8,D} {18,S}
10 C u0 p0 c0 {4,D} {12,S} {19,S}
11 C u0 p0 c0 {2,S} {12,D} {21,S}
12 C u0 p0 c0 {10,S} {11,D} {20,S}
13 C u0 p0 c0 {5,S} {14,D} {22,S}
14 C u1 p0 c0 {13,D} {23,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {12,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {13,S}
23 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.79889,0.145401,-0.00012836,5.15869e-08,-6.01742e-12,68709.5,69.3518], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.80127,0.0814615,-4.8765e-05,1.38133e-08,-1.5e-12,65087.1,-16.6225], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "A2R5C2H3",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {4,S} {5,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {6,D} {12,S}
4  C u0 p0 c0 {1,S} {7,D} {8,S}
5  C u0 p0 c0 {1,S} {9,S} {10,D}
6  C u0 p0 c0 {3,D} {7,S} {16,S}
7  C u0 p0 c0 {4,D} {6,S} {17,S}
8  C u0 p0 c0 {4,S} {9,D} {18,S}
9  C u0 p0 c0 {5,S} {8,D} {19,S}
10 C u0 p0 c0 {5,D} {13,S} {20,S}
11 C u0 p0 c0 {2,S} {13,D} {22,S}
12 C u0 p0 c0 {3,S} {14,D} {15,S}
13 C u0 p0 c0 {10,S} {11,D} {21,S}
14 C u0 p0 c0 {12,D} {23,S} {24,S}
15 H u0 p0 c0 {12,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {13,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {14,S}
24 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.71641,0.142588,-0.000113608,3.58789e-08,-4.84218e-13,36750.5,68.632], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.52003,0.0891009,-5.35155e-05,1.52093e-08,-1.65642e-12,33628.6,-5.99395], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "A3a",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {7,D}
2  C u0 p0 c0 {3,S} {5,D} {8,S}
3  C u0 p0 c0 {2,S} {6,D} {9,S}
4  C u0 p0 c0 {1,S} {6,S} {10,D}
5  C u0 p0 c0 {1,S} {2,D} {18,S}
6  C u0 p0 c0 {3,D} {4,S} {23,S}
7  C u0 p0 c0 {1,D} {12,S} {17,S}
8  C u0 p0 c0 {2,S} {13,D} {19,S}
9  C u0 p0 c0 {3,S} {14,D} {22,S}
10 C u0 p0 c0 {4,D} {11,S} {24,S}
11 C u0 p0 c0 {10,S} {12,D} {15,S}
12 C u0 p0 c0 {7,S} {11,D} {16,S}
13 C u0 p0 c0 {8,D} {14,S} {20,S}
14 C u0 p0 c0 {9,D} {13,S} {21,S}
15 H u0 p0 c0 {11,S}
16 H u0 p0 c0 {12,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {13,S}
21 H u0 p0 c0 {14,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-11.6564,0.144875,-0.0001135,3.37639e-08,5.74214e-13,25647.7,75.0715], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.62269,0.0917533,-5.53933e-05,1.57984e-08,-1.72476e-12,22511.6,0.158652], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "A3p",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,D}
2  C u0 p0 c0 {1,S} {4,S} {10,D}
3  C u0 p0 c0 {1,S} {6,D} {7,S}
4  C u0 p0 c0 {2,S} {8,S} {9,D}
5  C u0 p0 c0 {1,D} {12,S} {17,S}
6  C u0 p0 c0 {3,D} {11,S} {18,S}
7  C u0 p0 c0 {3,S} {8,D} {19,S}
8  C u0 p0 c0 {4,S} {7,D} {20,S}
9  C u0 p0 c0 {4,D} {13,S} {21,S}
10 C u0 p0 c0 {2,D} {14,S} {24,S}
11 C u0 p0 c0 {6,S} {12,D} {15,S}
12 C u0 p0 c0 {5,S} {11,D} {16,S}
13 C u0 p0 c0 {9,S} {14,D} {22,S}
14 C u0 p0 c0 {10,S} {13,D} {23,S}
15 H u0 p0 c0 {11,S}
16 H u0 p0 c0 {12,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {13,S}
23 H u0 p0 c0 {14,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-11.5461,0.143758,-0.000110869,3.1218e-08,1.45975e-12,22168.8,75.4983], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.38726,0.0921886,-5.57287e-05,1.59124e-08,-1.73884e-12,19106.2,2.24294], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "A3p-",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,D}
2  C u0 p0 c0 {1,S} {7,S} {8,D}
3  C u0 p0 c0 {4,S} {5,D} {6,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  C u0 p0 c0 {3,D} {12,S} {16,S}
6  C u0 p0 c0 {3,S} {7,D} {17,S}
7  C u0 p0 c0 {2,S} {6,D} {18,S}
8  C u0 p0 c0 {2,D} {10,S} {19,S}
9  C u0 p0 c0 {1,D} {11,S} {22,S}
10 C u0 p0 c0 {8,S} {11,D} {20,S}
11 C u0 p0 c0 {9,S} {10,D} {21,S}
12 C u0 p0 c0 {5,S} {13,D} {15,S}
13 C u0 p0 c0 {12,D} {14,S} {23,S}
14 C u1 p0 c0 {4,D} {13,S}
15 H u0 p0 c0 {12,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-10.8882,0.141187,-0.000113531,3.59175e-08,-4.50212e-13,57015.9,73.813], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.71265,0.086723,-5.26012e-05,1.5046e-08,-1.64564e-12,53794,-2.69868], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "A3pC2H",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {5,S}
2  C u0 p0 c0 {1,D} {4,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {7,D}
4  C u0 p0 c0 {2,S} {8,D} {9,S}
5  C u0 p0 c0 {1,S} {11,D} {15,S}
6  C u0 p0 c0 {3,S} {12,D} {19,S}
7  C u0 p0 c0 {3,D} {8,S} {20,S}
8  C u0 p0 c0 {4,D} {7,S} {21,S}
9  C u0 p0 c0 {4,S} {13,D} {22,S}
10 C u0 p0 c0 {2,S} {14,D} {25,S}
11 C u0 p0 c0 {5,D} {12,S} {17,S}
12 C u0 p0 c0 {6,D} {11,S} {18,S}
13 C u0 p0 c0 {9,D} {14,S} {23,S}
14 C u0 p0 c0 {10,D} {13,S} {24,S}
15 C u0 p0 c0 {5,S} {16,T}
16 C u0 p0 c0 {15,T} {26,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {12,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {13,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-11.1174,0.164862,-0.000148933,6.35625e-08,-8.94915e-12,50302.1,74.879], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.2285,0.0903138,-5.35519e-05,1.50612e-08,-1.62683e-12,46097.4,-24.4715], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "A3pC2H2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {5,S}
2  C u0 p0 c0 {1,D} {4,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {8,D}
4  C u0 p0 c0 {2,S} {9,D} {10,S}
5  C u0 p0 c0 {1,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {12,S} {17,S}
7  C u0 p0 c0 {3,S} {12,D} {19,S}
8  C u0 p0 c0 {3,D} {9,S} {20,S}
9  C u0 p0 c0 {4,D} {8,S} {21,S}
10 C u0 p0 c0 {4,S} {13,D} {22,S}
11 C u0 p0 c0 {2,S} {14,D} {25,S}
12 C u0 p0 c0 {6,S} {7,D} {18,S}
13 C u0 p0 c0 {10,D} {14,S} {23,S}
14 C u0 p0 c0 {11,D} {13,S} {24,S}
15 C u0 p0 c0 {5,S} {16,D} {26,S}
16 C u1 p0 c0 {15,D} {27,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {12,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {13,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {15,S}
27 H u0 p0 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-11.6614,0.165961,-0.000139357,5.0298e-08,-3.70389e-12,66141.5,77.5492], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.22603,0.0983998,-5.90146e-05,1.67471e-08,-1.82147e-12,62265.1,-14.8176], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "A4p",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {6,S}
2  C u0 p0 c0 {1,D} {4,S} {5,S}
3  C u0 p0 c0 {1,S} {7,S} {8,D}
4  C u0 p0 c0 {2,S} {9,D} {10,S}
5  C u0 p0 c0 {2,S} {11,D} {12,S}
6  C u0 p0 c0 {1,S} {13,S} {14,D}
7  C u0 p0 c0 {3,S} {15,D} {18,S}
8  C u0 p0 c0 {3,D} {9,S} {19,S}
9  C u0 p0 c0 {4,D} {8,S} {20,S}
10 C u0 p0 c0 {4,S} {16,D} {21,S}
11 C u0 p0 c0 {5,D} {16,S} {23,S}
12 C u0 p0 c0 {5,S} {13,D} {24,S}
13 C u0 p0 c0 {6,S} {12,D} {25,S}
14 C u0 p0 c0 {6,D} {15,S} {26,S}
15 C u0 p0 c0 {7,D} {14,S} {17,S}
16 C u0 p0 c0 {10,D} {11,S} {22,S}
17 H u0 p0 c0 {15,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {16,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {13,S}
26 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-13.1524,0.160879,-0.00012772,3.90919e-08,7.43991e-14,24967.4,80.7618], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.5406,0.0998115,-6.06376e-05,1.73575e-08,-1.89902e-12,21275.6,-6.19295], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "A4t",
    molecule = 
"""
1  C u0 p0 c0 {6,S} {7,S} {11,D}
2  C u0 p0 c0 {5,S} {7,D} {8,S}
3  C u0 p0 c0 {4,S} {8,D} {12,S}
4  C u0 p0 c0 {3,S} {9,D} {13,S}
5  C u0 p0 c0 {2,S} {9,S} {10,D}
6  C u0 p0 c0 {1,S} {10,S} {14,D}
7  C u0 p0 c0 {1,S} {2,D} {22,S}
8  C u0 p0 c0 {2,S} {3,D} {23,S}
9  C u0 p0 c0 {4,D} {5,S} {28,S}
10 C u0 p0 c0 {5,D} {6,S} {29,S}
11 C u0 p0 c0 {1,D} {16,S} {21,S}
12 C u0 p0 c0 {3,S} {17,D} {24,S}
13 C u0 p0 c0 {4,S} {18,D} {27,S}
14 C u0 p0 c0 {6,D} {15,S} {30,S}
15 C u0 p0 c0 {14,S} {16,D} {19,S}
16 C u0 p0 c0 {11,S} {15,D} {20,S}
17 C u0 p0 c0 {12,D} {18,S} {25,S}
18 C u0 p0 c0 {13,D} {17,S} {26,S}
19 H u0 p0 c0 {15,S}
20 H u0 p0 c0 {16,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {17,S}
26 H u0 p0 c0 {18,S}
27 H u0 p0 c0 {13,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-14.6027,0.184683,-0.000147521,4.62742e-08,-4.61011e-13,35531.7,88.1952], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.56187,0.114459,-6.92666e-05,1.97788e-08,-2.16052e-12,31358.1,-10.7436], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "A4c",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {7,D}
2  C u0 p0 c0 {3,D} {4,S} {10,S}
3  C u0 p0 c0 {2,D} {6,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {14,D}
5  C u0 p0 c0 {1,S} {8,D} {9,S}
6  C u0 p0 c0 {3,S} {12,S} {13,D}
7  C u0 p0 c0 {1,D} {16,S} {21,S}
8  C u0 p0 c0 {5,D} {15,S} {22,S}
9  C u0 p0 c0 {5,S} {10,D} {23,S}
10 C u0 p0 c0 {2,S} {9,D} {24,S}
11 C u0 p0 c0 {3,S} {17,D} {25,S}
12 C u0 p0 c0 {6,S} {18,D} {28,S}
13 C u0 p0 c0 {6,D} {14,S} {29,S}
14 C u0 p0 c0 {4,D} {13,S} {30,S}
15 C u0 p0 c0 {8,S} {16,D} {19,S}
16 C u0 p0 c0 {7,S} {15,D} {20,S}
17 C u0 p0 c0 {11,D} {18,S} {26,S}
18 C u0 p0 c0 {12,D} {17,S} {27,S}
19 H u0 p0 c0 {15,S}
20 H u0 p0 c0 {16,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {17,S}
27 H u0 p0 c0 {18,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {13,S}
30 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-14.3183,0.182115,-0.000141736,4.08235e-08,1.40318e-12,28599.4,88.1184], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.08082,0.115309,-6.9912e-05,1.99972e-08,-2.18747e-12,24586.7,-7.15206], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "A4p-",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {5,S}
2  C u0 p0 c0 {1,D} {4,S} {6,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,D}
5  C u0 p0 c0 {1,S} {7,S} {15,D}
6  C u0 p0 c0 {2,S} {12,S} {16,D}
7  C u0 p0 c0 {5,S} {14,D} {19,S}
8  C u0 p0 c0 {3,D} {14,S} {21,S}
9  C u0 p0 c0 {3,S} {10,D} {22,S}
10 C u0 p0 c0 {4,S} {9,D} {23,S}
11 C u0 p0 c0 {4,D} {13,S} {24,S}
12 C u0 p0 c0 {6,S} {13,D} {18,S}
13 C u0 p0 c0 {11,S} {12,D} {17,S}
14 C u0 p0 c0 {7,D} {8,S} {20,S}
15 C u0 p0 c0 {5,D} {16,S} {25,S}
16 C u1 p0 c0 {6,D} {15,S}
17 H u0 p0 c0 {13,S}
18 H u0 p0 c0 {12,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {14,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-12.3672,0.157658,-0.000129244,4.2863e-08,-1.54492e-12,62779.8,79.3139], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.85098,0.0943231,-5.74898e-05,1.64859e-08,-1.80542e-12,58957.3,-10.2177], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "A3R5",
    molecule = 
"""
1  C u0 p0 c0 {3,D} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {4,S} {8,D}
3  C u0 p0 c0 {1,D} {2,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {9,D}
5  C u0 p0 c0 {1,S} {7,D} {10,S}
6  C u0 p0 c0 {1,S} {11,S} {12,D}
7  C u0 p0 c0 {4,S} {5,D} {21,S}
8  C u0 p0 c0 {2,D} {15,S} {19,S}
9  C u0 p0 c0 {4,D} {14,S} {20,S}
10 C u0 p0 c0 {5,S} {11,D} {22,S}
11 C u0 p0 c0 {6,S} {10,D} {23,S}
12 C u0 p0 c0 {6,D} {16,S} {24,S}
13 C u0 p0 c0 {3,S} {16,D} {26,S}
14 C u0 p0 c0 {9,S} {15,D} {17,S}
15 C u0 p0 c0 {8,S} {14,D} {18,S}
16 C u0 p0 c0 {12,S} {13,D} {25,S}
17 H u0 p0 c0 {14,S}
18 H u0 p0 c0 {15,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {16,S}
26 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-13.2242,0.162863,-0.000131967,4.24394e-08,-8.53172e-13,34443.1,83.0299], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.07025,0.0989917,-6.014e-05,1.72205e-08,-1.88476e-12,30652.8,-6.7218], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "A3R5-",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,D}
2  C u0 p0 c0 {3,S} {6,S} {8,D}
3  C u0 p0 c0 {2,S} {7,S} {9,D}
4  C u0 p0 c0 {1,S} {7,D} {10,S}
5  C u0 p0 c0 {1,S} {11,S} {12,D}
6  C u0 p0 c0 {1,D} {2,S} {16,S}
7  C u0 p0 c0 {3,S} {4,D} {21,S}
8  C u0 p0 c0 {2,D} {14,S} {19,S}
9  C u0 p0 c0 {3,D} {13,S} {20,S}
10 C u0 p0 c0 {4,S} {11,D} {22,S}
11 C u0 p0 c0 {5,S} {10,D} {23,S}
12 C u0 p0 c0 {5,D} {15,S} {24,S}
13 C u0 p0 c0 {9,S} {14,D} {17,S}
14 C u0 p0 c0 {8,S} {13,D} {18,S}
15 C u0 p0 c0 {12,S} {16,D} {25,S}
16 C u1 p0 c0 {6,S} {15,D}
17 H u0 p0 c0 {13,S}
18 H u0 p0 c0 {14,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-12.5419,0.160371,-0.000135029,4.76044e-08,-2.93662e-12,68710.8,80.607], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.47777,0.0933338,-5.68627e-05,1.63047e-08,-1.78567e-12,64749,-12.6769], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "A3R5C2H",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {4,S} {5,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {6,S} {13,D}
4  C u0 p0 c0 {1,S} {9,D} {10,S}
5  C u0 p0 c0 {1,S} {8,D} {11,S}
6  C u0 p0 c0 {3,S} {8,S} {12,D}
7  C u0 p0 c0 {2,S} {14,D} {17,S}
8  C u0 p0 c0 {5,D} {6,S} {23,S}
9  C u0 p0 c0 {4,D} {14,S} {20,S}
10 C u0 p0 c0 {4,S} {11,D} {21,S}
11 C u0 p0 c0 {5,S} {10,D} {22,S}
12 C u0 p0 c0 {6,D} {15,S} {24,S}
13 C u0 p0 c0 {3,D} {16,S} {27,S}
14 C u0 p0 c0 {7,D} {9,S} {19,S}
15 C u0 p0 c0 {12,S} {16,D} {25,S}
16 C u0 p0 c0 {13,S} {15,D} {26,S}
17 C u0 p0 c0 {7,S} {18,T}
18 C u0 p0 c0 {17,T} {28,S}
19 H u0 p0 c0 {14,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {15,S}
26 H u0 p0 c0 {16,S}
27 H u0 p0 c0 {13,S}
28 H u0 p0 c0 {18,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-12.818,0.184106,-0.000170347,7.50709e-08,-1.13553e-11,61927.3,81.2365], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.9364,0.0970461,-5.79062e-05,1.63504e-08,-1.7705e-12,56985.6,-34.8364], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "A4R5",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {4,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {5,S}
3  C u0 p0 c0 {2,S} {6,D} {7,S}
4  C u0 p0 c0 {1,S} {10,S} {11,D}
5  C u0 p0 c0 {2,S} {12,D} {13,S}
6  C u0 p0 c0 {3,D} {14,S} {15,S}
7  C u0 p0 c0 {3,S} {9,D} {16,S}
8  C u0 p0 c0 {1,S} {9,S} {17,D}
9  C u0 p0 c0 {7,D} {8,S} {27,S}
10 C u0 p0 c0 {4,S} {18,D} {20,S}
11 C u0 p0 c0 {4,D} {12,S} {21,S}
12 C u0 p0 c0 {5,D} {11,S} {22,S}
13 C u0 p0 c0 {5,S} {14,D} {23,S}
14 C u0 p0 c0 {6,S} {13,D} {24,S}
15 C u0 p0 c0 {6,S} {16,D} {25,S}
16 C u0 p0 c0 {7,S} {15,D} {26,S}
17 C u0 p0 c0 {8,D} {18,S} {28,S}
18 C u0 p0 c0 {10,D} {17,S} {19,S}
19 H u0 p0 c0 {18,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {13,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {15,S}
26 H u0 p0 c0 {16,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {17,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-14.7696,0.179658,-0.00014819,4.97722e-08,-2.06437e-12,37846.8,88.8184], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.20191,0.106656,-6.50829e-05,1.86776e-08,-2.04647e-12,33443.9,-14.2388], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "P2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u0 p0 c0 {1,D} {8,S} {15,S}
4  C u0 p0 c0 {1,S} {9,D} {16,S}
5  C u0 p0 c0 {2,D} {10,S} {18,S}
6  C u0 p0 c0 {2,S} {12,D} {22,S}
7  C u0 p0 c0 {8,D} {9,S} {13,S}
8  C u0 p0 c0 {3,S} {7,D} {14,S}
9  C u0 p0 c0 {4,D} {7,S} {17,S}
10 C u0 p0 c0 {5,S} {11,D} {19,S}
11 C u0 p0 c0 {10,D} {12,S} {20,S}
12 C u0 p0 c0 {6,D} {11,S} {21,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {12,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-11.9438,0.142163,-0.000133497,6.20506e-08,-1.05767e-11,20193.7,78.1851], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.73687,0.0754659,-4.38685e-05,1.21616e-08,-1.30012e-12,16602.2,-7.75536], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "P2-",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {5,S} {12,D}
3  C u0 p0 c0 {1,D} {7,S} {15,S}
4  C u0 p0 c0 {1,S} {8,D} {16,S}
5  C u0 p0 c0 {2,S} {9,D} {20,S}
6  C u0 p0 c0 {7,D} {8,S} {13,S}
7  C u0 p0 c0 {3,S} {6,D} {14,S}
8  C u0 p0 c0 {4,D} {6,S} {17,S}
9  C u0 p0 c0 {5,D} {10,S} {19,S}
10 C u0 p0 c0 {9,S} {11,D} {18,S}
11 C u0 p0 c0 {10,D} {12,S} {21,S}
12 C u1 p0 c0 {2,D} {11,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.50092,0.125211,-9.83718e-05,2.75934e-08,1.67954e-12,52990.3,69.1608], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.9767,0.0779432,-4.74482e-05,1.36376e-08,-1.49858e-12,50296.4,3.31269], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "A5",
    molecule = 
"""
1  C u0 p0 c0 {3,D} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,D} {8,S}
3  C u0 p0 c0 {1,D} {4,S} {11,S}
4  C u0 p0 c0 {2,S} {3,S} {12,D}
5  C u0 p0 c0 {2,D} {6,S} {15,S}
6  C u0 p0 c0 {1,S} {5,S} {16,D}
7  C u0 p0 c0 {1,S} {9,S} {10,D}
8  C u0 p0 c0 {2,S} {13,S} {14,D}
9  C u0 p0 c0 {7,S} {17,D} {22,S}
10 C u0 p0 c0 {7,D} {18,S} {23,S}
11 C u0 p0 c0 {3,S} {18,D} {25,S}
12 C u0 p0 c0 {4,D} {19,S} {26,S}
13 C u0 p0 c0 {8,S} {19,D} {28,S}
14 C u0 p0 c0 {8,D} {20,S} {29,S}
15 C u0 p0 c0 {5,S} {20,D} {31,S}
16 C u0 p0 c0 {6,D} {17,S} {32,S}
17 C u0 p0 c0 {9,D} {16,S} {21,S}
18 C u0 p0 c0 {10,S} {11,D} {24,S}
19 C u0 p0 c0 {12,S} {13,D} {27,S}
20 C u0 p0 c0 {14,S} {15,D} {30,S}
21 H u0 p0 c0 {17,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {18,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {19,S}
28 H u0 p0 c0 {13,S}
29 H u0 p0 c0 {14,S}
30 H u0 p0 c0 {20,S}
31 H u0 p0 c0 {15,S}
32 H u0 p0 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-15.6026,0.197486,-0.000154774,4.50107e-08,1.31799e-12,33968.7,92.9223], Tmin=(300,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.03814,0.123421,-7.5251e-05,2.15982e-08,-2.36763e-12,29443.2,-13.5374], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (300,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G3B3""",
    longDesc = 
u"""

""",
)

# The following entry was included in the supporting information
# in the paper, but does not seem to be correct, possibly due to
# a typo. Enthalpy is ~3 orders of magnitude too big.
# entry(
#     index = 45,
#     label = "A7",
#     molecule = 
# """
# 1  C u0 p0 c0 {2,D} {6,S} {12,S}
# 2  C u0 p0 c0 {1,D} {3,S} {7,S}
# 3  C u0 p0 c0 {2,S} {4,D} {8,S}
# 4  C u0 p0 c0 {3,D} {5,S} {9,S}
# 5  C u0 p0 c0 {4,S} {6,D} {10,S}
# 6  C u0 p0 c0 {1,S} {5,D} {11,S}
# 7  C u0 p0 c0 {2,S} {14,S} {15,D}
# 8  C u0 p0 c0 {3,S} {16,D} {17,S}
# 9  C u0 p0 c0 {4,S} {18,S} {19,D}
# 10 C u0 p0 c0 {5,S} {20,D} {21,S}
# 11 C u0 p0 c0 {6,S} {22,S} {23,D}
# 12 C u0 p0 c0 {1,S} {13,S} {24,D}
# 13 C u0 p0 c0 {12,S} {14,D} {25,S}
# 14 C u0 p0 c0 {7,S} {13,D} {26,S}
# 15 C u0 p0 c0 {7,D} {16,S} {27,S}
# 16 C u0 p0 c0 {8,D} {15,S} {28,S}
# 17 C u0 p0 c0 {8,S} {18,D} {29,S}
# 18 C u0 p0 c0 {9,S} {17,D} {30,S}
# 19 C u0 p0 c0 {9,D} {20,S} {31,S}
# 20 C u0 p0 c0 {10,D} {19,S} {32,S}
# 21 C u0 p0 c0 {10,S} {22,D} {33,S}
# 22 C u0 p0 c0 {11,S} {21,D} {34,S}
# 23 C u0 p0 c0 {11,D} {24,S} {35,S}
# 24 C u0 p0 c0 {12,D} {23,S} {36,S}
# 25 H u0 p0 c0 {13,S}
# 26 H u0 p0 c0 {14,S}
# 27 H u0 p0 c0 {15,S}
# 28 H u0 p0 c0 {16,S}
# 29 H u0 p0 c0 {17,S}
# 30 H u0 p0 c0 {18,S}
# 31 H u0 p0 c0 {19,S}
# 32 H u0 p0 c0 {20,S}
# 33 H u0 p0 c0 {21,S}
# 34 H u0 p0 c0 {22,S}
# 35 H u0 p0 c0 {23,S}
# 36 H u0 p0 c0 {24,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[-16.9422,0.223766,-0.00017466,4.97168e-08,1.90882e-12,2.90661e+08,93.906], Tmin=(300,'K'), Tmax=(1000,'K')),
#             NASAPolynomial(coeffs=[8.19741,0.139202,-8.55704e-05,2.46728e-08,-2.71165e-12,2.90655e+08,-30.2293], Tmin=(1000,'K'), Tmax=(3000,'K')),
#         ],
#         Tmin = (300,'K'),
#         Tmax = (3000,'K'),
#     ),
#     shortDesc = u"""G3B3""",
#     longDesc = 
# u"""
# 
# """,
# )

