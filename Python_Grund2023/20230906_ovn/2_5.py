"""Man kan beräkna avståndet mellan två punkter (x₁, y₁) och (x₂, 
y₂) i ett tvådimensionellt koordinatsystem med formeln. 

s= √(x₁-x₂)²+(y₁-y₂)²    

Skriv ett program som läser in punkternas koordinater och som 
beräknar avståndet mellan punkterna.  """

x1=float(input('Ange x₁: '))
y1=float(input('Ange y₁: '))
x2=float(input('Ange x₂: '))
y2=float(input('Ange y₂: '))


import math
avstånd= math.sqrt((x1-x2)**2+(y1-y2)**2)

print(f'''Avståndet mellan punkterna ({x1};{y1}) och ({x2};{y2}) är {avstånd:.2f}.''')