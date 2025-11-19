try:
    x = int(input("kérek egy számot: "))
    print(f"A szám négyzete: {x * x}")
except ValueError:
    print("Nem számot adtál meg!")