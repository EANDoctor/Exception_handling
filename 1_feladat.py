x = 10
while True:
    try:
        y = int(input(f"Mennyivel osszam el a {x}-es szamot? "))
        print(f"eredmény: {x / y}")
        break
    except ZeroDivisionError as e:
        print(f"{e} \n Nullával nem osztunk!")
    except ValueError as e:
        print(f"{e} \n Nem számot adtál meg!")