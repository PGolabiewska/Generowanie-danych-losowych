from faker import Faker
import csv

fake = Faker()

def losuj_dane():
    temperatura = fake.pyfloat(left_digits=2, right_digits=1, positive=True, min_value=36.5, max_value=37.5)
    cisnienie = f"{fake.random_int(min=115, max=140)} / {fake.random_int(min=70, max=90)}"
    puls = fake.random_int(min=70, max=109)
    czestotliwosc_oddechu = fake.random_int(min=15, max=25)

    return temperatura, cisnienie, puls, czestotliwosc_oddechu

def przypisz_stan(temperatura, cisnienie, puls, czestotliwosc_oddechu):
    if 36.5 <= temperatura <= 37.0 and 115 <= int(cisnienie.split('/')[0]) <= 130 and 70 <= int(cisnienie.split('/')[1]) <= 80:
        return "Zestresowany"
    elif 130 <= int(cisnienie.split('/')[0]) <= 140 and 70 <= int(cisnienie.split('/')[1]) <= 85:
        return "Pobudzony"
    elif 37.2 <= temperatura <= 37.5 and 20 <= czestotliwosc_oddechu <= 23:
        return "Szczęśliwy"
    elif 70 <= puls <= 75 and 20 <= czestotliwosc_oddechu <= 25:
        return "Przestraszony"
    elif 37.0 <= temperatura <= 37.3 and 85 <= puls <= 95:
        return "Zdenerwowany"
    elif 36.5 <= temperatura <= 36.8 and 15 <= czestotliwosc_oddechu <= 17:
        return "Zrelaksowany"
    elif 115 <= int(cisnienie.split('/')[0]) <= 125 and 70 <= int(cisnienie.split('/')[1]) <= 81 and 70 <= puls <= 88:
        return "Smutny"
    else:
        return "Spokojny"

def zapisz_do_pliku(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Temperatura (°C)", "Ciśnienie (mm Hg)", "Puls (uderzeń/min)", "Częstot. oddechu (ilość/min)", "Stan"])
        for row in data:
            writer.writerow(row)

for i in range(3):
    data = []
    for _ in range(50):
        temperatura, cisnienie, puls, czestotliwosc_oddechu = losuj_dane()
        stan = przypisz_stan(temperatura, cisnienie, puls, czestotliwosc_oddechu)
        temperatura_rounded = round(temperatura, 1)
        data.append([temperatura_rounded, cisnienie, puls, czestotliwosc_oddechu, stan])
    filename = f"dane_{i+1}.csv"
    zapisz_do_pliku(filename, data)
    print(f"Dane zostały zapisane do pliku CSV: {filename}")
