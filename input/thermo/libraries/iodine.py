#!/usr/bin/env python
# encoding: utf-8

name = "iodine"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "I",
    molecule = 
"""
multiplicity 2
1 I u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.50042,-4.48047e-06,1.69963e-08,-2.67708e-11,1.48927e-14,12094.8,7.49817], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.61668,-0.00026601,1.8606e-07,-3.81927e-11,2.52036e-15,12058.3,6.87897], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""J 6/82
From Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "HI",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 I u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.555,-0.00034892,2.02666e-07,1.78572e-09,-1.21092e-12,2145.01,4.67388], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.97348,0.00143565,-5.02266e-07,8.1577e-11,-4.90179e-15,2254.05,7.52526], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""j 9/61
From Third Millennium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "1IA2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u0 p0 c0 {1,D} {7,S} {12,S}
4  C u0 p0 c0 {2,D} {8,S} {15,S}
5  C u0 p0 c0 {2,S} {9,D} {16,S}
6  C u0 p0 c0 {1,S} {10,D} {11,S}
7  C u0 p0 c0 {3,S} {8,D} {13,S}
8  C u0 p0 c0 {4,S} {7,D} {14,S}
9  C u0 p0 c0 {5,D} {10,S} {17,S}
10 C u0 p0 c0 {6,D} {9,S} {18,S}
11 I u0 p3 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.93334,0.0380083,6.0722e-05,-1.1255e-07,4.95583e-11,24645.9,6.16018], Tmin=(298.15,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.9061,0.0327871,-1.33178e-05,2.46737e-09,-1.71269e-13,19155.1,-74.0258], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""1-Iodona  T07/06
From Third Millenium Database""",
    longDesc = 
u"""

""",
)

