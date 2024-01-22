
with open('Perepis.txt', 'r') as file:
    total_population = 0
    for line in file:
        data = line.split()
        year_of_birth = int(data[-1])
        if year_of_birth < 1978:
            print(data[0])
            total_population += 1
    print("Общее число жителей, родившихся раньше 1978 года:", total_population)


start_year = int(input("Введите начальный год: "))
end_year = int(input("Введите конечный год: "))

with open('Perepis.txt', 'r') as file:
    for line in file:
        data = line.split()
        year_of_birth = int(data[-1])
        if start_year <= year_of_birth <= end_year:
            print(' '.join(data[:-1]), year_of_birth)




