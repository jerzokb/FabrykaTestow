x = 5
imie = 'Beata'
nazwisko = 'Palka'
wiek = 49

if nazwisko == 'Palka' and wiek == 49:
    print('Czesc Palka, masz ', wiek, ' lat')
else:
    print('to nie ty!')

if imie in ['Beata', 'Marek'] and wiek == 49:
    print('Czesc Palka, masz ', wiek, ' lat')
else:
    print('Nie jesteś Beata ani Marek')

zmienna1 = -1
zmienna2 = 2
zmienna3 = 3

if zmienna1 > 0:
    print('1')
elif zmienna2 < 0:
    print('2')
else:
    print('same falsy')