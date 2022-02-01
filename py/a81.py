# !/usr/bin/env python3

# Aufgabe 8.1 (Funktionsargumente)

def h(a,b,c=1000,*d,**e):
    print(a,b,c,d,e)

tup = ('ene', 'mene', 'mu')
kw = {'x':'iks', 'b':'beh', 'lst': [17,17,17]}
h(17,21) # 17 21 1000 () {} -> c hat Defaultwert 1000
h(10,20,30) # 10 20 30 () {} -> Wert für c übergeben
h(1,2,3,4,5,6,x=7,y=22) # 1 2 3 (4, 5, 6) {'x': 7, 'y': 22} -> *d wird mit restlichen Werten gefüllt; **kw ist dictionary, wird mit allen weiteren Keyword-Parametern gefüllt
# h(1,2,3,4,5,6,c=7) # TypeError: h() got multiple values for argument 'c' -> 
h(*tup) # ene mene mu () {} -> * "entpackt" Tupel und packt die Werte in die ersten Funktionsparameter
h(1,2,*tup,3) # 1 2 ene ('mene', 'mu', 3) {} -> füllt die ersten Parameter und packt den Rest in Tupel für restliche Parameter (*d)
h(10, **kw) # 10 beh 1000 () {'x': 'iks', 'lst': [17, 17, 17]} -> sieht b in dict kw
h(10,20,*tup, **kw) # TypeError: h() got multiple values for argument 'b' -> sieht b in dict kw
