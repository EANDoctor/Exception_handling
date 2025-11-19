x = 10
try:
    y = int(input("Mennyivel osszam el a(z) {x}-es szamot? "))
    print(f"eredmény: {x / y}")
except ZeroDivisionError as e:
    print(f"{e} Nullával nem osztunk!")
except ValueError as e:
    print(f"{e} Nem számot adtál meg!")