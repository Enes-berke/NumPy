# NumPy - Why Numpy ?

import numpy as np
from numpy import *

a = [1 , 2 , 3 , 4 , 5]
b = [6 , 7 , 8 , 9 , 10]

ab = []

for i in range(0,len(a)):
    ab.append( a[i] * b[i] )

print("for dongusu ile yaptik ==> " , ab)

a = np.array([1 , 2 , 3 , 4 , 5])
b = np.array([6 , 7 , 8 , 9 , 10])

islem_2 = a * b

print("Numpy kutuphaneini kullanarak islem yaptik ==>" , islem_2)