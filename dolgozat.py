while True:
    try:
        maxPoint = int(input("Adja mag a maximálisan elérhető pontszámot"))
        break
    except:
        print("AZ NEM EGY SZÁM !!!!!!!!!")
pontszam = 0
eredmenyseged = (pontszam / maxPoint) * 100
otos = 80
negyes = 70
harmas = 60
kettes = 40

while True:
    try:
        pontszam += int(input("Adja meg a pontszámot vagy nyomjon meg egy betűt a végeredményhez"))
    except:
        szazalek = pontszam / maxPoint * 100
        print(szazalek, end="")
        print("%")
        break

def hanyas():
    if otos < pontszam:
        print("Ötös")
    elif negyes < pontszam >= otos:
        print("Négyes")
    elif harmas < pontszam >= negyes:
        print("Hármas")
    elif kettes < pontszam >= harmas:
        print("Kettes")
    elif kettes >= pontszam:
        print("Egyes")

hanyas()