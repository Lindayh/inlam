"""
Halveringstid för isotopen 14c är 5730 år. 

Hur många procent av denna isotop återstår efter S år? S är indata till programmet.
"""

#Halveringstiden 
halvTid=5730
S=float(input("Ange antal år: "))

import math

materialKonstant=(math.log(2))/halvTid
#print("Material konstant λ är: ", materialKonstant)

n0=100

kvarvarande=n0*math.exp(-materialKonstant*S) 
print(f'''Kvarvarande radioaktivt material är: {kvarvarande:.2f} %''')