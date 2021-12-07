# Задача 1. Кубы и квадраты

left = int(input('Левая граница: '))
right = int(input('Правая граница: '))

qube_list = [i ** 3 for i in range(left, right + 1)]
quatro_list = [i ** 2 for i in range(left, right + 1)]

print('\nСписок кубов чисел в диапазоне от ', right, 'до', left, ':', qube_list)
print('Список квадратов чисел в диапазоне от ', right, 'до', left, ':', quatro_list)
