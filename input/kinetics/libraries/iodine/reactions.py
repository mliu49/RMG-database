#!/usr/bin/env python
# encoding: utf-8

name = "iodine"
shortDesc = u""
longDesc = u"""

"""
duplicatesChecked=True
entry(
    index = 0,
    label = "1IA2 <=> A2_rad1 + I",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.052e+19, 's^-1'),
        n = -0.98,
        Ea = (68.121, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Based on iodobenzene decomposition, Tranter et al. 2010',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
Based on iodobenzene decomposition, Tranter et al. 2010
""",
)

entry(
    index = 1,
    label = "1IA2 + H <=> A2_rad1 + HI",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From Lifshitz et al. 2009',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From Lifshitz et al. 2009
""",
)

entry(
    index = 2,
    label = "1IA2 + H <=> A2 + I",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9.4, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From Lifshitz et al. 2009',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From Lifshitz et al. 2009
""",
)

