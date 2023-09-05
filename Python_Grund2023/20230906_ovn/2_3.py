"""I USA brukar man ange temperaturer i grader Fahrenheit (2F) i stället för grader Celsius (2C). 
0°C motsvarar 32°F och 100°C motsvarar 212°F. 
Man kan använda formeln °C=(0F-32)x5/9 för att omvandla från °F till °C. 
Skriv ett program som läser in en temperatur uttryckt i grader Fahrenheit (2F) och som översätter 
temperaturen till grader Celsius (°C). """

fahrenheit=input("Vad är temperaturen i Fahrenheit? ")

celsius= (int(fahrenheit)-32)*5/9

print(f'''{float(fahrenheit):.2f}°F motsvarar {celsius:.2f}°C''')