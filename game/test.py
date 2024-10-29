import numbers

liste = {"ferrari"}
liste2 = list(liste)
length = liste2[0]
length_word = len(length)
leer = []
i = 0


for platz in length:
    leer.append(" ")

def liste_update_(swag="_"):
     for x in leer:
            print(x, end=" ")

def leer_():

    global i
    while i < length_word:
        print(leer[i], end=" ")
        i += 1

leer_()

#def platz2_():
#    for platz2 in leer:
#        global i
#        while i < length_word:
#            print(leer[i], end="a")
#            i +=1 
        
print()

def buch_():
    for buch in length:
        print("_", end=" ")

buch_()
    
print()           

def spiel_():
    raten = input("\nBuchstabe: ").lower()
    for stabe in length:
        if raten in stabe: 
            print("Richtig")
            position = length.find(raten)+1


            positionen = [i for i, x in enumerate(length) if x == raten]
             
            positionen = list(map(int, positionen))
            for x in positionen:
                leer[x] = raten

            string_liste = " ".join(str(k) for k in positionen)
            
            ergebnis = string_liste
            
#            for x in range(len(positionen)):           
#                print(x[positionen])
            print(f"{raten} befindet sich auf Position/en: {ergebnis}")
#            leer[position-1] = raten
            liste_update_()
            print()
            buch_()
            spiel_()
spiel_() 
