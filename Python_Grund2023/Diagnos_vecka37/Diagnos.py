'''Diagnos: Skriv en funktion där utdata är alla primtal mellan 2 och n. Där tal n är ett heltal mellan 1-99.
(Erathostenes såll)'''

def skrivTal(tal):
    numList=[]
    p=2
    for i in range(2,tal+1,1):   #Skapa en lista med alla nummer mellan 2 och input
        numList.append(i)

    for p in range(2,tal,1):
        for i in range(1, tal+1,1):        
            while i in numList:         #Kolla om ett nummer har inte tagits bort från lista än
                if i%p==0 and p!=i:     #Kolla om numret är multiplikator. Man ska inte dela samma nummer med sig själv (t.ex. 3/3)
                    numList.remove(i)   #Ta bort från listan dem numren som uppfyller villkoren för att de är inte primtal
                else:
                    break
    
    return numList

while True:              
    tal=int(input("Ange heltal: "))
    if tal>=1 and tal<=99:
        break

print(skrivTal(tal))