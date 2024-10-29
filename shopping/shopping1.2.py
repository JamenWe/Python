
# Meine Variablen und Arrays (Listen) 
a_food = []
foods = []
prices = []
total = 0
products = []

# Meine Funktionen
def liste_():  
        food = input("\nWas möchten sie kaufen ? (E wenn sie fertig sind): ").lower() 
        if food == "e":
            print("\nSie haben ihren Einkauf beendet, auf zur Kasse: \n")
            kasse_()
        else: 
            price = float(input(f"Wie ist der Preis für {food}?: "))
            price_str = str(f"{price:.2f}")
            product = (f"{food:<10} {price_str:>10}") 
            products.append(product)
            prices.append(price)
            liste_()





#def einpacken_():
#    einpacken = input("Welche/n Artikel wollen sie in ihren Warenkorb packen?:")
   




def weiter_():

    weiter = input("Wollen sie noch weitere Artikel aus der Liste hinzufügen?(Y/N):").lower()         
    if weiter == "y":                                                   
        pack_()                                                            
    elif weiter == "n":                                                 
        frage = input("Zur Kasse oder eigene Artikel bestellen?(K/E):").lower()           
        if frage == "k":                                                
             kasse_()                                                        
        elif frage == "e":
             liste_()
        else:                                                                   
             print("Falsche Eingabe!!!\n")                                           
             weiter_() 
    else:
        print("Falsche Eingabe!!!\n")
        weiter_()



def pack_():                                                                     
     artikel = { 
         "Brot": "1.99",
         "Butter": "2.50",
         "Nutella": "4.95",
         "Milch": "1.75",
         "Kekse": "2.75",
         "Schokolade": "1.00"
     }
     einpacken = input("Welche/n Artikel wollen sie in ihren Warenkorb packen?:")
    
     if einpacken in artikel:
        preis2 = artikel[einpacken]
        preis = float(artikel[einpacken])
        prices.append(preis)
        stuff = einpacken   
        product2 = (f"{stuff:<10} {preis2:>10}")
        products.append(product2)
        print(f"{einpacken} wurde dem Warenkorb hinzugefügt!\n\n")                   
        weiter_()                                                           
     else:                                                                       
        print("Falsche Eingabe!!!\n")                                                
        pack_()   
    
    
    
    
    
def article_():
    artikel = { 
        "Brot": 1.99,
        "Butter": 2.50,
        "Nutella": 4.95,
        "Milch": 1.75,
        "Kekse": 2.75,
        "Schokolade": 1.00
    }
    
    
    for a,p in artikel.items():
        print(f"{a:10}: {p:.2f}€")





def kasse_():
    global total
    print("-----Ihr Warenkorb----\n")

    for product in products: 
        print(f"{product}€")  
    print("\n")
    
    print("------Ihr Preis------")
    
    for price in prices:
        total += price  
         
    print(f"Total:           {total:.2f}€")

     
def alles_():
    listen = input("Möchten sie unsere Produktliste sehen oder eigene Produkte bestellen lassen ?:\n(P) für die Produktliste\n(E) für eiegene Artikel\n(X) um zum Ausgangs zu gelangen\nEingabe:").lower() 
    
    if listen == "p":
        print("\nUnsere Artikel:\n")
        article_()
        print("\n")
        pack_() 
     
        artikel = { 
            "Brot": "1.99€",
            "Butter": "2.50€",
            "Nutella": "4.95€",
            "Milch": "1.75€",
            "Kekse": "2.75€",
            "Schokolade": "1.00€"
        }
        
        #pack_()   
    elif listen == "e":
        liste_()
    
    elif listen == "x":
        print("\nAuf Wiedersehen!")
        return None
    
    else:
        print("Falsche Eingabe!!!\n")
        alles_()

alles_()

