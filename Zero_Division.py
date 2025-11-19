try:
    x = 10
    y = int(input("Mennyivel osszam el a(z) {x}-es szamot? "))
    print(f"eredmény: {x / y}")

except ZeroDivisionError:
    print("Nullával nem osztunk!")