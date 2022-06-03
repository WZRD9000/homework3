first_list = input('ведите элементы первого списка: ')
first_list = first_list.split(' ')

second_list = input('ведите элементы второго списка: ')
second_list = second_list.split(' ')

for i in first_list[:]:
    if i in second_list:
        first_list.remove(i)
print(first_list)