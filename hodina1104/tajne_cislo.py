import random

tajne_cislo = random.randint(1, 20)
pokusy = 0

while True:
  tip = int(input("Hádej číslo mezi 1 až 20: "))

  if tip < 1 or tip > 20:
    print("Prosím, hádej čísla pouze v rozmezí 1 až 20.")
    continue  

  pokusy += 1

  if tip == tajne_cislo:
    print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokusy}. pokus.")
    break  
  elif tip < tajne_cislo:
    print("Číslo je větší")
  else:
    print("Číslo je menší")
    

