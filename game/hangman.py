
Obst = ["apfel", "birne", "orange", "olive"]
Automarke = ["mercedes", "volvo", "volkswagen", "subaru", "porsche", "ferrari"]
Land = ["deutschland", "spanien", "frankreich", "schweiz", "belgien", "schweden"]

pre_game_liste = {"olive"}
pre_game_liste.update(Obst, Automarke, Land)

game_liste = list(pre_game_liste)

random_wort = game_liste[1]
length = len(random_wort)
check_wort = list(random_wort)

pre_categorie = [] 


if random_wort in Obst:
    pre_categorie.append("Obst")
elif random_wort in Automarke:
    pre_categorie.append("Automarke")
else:
    pre_categorie.append("Land")

categorie = pre_categorie[0]

nummern = []
eingabe = []
richtig = []
gefragt = []

i = 0
f = 0 


hangman = {
      1: ( "     _______   ",
           "    |/      |  ",
           "    |          ",
           "    |          ",
           "    |          ",
           "    |          ",
           "    |          ",
           " ___|___ (1/6) "),
      2: ( "     _______   ",
           "    |/      |  ",
           "    |      (_) ",
           "    |          ",
           "    |          ",
           "    |          ",
           "    |          ",
           " ___|___ (2/6) "),
      3: ( "     _______   ",
           "    |/      |  ",
           "    |      (_) ",
           "    |       |  ",
           "    |          ",
           "    |          ",
           "    |          ",
           " ___|___ (3/6) "),
      4: ( "     _______   ",
           "    |/      |  ",
           "    |      (_) ",
           "    |      \|/ ",
           "    |          ",
           "    |          ",
           "    |          ",
           " ___|___ (4/6) "),
      5: ( "     _______   ",
           "    |/      |  ",
           "    |      (_) ",
           "    |      \|/ ",
           "    |       |  ",
           "    |          ",
           "    |          ",
           " ___|___ (5/6) "),     
      6: ( "     _______   ",
           "    |/      |  ",
           "    |      (_) ",
           "    |      \|/ ",
           "    |       |  ",
           "    |      / \ ",
           "    |          ",
           " ___|___ (6/6) "),

}  


def hangman_start():
    print()
    for man in hangman.get(6): print(man)

def hangman_():
    print()
    for man in hangman.get(f): print(man)
    print(name)
    print()
    
for platz in random_wort: richtig.append(" ")


name = input("Willkommen bei Hangman, wie ist dein Name: ")
        
hangman_start()           

print(f"\nDu hast 6 Versuche das Wort zu erraten.")

def start_():
    
    entscheidung = input(f"{name}, möchtest du Hangman spielen oder hast du dich verlaufen ?\n(S zum spielen | X zum beenden): ").lower()
    if entscheidung == "s":
        print(f"\nAls kleiner Tipp, das Wort ist ein/e {categorie}.\n")
        raten_()

    elif entscheidung == "x":
        print(f"\nDann halt nicht {name}")
        return None
    
    else:
        print("\nGanz ruhig, S oder X")
        start_()

def check_falsch_():
    global f 
    if f == 6:
        hangman_()
        print(f"Das wars dann wohl... (loser)\nDas Wort war: {random_wort}")
        exit()
    else:
        f += 1
        if f == 6:
            check_falsch_()


def linie_():
    for line in random_wort: print("▔", end=" ")

#def linie_():
#    print()
#    for line in random_wort:
#            print("_", end=" ")


def liste_updaten_():
    for x in richtig: print(x, end=" ")

def raten_():
    linie_()
    raten = input("\nDein Buchstabe: ").lower()
    eingabe = list(raten)
    print()
    for b in eingabe:
        if b in gefragt:
         print(f"{b} wurde bereits angegeben\n")
         liste_updaten_()
         print()   
         raten_()
   
    for buchstaben in random_wort:
       for b in eingabe: 
        if b in buchstaben:
#        if raten in buchstaben:
            
            print("\nOho richtig richtig weiter so!")
            
            positionen = None
            for b in raten: 
                  positionen = [i for i, x in enumerate(random_wort) if x == b] #raten]
                  positionen = list(map(int, positionen))
                  for x in positionen: richtig[x] = b #raten
                  
            string_position = " & ".join(str(x+1) for x in positionen)
            position = string_position
                  
                 
            print(f"{raten} befindet sich auf Position/en {position} im Wort\n")
            liste_updaten_()     
            gefragt.append(b)
            print()
            
                       
            if richtig == check_wort:
                print(f"\nWinner, Winner, Chicken Dinner!!!\n{random_wort} ist richtig!!!")
                exit()
            else:
                raten_()            
       
    if b not in buchstaben:
#      if raten not in buchstaben:
            print(f"Leider ist {raten} nicht im Wort :(")
            check_falsch_()
            hangman_()
            liste_updaten_()
            print()
            gefragt.append(b)
            raten_()
     
       

start_() 
