
foods = []
prices = []
total = 0

while True: 
    food = input("Was möchtest du kaufen ? (Drücke E wenn du fertig bist )") 
    if food.lower() == "e":
        print("Du hast deinen Einkauf beendet auf zur Kasse: \n")
        break
    else: 
        price = float(input(f"Wie ist der Preis für {food}?: "))
        foods.append(food)
        prices.append(price)


print("-----Dein Warenkorb----\n")

for food in foods:
     print(food, end=" ")

print("\n")

print("-----Dein Preis-----")

for price in prices:
    total += price 

print(f"Total: {total:.2f}€")
 
