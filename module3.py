# Открываем файл и считываем данные
with open('travels.txt', 'r') as file:
    lines = file.readlines()

max_volume = 0
max_volume_date = ''
mass_from_lipki = 0
total_distance_oct_1 = 0

for line in lines:
    data = line.strip().split(',')
    date = data[0]
    departure = data[-1]
    destination = data[0]
    distance = int(data[1])
    fuel_consumption = int(data[2])
    cargo_mass = int(data[3])

    if cargo_mass > max_volume:
        max_volume = cargo_mass
        max_volume_date = date

    if departure == 'Липки':
        mass_from_lipki += cargo_mass

    if date == '1.10':
        total_distance_oct_1 += distance

print(f"В перевезено больше всего грузов, их суммарный объем: {max_volume}")
print(f"Масса всех грузов, отправленных из поселка «Липки»: {mass_from_lipki}")
print(f"Суммарное расстояние, которое проехал грузовой транспорт за 1 октября: {total_distance_oct_1}")