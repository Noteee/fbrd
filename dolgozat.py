while True:
    try:
        maxPoint = int(input("Adja mag a maximálisan elérhető pontszámot"))
        break
    except:
        print("AZ NEM EGY SZÁM !!!!!!!!!")
pontszam = 0
otos = 80.0
negyes = 70.0
harmas = 60.0
kettes = 40.0
breaker = 0
def hanyas():
    if otos < szazalek:
        print("Ötös")
    elif negyes < szazalek >= otos:
        print("Négyes")
    elif harmas < szazalek >= negyes:
        print("Hármas")
    elif kettes < szazalek >= harmas:
        print("Kettes")
    elif kettes >= szazalek:
        print("Egyes")

while breaker == 0:
    pontszam = 0
    while True:
        try:
            pontszam += float(input("Adja meg a pontszámot vagy nyomjon meg egy betűt a végeredményhez"))
        except:
            szazalek = pontszam / maxPoint * 100
            print(szazalek, end="")
            print("%")
            hanyas()
            again = input("again? y or n")
            if again == "y":
                break
            else:
                breaker = 1


