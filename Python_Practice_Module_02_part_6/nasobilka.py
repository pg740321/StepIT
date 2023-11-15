
# Print the multiplication table for the user-defined number. #
# If the user typed in 7, the output should be as follows:    #
#  7 * 1 = 7    #
#  7 * 2 = 14   #
#  7 * 3 = 21   #

cislos = input('Zadejte číslo pro vypsání násobilky:')

if not cislos.isnumeric():
    print('Zadany udaj neni cislo !!!!!')
else:
    print() #odradkovani

    cislo = int(cislos)
    pocetznaku = len(str(cislo))

#prvni zpusob vypisu se zarovnanim
    for i in range(1,11):
        print(str(cislo).rjust(pocetznaku),'*',str(i).rjust(2),'=',
           str(cislo*i).rjust(pocetznaku+1))


#druhy zpusob vypisu
    for i in range(1,11):
        print(f"{cislo} * {i} = {cislo*i}")
