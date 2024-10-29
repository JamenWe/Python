
foods = []
prices = []
total = 0
products = []

def liste():  
        food = input("Was möchtest du kaufen ? (Drücke E wenn du fertig bist): ") 
        if food.lower() == "e":
            print("\nDu hast deinen Einkauf beendet, auf zur Kasse: \n")
            return None
        else: 
            price = float(input(f"Wie ist der Preis für {food}?: "))
        product = food + " " + str(price) 
        products.append(product)
        prices.append(price)
        liste()
liste()

print("-----Dein Warenkorb----\n")
#
for product in products: 
    print(f"{product}€")  

print("\n")

print("-----Dein Preis-----")

for price in prices:
    total += price 

print(f"Total: {total:.2f}€")
 
