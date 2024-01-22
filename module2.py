summa = 0
file = open('Perepis.txt','r')
for i in file:
    s = str(i)
    lastname = s.split()
    print(lastname)
    date = lastname[3].split('.')
    print (date)
    if int(date[2]) < 1978:
        summa += 1

file.close()
print("Общее число жителей, родившихся раньше 1978 года:", summa)

print('Введите диапазон годов рождения')
d1 = int(input())
d2 = int(input())

file = open('Perepis.txt', 'r')
for i in file:
    s = str(i)
    lastname = s.split()
    date = lastname[3].split('.')

    if int(date[2]) >= d1 and int(date[2]) <= d2:
        print(lastname[0], lastname[1], lastname[2], date[2])

file.close()