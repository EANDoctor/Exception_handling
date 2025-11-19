"""
1. Feladat
Írj egy programot, ami a felhasználótól három egész számot számot kér be egyesével, ezeket eltárolja egy listában, majd a képernyőre kiírja a lista tartalmát! Ha a felhasználó nem számot ad meg, kapjon hibaüzenetet, és ismétlődjön meg a bekérés! 
"""
numbers = []
while len(numbers) < 3:
    try:
        num = int(input("Kérek 3 egész számot: "))
        numbers.append(num)
    except ValueError as e:
        print(f"{e} \nNem számot adtál meg!")

print("A megadott számok:", numbers)