x = int(input("Kolik je hodin: "))

if x < 0:
    print("Hodina nemůže být záporná.")
elif x>23:
    print("Zadávej hodiny v rozmezí 0-23")
elif 5<= x <10:
    print("Dobré ráno")
elif 10<= x <12:
    print("Dobré dopoledne")
elif 12==x:
    print("Dobré poledne")
elif 12< x <17:
    print("Dobré odpoledne")
elif 17<= x <22:
    print("Dobrý večer")
else: 
    print("Dobrou noc")
