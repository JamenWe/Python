unit = input("Ist die Temperatur in Celsius oder Fahrenheit (C/F): ")
temp = float(input("Gib die Temperatur an: "))
unit = unit.upper()

if unit == "C":
    temp_new = round((9 * temp)/ 5 + 32, 1)
    print(f"Die Temperatur {temp} in Fahrenheit ist: {temp_new}°F")
elif unit == "F":
    temp_new = round((temp - 32) * 5 / 9, 1)
    print(f"Die Temperatur {temp} in Celsius ist: {temp_new}°C")
else: 
    print(f"Die Angabe der Einheit ist Falsch: {unit}") 
