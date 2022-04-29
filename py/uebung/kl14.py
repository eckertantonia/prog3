# !/usr/bin/env python3

from asyncio.windows_events import NULL
import re

pattern = re.compile("a([ab](a|b)+)+")

def reg(s):
    match = pattern.search(s)
    if match:
        print(match.group())
    else:
        print("Yokka")

""" reg("aba")
reg("babb")
reg("ab")
reg("abbabb")
reg("abbbbb")
reg("bbaabab")
reg("ab") """

def reg2(s):
    pattern = re.compile("[A-Z][a-zA-Z]*[aeiou]$")

    match = pattern.search(s)
    if match:
        print(match.group())
    else:
        print(s+" failed")

""" reg2("Helga")
reg2("Heidi")
reg2("Jöndhard") """

def kombiniere(*vars, func = NULL):
    erg = 0
    for ele in vars:
        if func is NULL:
            erg += ele
        else:
            erg += func(ele)

    print(erg)

""" kombiniere(1,2,3)
kombiniere(1,2,3, func = lambda x: x**3) """

class A(object):
    def __init__(self, a):
        self.a = a
        print(self.a)
    
    def f(self, v):
        return self.a*v

class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.a = a
        self.b = b
        print(self.a, self.b)
    
    def f(self, v):
        return super().f(v)+self.b

ah = A(3)
print(ah.f(3))
be = B(4,5)
print(be.f(3))