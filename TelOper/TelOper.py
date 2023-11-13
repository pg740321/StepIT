# Write a program that calculates the cost of a call for different
# mobile phone operators. The user types in the cost of
# the call and chooses operators for the outgoing and incoming
# calls. Print the cost

import math

telefon_operator = [
  {'operator':'T-Mobile', 'tarif': 1.2, 'cena': 0 },
  {'operator':'O2'      , 'tarif': 1.0, 'cena': 0  },
  {'operator':'Vodafone', 'tarif': 1.6, 'cena': 0  }
]

def sortfunct(toperator):
    return toperator['cena']

delkas = input('Zadejte délku hovoru v minutách :')
if not delkas.replace(',','').replace('.','').isnumeric():
    print('zadany udaj neni cislo !!!!!')
    exit()

print('')
print('')
print('***********************************************************')
print('Výpis telefoních operátorů :')
print('-----------------------------------------------------------')
print('')

i = 1
for x in telefon_operator:
    delka =  float(delkas.replace(',','.'))

    d = math.trunc(delka)
    if delka - math.trunc(delka) > 0 :
       d = d + 1

    cena = d * x['tarif'];
    x['cena'] = cena;

    print(str(i) + '.', 'Operátor :', (x['operator']).ljust(12) , '   Tarif za min:' + str(x['tarif']).rjust(5), '   Cena hovoru:', str(cena).rjust(6))
    i = i + 1


telefon_operator.sort(key=sortfunct, reverse=False)

print('')
print('***********************************************************')
print('')
print('Nejlepší cena :')
print('-----------------')
print('Operátor :', (telefon_operator[0]['operator']).ljust(12) , '   Tarif za min:' + str(telefon_operator[0]['tarif']).rjust(5), '   Cena hovoru:', str(telefon_operator[0]['cena']).rjust(6))


