pocet_mesicu = int(input("Zadej počet měsíců simulace: "))

while pocet_mesicu < 1 or pocet_mesicu > 12:
    print("Číslo nesmí být záporné a nesmí být větší než 12.")
    pocet_mesicu = int(input("Zadej počet měsíců znovu: "))

a = 1
b = 1
mesic = 1


while mesic <= pocet_mesicu:
    
    if mesic == 1:
        aktualni_pocet = 1
    else:
        dopredu = a + b
        a = b
        b = dopredu
        aktualni_pocet = b

    
    vizualizace = "🐇" * aktualni_pocet
    
    print(f"Měsíc {mesic}: {aktualni_pocet} párů | {vizualizace}")
    
    
    mesic = mesic + 1