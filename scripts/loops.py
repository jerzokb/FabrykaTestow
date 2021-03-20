liczby = [1, 2, 3, 4, 5]

for i in liczby:
    print(i)
print('***** ***')
for i in range(10):
    print(i)
print('***** ***')
for i in range(15, 18):
    print(i)
print('***** ***')
licznik1 = 0

while licznik1 < 10:
    print(licznik1)
    licznik1 += 1
print('***** ***')

licznik2 = 0
while True:
    print(licznik2)
    licznik2 += 1
    if licznik2 >= 5:
        break
print('***** ***')

for x in range(20):
    if x % 2 == 0:
        continue
    print(x)
