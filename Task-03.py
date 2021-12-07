# Задача 3. Повышение цен

product = []
for i in range(5):
    product.append(float(input(f'Цена на товар № {i + 1}: ')))

first_year_percent = int(input('Повышение на первый год: '))
second_year_percent = int(input('Повышение на второй год: '))

first_year_prises = [round(first_year_percent, 2) * 0.1 * i for i in product]
second_year_prises = [round(second_year_percent, 2) * 0.1 * i for i in product]

sum_prices = [round(first_year_prises[i]+second_year_prises[i], 2) for i in range(5)]

print('Сумма цен за каждый год:', sum_prices)
