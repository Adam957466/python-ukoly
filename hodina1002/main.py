

# příkaz větvení
x = -5
if x>=0:
    if x>0:
        print(f"{x} je kladné číslo")
    else:
        print(f"{x} je nula")
else:
    print(f"{x} je záporné")
    x = -x
print(f"Absulutní hodnota: {x}")

#druha varianta

x = -5

if x>0:
    print(f"{x} je kladné číslo")
elif x==0:
    print(f"{x} je nula")
else:
    print(f"{x} je záporné")
    x = -x
print(f"Absulutní hodnota: {x}")