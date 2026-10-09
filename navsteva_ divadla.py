#*****************************************
#
# Prodej listků do divadla
#
#*****************************************






#zakladni cena
zakladni_cena = 500

print("Vítáme vás v našem divadle")

# vstupní údaje
pocet_osob = int(input("Zadejte počet osob: "))
vek = float(input("Zadejte věk osob: "))
student = input("Ještě student (Ano/Ne): ")

#slevy

if pocet_osob >= 4:
     typ_sleva = "rodina sleva (25%)"
     cena_za_jednoho = 500*0.75
elif student == "Ano" and vek <26:
     typ_sleva = "Studentská sleva (30%)"
     cena_za_jednoho = 500*0.7
elif vek >= 65:
     typ_sleva = "Seniorská sleva (20%)"
     cena_za_jednoho = 500*0.80
else:
     typ_sleva = "Bez slevy"
     cena_za_jednoho = 500

#výpočet celkové cena
celkova_cena = cena_za_jednoho * pocet_osob

#výpis výsledku
print("Typ slevy: ", typ_sleva)
print("Cena za jednu vstupenku: ", cena_za_jednoho)
print("Celková cena: ", celkova_cena,"Kč")