cis = input('Zadej cislo 1 .. 100 :');

if not cis.isnumeric() :
  print('Zadany udaj neni cislo !!!!!');
  exit();


cislo = int(cis);

if (cislo<1) or (cislo>100):
  print('Zadane cislo neni v rozsahu 1 az 100');
  exit();


# Prvni moznost reseni

slovo = '';

if (cislo % 3 == 0) :
    slovo = slovo + 'Fizz';

if (cislo % 5 == 0):
    slovo = slovo + 'Buzz';

if slovo == '':
    slovo = str(cislo);

print(slovo);

# ------------------------------------------------------------------------



# druha moznost reseni

if (cislo % 3 == 0) and (cislo % 5 == 0):
  print('FizzBuzz')
elif (cislo % 3 == 0):
  print('Fizz')
elif  (cislo % 5 == 0):
  print('Buzz')
else :
  print(cislo);

