# -------------------------------------------------------------------------------
# The user types in the start and end points of the range and
# a number. If the number is not in the range, the program asks
# the user to re-enter the number, and so on until the user enters
# the number correctly. The program displays all numbers in
# the range, highlighting the number with exclamation marks.
# For instance: 1 2 3 !4! 5 6 7.
# -------------------------------------------------------------------------------

cislo_od_s = input('Zadejte číslo od:')
if not cislo_od_s.isnumeric():
    print('Zadany udaj neni cislo !!!!!')
    exit

cislo_do_s = input('Zadejte číslo do:')
if not cislo_do_s.isnumeric():
    print('Zadany udaj neni cislo !!!!!')
    exit


cislo_od = int(cislo_od_s)
cislo_do = int(cislo_do_s)

spravne = False
while not spravne:

    cislo_uzivatels = input('Zadejte číslo v rozsahu :')
    if not cislo_uzivatels.isnumeric():
        print('Zadany udaj neni cislo !!!!!')
    else:
        cislo_uzivatel = int(cislo_uzivatels)
        if (cislo_uzivatel < cislo_od) or (cislo_uzivatel > cislo_do):
            print(
                f'Zadané číslo musí být v rozsahu od {cislo_od} do {cislo_do}')
        else:
            spravne = True

            #jeden zpusob
            s = ''
            for i in range(cislo_od, cislo_uzivatel):
                s = s + str(i) + ' '

            s = s + '!' + str(cislo_uzivatel) + '! '

            for i in range(cislo_uzivatel + 1, cislo_do + 1):
                s = s + str(i) + ' '

            print(s.strip())

            #druhy zpusob
            s = ' '
            for i in range(cislo_od, cislo_do + 1):
                s = s + str(i) + ' '
            s = s.replace(' '+str(cislo_uzivatel) +' ', ' !'+str(cislo_uzivatel) +'! ').strip();
            print(s)

