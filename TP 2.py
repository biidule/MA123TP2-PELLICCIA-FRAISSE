# -*- coding: utf-8 -*-
"""
fait le Mon Mar  1 10:06:10 2021

par thibault pelliccia
"""
import math as m


def g0(x):
    return (1 + m.sin(x)) / 2


############################### f1 x**4+3x=9
def g11(x):
    return ((x ** 4) - 9) / 3


def g12(x):
    return (9 - 3 * x) ** (1 / 4)


############################### f2 x=3cosx-2
def g21(x):
    return 3 * m.cos(x) - 2


def g22(x):
    return m.acos((x - 2) / 3)


################################### f3 xe^x=7
def g31(x):
    return 1 / (m.exp(x) - 7)


def g32(x):
    return m.log(7 / x)


################################### f4 e^x−x= 10
def g41(x):
    return m.log(x + 10)


def g42(x):
    return m.exp(x) - 10


################################### f5 2tanx=x+5
def g51(x):
    return 2*m.tan(x)/5


def g52(x):
    return m.atan((x+5)/2)


################################### f6 e^x=x^2+3
def g61(x):
    return m.log((x**2)+3)


def g62(x):
    return m.sqrt(m.exp(x)-3)


###################################
def g71(x):
    return (-4*m.log(x)+7)/3


def g72(x):
    return m.exp(-(3*x+7)/4)


###################################
def g81(x):
    return 0


def g82(x):
    return 0


###################################
def g91(x):
    return m.acos((-m.exp(x)+7)/2)


def g92(x):
    return m.log(-2*m.sin(x)-7)


###################################
def g101(x):
    return m.log(10/m.log((x**2)+4))


def g102(x):
    return m.sqrt(m.exp(10/m.exp(x))-4)


def point_fixe(g, x0, epsilon, Nitermax):
    n = 0
    xold = x0
    xnew = g(xold)
    erreur = (xnew - xold)

    while (abs(erreur) > epsilon) and n < Nitermax:
        xnew = g(xold)
        erreur = xnew - xold
        xold = xnew
        print(xnew, erreur, n)
        n += 1


point_fixe(g102, 1, 1e-10, 1e4)  # g, x0, epsilon, nitermax
