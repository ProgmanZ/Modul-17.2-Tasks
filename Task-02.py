# Задача 2. Сообщение

inp_string = input('Введите строку: ')
symbol = input('Введите дополнительный символ: ')

double_symbol_list = [i * 2 for i in inp_string]
merge_list = [i + symbol for i in double_symbol_list]

print('Список удвоенных символов:', double_symbol_list)
print('Склейка с дополнительным символом:', merge_list)
