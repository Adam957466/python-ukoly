dole = 1
nahore = 100
tip = (dole+nahore) // 2
pokusy = 0


while True:
    if dole > nahore:
        print("Ty mi lžeš. Lhát se nemá")
        break
    print(f"Můj typ je {tip}")

    pokusy += 1

    odpoved  = input("Je číslo větší, menší nebo rovno (v,m,s): ").lower()

    if odpoved == "s":
        print(f"Huhodl jsem číslo {tip} na {pokusy} pokusů")
        break
    elif odpoved == "v":
        dole = tip +1
    elif odpoved == "m":
        nahore = tip -1
    else:
        print("Co to píšeš odpovídej pouze 'v', 'm' nebo 's' ")
    tip = (dole+nahore) // 2