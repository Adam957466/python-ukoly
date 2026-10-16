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



#slevy



if pocet_osob >= 4:
     typ_sleva = "rodina sleva (25%)"
     cena_za_jednoho = zakladni_cena*0.75
elif pocet_osob < 0:
     print("Zadejte správný počet lidí")     
else:
     vek = float(input("Zadejte věk: "))
     if vek >= 65:
          typ_sleva = "Seniorská sleva (20%)"
          cena_za_jednoho = zakladni_cena*0.80
     elif vek < 26:
          student = input("Ještě student (Ano/Ne): ")
          if student == "Ano":
               typ_sleva = "Studentská sleva (30%)"
               cena_za_jednoho = zakladni_cena*0.70
          else:
               typ_sleva = "Bez slevy"
               cena_za_jednoho = zakladni_cena
     else:
          typ_sleva = "Bez slevy"
          cena_za_jednoho = zakladni_cena



#výpočet celkové cena
celkova_cena = zakladni_cena * pocet_osob

#výpis výsledku
print("Typ slevy: ", typ_sleva)
print("Cena za jednu vstupenku: ", cena_za_jednoho)
print("Celková cena: ", celkova_cena,"Kč")