import random
tajne_cislo = random.randint (1,20)
pokusy = 0



while True:
    tip = int(input("Hádej číslo mezi 1 až 20: "))
    pokusy +=1

    if tip == tajne_cislo:
        print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokusy}. pokus.")
    elif tip < tajne_cislo:
        print("Číslo je větší")
    else:
        print("Číslo je menší")
    if tip > 20:
        print("Hádej číslo v rozmezí 1 až 20")
    elif tip < 1:
            print("Hádej číslo v rozmezí 1 až 20")
    

