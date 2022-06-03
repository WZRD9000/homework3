numbers = input('ведите элементы списка через запятую: ')
numbers = numbers.split(',')

result = []
for i in numbers:
    if numbers.count(i) == 1:
        result.append(i)
print(result)