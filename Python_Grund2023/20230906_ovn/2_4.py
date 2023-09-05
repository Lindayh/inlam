"""I USA brukar en bils bensinförbrukning anges i miles/gallon. Skriv 
ett program som läser in en bensinförbrukning som är angiven 
på detta sätt och översätter den till det för oss vanligare liter/mil. 
Följande gäller: 
1 mile = 1,609 km och 1 gallon = 3,785 liter. """

miles=input("Ange miles: ")
gallon=input("Ange gallon: ")

gallon=float(gallon)
miles=float(miles)
print("\nMiles per gallon -mpg-:", miles/gallon)

km= miles*1.609
liter= gallon*3.785

lpk= liter/km

print(f"""\nBensinförbrukning i liter/km blir: {lpk:.2f}.
I liter/10km blir det : {lpk*10:.2f}""")