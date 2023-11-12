
# The salary of a salesperson is $200 + percentage of sales
# as follows:
#    up to $500 — 3%,
#    from 500 to 1000 — 5%,
#    over 1000 — 8%. The user types in the sales for three salespersons.
# Determine their salary, the best salesperson, give him or her
# a $200 bonus, print the result.


import os

ZAKLADNI_PLAT = 200
POCET_PRODEJCU = 3

# *************************************************************************************


class ProdejceClass():
    jmeno: str = "Prodejce 1"
    castka: float = 0
    vyplata: float = 0
    bonus: float = 0

# *************************************************************************************


def vypocet(castka):
    if (castka > 1000):
        return ZAKLADNI_PLAT + castka * 0.08
    elif (castka >= 500) and castka <= 1000:
        return ZAKLADNI_PLAT + castka * 0.05
    else:
        return ZAKLADNI_PLAT + castka * 0.03

# *************************************************************************************


def sortfunct(prodejce):
    return prodejce.vyplata

# *************************************************************************************


def vypis(poradi, prodejce):
    print(poradi + '.', 'Jmeno :', prodejce.jmeno, 'Castka:', prodejce.castka, 'Bonus:', prodejce.bonus,
          'Vyplata:', prodejce.vyplata, 'Celkem:', prodejce.vyplata + prodejce.bonus)

# *************************************************************************************


prodej = list()

os.system('cls')

i = 1
while i <= POCET_PRODEJCU:
    prodejces = input('Zadejte castku prodeje pro "Prodejce ' + str(i) + '":')
    if not prodejces.isnumeric():
        print('Zadany udaj neni cislo !!!!!')
        exit()

    Prodejce = ProdejceClass()
    Prodejce.castka = float(prodejces)
    Prodejce.vyplata = vypocet(Prodejce.castka)
    Prodejce.jmeno = "Prodejce "+str(i)
    Prodejce.bonus = 0

    prodej.append(Prodejce)

    i = i + 1

prodej.sort(key=sortfunct, reverse=True)
prodej[0].bonus = 200

os.system('cls')

# vypis('1', prodej[0])

i = 1
for x in prodej:
    vypis(str(i), x)
    i = i + 1
