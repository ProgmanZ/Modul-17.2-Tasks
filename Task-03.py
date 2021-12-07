# Задача 3. Повышение цен

def print_prise(list_prise):
    price_string = ''
    for part in list_prise:
        price_string += str(part) + ' '
    return price_string


product = []
for i in range(5):
    product.append(float(input(f'Цена на товар № {i + 1}: ')))

first_year_percent = int(input('\nПовышение на первый год: '))
second_year_percent = int(input('Повышение на второй год: '))

first_year_prises = [first_year_percent / 100 * i + i for i in product]
second_year_prises = [second_year_percent / 100 * i + i for i in product]

all_prices = [product, first_year_prises, second_year_prises]
all_prices = [round(sum(i), 2) for i in all_prices]

print_prise(all_prices)

print('\nСумма цен за каждый год: ' + print_prise(all_prices))
